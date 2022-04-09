# Auxiliary

> Auto-generated documentation for [checkpasswords.auxiliary](../../../checkpasswords/auxiliary.py) module.

Auxiliary functions used by the credentials class

- [Checkpasswords](../README.md#checkpasswords-index) / [Modules](../MODULES.md#checkpasswords-modules) / [Checkpasswords](index.md#checkpasswords) / Auxiliary
    - [ZxcvbnScore](#zxcvbnscore)
    - [entropyLen](#entropylen)
    - [isHttp](#ishttp)
    - [isMfaAvailable](#ismfaavailable)
    - [isMfaEnabled](#ismfaenabled)
    - [passwordPrint](#passwordprint)
    - [zxcvbnScore](#zxcvbnscore)

## ZxcvbnScore

[[find in source code]](../../../checkpasswords/auxiliary.py#L13)

```python
class ZxcvbnScore(TypedDict):
```

ZxcvbnScore is a dict containing the following attributes:

- score: int
- suggestions: str
- crack_time: float

## entropyLen

[[find in source code]](../../../checkpasswords/auxiliary.py#L50)

```python
def entropyLen(string: str):
```

Calculates the Shannon entropy * length of a string

## isHttp

[[find in source code]](../../../checkpasswords/auxiliary.py#L38)

```python
def isHttp(urlstr: str) -> bool:
```

Use the urls field to determine if http is used instead of https

#### Arguments

- `urlstr` *str* - urlstr field

#### Returns

- `bool` - isHttp

## isMfaAvailable

[[find in source code]](../../../checkpasswords/auxiliary.py#L95)

```python
def isMfaAvailable(urlstr: str) -> bool:
```

Identify if mfa is available using data from https://2fa.directory/

#### Arguments

- `urlstr` *str* - urlstr field

#### Returns

- `bool` - isMfaAvailable

## isMfaEnabled

[[find in source code]](../../../checkpasswords/auxiliary.py#L26)

```python
def isMfaEnabled(notes: str) -> bool:
```

Use the notes field to determine if MFA has been enabled

#### Arguments

- `notes` *str* - notes field

#### Returns

- `bool` - isMfaEnabled

## passwordPrint

[[find in source code]](../../../checkpasswords/auxiliary.py#L78)

```python
def passwordPrint(password: str) -> str:
```

Output a password whilst obfuscating details

#### Arguments

- `password` *str* - raw password

#### Returns

- `str` - obfuscated password

## zxcvbnScore

[[find in source code]](../../../checkpasswords/auxiliary.py#L57)

```python
def zxcvbnScore(password: str) -> ZxcvbnScore:
```

Calculate a ZxcvbnScore from a password

#### Arguments

- `password` *str* - password

#### Returns

- `ZxcvbnScore` - Return a dict of type ZxcvbnScore

#### See also

- [ZxcvbnScore](#zxcvbnscore)
