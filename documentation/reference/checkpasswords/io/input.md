# Input

[Checkpasswords Index](../../README.md#checkpasswords-index) / [Checkpasswords](../index.md#checkpasswords) / [Io](./index.md#io) / Input

> Auto-generated documentation for [checkpasswords.io.input](../../../../checkpasswords/io/input.py) module.

- [Input](#input)
  - [passImport](#passimport)
  - [transformPass](#transformpass)

## passImport

[Show source in input.py:14](../../../../checkpasswords/io/input.py#L14)

Use pass_import to convert an ambiguous source file to a list[Credentials].

#### Arguments

----
 - `path` *str* - path to password source file
 - `manager` *str, optional* - specify a pasword manager if pass_import fails to identify it.
 Defaults to None.

#### Returns

-------
 - `list[Credentials]` - list of credentials used by the rest of checkpasswords

#### Signature

```python
def passImport(path: str, manager: str | None = None) -> list[Credentials]: ...
```

#### See also

- [Credentials](../credentials.md#credentials)



## transformPass

[Show source in input.py:55](../../../../checkpasswords/io/input.py#L55)

Convert pass_import representation to checkpasswords representation (list[Credentials]).

:param dict list[dict]: pass_import representation

#### Returns

Type: *list[Credentials]*
checkpasswords representation

#### Signature

```python
def transformPass(data: list[dict]) -> list[Credentials]: ...
```

#### See also

- [Credentials](../credentials.md#credentials)