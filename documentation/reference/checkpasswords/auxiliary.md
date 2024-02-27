# Auxiliary

[Checkpasswords Index](../README.md#checkpasswords-index) / [Checkpasswords](./index.md#checkpasswords) / Auxiliary

> Auto-generated documentation for [checkpasswords.auxiliary](../../../checkpasswords/auxiliary.py) module.

- [Auxiliary](#auxiliary)
  - [ZxcvbnScore](#zxcvbnscore)
  - [entropyLen](#entropylen)
  - [isHttp](#ishttp)
  - [isMfaAvailable](#ismfaavailable)
  - [isMfaEnabled](#ismfaenabled)
  - [passwordPrint](#passwordprint)
  - [zxcvbnScore](#zxcvbnscore)

## ZxcvbnScore

[Show source in auxiliary.py:13](../../../checkpasswords/auxiliary.py#L13)

ZxcvbnScore is a dict containing the following attributes.

- score: int
- suggestions: str
- crack_time: float

#### Signature

```python
class ZxcvbnScore(TypedDict): ...
```



## entropyLen

[Show source in auxiliary.py:72](../../../checkpasswords/auxiliary.py#L72)

Calculate the Shannon entropy * length of a string.

#### Signature

```python
def entropyLen(string: str) -> float: ...
```



## isHttp

[Show source in auxiliary.py:57](../../../checkpasswords/auxiliary.py#L57)

Use the urls field to determine if http is used instead of https.

#### Arguments

----
 - `urlstr` *str* - urlstr field

#### Returns

-------
 - `bool` - isHttp

#### Signature

```python
def isHttp(urlstr: str) -> bool: ...
```



## isMfaAvailable

[Show source in auxiliary.py:123](../../../checkpasswords/auxiliary.py#L123)

Identify if mfa is available using data from https://2fa.directory/.

#### Arguments

----
 - `urlstr` *str* - urlstr field

#### Returns

-------
 - `bool` - isMfaAvailable

#### Signature

```python
def isMfaAvailable(urlstr: str) -> bool: ...
```



## isMfaEnabled

[Show source in auxiliary.py:26](../../../checkpasswords/auxiliary.py#L26)

Use the notes field to determine if MFA has been enabled.

#### Arguments

----
 - `notes` *str* - notes field

#### Returns

-------
 - `bool` - isMfaEnabled

#### Signature

```python
def isMfaEnabled(notes: str) -> bool: ...
```



## passwordPrint

[Show source in auxiliary.py:103](../../../checkpasswords/auxiliary.py#L103)

Output a password whilst obfuscating details.

#### Arguments

----
 - `password` *str* - raw password

#### Returns

-------
 - `str` - obfuscated password

#### Signature

```python
def passwordPrint(password: str) -> str: ...
```



## zxcvbnScore

[Show source in auxiliary.py:79](../../../checkpasswords/auxiliary.py#L79)

Calculate a ZxcvbnScore from a password.

#### Arguments

----
 - `password` *str* - password

#### Returns

-------
 - [ZxcvbnScore](#zxcvbnscore) - Return a dict of type ZxcvbnScore

#### Signature

```python
def zxcvbnScore(password: str) -> ZxcvbnScore: ...
```

#### See also

- [ZxcvbnScore](#zxcvbnscore)