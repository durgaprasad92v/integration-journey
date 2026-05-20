"""
Session 1 — My first HTTP integration
======================================
Purpose: Send a GET request to the public PokeAPI and read the JSON response.
This is the smallest possible "integration" — one program asking another for data.

Mapping to pharma/biotech:
  - In real work, this same shape is used when a LIMS asks Empower for a chromatogram,
    or when an ELN asks a LIMS for sample metadata.
"""

import requests   # 'requests' is a Python library that handles HTTP plumbing for us

# Step 1: Build the URL we want to call.
# This is the "endpoint" that returns information about a specific Pokemon.
url = "https://pokeapi.co/api/v2/pokemon/pikachu"

# Step 2: Send the GET request and wait for the response.
# 'requests.get(url)' is the integration equivalent of "asking a question across the internet".
response = requests.get(url)

# Step 3: Inspect the response status code.
# 200 = success (the server understood and is sending back data).
print("Status code:", response.status_code)

# Step 4: Parse the response body as JSON.
# The server returned text formatted as JSON; .json() converts it to a Python dict.
data = response.json()

# Step 5: Read fields from the dictionary, just like reading from any Python dict.
print("Name:", data["name"])
print("Weight:", data["weight"])
print("Number of abilities:", len(data["abilities"]))