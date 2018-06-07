# -*- coding: utf-8 -*-

import sys
from pymongo import MongoClient

#----quicksort
def quick_sort(arrayi):
    if len(arrayi) < 2:
        return arrayi
    else:
        lst0 = []
        lst2 = []
        for i in range(1, len(arrayi)):
            if arrayi[i] <= arrayi[0]:
                lst0.append(arrayi(i))
            else:
                lst1.append(arrayi(i))
        return quick_sort(lst0)+[arrayi(0)]+quick_sort(lst2)

# fantasy-- mergesort
def merge_sort(arrayi):
    if len(arrayi) == 1:
        return arrayi
    mid = len(arrayi)//2
    lt = arrayi[:mid]
    rt = arrayi[mid:]
    lt_i = merge_sort(lt)
    rt_i = merge_sort(rt)
    return merge(lt_i, rt_i)

def merge(lt, rt):
    result = []
    while len(lt) > 0 and len(rt) > 0:
        if lt[0] <= rt[0]:
            result.append(lt.pop(0))
        else:
            result.append(rt.pop(0))
    result += lt
    result += rt 
    return result
    

# ---------------------
def get_rank(user_id):
    client = MongoClient()
    db = client.shiyanlou
    contests = db.contests
    dict_id = {}
    # calculate the rank, grade and time of user_id
    for i in contests.find():
        id = dict_id.get(i['user_id'])
        if id is not None:
            id['score'] = id['score']+i['score']
            id['submit_time'] = id['submit_time']+i['submit_time']
        else:
            dict_id[i['user_id']] = {'score':i['score'], 'submit_time':i['submit_time']}
    lst = sorted(dict_id.items(), key=lambda x:x[1]['score'], reverse=True) 
    lst_1 = []
    lst_2 = []
    lst_1.append(lst.pop(0))
    #while lst: -->the last one is lost--do loop?
        #if lst_1[1][1]['score'] == lst[0][1]['score']:  -->Error the first same score
        #wont be included
        #if lst[1][1]['score'] == lst[0][1]['score']: --> Error the last one of lst
        #will raise indexerror
    for i in range(len(lst)):
#        if lst[1][1]['score'] == lst[0][1]['score'] and lst_2 == []:--> lst_2 =[] the # index error
        if i < len(lst):
            if lst[i][1]['score'] == lst[i+1][1]['score']: 
                lst_2.append(lst.pop(0))
                continue # because of it, the below canot in the if
        if lst_2==[]:
            lst_1.append(lst.pop(0))
        else:
            lst_2.append(lst.pop(0))
            lst_2 = sorted(lst_2, key=lambda x:x[1]['submit_time'], reverse=False)
            lst_1 += lst_2
            lst_2 = []
        
    try:
        for i,v in enumerate(lst_1, start=1):
            if user_id != v[0]:
                continue
            else:
                rank = i
                score = v[1]['score']
                submit_time = v[1]['submit_time']
                break
        else:
            raise ValueError
    except:
        print('NOTFOUND')
        exit()
#return rank, score, submit_time in order

    return rank, score, submit_time
if __name__ == '__main__':
    try:
        if len(sys.argv) == 2:
            user_id = int(sys.argv[1])
        else:
            raise ValueError
    except:
        print('Parameter Error')
        exit()
    userdata  =get_rank(user_id)
    print(userdata)


'''

def get_rank(user_id):
    client = MongoClient()
    content = client.shiyanlou.contests
    d = {}
    for i in content.find():
        id, score, time = i['user_id'], i['score'], i['submit_time']

        if d.get(id):
            d[id][0] += score
            d[id][1] += time
        else:
            d[id] = [score, time]

    l = sorted(d.values(), key=lambda x:(-x[0], x[1]))
    print(l)
    for x, y in enumerate(l):
        if d[user_id] == y:
            return [x+1] + y
'''
