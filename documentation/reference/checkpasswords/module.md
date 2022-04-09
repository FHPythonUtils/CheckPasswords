# Module

> Auto-generated documentation for [checkpasswords.__main__](../../../checkpasswords/__main__.py) module.

checkpasswords: Uses pass_import to read a password manager source file storing raw
data and infers data such as:

- [Checkpasswords](../README.md#checkpasswords-index) / [Modules](../MODULES.md#checkpasswords-modules) / [Checkpasswords](index.md#checkpasswords) / Module
    - [main](#main)

- zxcvbnScore
- isPasswordDuplicate
- passwordPrint
- isHttp
- isMfaAvailable
- isMfaEnabled

Used to:

- check for duplicate passwords
- check for weak passwords
- identify http sites
- list available 2fa options using data from https://2fa.directory/
- list emails to submit to HIBP or similar

## main

[[find in source code]](../../../checkpasswords/__main__.py#L29)

```python
def main():
```

Main entry point.
