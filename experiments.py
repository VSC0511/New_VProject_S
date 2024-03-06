import numpy as np

import pandas as pd

from vdatasaver import CsvHome


writer = CsvHome('VDATA.csv')

writer.write_file(['Lol'], [], fill_up_option=True,remove_del_thg=True, check_file=True)


