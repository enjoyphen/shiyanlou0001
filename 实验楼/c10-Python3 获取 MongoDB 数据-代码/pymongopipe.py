#!/usr/bin/env python3

import pymongo
from bson.son import SON
client = pymongo.MongoClient()
db = client.shiyanlou
contests = db.contests
for i in contests.aggregate(
        [
            {'$group':
                {'_id':'$user_id','sum_score':
                    {'$sum':'$score'
                    },'sum_time':
                    {'$sum':'$submit_time'
                    }
                }
            },
            {'$sort':
                SON([('sum_score',-1),('sum_time',1)])
            }
          # ''' {'$match':
                #{'_id':1
                #}
                #}
                #
        ]):
    print(i)
                                  
