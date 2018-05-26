#!/usr/bin/env python3
# -*- coding utf-8 -*-
import sys
import csv
import time
import os
from multiprocessing import Process, Queue, Pool, Value
# amount_of_income = salary-3500-social_insurance
# tax_amount_payable = amount_of_income*rate-sub
# social_insurance = salary_insurance*0.165(salary_insurance)


# it is used to get the cfg:
# tax_levyPoint, lst_salaryLevel, lst_quickDeducation, lst_taxRate
# salary, JishuL, JishuH, social_insurance_rate, worker_id
# sys.argv
class Get_cfg():
    
    # tup_args:the tuple maked up by args
    def __init__(self,sys.argv):
        self.args = args
    
    def __parse_arg(self, arg):
        try:
            value = self.args[self.args.index(arg) + 1]
        except (ValueError, IndexError):
            value = None
        return value #元组错误类型,出现错误将value设为None

    def get_arg(self, arg):
        '''外部调用的方法
        (external invoked methods)
        '''
        value =  self.__parse_arg(arg)
        if value is None:
            raise ArgError('not found...') # raise
#        抛出错误还可以打印错误信息(print information of Error)
        return value # 继续返回None

        '''与我的思路不同的是,将解析参数和提取文件分开了.不同
        文件的提取分开了
        (separating parse parameter from file extraction)

        sysArgs = sys.argv[1:]
        self.dict_tmp = {}
        try:
            self.c = sysArgs[sysArgs.index('-c')+1]
            self.d = sysArgs[sysArgs.index('-d')+1]
            self.o = sysArgs[sysArgs.index('-o')+1]
            if not(os.path.isfile(self.c)
                    and os.path.isfile(self.d)
                    and self.o.endswith(".csv")
                    ):
                raise ValueError
        except ValueError:
            print('sys paramer error')
            sys.exit(-1)
        except:
            print("Parameter Error")
            exit()
    
    # process put queue the usrdata
    def process_send(self, q):
       if q is not None:
           q.put(self.dict_tmp)

    #extract the cfg and usrdata,save as dict and return as property
    def extract(self, filename, separator, q=None):
        f= list(csv.reader(filename, separator))#error,filename must be open
        for line in f:
            try:
                line[1] = float(line[1])
                if line[1] < 0:
                    raise ValueError
                self.dict_tmp[line[0].strip()] = line[1]
                self.process_send(q)
            except:
                print("find one error in'{}' of {}".format(
                    line,filename))
                continue
       return self.dict_tmp
       v.value = 1
'''
class SheBaoConfig:
    '''社保配置文件类
    '''

    def __init__(self, file):
        self.jishu_low, self.jishu_high, self.total_rate = (self.
                __parse_config(file)
    
    def __parse_config(self, file):
        rate = 0
        jishu_low = 0
        jishu_high = 0
        with open(file) as f:
            for line in f:
                key, value = line
                ...
        return jishu_low, jishu_high, rate #元组返回方式,反映到属性


class EmployeeData(Process):
    '''继承Process类,并实现run方法
    inherit the Process class and implement the run method
    '''
    def __init__(self, file, output_queue):
        self.file = file
        self.output_q = output_queue
        super().__init__()

    def __parse(self):
        '''
        '''
        for line in open(self.file)
        ....
            yield (int(employee_id), int(gongzi))#yield...
    def run(self):
        '''进程启动后真正执行代码的方法
        (actually execute code after a process start)
        '''
        for item in self.__parse():
            self.output_q.put(item)#yield...使用yield可以把
            #代码分成两半

class Calculator(Process):
    '''计算方法...
    
    '''

    tax_start = 3500 # 设置为静态变量(set to static value)
    tax_table = [(80,293,39)] # 表格形式,减少了变量名的引用

    def calculate(self, data):
        employee, gongzi = data
        ...
        return '{:.2f}'.format(shebao) # 格式化返回
# calculator salary class
class Cal_salary():
    
    # initialize the args maybe they are hanged in main process
    def __init__(self, lst_levy, lst_quick_deducation,
            lst_taxrate, tax_levy_point, dict_cfg):
        self.lst_levy = lst_levy
        self.lst_quick_deducation= lst_quick_deducation
        self.lst_taxrate= lst_taxrate
        self.tax_levy_point= tax_levy_point
        self.dict_result = {}
        self.dict_result['sum_insurance'] = 0
        self.dict_cfg = dict_cfg
        lst_tmp = ['JiShuL', 'JiShuH', 'YangLao', 'ShiYe', 'GongShang', 
                'ShengYu','GongJiJin'
                ]
        try:
            for i in lst_tmp:
                if i not in self.dict_cfg.keys():
                    raise ValueError
        except ValueError:
            print('file Parameter Error')
            exit()

    # compare the salary with JiShuL and JiShuL,return right value 
    def calc_salary_i(self, salary):
        try:
            if self.dict_cfg['JiShuL'] > self.dict['JiShuH']:
                raise ValueError
        except ValueError:
            print("JiShuL is above JiShH")
            exit()
        if salary < JiShuL:
            return JiShuL
        elif salary > JiShuH:
            return JiShuH
        else:
            return salary

    # calculate all kinds of insurance and the sum of them, save in property
    # dict_result
    def get_insurancerate(self, salary_i):
        for k in self.dict_cfg.keys():
            if k != "JiShuL" and k != 'JiShuH':
                self.dict_result[k] = self.dict_cfg[k]*salary_i
                self.dict_result['sum_insurance'] += self.dict_result[k]
    
    # calculate tax, save in property dict_result
    def calc_tax(self, sum_insurance, salary):
        tax = salary-self.tax_levy_point-self.dict_result[
                'sum_insurance'] # tax isnt result now
        if tax <= 0:
          self.dict_result['tax'] = 0
        else:
            for i, k in enumerate(self.lst_levy):
                if tax < k:
                    self.dict_result['tax'] = (tax*self.lst_taxrate[i-1]-
                            lst_quick_deducation[i-1])
                    break
            else:
                self.dict_result['tax'] = (tax*self.lst_taxrate[-1]-
                        lst_quick_deducation[-1])

    # combine functions to calculate the result
    def calc_result(self, getdata):
        for k, v in getdata():
        self.dict_result['id'], self.dict_result['salary'] = k, v
        salary_i = calc_salary_i(self.dict_result['salary'])
        self.get_insurancerate(salary_i) # everyrate will be got
        self.calc_tax(self.dict_result['sum_insurance'],
            self.dict_result['salary'])
        self.dict_result['real_wage'] =(self.dict['salary']-
            self.dict_result['tax']
    

    # process q0.get and q1.put. i want to split it into two parts
    # because it will start 2 processes, so give up
    def get_send_que(self, q0, q1):
        pool = Pool()
        while True:
            if not q0.empty():
                pool.apply(self.calc_result,(q0.get(),))
                q1.put(self.dict_result)
            if v.value == 1:
                break
        pool.close()
        pool.join()

# write it to csvfile
class Writefile():
    def __init__(self, filename):
        self.filename = filename
    def writeto(self, q):
        with open(self.filename, "a") as f:
            while not q.empty:
                data = q.get()
                f.write(data['id'], data['salary'], data['tax'],
                    data['real_wage']) 
            
v = Value('i',0)
tax_levy_point = 3500
standart_lst = [0, 1500, 4500, 9000, 35000, 55000, 80000]
sub_lst = [0, 105, 555, 1005, 2755, 5505, 13505]
tax_rate = [0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]
q0 = Queue()
q1 = Queue()
pool = Pool(3)
cfg = Get_cfg(sys.argv)
cfg.extract(cfg.c,"=")
v.value = 0
cal_salary = Cal_salary(standart_lst, sub_lst, tax_levy_point,
    cfg.dict_cfg)
p1 = Process(target=cfg.extract, args=(cfg.d, ',', q=q0))
p2 = Process(target=calc_salary.get_send_que, args(q0, q1))
witefile = Writefile(self.o)
p3 = Porcess(target=writefile.wirteto, args=(q1,))
p1.start()
p2.start()
p1.join()
p2.join()


