from vdatasaver import CsvHome


writer = CsvHome('VDATA.csv')

print(writer.take_back(start=1, end=5))

