# Output

[Checkpasswords Index](../../README.md#checkpasswords-index) / [Checkpasswords](../index.md#checkpasswords) / [Io](./index.md#io) / Output

> Auto-generated documentation for [checkpasswords.io.output](../../../../checkpasswords/io/output.py) module.

- [Output](#output)
  - [_stripAnsi](#_stripansi)
  - [ansi](#ansi)
  - [jsonF](#jsonf)
  - [markdown](#markdown)
  - [plainText](#plaintext)
  - [raw](#raw)
  - [rawCsv](#rawcsv)

## _stripAnsi

[Show source in output.py:36](../../../../checkpasswords/io/output.py#L36)

Strip ansi codes from a given string.

#### Arguments

----
 - `string` *str* - string to strip codes from

#### Returns

-------
 - `str` - plaintext, utf-8 string (safe for writing to files)

#### Signature

```python
def _stripAnsi(string: str) -> str: ...
```



## ansi

[Show source in output.py:51](../../../../checkpasswords/io/output.py#L51)

Format to ansi.

#### Arguments

----
 - `credentials` *list[Credentials]* - list of credentials parsed from some input file.
 Such as a bitwarden export to CSV

#### Returns

-------
 - `str` - string to send to specified output in ansi format

#### Signature

```python
def ansi(credentials: list[Credentials]) -> str: ...
```

#### See also

- [Credentials](../credentials.md#credentials)



## jsonF

[Show source in output.py:197](../../../../checkpasswords/io/output.py#L197)

Format to json.

#### Arguments

----
 - `credentials` *list[Credentials]* - list of credentials parsed from some input file.
 Such as a bitwarden export to CSV

#### Returns

-------
 - `str` - string to send to specified output in json format

#### Signature

```python
def jsonF(credentials: list[Credentials]) -> str: ...
```

#### See also

- [Credentials](../credentials.md#credentials)



## markdown

[Show source in output.py:147](../../../../checkpasswords/io/output.py#L147)

Format to markdown.

#### Arguments

----
 - `credentials` *list[Credentials]* - list of credentials parsed from some input file.
 Such as a bitwarden export to CSV

#### Returns

-------
 - `str` - string to send to specified output in markdown format

#### Signature

```python
def markdown(credentials: list[Credentials]) -> str: ...
```

#### See also

- [Credentials](../credentials.md#credentials)



## plainText

[Show source in output.py:131](../../../../checkpasswords/io/output.py#L131)

Format to plain text.

#### Arguments

----
 - `credentials` *list[Credentials]* - list of credentials parsed from some input file.
 Such as a bitwarden export to CSV

#### Returns

-------
 - `str` - string to send to specified output in plain text format

#### Signature

```python
def plainText(credentials: list[Credentials]) -> str: ...
```

#### See also

- [Credentials](../credentials.md#credentials)



## raw

[Show source in output.py:242](../../../../checkpasswords/io/output.py#L242)

Format to raw json.

#### Arguments

----
 - `credentials` *list[Credentials]* - list of credentials parsed from some input file.
 Such as a bitwarden export to CSV

#### Returns

-------
 - `str` - string to send to specified output in raw json format

#### Signature

```python
def raw(credentials: list[Credentials]) -> str: ...
```

#### See also

- [Credentials](../credentials.md#credentials)



## rawCsv

[Show source in output.py:258](../../../../checkpasswords/io/output.py#L258)

Format to raw csv.

#### Arguments

----
 - `credentials` *list[Credentials]* - list of credentials parsed from some input file.
 Such as a bitwarden export to CSV

#### Returns

-------
 - `str` - string to send to specified output in raw csv format

#### Signature

```python
def rawCsv(credentials: list[Credentials]) -> str: ...
```

#### See also

- [Credentials](../credentials.md#credentials)