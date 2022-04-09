# Output

> Auto-generated documentation for [checkpasswords.io.output](../../../../checkpasswords/io/output.py) module.

Output

- [Checkpasswords](../../README.md#checkpasswords-index) / [Modules](../../MODULES.md#checkpasswords-modules) / [Checkpasswords](../index.md#checkpasswords) / [Io](index.md#io) / Output
    - [ansi](#ansi)
    - [jsonF](#jsonf)
    - [markdown](#markdown)
    - [plainText](#plaintext)
    - [raw](#raw)
    - [rawCsv](#rawcsv)
    - [stripAnsi](#stripansi)

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

## ansi

[[find in source code]](../../../../checkpasswords/io/output.py#L45)

```python
def ansi(credentials: list[Credentials]) -> str:
```

Format to ansi

#### Arguments

- `credentials` *list[Credentials]* - list of credentials parsed from some input file.
Such as a bitwarden export to CSV

#### Returns

- `str` - string to send to specified output in ansi format

#### See also

- [Credentials](../credentials.md#credentials)

## jsonF

[[find in source code]](../../../../checkpasswords/io/output.py#L176)

```python
def jsonF(credentials: list[Credentials]) -> str:
```

Format to json

#### Arguments

- `credentials` *list[Credentials]* - list of credentials parsed from some input file.
Such as a bitwarden export to CSV

#### Returns

- `str` - string to send to specified output in json format

#### See also

- [Credentials](../credentials.md#credentials)

## markdown

[[find in source code]](../../../../checkpasswords/io/output.py#L133)

```python
def markdown(credentials: list[Credentials]) -> str:
```

Format to markdown

#### Arguments

- `credentials` *list[Credentials]* - list of credentials parsed from some input file.
Such as a bitwarden export to CSV

#### Returns

- `str` - string to send to specified output in markdown format

#### See also

- [Credentials](../credentials.md#credentials)

## plainText

[[find in source code]](../../../../checkpasswords/io/output.py#L120)

```python
def plainText(credentials: list[Credentials]) -> str:
```

Format to plain text

#### Arguments

- `credentials` *list[Credentials]* - list of credentials parsed from some input file.
Such as a bitwarden export to CSV

#### Returns

- `str` - string to send to specified output in plain text format

#### See also

- [Credentials](../credentials.md#credentials)

## raw

[[find in source code]](../../../../checkpasswords/io/output.py#L214)

```python
def raw(credentials: list[Credentials]) -> str:
```

Format to raw json

#### Arguments

- `credentials` *list[Credentials]* - list of credentials parsed from some input file.
Such as a bitwarden export to CSV

#### Returns

- `str` - string to send to specified output in raw json format

#### See also

- [Credentials](../credentials.md#credentials)

## rawCsv

[[find in source code]](../../../../checkpasswords/io/output.py#L227)

```python
def rawCsv(credentials: list[Credentials]) -> str:
```

Format to raw csv

#### Arguments

- `credentials` *list[Credentials]* - list of credentials parsed from some input file.
Such as a bitwarden export to CSV

#### Returns

- `str` - string to send to specified output in raw csv format

#### See also

- [Credentials](../credentials.md#credentials)

## stripAnsi

[[find in source code]](../../../../checkpasswords/io/output.py#L33)

```python
def stripAnsi(string: str) -> str:
```

Strip ansi codes from a given string

#### Arguments

- `string` *str* - string to strip codes from

#### Returns

- `str` - plaintext, utf-8 string (safe for writing to files)
