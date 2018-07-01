#! /usr/bin/python3
# coding:utf-8
# auther:hyhmnn
import xlrd


class OpenXlsx(object):
    def __init__(self, filename, sheet):
        self.filename = filename
        self.workbook = xlrd.open_workbook(self.filename)
        self.booksheet = self.workbook.sheet_by_name(sheet)

    def Acolumn(self, n):
        p = list()
        for col in range(self.booksheet.ncols):
            cel = self.booksheet.cell(n, col)
            try:
                val = cel.value
                val.re.sub(r'\s+', '', val)
            except:
                pass
            if type(val) == float:
                val = str(int(val))
                # 会员名 为数字时
            else:
                val = str(val)
            p.append(val)
        # print(p)
        return p
        # 一行的信息 list类型

    def lines(self):
        return self.booksheet.nrows
        # xlsx行数

    @staticmethod
    def is_chinese(uchar):
        '''是否为中文'''
        zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
        match = zhPattern.search(uchar)
        if match:
            return True
        else:
            return False
