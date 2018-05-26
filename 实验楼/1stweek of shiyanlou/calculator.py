#!/usr/bin/env python3
import sys
import time
import os
from multiprocessing import Process, Queue
# amount_of_income = salary-3500-social_insurance
# tax_amount_payable = amount_of_income*rate-sub
# social_insurance = salary_insurance*0.165(salary_insurance)

q0 = Queue() # queue between read worker_salary and calculate tax
q1 = Queue() # queue between calculate tax and write tax
tax_levy_point = 3500
standard_lst = [0, 1500, 4500, 9000, 35000, 55000, 80000]
sub_lst = [0, 105, 555, 1005, 2755, 5505, 13505]
tax_rate = [0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]

def calc_social_insurance(salary, JiShuL, JiShuH, social_insurance_rate):
    if salary < JiShuL:
        social_insurance = JiShuL*social_insurance_rate
    elif salary >JiShuH:
        social_insurance = JiShuH*social_insurance_rate
    else:
        social_insurance = salary*social_insurance_rate
    return social_insurance
def cfg_dict_haskey(cfg_dict):
    lst_tmp = ['JiShuL', 'JiShuH', 'YangLao', 'ShiYe', 'GongShang', 'ShengYu','GongJiJin']
    try:
        for i in lst_tmp:
            if i not in cfg_dict.keys():
                raise ValueError
        else:
            return True
    except ValueError:
        print('file Parameter Error')
        return False
    
def if_file_exist():
    # judge if the sys.argv are right
    try:
        if not(len(sys.argv) == 7  
                and os.path.isfile(sys.argv[2])
                and os.path.isfile(sys.argv[4])
                and sys.argv[6].endswith(".csv")
                ):
            raise ValueError
    except ValueError:
        print('sys Paramer Error')
        sys.exit(-1)
class Extract():
    def __init__(self, filename, separator, q=None):
        self.filename = filename
        self.separator = separator
        self.dict_l = {}
        self.q = q
    def extract_file(self):
        # return a dict
        with open(self.filename) as f:
            for line in f:
                line_lst = line.strip().split(self.separator)
                try:
                    if len(line_lst) < 2:
                        raise ValueError
                    line_lst[1] = float(line_lst[1])
                    if line_lst[1]< 0:
                        raise ValueError
                except ValueError:
                    print("find one error in'{}' of {}".format(line,self.filename))
                    continue
                if self.q:
                    self.q.put((line_lst[0],line_lst[1]))
                else:
                    self.dict_l[line_lst[0].strip()] = line_lst[1]
            return self.dict_l
def calculate_realwage(social_insurance_rate, q0, q1):
    while True:
        if not(q0.empty()):
            worker_num, salary = q0.get()
            social_insurance = calc_social_insurance(salary, JiShuL, JiShuH, social_insurance_rate)
            amount_of_income = salary-tax_levy_point-social_insurance
            if amount_of_income <= 0:
                tax = 0
                
            else:
                for i in range(len(standard_lst)):
                    if amount_of_income <= standard_lst[i]:
                        tax = amount_of_income*tax_rate[i-1]-sub_lst[i-1]
                        break
                else:

                    tax = (amount_of_income-standard_lst[-1])*tax_rate[-1]-sub_lst[-1]
            real_wage = salary-social_insurance-tax
            q1.put((worker_num, salary, social_insurance, real_wage))
def write_result_tofile(q):
    with open(sys.argv[6], 'w') as f:
        f.write("sucess")
        while True:
            if not(q.empty()):
                data = q.get()
                worker_num, salary, social_insurance, real_wage = data
                f.write('{},{},{:.2f},{:.2f} \n'.format(worker_num, int(salary), social_insurance, real_wage))
    
if_file_exist()
extract_cfg = Extract(sys.argv[2],'=',q=None)
cfg_dict = extract_cfg.extract_file()
if cfg_dict_haskey(cfg_dict):
    JiShuL = cfg_dict['JiShuL']
    JiShuH = cfg_dict['JiShuH']
    social_insurance_rate = cfg_dict['GongJiJin']+cfg_dict['YangLao']+cfg_dict['YiLiao']+cfg_dict['ShiYe']+cfg_dict['GongShang']+cfg_dict['ShengYu']
else:
    sys.exit(-1)
extract_usercsv = Extract(sys.argv[4], ',', q0)    
p1 = Process(target=extract_usercsv.extract_file)
p2 = Process(target=calculate_realwage, args=(social_insurance_rate, q0, q1))
p3 = Process(target=write_result_tofile, args=(q1,))
p1.start()
p2.start()
p3.start()
p1.join()
while True:
    if q0.empty() and q1.empty():
        p2.terminate()
        p3.terminate()
        break
    else:
        time.sleep(0.1)


