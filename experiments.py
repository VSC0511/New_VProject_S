import numpy as np

import pandas as pd

from vdatasaver import CsvHome



writer = CsvHome('VDATA.csv')

writer.columns = ['Hello']

writer.rows = [['ol']]
print(writer.columns)
print(writer.rows)


