# *vdatasaver.py*
## CsvHome: Class for csv files

- ## Attributes
  - ### self.file_name
     file name where data will be written
    
  - ### self._columns
    Columns of a csv file or headers
    
  - ### self._rows
    Rows it is a matrix [[], [], ...]
    
  - ### self.delimeter
    Delimeter to separate rows and headers
    By default is delimeter is a comma -> ,
    
  - ### self.fill_up
    for _prepare_length()

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


## _prepare_length()
*if headers and rows are empty raises an exception.
Used to fill up short headers, rows or rows elements,
headers = ['Names', 'Age'],
rows = [['Viper'], [23, 45, 23], [3, 4]],
headers will be filled up with numbers starting from 0.
fills up short rows until their length fit the longest one(3)*
```py
from vdatasaver import CsvHome

writer = CsvHome('File_name.csv', delimeter=',')

headers = ['Names', 'Age']

rows = [['Viper'],[16, 23, 20], [3, 4]]

# Preparing lengths
# just a test you won't be able to use this function 
writer._prepare_length(headers, *rows, fill_up=True)

```
## output: 

headers: ['Names', 'Age', 0]

rows: [['Viper', '', ''], [16, 23, 20], [3, 4, '']]

----------------------------------------------------

*or by default fill_up is False.
if either headers or rows are empty raises an Exception.
cuts off headers and rows to the shortest length.
headers = ['Names', 'Age']
rows = [['Viper'], [23, 45, 23], [3, 4]].
cuts off headers and makes equal to the number of rows(3)
and deletes rows elements until the row fits the shortest one (['Viper'])
headers  = ['Names', 'Age'],
rows = [['Viper'], [2]].
Removes delimeters in headers and rows
self.remove_del_thg = False
if headers and rows are empty raises an exception
Used to fill up short headers, rows or rows elements
headers = ['Names', 'Age']
rows = [['Viper'], [23, 45, 23], [3, 4]]
headers will be filled up with numbers starting from 0
headers: ['Names', 'Age', 0]
fills up short rows until their length fit the longest one(3)
rows: [['Viper', '', ''], [23, 45, 23], [3, 4, '']]*

```py
headers = ['Names', 'Age']

rows = [['Viper'],[16, 23, 20], [3, 4]]

# Preparing lengths
# just a test you won't be able to use this function 
writer._prepare_length(headers, *rows, fill_up=False)
```

## output if there is no data in the file: 

| Names | Age | Status |
| ----- | --- | ------ |
| Viper | 16  |    1   |
| Gola  | 23  |    0   |
| Lol   | 20  |    1   |


