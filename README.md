# System Security Requirements

Vibrant continues to invest in securing service delivery and proteching data critical to help seekers.  Meanwhile, we are learning again that we write software.

This repository contains Vibrant's development of system security requirements.  It is maintained by the InfoSec team.

# Index 

  1. [architecture](./architecture.md)
  1. [authentication](./authentication.md)
  1. [session-management](./session-management.md)
  1. [access-control](./access-control.md)
  1. [validation-sanitation-encoding](./validation-sanitation-encoding.md)
  1. [cryptography](./cryptography.md)
  1. [error-logging](./error-logging.md)
  1. [data-protection](./data-protection.md)
  1. [commumnications](./commumnications.md)
  1. [malicious-code](./malicious-code.md)
  1. [business_logic](./business_logic.md)
  1. [files-resources](./files-resources.md)
  1. [api](./api.md)
  1. [configuration-management](./configuration-management.md)
  
  ## other resources
  - [Glossary](./glossary.md)

## Introduction 

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

