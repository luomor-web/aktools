import akshare as ak
stock_info_a_code_name_df = ak.stock_info_a_code_name()
print(stock_info_a_code_name_df)

import csv
 
# path为输出路径和文件名，newline=''是为了不出现空行
csvFile = open("./test.csv", "w+", newline='')
# name为列名
name = ['code', 'name']
try:
    writer = csv.writer(csvFile)
    writer.writerow(name)
    # stock_info_a_code_name_df为list类型
    for i in range(len(stock_info_a_code_name_df)):
        writer.writerow(stock_info_a_code_name_df[i])
finally:
    csvFile.close()