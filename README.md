# Integration Journey

A hands-on 8-week path from pharma/biotech Lab Informatics
domain expertise into modern integration engineering.

## Who I am
Lead Solution Consultant in Lab Informatics with deep domain expertise in LIMS, CDS, ELN, SDMS and  MES integrations across pharma and biotech. Currently engaged on the Fraunhofer FFB battery cell research production facility (Münster, DE), applying pharma 21 CFR Part 11 / GAMP 5 / ALCOA+ thinking to battery manufacturing data integrity.

This repo is my deliberate practice — moving from architect- level conceptual understanding to hands-on integration implementation.

## The path

| Week | Focus | What I built |
|------|-------|--------------|
| 1 | HTTP fundamentals | First API requests, failure modes, POST with JSON |
| 2 | Build a server | A 30-line "fake LIMS" with one endpoint |
| 3 | Connect client + server | A CDS-style script that POSTs to my fake LIMS |
| 4 | Reliability | Idempotency, schema validation, error handling |
| 5 | Observability | Correlation IDs, structured logging, audit trail |
| 6 | Async messaging | Replacing direct calls with RabbitMQ |
| 7 | Cryptographic signatures | Why e-signatures don't cross system boundaries |
| 8 | Synthesis | A working CDS→LIMS-style integration, mapped to FFB |

## Why this matters
In regulated industries, integration is not just plumbing —it's the substrate of data integrity, batch release, and Digital Battery Passport compliance. This repo is my way of learning the plumbing as deeply as I already know the regulations.

## How to read this repo
Start with `week-01-foundations/README.md` and proceed in order. Each week's README explains what was built, what it taught me, and how it maps to real pharma/biotech integration patterns.
