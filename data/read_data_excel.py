import xlrd
class Data:

    def __init__(self,filePath,fileName):
        self.filePath = filePath
        self.fileName = fileName

        #读取文件路径
        file = xlrd.open_workbook(self.filePath)

        #获取表格
        self.sheet = file.sheet_by_name(self.fileName)

        #获取第一行字段名
        self.keys = self.sheet.row_values(0)

        #获取所有行
        self.nrows = self.sheet.nrows

        #获取所有的列
        self.ncols = self.sheet.ncols



    def readData(self):
        if self.nrows <=1:
            print("行数小于等于1")
        else:
            data_list = list()
            for i in range(1,self.nrows):
                data_row_value = self.sheet.row_values(i)
                data_dic = {}
                for j in range(0,self.ncols):
                   data_dic[self.keys[j]] = data_row_value[j]
                data_list.append(data_dic)

            return data_list


if __name__ == '__main__':
    data = Data('./data.xls','data').readData()
    print(data)