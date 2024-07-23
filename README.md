# WTF (What's this for?)

Vibrant continues to invest in securing data critical to help seekers; and increasingly we are learning that we write software.

This repository contains Vibrant's development of software security requirements.  It is maintained by the InfoSec team, specifically [Eoin](https://github.com/Celtikill).

## Security Requirements

We recommend treating all requirements with a mild skepticism.  Having said that, we also enjoy (shall we say) vibrant discussion.

Please consider these a starting point for understanding general security within the context of modern software.

>[!NOTE]
> As read on the cover of the Guide . . . DON'T PANIC.  This is only a draft.

### Origins

InfoSec chose the latest release of [OWASP Application Security Verification Standard](https://github.com/OWASP/ASVS) as the inspiration for Vibrant's security requirements, for a variety of reasons.  Here are a few:

- it maps directly to NIST guidelines
- it offers tiers of requirements, allowing for variation in maturity and risk management
- it represents consensus best-practice within a global application security community

We currently fork the [actual ASVS](./ASVS_docs/README.md) into this repository (periodically) for quick & easy reference.

## Usage

At least initially, this documentation will be used by InfoSec to measure systems against consensus best practice (informed by NIST).

As we understand need and appetite, we will work with you (dear reader) to craft [SMART](https://en.wikipedia.org/wiki/SMART_criteria) requirements for your specific system development needs. (together ::hearts::) 

Here's how we do this.

### Validation

InfoSec uses the full ASVS, unedited, as our [validation standard](./validation_requirements/INDEX.md) for all applications.  If we encounter software not matching the ASVS model, we will adapt.

### System Development

You may use a [maturity-calibrated](./system_requirements/INDEX.md) set of requirements as a way to reach Vibrant's "next step" assurance level.

> [!IMPORTANT]
> This set of requirements in no way represents a complete alignment to NIST.  Consider it Vibrant's (give or take) consensus "next step" security assurance for your application.

## References

- [Glossary of terms](./glossary.md)
