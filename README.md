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

- # Methods:
  
# clean_file()
cleans up the file

# is_empty()
checks if the file is empty or not

# _check_data() -> removes delimeters from headers and rows elements
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

## output if remove_del_thg is True: 

headers: ['Gola', 'Status']

rows: [['Viper', 'Lol'], [16, 23, 20], [1, 0, 1]]


## output if remove_del_thg is False:

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
----------------------------------------------------

# structure_data()

Takes each element from a row and adds it to a list (list_to_add)

and then adds to another list (prepared_data)

```py
from vdatasaver import CsvHome

writer = CsvHome('File_name.csv', delimeter=',')

headers = ['Names', 'Age', 'lol']

rows = [['Viper', 'Nolan', 'Golang'], [3, 4, 23], ['extra', 'eatr', 'extr']]

# Just a test, won't be able to use outside the class
print(writer.structure_data(headers, *rows))
```

## output:

rows = [['Viper', 3, 'extra'], ['Nolan', 4, 'eatr'], ['Golang', 23, 'extr']]

----------------------------------------------------
----------------------------------------------------

# write_file()

```py
from vdatasaver import CsvHome

writer = CsvHome('File_name.csv', delimeter=',')

headers = ['Names', 'Age', 'Status']

rows = [['Viper', 'Nolan', 'Golang'], [3, 4, 23], ['extra', 'eatr', 'extr']]

# Just a test, won't be able to use outside the class
print(writer.write_file(headers, *rows, fil_up=Optional, check_file=Optional, remove_del_thg=Optional))
```

## output if check_file is False or there is no data in the file: 

| Names  | Age | Status |
| ------ | --- | ------ |
| Viper  | 3   |  extra |
| Nolan  | 4   |  eatr  |
| Golang | 23  |  extr  |

## output if check_file is True or there is some data in the file:
```py
if is_empty(self.file_name):
    return 'Empty file'
else:
    return 'Some data in file'
```
