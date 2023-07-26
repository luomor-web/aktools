import pandas as pd
 
# data1为list类型，参数index为索引，column为列名
data2 = pd.DataFrame(data = data1,index = None,columns = name)
# PATH为导出文件的路径和文件名
data2.to_csv(PATH)


import csv
 
# path为输出路径和文件名，newline=''是为了不出现空行
csvFile = open(path, "w+",newline='')
# name为列名
name = ['sessionId','itemId']
try:
    writer = csv.writer(csvFile)
    writer.writerow(name)
    # data为list类型
    for i in range(len(data)):
        writer.writerow(data[i])
finally:
    csvFile.close()