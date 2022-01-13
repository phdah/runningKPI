import pandas as pd
import datetime

wd = '/mnt/c/Users/philip.dahlqvist/runningKPI/'
file = 'Activities.csv'

data = pd.read_csv(wd+file, encoding='utf-8')