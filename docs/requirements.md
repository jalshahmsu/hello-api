# hello-api: Requirements

## Problem
A minimal web service that greets a caller by name, used to practice
the full build-and-deploy lifecycle.

## Functional requirements
- FR1: GET /hello?name=<str> returns JSON {"message": "Hello, <name>!"}
- FR2: If name is missing, default to "World".
- FR3: GET /health returns JSON {"status": "ok"}

## Non-functional requirements
- NFR1: p95 latency < 100 ms
- NFR2: Served over HTTPS on a custom domain
- NFR3: Starts from a fresh clone with one command

## Acceptance criteria (Given / When / Then)
- AC1: Given the server is running, when GET /hello?name=JS,
  then status 200 and body {"message": "Hello, JS!"}
- AC2: Given the server is running, when GET /hello,
  then body {"message": "Hello, World!"}
- AC3: Given the server is running, when GET /health,
  then status 200 and body {"status": "ok"}

## Non-goals
- No database, no authentication, no UI.

## Risks / unknowns
- Which host to deploy on (decided in Task 10).
