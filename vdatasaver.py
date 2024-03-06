# Importing neccessary libraries

import os # used to check files

import csv # To write data



# For empty columns
class EmptyColumnsError(Exception):
    pass



# For empty rows
class EmptyRowsError(Exception):
    pass



# For both empty columns and rows
class EmptyColumnsAndRows(Exception):
    pass



# Used when a delimeter in headers
class DelimeterInColumns(Exception):
    pass



# Used when a delimeter in rows elements
class DelimeterInRows(Exception):
    pass
    


# If rows not similar to rows
class NotSimilar(Exception):
    pass



# If file is empty
class EmptyFile(Exception):
    pass



# If line in a file is empty
class EmptyLine(Exception):
    pass



# Cleans up a file
def clean_file(file_name) -> None:
    return open(file_name, 'w').close()


# Check is data in files exists
def is_empty(file_name: str) -> bool:
    return os.path.getsize(file_name) == 0



class CsvHome:
    def __init__(self, file_name: str, 
                 delimeter: str = ',') -> None:
        
        self.file_name = file_name
        self._columns: list = []
        self._rows: list = []
        self.delimeter = delimeter
        self.fill_up = False
        self.remove_del_thg = False
        
    
    def __repr__(self) -> str:
        return "File: {}".format(self.file_name)

    
    def _check_data(self) -> None:
        
        # If option to delete elements where delimeter is in
        if self.remove_del_thg:   
            
            # deleting wrong headers
            for head_indx, head in enumerate(self.columns):
                if self.delimeter in head:
                    self.columns.pop(head_indx)
            
            # deleting wrong rows's elements
            for row in self.rows:
                for indx, inside in enumerate(row):
                    if self.delimeter in inside:
                        row.pop(indx)
        
        else: # Or just awares us about the delimeter
            
            # For headers
            for head in self.columns:
                if self.delimeter in head:
                    raise DelimeterInColumns('No delimeter!')
                
            # For row's elements
            for row in self.rows:
                if self.delimeter in row:
                    raise DelimeterInRows('No delimeter!')
                 
                 
    # Prepares lengths for rown and headers 
    def _prepare_length(self) -> None:
        
        # Cheking delimeters in data
        self._check_data()
        
        # Number of headers
        headers_length: int = len(self.columns)
        
        # Number of elements in rows
        rows_length: int = len(self.rows)

        # Let's prepare out data's length
        # Here we check if one or both of the headers and rows are empty
        if (not self.columns) and (not self.rows):
            raise EmptyColumnsAndRows('No data :(')
            
        # Now let's check if lengths are similar or not
        # fills up empty with empty spaces or number is fill_up is True
        # cuts off to the shortest row or header if cut_off is True
        if self.fill_up: 
            
            # Adds extra elements to short rows
            if headers_length > rows_length:
                for _ in range(headers_length - rows_length):
                    self.rows.append([''])
            
            # Adds extra header if there isn't enought 
            if rows_length > headers_length:
                for new_head in range(rows_length - headers_length):
                    self.columns.append(str(new_head))
        
            rows_elem_length: list = [len(row) for row in self.rows]
              
            # Adds extra elements into rows
            if max(rows_elem_length) != min(rows_elem_length):
                for row in self.rows:
                    while len(row) != max(rows_elem_length):
                        row.append('')
        
        else: # Here we cut off eveything to the shortest vesion
    
            # Can't just cut off without any data
            if not self.columns:
                raise EmptyColumnsError('Columns are empty :(')
            
            if not self.rows:
                raise EmptyRowsError('Rows are empty :(')
            
            # Deletes headers untill it equals to the number of rows
            if headers_length > rows_length:
                for _ in range(headers_length - rows_length):
                    self.columns.pop()

            # deletes rows untill it equals to the number of headers
            if rows_length > headers_length:
                for _ in range(rows_length - headers_length):
                    self.rows.pop()
                    
            rows_elem_length = [len(row) for row in self.rows]
            
            # Takes the shortes length and make all the other rows short
            if max(rows_elem_length) != min(rows_elem_length):
                
                for row in self.rows:
                    # Deletes row's elements until it fits the shortest row
                    while len(row) != min(rows_elem_length):
                        row.pop()


    # Structures data
    def structure_data(self) -> list[list]:
                
        # First, prepares rows and headers to a desired length
        self._prepare_length()
        
        # Will be used to write data to files
        structured_data: list = []
        
        # A point to add data particularly
        list_to_add: list = []

        # Prepares data for future writing
        # Takes each first element of each row and adds it to another list
        # After finishing adds this list to the output list
        for index in range(len(self.rows[0])):
            for value in self.rows:
                # the first element of each row
                list_to_add.append(value[index])
    
            # Adds the list to the final one and makes an empty list
            structured_data.append(list_to_add)
            list_to_add = []  
        
        return structured_data
    
    
    # Creates adn writes data into the file
    def write_file(self, headers: list, *rows: list,
                       fill_up_option: bool = False,
                       check_file: bool = False,
                       remove_del_thg: bool = False) -> None | str:
    
        if check_file:
            if is_empty(self.file_name):
                return 'Empty file'
            else:
                return 'Some data in file'
        
        self.columns = headers
        self.rows = list(rows)
        self.fill_up = fill_up_option
        self.remove_del_thg = remove_del_thg
        
        # Cooked data :>
        prepared_data = self.structure_data()
        
        with open(self.file_name, 'w', newline='') as write_file:
            write_csv = csv.writer(write_file, delimiter=self.delimeter)
            write_csv.writerow(self.columns)
            write_csv.writerows(prepared_data)
    
    
    # Updates the file adding new rows
    def add_data(self, headers: list, *lines: list, 
                fill_up_option: bool = False,
                check_headers: bool = True) -> None:
        
        """_summary_
            check_headers: checks for headers in the file
            
        Raises:
            ValueError: if number of row's elements doesn't fit the existing one
        """
        
        self.columns = headers
        self.rows = list(lines)
        
        self.fill_up = fill_up_option
        
        # Preparing data before writing
        prepared_data = self.structure_data()
        
        # to check if there are any headers
        # If there aren't any headers we write them and continue
        if check_headers:
            with open(self.file_name, 'a', newline='') as addrows:
                
                # need to check if new data fits the in file format 
                # if file is empty writes headers
                if is_empty(self.file_name):
                    writer_headers = csv.writer(addrows, delimiter=self.delimeter)
                    writer_headers.writerow(self.columns)
    
    
        # After checking headers in the file we write rows
        with open(self.file_name, 'r+', newline='') as add_data:
            
            # If headers were written
            # separates headers to check if new data fits existing data
            if check_headers:
                num_of_chars = add_data.readlines()[-1].split(',')
                
                # If false throws an error
                if (len(prepared_data[0]) != len(num_of_chars)):
                    raise NotSimilar('Rows and headers are not the same')
            
            # If headers weren't written we just add a row
            # now we write our new data
            write_rows = csv.writer(add_data, delimiter=self.delimeter)
            write_rows.writerows(prepared_data)


    # Gets data back from a file in the original form
    def take_back(self, line: int = 1, start: int = None,
                 end: int = None) -> list | list[list]:

        """_summary_

        Raises:
            ValueError: if file is empty
            ValueError: if line is empty

        Returns:
            list[list]: list of prepared rows or just a list
        """
        
        # If the file is empty return this message
        if is_empty(self.file_name):
            raise EmptyFile('Empty file')
        
        # Used to add lists of the original form
        single: list = []
        
        # A list where original form data is added
        prepared: list = []
        
        with open(self.file_name, '+r') as back:
            # If these two options are not None
            if (start is not None) and (end is not None):
                
                # Lines from start to end
                lines_back = back.readlines()[start:end]
                
                # Separates values in the rows
                row_elme = [row.split(',') for row in lines_back]
                
                # Getting rid of '\n' from the last element in each row
                row_elme = [row[-1][:row[-1].find('\n')] for row in row_elme]
                
                # Restructures data. Turning it back to the original form
                for index in range(len(row_elme[0])):
                    for val in row_elme:
                        single.append(val[index])
                    
                    prepared.append(single)
                    single = []
                        
            else: # gets the line's data back
                try:
                    curnt_line = back.readlines()[line].split(',')
                    
                    # Also gets rids of '\n' in the end
                    curnt_line[-1] = curnt_line[-1][:curnt_line[-1].find('\n')]
                    
                    for el in curnt_line:
                        prepared.append([el])
                        
                except IndexError:
                    raise EmptyLine('Empty line')
                    
        return prepared
