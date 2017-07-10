# book-metadata-jsonld
Read book metadata from a spreadsheet an produce JSON-LD scripts in http://schema.org/Book format

## Usage

```bash
book-json-ld metadata.xlsx
```

### Parameters

| Parameter            | Description                                                                                                         |
|----------------------|---------------------------------------------------------------------------------------------------------------------|
| `-f`, `--force`      | Overwrite existing scripts (if any). Defaults to false.                                                             |
| `-o`, `--output-dir` | Specify a directory to output the scripts. Defaults to,a directory called "scripts" within the path of this script. |

All parameters are optional and have a default value.

## Dependencies

| Package | Version | URL                                                                    |
|---------|---------|------------------------------------------------------------------------|
| xlrd    | 1.0.0   | [https://pypi.python.org/pypi/xlrd](https://pypi.python.org/pypi/xlrd) |
