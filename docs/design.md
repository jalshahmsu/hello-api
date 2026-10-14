# hello-api: Design

## Context (C4 level 1)
User/browser --HTTPS--> hello-api service

## Containers (C4 level 2)
Internet --443--> [Caddy: TLS termination, reverse proxy]
                      --8000--> [hello-api container: FastAPI + uvicorn]
Hosted on one AWS EC2 instance (Linux). DNS: domain -> Elastic IP.

## Interface (defined before implementation)
GET /hello?name={string, optional, default "World", max length 50}
  200 -> {"message": "Hello, <name>!"}
  422 -> validation error if name is longer than 50 characters
GET /health
  200 -> {"status": "ok"}

## Data model
None. The service is stateless.

## Module layout
src/hello_api/main.py       # routes only (HTTP layer)
src/hello_api/greeting.py   # build_greeting(name) -> str (pure logic)
tests/test_greeting.py      # unit tests
tests/test_api.py           # API tests

## Threat model (mini STRIDE)
- Spoofing: not applicable, no auth
- Tampering: HTTPS in transit
- Information disclosure: no secrets or user data stored; no stack traces in responses
- Denial of service: input length cap; instance-level rate limit later if needed
- Injection: name is only ever returned as JSON, never executed or put in a query
- Elevation: container runs as non-root; SSH restricted to my IP
