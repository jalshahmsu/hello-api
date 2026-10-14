# ADR 0002: Host on EC2 + Docker + Caddy

Status: Accepted
Date: 2026-10-12

## Context
Must run on AWS with a custom domain over HTTPS, at minimal cost,
and teach Linux operations.

## Options considered
- EC2 + Docker + Caddy: full control, automatic Let's Encrypt certificates,
  roughly one small instance of cost. Manual patching and ops.
- App Runner: managed HTTPS and scaling, less Linux exposure, more AWS-specific.
- ECS Fargate + ALB + ACM: production-grade, but the load balancer costs
  more than the app is worth at this scale.

## Decision
EC2 + Docker + Caddy.

## Consequences
+ Cheap, simple, transferable Linux skills.
- Single instance means no high availability; we patch the OS ourselves.
- Revisit if traffic or uptime requirements grow.
