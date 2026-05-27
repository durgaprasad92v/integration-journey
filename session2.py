"""
Session 2 — Causing four distinct failure modes
================================================
Purpose: Deliberately trigger the four categories of HTTP failure
         and observe how Python's `requests` library reports each.

Failure categories covered:
  1. Client error (4xx) — we ask for something that doesn't exist
  2. Server error (5xx) — we ask a service that's designed to fail
  3. Network error    — we try to reach a server that doesn't exist
  4. Timeout          — we set a very short timeout on a slow server

Mapping to pharma/biotech:
  Each of these is a real scenario in a LIMS-CDS-SAP integration.
  Today we feel them deliberately, so we recognize them in production.
"""
import requests
print("=" * 60)
print(" SESSION 2: Four failure modes")
print("=" * 60)

print("\n--- cASE 1 : Success (baseline)---" )  
r = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
print(f"status code: {r.status_code}")
print(f"r.ok (True for 2xx) : {r.ok}")
print(f" Verdict : Request succeeded, safe to use response data.")

print("\n--- cASE 2 : Client error (400 Not found) ---" )
r = requests.get("https://pokeapi.co/api/v2/pokemon/notarealpokemon")
print(f"status code: {r.status_code}")
print(f"r.ok: {r.ok}")
print(f"First 100 chars of response body: {r.text[:100]}")
print(f"Verdict: We asked wrong.Retrying won't help.Fix the request")

print("\n--- cASE 3 : Server error (500 Internal Server Error) ---" )
r = requests.get("https://httpbin.org/status/500")
print(f"status code: {r.status_code}")
print(f"r:ok: {r.ok}")
print(f"First 100 chars of response body: {r.text[:100]}")
print(f"verdict: Server failed.Not our fault,Safe to retry with backoff.")

print("\n--- CASE 4: Network error (server doesn't exist) ---")
try:
    r = requests.get("https://thisdoesnotexistonanyserver.com",
            timeout = 5
            )
    print(f"status code: {r.status_code}")
except requests.exceptions.ConnectionError as e:
    print(f"Caught a ConnectionError (no status code received)")
    print(f"Exception type: {type(e). __name__}")
    print(f"verdict: Can't reach server. Check network or URL.")


print("\n--- cASE 5 : Timeout (Server is slow) ---" )
try:
    r = requests.get(
        "https://httpbin.org/delay/10", timeout=2)
    print(f"status code: {r.status_code}")
except requests.exceptions.Timeout as e:
    print(f"Caught a Timout exception")
    print(f"Exception type: {type(e).__name__}")
    print(f"verdict: Server is alive but slow. We don't know if the.")
    print(f"        request was processed .THIS is where idempoteny")
    print(f"       keys become critical ")

print("\n" + "=" * 60)
print("End of Session 2")
print("=" * 60)




        


      

