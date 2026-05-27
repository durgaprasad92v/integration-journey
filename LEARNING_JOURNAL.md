# Learning Journal

## Session 2 — Causing failure on purpose (Date: <28/05/2026>)

### What I built
A script that triggers and gracefully handles four HTTP failure
modes: 4xx (client error), 5xx (server error), network error,
and timeout. The script never crashes — it observes failures
and reports them.

### What surprised me
Case 3 (500 error) returned an empty response body. The server
said "I failed" with no explanation. This taught me that
production integration code has to handle the case where the
upstream system tells you nothing useful. You can't always
parse a meaningful error message.

### Three things I learned (in my own words)

1.4xx is a client error and retry doesn't work , and 5xx is server error and sometimes if we try again server may respond.
2.Timeout fail is the most dangerous of all, beccause we don't know whether it really created the request and processed ,so we should not retry unless we have idempotency key
3.In the python code , we given "try" and "except" . we will give some internet address which may fail under "try" , so when it fails then it will come to a safety code if give "except"
### Debugging notes
I hit syntax errors and indentation errors while typing this
script. Each one taught me to read the Python error message
carefully — the line number and error type usually tell me
exactly where to look. Indentation matters in Python:
unlike braces in other languages, whitespace is meaningful.
### How this maps to pharma
 In my current project this scenario could occur with LIMS with MES Integration where Registration ID is the main check, In this any failure could occur .






A running log of what I learn each session — in my own words.

---

## Session 1 — First GET request (Date: <22/05/2026>)

### What I built
A 12-line Python script that fetches Pokemon data from a public
API and prints selected fields. (Pokemon is just stand-in data;
the plumbing is identical to a real LIMS→Empower call.)

### Three things I learned
1. HTTP is a language for the software to connect with other software through internet
2. Differemt status codes we will receive for example 200 means success 
3. JSON is a structured format for text and API is framework of endpoints and you can design this like a RESTAPI

### A question I still have
How we will design this?

### How this maps to my domain
In pharma LIMS can fetch data from CDS through API endpoints by using GET  and also ELN can post result to LIMS by using commands like POST etc