# Output

[Checkpasswords Index](../../README.md#checkpasswords-index) /
[Checkpasswords](../index.md#checkpasswords) /
[Io](./index.md#io) /
Output

> Auto-generated documentation for [checkpasswords.io.output](../../../../checkpasswords/io/output.py) module.

- [Output](#output)
  - [ansi](#ansi)
  - [jsonF](#jsonf)
  - [markdown](#markdown)
  - [plainText](#plaintext)
  - [raw](#raw)
  - [rawCsv](#rawcsv)

## ansi

[Show source in output.py:45](../../../../checkpasswords/io/output.py#L45)

Format to ansi

#### Arguments

- `credentials` *list[Credentials]* - list of credentials parsed from some input file.
Such as a bitwarden export to CSV

#### Returns

- `str` - string to send to specified output in ansi format

#### Signature

```python
def ansi(credentials: list[Credentials]) -> str:
    ...
```

#### See also

- [Credentials](../credentials.md#credentials)



## jsonF

[Show source in output.py:176](../../../../checkpasswords/io/output.py#L176)

Format to json

#### Arguments

- `credentials` *list[Credentials]* - list of credentials parsed from some input file.
Such as a bitwarden export to CSV

#### Returns

- `str` - string to send to specified output in json format

#### Signature

```python
def jsonF(credentials: list[Credentials]) -> str:
    ...
```

#### See also

- [Credentials](../credentials.md#credentials)



## markdown

[Show source in output.py:133](../../../../checkpasswords/io/output.py#L133)

Format to markdown

#### Arguments

- `credentials` *list[Credentials]* - list of credentials parsed from some input file.
Such as a bitwarden export to CSV

#### Returns

- `str` - string to send to specified output in markdown format

#### Signature

```python
def markdown(credentials: list[Credentials]) -> str:
    ...
```

#### See also

- [Credentials](../credentials.md#credentials)



## plainText

[Show source in output.py:120](../../../../checkpasswords/io/output.py#L120)

Format to plain text

#### Arguments

- `credentials` *list[Credentials]* - list of credentials parsed from some input file.
Such as a bitwarden export to CSV

#### Returns

- `str` - string to send to specified output in plain text format

#### Signature

```python
def plainText(credentials: list[Credentials]) -> str:
    ...
```

#### See also

- [Credentials](../credentials.md#credentials)



## raw

[Show source in output.py:214](../../../../checkpasswords/io/output.py#L214)

Format to raw json

#### Arguments

- `credentials` *list[Credentials]* - list of credentials parsed from some input file.
Such as a bitwarden export to CSV

#### Returns

- `str` - string to send to specified output in raw json format

#### Signature

```python
def raw(credentials: list[Credentials]) -> str:
    ...
```

#### See also

- [Credentials](../credentials.md#credentials)



## rawCsv

[Show source in output.py:227](../../../../checkpasswords/io/output.py#L227)

Format to raw csv

#### Arguments

- `credentials` *list[Credentials]* - list of credentials parsed from some input file.
Such as a bitwarden export to CSV

#### Returns

- `str` - string to send to specified output in raw csv format

#### Signature

```python
def rawCsv(credentials: list[Credentials]) -> str:
    ...
```

#### See also

- [Credentials](../credentials.md#credentials)


