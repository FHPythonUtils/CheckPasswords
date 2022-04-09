# Changelog

All major and minor version changes will be documented in this file. Details of
patch-level version changes can be found in [commit messages](../../commits/master).

## 2022.0.1 - 2022/04/09

- First release

Uses pass_import to read a password manager source file storing raw data and infers data such as:

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

Output

- summary table
- duplicate passwords table
- weak passwords table
- http sites table
- enable2fa table
- emails table

To one of the following formats:

- ansi
- plain
- markdown
- json
- raw
- raw-csv
