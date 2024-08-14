# WTF (What's this for?)

Vibrant continues to invest in securing service delivery and proteching data critical to help seekers.  Meanwhile, we are learning again that we write software.

This repository contains Vibrant's development of software security requirements.  It is maintained by the InfoSec team.

# Index

  - [data-protection](./data-protection.md)
  - [authentication](./authentication.md)
  - [cryptography](./cryptography.md)
  - [files-resources](./files-resources.md)
  - [business_logic](./business_logic.md)
  - [architecture](./architecture.md)
  - [api](./api.md)
  - [commumnications](./commumnications.md)
  - [error-logging](./error-logging.md)
  - [validation-sanitation-encoding](./validation-sanitation-encoding.md)
  - [configuration-management](./configuration-management.md)
  - [access-control](./access-control.md)
  - [malicious-code](./malicious-code.md)
  - [session-management](./session-management.md)

## System Security Requirements

Vibrant continues to awaken to concepts of security, and the control of IT systems - and though we have started to invest (time, money, and person-power) in security, we have a long way to go.

So, these requirements should match Vibrant's consensus on achievable state-of-the-art.  If you see anything that doesn't pass the Vibrant smell test, do reach out!

> [!IMPORTANT]
> It is very unlikely we meet the level 1 requirements considered 'adequate' first steps by NIST, much less level 2 or 3.
> 
> This set of requirements should be **achievable**. Consider them as possible release standards sometime in the near future and comment accordingly.  

## Usage

As we understand need and appetite, we will work with you (dear reader) to craft [SMART](https://en.wikipedia.org/wiki/SMART_criteria) requirements for your specific system development needs. (together :love_letter:) 


### Origins

InfoSec chose the latest release of [OWASP Application Security Verification Standard](https://github.com/OWASP/ASVS) as the inspiration for Vibrant's security requirements, for a variety of reasons.  Here are a few:

- it maps directly to NIST guidelines
- it offers tiers of requirements, allowing for variation in maturity and risk management
- it represents consensus best-practice within a global application security community

We currently fork the [actual ASVS](./ASVS_docs/README.md) into this repository (periodically) for quick & easy reference.

## References

- [Glossary of terms](./glossary.md)
