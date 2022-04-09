# Input

> Auto-generated documentation for [checkpasswords.io.input](../../../../checkpasswords/io/input.py) module.

Use pass_import to convert an ambiguous password manager source file to a list[Credentials]

- [Checkpasswords](../../README.md#checkpasswords-index) / [Modules](../../MODULES.md#checkpasswords-modules) / [Checkpasswords](../index.md#checkpasswords) / [Io](index.md#io) / Input
    - [passImport](#passimport)

## passImport

[[find in source code]](../../../../checkpasswords/io/input.py#L12)

```python
def passImport(path: str, manager: str | None = None) -> list[Credentials]:
```

Use pass_import to convert an ambiguous source file to a list[Credentials]

#### Arguments

- `path` *str* - path to password source file
- `manager` *str, optional* - specify a pasword manager if pass_import fails to identify it.
Defaults to None.

#### Returns

- `list[Credentials]` - list of credentials used by the rest of checkpasswords
