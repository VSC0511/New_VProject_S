import numpy as np

import pandas as pd

from vdatasaver import CsvHome



writer = CsvHome('VDATA.csv')

writer.columns = ['Hello']
writer.rows = [['NA'], [2]]
print(writer.columns)


