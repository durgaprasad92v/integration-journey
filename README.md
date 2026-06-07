# Integration Journey

A hands-on, structured learning path from pharma/biotech Lab
Informatics domain expertise into modern integration engineering.

> This is a real learning journey conducted alongside a full-time
> consulting role on Fraunhofer FFB (Münster, Germany), German
> language preparation, and an active EU job search.
>
> Pace is deliberate: roughly one session per week. Every commit
> reflects actual hands-on work, typed by hand and reflected on
> in writing. Quality of understanding is prioritized over speed.

## Who I am

Lead Solution Consultant in Lab Informatics with deep domain
expertise in LIMS, CDS, ELN, and MES integrations across pharma
and biotech. Currently engaged at the Fraunhofer FFB battery
cell research production facility (Münster, Germany), applying
pharma 21 CFR Part 11 / GAMP 5 / ALCOA+ discipline to battery
manufacturing data integrity.

This repository is my deliberate practice — moving from
architect-level conceptual understanding to hands-on integration
implementation, one small working piece at a time.

## Progress

| Session | Focus | Status |
|---------|-------|--------|
| 1 | First GET request to a real API | ✅ Done |
| 2 | Four HTTP failure modes | ✅ Done |
| 3 | Build a "fake LIMS" server | ⏳ Upcoming |
| 4 | Connect client and server | ⏳ Upcoming |
| 5 | Reliability — idempotency, schema validation | ⏳ Upcoming |
| 6 | Observability — correlation IDs, audit logs | ⏳ Upcoming |
| 7 | Async messaging with RabbitMQ | ⏳ Upcoming |
| 8 | Cryptographic signatures for GxP integrity | ⏳ Upcoming |
| 9+ | Synthesis — a CDS→LIMS-style integration mapped to FFB | ⏳ Upcoming |

## Repository structure

| File | Purpose |
|------|---------|
| `session1.py` | First GET request to PokeAPI (Session 1) |
| `session2.py` | Trigger and handle four HTTP failure modes (Session 2) |
| `README.md` | Overview and progress tracking (this file) |
| `LEARNING_JOURNAL.md` | Personal reflections, lessons, and questions per session |

## Why this matters

In regulated industries, integration is not just plumbing — it
is the substrate of data integrity, batch release, and (in
battery manufacturing) Digital Battery Passport compliance.
This repository is my way of internalizing that plumbing as
deeply as I already understand the regulations.

## How I'm building this

Each session is built through a deliberate three-pass method:

1. **Read** the concept and study the example code.
2. **Type** every line of code by hand — never copy-paste.
   Hit errors, fix them, understand why.
3. **Reflect** in `LEARNING_JOURNAL.md` in my own words, with
   a mapping to a real pharma/biotech integration scenario.

The journey emphasizes depth and reflection over speed. The
goal is not to finish in 8 weeks; it is to genuinely understand
integration engineering at a level I can defend in an interview
and apply to a real GxP system.