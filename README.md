# ili2mermaid

It's a ignorant mermaid. Still a prototype.

Makes MD Mermaid from INTERLIS classes and associations. Ignores the rest.

Make from this:
```
```

This:
```
```

## How it goes

```
pip install ili2mermaid
```

```
>>> import ili2mermaid

>>> ili2mermaid.maid( ilicontent='', theme='dark')

>>> ili2mermaid.maid_from_file( ilifile='ResidentialPlanning_V1.ili', theme='dark')

>>> ili2mermaid.md_from_file( ilifile='ResidentialPlanning_V1.ili', theme='dark', outputfile='residentialplanning_v1.md')
```

