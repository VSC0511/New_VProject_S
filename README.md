<--------vdatasaver.py-------->
CsvHome: Class for csv files

# file name where data will be written
self.file_name = file_name

# Columns of a csv file or headers
self._columns: list = []

# Rows it is a matrix [[], [], ...]
self._rows: list = []

# Delimeter to separate rows and headers
# By default is delimeter is a comma -> ,
self.delimeter = delimeter

# Used to fill up short headers, rows or rows elements
# headers = ['Names', 'Age']
# rows = [['Viper'], [23, 45, 23], [3, 4]]
# headers will be filled up with numbers starting from 0
# headers: ['Names', 'Age', 0]
# fills up short rows until their length fit the longest one(3)
# rows: [['Viper', '', ''], [23, 45, 23], [3, 4, '']]

# or by default fill_up is False
# if either headers or rows are empty raises an Exception
# cuts off headers and rows to the shortest length
# headers = ['Names', 'Age']
# rows = [['Viper'], [23, 45, 23], [3, 4]]
# cuts off headers and makes equal to the number of rows(3)
# and deletes rows elements until the row fits the shortest one (['Viper'])
# headers  = ['Names', 'Age']
# rows = [['Viper'], [2]]
self.fill_up = False

# Removes delimeters in headers and rows
self.remove_del_thg = False


# if remove_del_thg is false raises an excetion
# else just removes elements with the delimeter
_check_data() -> removes delimeters from headers and rows elements


# if headers and rows are empty raises an exception
_prepare_length() -> prepares headers and rows length for structuring


structure_data() -> structures rows for writing
# each first element of each row to another list
# and then this list is added to prepared_data list


# check_file used to avoid wring data again if any data in the file
write_file() -> writes headers and rows into a csv file


# if check_headers is True adds headers if there aren't any in the file
# raises an error if new data doesn't fit in-file rows 
add_data() -> adds data to the file


# if start and end are None takes line's data
# if line is empty raises an Exception
take_back() -> retrives data in the original form


