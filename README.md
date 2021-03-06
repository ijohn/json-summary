```
   _
  (_)___  ___  _ __        ___ _   _ _ __ ___  _ __ ___   __ _ _ __ _   _
  | / __|/ _ \| '_ \ _____/ __| | | | '_ ` _ \| '_ ` _ \ / _` | '__| | | |
  | \__ \ (_) | | | |_____\__ \ |_| | | | | | | | | | | | (_| | |  | |_| |
 _/ |___/\___/|_| |_|     |___/\__,_|_| |_| |_|_| |_| |_|\__,_|_|   \__, |
|__/                                                                |___/

```

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![mypy: checked](https://img.shields.io/badge/mypy-checked-green)](http://mypy-lang.org)
[![codecov](https://codecov.io/gh/ijohn/json-summary/branch/main/graph/badge.svg?token=VOXVoogjSK)](https://codecov.io/gh/ijohn/json-summary)

Ever wanted to view summary of a complex JSON? `json-summary` could help you.

Let's say you have the following JSON:

```
input_json = {
  "name": "John Doe",
  "height": 160.5,
  "age": 18,
  "friends": [
    {
      "name": "Jane Doe",
      "address": {
        "city": "Jakarta"
      }
    }
  ]
}
```

Feeding above JSON to `json_summary.summarise()` will give the following result:

```
from json_summary import summarise

result = summarise(input_json)

# result
# {
#   "name": "string",
#   "height": "number",
#   "age": "number",
#   "friends": [
#     {
#       "name": "string",
#       "address": {
#         "city": "string"
#       }
#     }
#   ]
# }
```
