import os
from glob import glob
import datetime as dt
import pandas as pd

fileCurrent = os.getcwd()+'\\'
fileName = sorted(glob(fileCurrent+'*.xlsx'))

excelList = []

print("Files to be merged.")
for path in fileName:
    print(path)
    excelList.append(pd.read_excel(path))

excelMergedOutput = pd.concat(excelList).drop_duplicates().reset_index(drop=True)

vdatestr = dt.datetime.now().strftime('%Y%m%d')
vtimestr = dt.datetime.now().strftime('%H%M%S')

fileNameMerged = 'Mergefile'+vdatestr+"_"+vtimestr+'.xlsx'
excelMergedOutput.to_excel(fileNameMerged, index=False)
print("Sucess!!\n\nOutput: ",end="")
print(fileCurrent+fileNameMerged)
