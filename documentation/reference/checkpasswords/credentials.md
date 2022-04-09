# Credentials

> Auto-generated documentation for [checkpasswords.credentials](../../../checkpasswords/credentials.py) module.

Credentials class and associated methods

- [Checkpasswords](../README.md#checkpasswords-index) / [Modules](../MODULES.md#checkpasswords-modules) / [Checkpasswords](index.md#checkpasswords) / Credentials
    - [Credentials](#credentials)
        - [Credentials().\_\_post\_init\_\_](#credentials__post_init__)
    - [applyPasswordDuplicate](#applypasswordduplicate)
    - [emails](#emails)
    - [generateTables](#generatetables)
    - [orderCredentials](#ordercredentials)

## Credentials

[[find in source code]](../../../checkpasswords/credentials.py#L18)

```python
dataclass
class Credentials():
```

Credentials storing raw data from IO and inferred data such as:
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

### Credentials().\_\_post\_init\_\_

[[find in source code]](../../../checkpasswords/credentials.py#L47)

```python
def __post_init__():
```

Populate/ update various attributes using auxiliary functions

## applyPasswordDuplicate

[[find in source code]](../../../checkpasswords/credentials.py#L60)

```python
def applyPasswordDuplicate(credentials: list[Credentials]):
```

Apply duplicate password flag to each credentials

#### Arguments

- `credentials` *list[Credentials]* - list of all credentials

#### See also

- [Credentials](#credentials)

## emails

[[find in source code]](../../../checkpasswords/credentials.py#L73)

```python
def emails(credentials: list[Credentials]) -> set[str]:
```

Return a set of unique emails from the list of credentials

#### Arguments

- `credentials` *list[Credentials]* - list of all credentials

#### Returns

- `set[str]` - set of unique emails

#### See also

- [Credentials](#credentials)

## generateTables

[[find in source code]](../../../checkpasswords/credentials.py#L98)

```python
def generateTables(
    credentials: list[Credentials],
) -> tuple[list[tuple[str, ...]], ...]:
```

generateTables

#### Arguments

- `credentials` *list[Credentials]* - list of credentials parsed from some input file.
Such as a bitwarden export to CSV

#### See also

- [Credentials](#credentials)

## orderCredentials

[[find in source code]](../../../checkpasswords/credentials.py#L85)

```python
def orderCredentials(credentials: list[Credentials]) -> list[Credentials]:
```

Order credentials by password crack time

#### Arguments

- `credentials` *list[Credentials]* - list of credentials parsed from some input file.
Such as a bitwarden export to CSV

#### Returns

- `list[Credentials]` - sorted credentials

#### See also

- [Credentials](#credentials)
