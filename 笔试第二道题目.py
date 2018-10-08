# -*- coding: utf-8 -*-


class Code(object):
    '''加密类'''

    def __init__(self, date_time, content_list):
        # 初始化
        self.date_time = date_time
        self.content_list = content_list
        self.code_list = ['ABCDEFGHI', 'JKLMNOPQR', 'STUVWXYZ ']

    def process_month(self):
        '''通过月来处理'''
        month = self.date_time[0]
        move_len = month % len(self.code_list)
        # print(move_len)
        if move_len != 0:
            for i in range(move_len):
                pop_c = self.code_list.pop(0)
                self.code_list.append(pop_c)
        # print(self.content_list)

    def process_date(self):
        '''通过日来处理'''
        date = self.date_time[1]
        move_len = date % 9
        if move_len != 0:
            for i in range(len(self.code_list)):
                self.code_list[i] = self.code_list[i][move_len:]+self.code_list[i][0:move_len+1]
        # print(self.code_list)

    def search_code(self):
        '''得出加密后的编码'''
        f_code_list = []
        for i in self.code_list:
            t = str(self.code_list.index(i))
            for j in self.content_list:
                try:
                    c = str(i.index(j))
                except Exception:
                    pass
                else:
                    f_code_list.append(t+c)
        print(' '.join(f_code_list))



def main():
    date_time = [int(i) for i in input('请输入日期，用空格分开（3 3, 代表三月三日）:').split()]
    print(date_time)
    # 输入要加密的内容
    content = input('请输入要加密的内容：')
    content_list = [i for i in content ]

    # print(content_list)
    # 创建对象
    c = Code(date_time, content_list)
    # 通过月份来处理
    c.process_month()
    # 通过日来处理
    c.process_date()
    # 查找编码,并打印
    c.search_code()


if __name__ == '__main__':
    main()

