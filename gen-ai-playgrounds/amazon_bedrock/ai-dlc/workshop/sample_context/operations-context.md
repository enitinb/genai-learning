This document provides background context for the operations phase.

---

## Operational Expectations (Simple)

- The application is expected to run in a serverless environment
- Deployments should be repeatable and automated
- Failures should be visible through logs and metrics

---

## Monitoring and Visibility

- Use CloudWatch Logs for application and access logs
- Basic metrics (errors, latency, invocation counts) are sufficient
- No advanced observability tooling is required for this exercise

---

## Scaling and Reliability

- Rely on built-in scaling of AWS Lambda and API Gateway
- No manual scaling or capacity planning is required
- Design for stateless execution

---

## Change and Validation

- Changes should be small and incremental
- Validate functionality after deployment
- Roll back if something does not behave as expected
