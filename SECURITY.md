# Security Policy

`redteam-foundry` is a research/measurement tool for auditing adversarial
benchmarks. This policy covers how to report a security **or safety** issue in
the tool itself. For content takedowns (a model provider wanting example
transcripts removed), see [`ETHICS.md`](ETHICS.md).

## Supported versions

| Version | Supported |
| --- | --- |
| 0.2.x | ✅ |
| < 0.2 | ❌ |

Fixes land on the latest release line.

## Reporting a vulnerability

**Please do not open a public issue for a security- or safety-sensitive report.**
Report it privately, either:

- **GitHub** — *Security → Report a vulnerability* (private advisory) on the repo, or
- **Email** — <rosscyking@gmail.com>

Include what you found, how to reproduce it (**aggregate / redacted — do not
paste raw harmful content**), and the version or commit.

### In scope

- Vulnerabilities in the tool: code execution, path traversal, unsafe
  deserialization, secret handling, etc.
- **Safety-relevant defects** — especially anything that lets an excluded
  category (CSAM / WMD-synthesis / detailed self-harm) slip past the exclusion
  filter, or makes the tool emit raw harmful prompts/outputs. Treat these as
  security issues and report them privately.

### Out of scope

- Findings that a benchmark is stale, duplicated, or monolingual — that is the
  tool's normal output; open a regular issue.
- Vulnerabilities in third-party datasets or model providers (report to them).

## Response

Solo-maintained and best-effort: acknowledgement within a few days, and a fix or
mitigation as fast as is practical for confirmed issues. Please allow reasonable
time to remediate before any public disclosure.
