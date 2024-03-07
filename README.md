# *vdatasaver.py*
## CsvHome: Methods for csv files

- ## Attributes
  - ### self.file_name: str
     file name where data will be written
    
  - ### self._columns: list
    Columns of a csv file or headers
    
  - ### self._rows: list[list]
    Rows it is a matrix [[], [], ...]
    
  - ### self.delimeter: str
    Delimeter to separate rows and headers.
    By default, delimeter is a comma -> ,
    
  - ### self.fill_up: bool
    for _prepare_length() as an option
    
----------------------------------------------------
----------------------------------------------------
----------------------------------------------------

## _check_data() -> removes delimeters from headers and rows elements
if remove_del_thg is false raises an excetion
else just removes elements with the delimeter

```py
from vdatasaver import CsvHome

writer = CsvHome('File_name.csv', delimeter=',')

headers = ['Names,', 'Age', 'Status']

rows = [['Viper', 'Gola,', 'Lol'],
        [16, 23, 20], [1, 0, 1]]

# Checking delimeters in data
# just a test you won't be able to use this function 
writer._check_data(headers, *rows, remove_del_thg = True)
```

### output if remove_del_thg is True: 

headers: ['Gola', 'Status']

rows: [['Viper', 'Lol'], [16, 23, 20], [1, 0, 1]]


### output if remove_del_thg is False:

*raise DelimeterInColumns('No delimeter!')*

vdatasaver.DelimeterInColumns: No delimeter!

----------------------------------------------------


# _prepare_length()
*if headers and rows are empty raises an exception*

## if fill up is True:
*1) Adds extra numbers starting from zero to headers when the number of headers doesn't equal to the number of rows*

```py
from vdatasaver import CsvHome

writer = CsvHome('File_name.csv', delimeter=',')

headers = ['Names', 'Age']

rows = [['Viper', 'gola', 'adff'], [16, 23, 20], [3, 4, 23]]

# Preparing lengths
# just a test you won't be able to use this function 
writer._prepare_length(headers, *rows, fill_up=True)

```
## output: 

headers: ['Names', 'Age', 0] <-- zero

rows: [['Viper', 'gola', 'adff'], [16, 23, 20], [3, 4, 23]]

----------------------------------------------------


*2) Adds extra row(list) to rows when the number of rows doesn't equal to the number of headers*

```py
from vdatasaver import CsvHome

writer = CsvHome('File_name.csv', delimeter=',')

headers = ['Names', 'Age', 'lol', 'extra']

rows = [['Viper', 'gola', 'adff'],[16, 23, 20], [3, 4, 23]]

# Preparing lengths
# just a test you won't be able to use this function 
writer._prepare_length(headers, *rows, fill_up=True)

```
## output: 

headers: ['Names', 'Age', 'lol', 'extra']

rows: [['Viper', 'gola', 'adff'], [16, 23, 20], [3, 4, 23], ['', '', '']]

----------------------------------------------------


*3) Adds empty values toshort rows till the short row equals the longest one*

```py
from vdatasaver import CsvHome

writer = CsvHome('File_name.csv', delimeter=',')

headers = ['Names', 'Age', 'lol']

rows = [['Viper'],[16, 23], [3, 4, 23]]

# Preparing lengths
# just a test you won't be able to use this function 
writer._prepare_length(headers, *rows, fill_up=True)

```
## output: 

headers: ['Names', 'Age', 'lol']

rows: [['Viper', '', ''], [16, 23, ''], [3, 4, 23]]

----------------------------------------------------

## if fill up is false:

*Raises an exception if either headers or rows are empty.*

----------------------------------------------------

*Deletes rows if the number of headers is less than the number of rows.*

```py
from vdatasaver import CsvHome

writer = CsvHome('File_name.csv', delimeter=',')

headers = ['Names', 'Age', 'lol']

rows = [['Viper'],[16, 23], [3, 4, 23], ['extra', 'eatr', 'extr', 'we']]

# Preparing lengths
# just a test you won't be able to use this function 
writer._prepare_length(headers, *rows, fill_up=False)
```

## output: 

headers: ['Names', 'Age', 'lol']

rows: [['Viper'], [16], [3]]

----------------------------------------------------

*Deletes headers if the number of rows is less than the number of headers.*

```py
from vdatasaver import CsvHome

writer = CsvHome('File_name.csv', delimeter=',')

headers = ['Names', 'Age', 'lol', 'ada', 'aaww', 'add']

rows = [['Viper'],[16, 23], [3, 4, 23], ['extra', 'eatr', 'extr', 'we']]

# Preparing lengths
# just a test you won't be able to use this function 
writer._prepare_length(headers, *rows, fill_up=False)
```

## output: 

headers: ['Names', 'Age', 'lol', 'ada']

rows: [['Viper'], [16], [3], ['extra']]

----------------------------------------------------

*Deletes rows elements till this row's length fits the shortest one*

```py
from vdatasaver import CsvHome

writer = CsvHome('File_name.csv', delimeter=',')

headers = ['Names', 'Age', 'lol']

rows = [['Viper'],[16, 23], [3, 4, 23], ['extra', 'eatr', 'extr', 'we']]

# Preparing lengths
# just a test you won't be able to use this function 
writer._prepare_length(headers, *rows, fill_up=False)
```

## output: 

headers: ['Names', 'Age', 'lol']

rows: [['Viper'], [16], [3]]

----------------------------------------------------


# structure_data()

## output if there is no data in the file: 

| Names | Age | Status |
| ----- | --- | ------ |
| Viper | 16  |    1   |
| Gola  | 23  |    0   |
| Lol   | 20  |    1   |


