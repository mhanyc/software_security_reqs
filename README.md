# System Security Requirements

Vibrant continues to invest in securing service delivery and proteching data critical to help seekers.  Meanwhile, we are learning again that we write software.

This repository contains Vibrant's development of system security requirements.  It is maintained by the InfoSec team.

# Requirements Index 

  1. [architecture](./1-architecture.md)
  3. [authentication](./i2-authentication.md)
  4. [session management](./3-session-management.md)
  6. [access control](./4-access-control.md)
  7. [validation, sanitation, & encoding](./5-validation-sanitation-encoding.md)
  8. [cryptography](./6-cryptography.md)
  9. [error logging](./7-error-logging.md)
  10. [data protection](./8-data-protection.md)
  11. [commumnications](./9-commumnications.md)
  12. [malicious code](./10-malicious-code.md)
  13. [business logic](./11-business-logic.md)
  14. [files resources](./12-files-resources.md)
  15. [api](./13-api.md)
  16. [configuration management](./14-configuration-management.md)
  
  ## other resources
  - [Glossary](./glossary.md)
  - [Origin Requirements Framework](https://owasp.org/www-project-application-security-verification-standard/)

# Introduction 

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

