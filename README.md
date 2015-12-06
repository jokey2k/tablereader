# TableReader

When handling with lots of data in the scientific environment, people often provide data tables as csv, xls or xlsx to you. These commonly have two issues:
They have a header you want to skip when iterating over the rows and they may have unicode data.

Both of these are problematic in Python.

# the solution

```python
from tablereader import TableReader

reader = TableReader("some_input.xlsx", sheet="The Data")
for row in reader:
    print row['valuecolumn']
```

Tested with Python 2.7 and 3.4, depends on xlrd and openpyxl for xl* support
