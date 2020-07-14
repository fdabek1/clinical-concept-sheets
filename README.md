# Clinical Concept Sheets

## What is this?

A library containing mappings for EHR codes (i.e. ICD-9, ICD-10). These mappings can be downloaded, or simply used within Python or R.

## Installation

> pip install ehr-code-mappings

## Documentation

The documentation can be found at: https://fdabek1.github.io/clinical-concept-sheets/

## Example

```python
import ehr_code_mappings as mappings

result = mappings.load_mapping('ccs_icd10')
print(result.head())
```

|  Code | Single | Level1 | Level2 |
|:-----:|:------:|:------:|:------:|
|  A000 |   135  |    9   |   9.1  |
|  A001 |   135  |    9   |   9.1  |
|  A009 |   135  |    9   |   9.1  |
| A0100 |   135  |    9   |   9.1  |
| A0101 |   76   |    6   |   6.1  |