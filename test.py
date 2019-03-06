from generate import *

db_begin('data')

res = databaseGen((100,300),100,(1,3),(1),[2])
print(res)
