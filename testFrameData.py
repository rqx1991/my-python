#!/usr/bin/python3.5
#coding=utf-8

# This file is used to test the usage of dataFrame.

import pandas as pd

# There several ways to set freamData, this is one of the methods.
originData = { 'code': [600600, 600601],
                'roe': [10, 12]}
frameData = pd.DataFrame(data = originData)
print(frameData)
#      code  roe
# 0  600600   10
# 1  600601   12

indexData = frameData.set_index('code')
print(indexData)
#         roe
# code
# 600600   10
# 600601   12

year = 2017
quarter = 3
changeColName1 = indexData.rename(columns={'roe':str(year*100+quarter)+'roe'})
print(changeColName1)
#         201703roe
# code
# 600600         10
# 600601         12
changeColName2 = indexData.rename(columns={'roe':str(year)+'-'+str(quarter)+'-roe'})
print(changeColName2)
#         2017-3-roe
# code
# 600600          10
# 600601          12
changeColName = indexData.rename(columns={'roe':str(year*100+quarter)+'-roe'})
print(changeColName)
#         201703-roe
# code
# 600600          10
# 600601          12

# haven't know how to use, since if 600600 is 600605, this will give an exception
queryData1 = indexData.ix[600600]
if queryData1 is not None:
    print(queryData1)
# this will give an exception the index is not in table
# roe    10
# Name: 600600, dtype: int64

queryData = indexData.query('code==600600')
if not queryData.empty:
    print(queryData)
#         roe
# code
# 600600   10

# function : join
# prototype : join(other[, on, how, lsuffix, rsuffix, sort])
# feature : Join columns with other DataFrame either on index or on a key column.
joinArray = { 'code': [600600],
                'roe-join': [15]}
joinData = pd.DataFrame(data = joinArray).set_index('code')
print(joinData)
#         roe-join
# code
# 600600        15
queryData = indexData.query('code==600600')
# if the stock code of the append data is already in the table
if not queryData.empty:
    joinIndexData = indexData.join(joinData, how='outer')
    print(joinIndexData)
#         roe  roe-join
# code
# 600600   10      15.0
# 600601   12       NaN

# function : append
# prototype : append(other[, ignore_index, verify_integrity])
# feature : Append rows of other to the end of this frame, returning a new object.
appendArray = { 'code': [600602],
                'roe': [16]}
appendData = pd.DataFrame(data = appendArray).set_index('code')
queryData = indexData.query('code==600602')
# if the stock code of the append data is not in the table
if queryData.empty:
    appendIndexData = indexData.append(appendData)
    print(appendIndexData)
#         roe
# code
# 600600   10
# 600601   12
# 600602   16

print('\n\n-------------test begin here----------------\n\n')









































print('\n\n-------------test end here----------------\n\n')
