# -*- coding: utf-8 -*-

import sys
from pymongo import MongoClient
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

# fantasy
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
    
def get_rank(user_id):
    client = MongoClient()
    db = client.shiyanlou
    contests = db.contests
    

    # calculate the rank, grade and time of user_id
    for i in contensts.find():
        id = dict_id.get(i['user_id'])
        if id !=None:
            dict_id[id]['score'] = dict_d[id]['score']+i['score']
            dict_id[id]['submit_time'] = dict_id[id]['submit_time']+i['submit_time']
        else:
            dict_id[id] = {'score':i['score'], 'submit_time':i['submit_time'], 
                    'rank':0}
    lst = [i['sore'] for i in dict_id.values()]
    lst = merge_sort(lst)
    rank = 0
    for i in lst:
        if lst.count(i)==1:
            user = contests.find_one({'score':i})
            dict_id[user['user_id']]['rank'] = rank
            rank = rank+1
        else:
            lst_1 = []
            for j in contests.find_many({'score':i}):
                lst_1 +=dict_id[j['id']]['submit_time']
            lst_1 = merge_sort(lst_1)
            lst_1.reverse()
            for j in lst_1:
                user = contests.find_one({'submit_time':j})
                dict_id[user['user_id']]['rank'] = rank
                rank += 1
        try:
            user = dict_id[user_id]
        except:
            print('NotFound')
        rank = user['rank']
        score = user['score']
        submit_time = user['submit_time']

        
    

#return rank, score, submit_time in order
    return rank, score, submit_time

if __name__ =='__main__':
    '''
    1.Is the parameter right
    2.get the user_id parameters
    '''
    try:
        user_id = sys.argv[1]
    excpet:
        print('Parameter Error')
    userdata  =get_rank(user_id)
    print(userdata)
