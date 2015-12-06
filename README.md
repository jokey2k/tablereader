# TableReader

TableReader is an unified abstraction for handling xls, xlsx and CSV files in Python. It also reads csv tables as unicode on request.

If you are familiar with csv.DictReader from the standard library, think of TableReader as DictReader on steroids.

.. code-block:: python

    from tablereader import TableReader

    reader = TableReader("some_input.xlsx", sheet="The Data")
    for row in reader:
        print row['valuecolumn']

In case you have csv and need unicode support:

.. code-block:: python

    reader = TableReader("unicode_input.csv", force_type="unicodecsv")
    for row in reader:
        print row['valuecolumn']

If you want to strip out leading and trailing spaces while reading rows, you can:

.. code-block:: python

    reader = TableReader("input_with_whitespaces.csv", strip_whitespaces=True)
    for row in reader:
        print row['valuecolumn']

And if for some reason you have a file with wrong type by line-ending (commonly found when sharing xls), override auto-detection:

.. code-block:: python

    reader = TableReader("wrong_named.xls", force_type="xlsx")
    for row in reader:
        print row['valuecolumn']

Sometimes headers are not in the first line. So specify some header row search text and the entire row will be used as column name and all rows after are returned:

.. code-block:: python

    from tablereader import OffsetTableReader

    reader = OffsetTableReader("wrong_named.xls", "BEGIN_DATA")
    for row in reader:
        print row['valuecolumn']

The library has been tested on CPython 2.6, 2.7 and 3.4 as well as PyPy 2.4.1.