# ADR 0001: Use FastAPI

Status: Accepted
Date: 2026-10-12

## Context
Need a small HTTP JSON service in Python with input validation and
auto-generated OpenAPI docs.

## Options considered
- Flask: simple, but validation and OpenAPI need extra libraries.
- FastAPI: built-in validation (pydantic), OpenAPI, async, easy testing.
- Django: far more than needed.

## Decision
FastAPI.

## Consequences
+ Validation and docs come for free.
- Adds a dependency on the pydantic/starlette ecosystem.
