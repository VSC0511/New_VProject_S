from vdatasaver import CsvHome


writer = CsvHome('VDATA.csv')

writer.write_file(['Names', 'extra'], [23, 23, 23], fill_up_option=True)

