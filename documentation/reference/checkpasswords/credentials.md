# Credentials

[Checkpasswords Index](../README.md#checkpasswords-index) / [Checkpasswords](./index.md#checkpasswords) / Credentials

> Auto-generated documentation for [checkpasswords.credentials](../../../checkpasswords/credentials.py) module.

- [Credentials](#credentials)
  - [Credentials](#credentials-1)
    - [Credentials().__post_init__](#credentials()__post_init__)
  - [applyPasswordDuplicate](#applypasswordduplicate)
  - [emails](#emails)
  - [generateTables](#generatetables)
  - [orderCredentials](#ordercredentials)

## Credentials

[Show source in credentials.py:20](../../../checkpasswords/credentials.py#L20)

Credentials storing raw data from IO and inferred data such as:
- zxcvbnScore
- isPasswordDuplicate
- passwordPrint
- isHttp
- isMfaAvailable
- isMfaEnabled.

Used to:
- check for duplicate passwords
- check for weak passwords
- identify http sites
- list available 2fa options using data from https://2fa.directory/

#### Signature

```python
class Credentials: ...
```

### Credentials().__post_init__

[Show source in credentials.py:49](../../../checkpasswords/credentials.py#L49)

Populate/ update various attributes using auxiliary functions.

#### Signature

```python
def __post_init__(self) -> Credentials: ...
```



## applyPasswordDuplicate

[Show source in credentials.py:62](../../../checkpasswords/credentials.py#L62)

Apply duplicate password flag to each credentials.

#### Arguments

----
 - `credentials` *list[Credentials]* - list of all credentials

#### Signature

```python
def applyPasswordDuplicate(credentials: list[Credentials]) -> None: ...
```

#### See also

- [Credentials](#credentials)



## emails

[Show source in credentials.py:77](../../../checkpasswords/credentials.py#L77)

Return a set of unique emails from the list of credentials.

#### Arguments

----
 - `credentials` *list[Credentials]* - list of all credentials

#### Returns

-------
 - `set[str]` - set of unique emails

#### Signature

```python
def emails(credentials: list[Credentials]) -> set[str]: ...
```

#### See also

- [Credentials](#credentials)



## generateTables

[Show source in credentials.py:108](../../../checkpasswords/credentials.py#L108)

generateTables.

#### Arguments

----
 - `credentials` *list[Credentials]* - list of credentials parsed from some input file.
 Such as a bitwarden export to CSV

#### Signature

```python
def generateTables(
    credentials: list[Credentials],
) -> tuple[list[tuple[str, ...]], ...]: ...
```

#### See also

- [Credentials](#credentials)



## orderCredentials

[Show source in credentials.py:92](../../../checkpasswords/credentials.py#L92)

Order credentials by password crack time.

#### Arguments

----
 - `credentials` *list[Credentials]* - list of credentials parsed from some input file.
 Such as a bitwarden export to CSV

#### Returns

-------
 - `list[Credentials]` - sorted credentials

#### Signature

```python
def orderCredentials(credentials: list[Credentials]) -> list[Credentials]: ...
```

#### See also

- [Credentials](#credentials)