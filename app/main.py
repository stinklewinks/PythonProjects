# Console Trivia
# 
# A Terminal Game built with Python
import os
import sys
import time
import random
import math
import pymongo
import pprint
from modules.level_one.lvl_one_questions import Question

the_client = pymongo.MongoClient("mongodb+srv://stinkledb:GMCie0ScYKbv1cZq@cluster0.5whmq9z.mongodb.net/?retryWrites=true&w=majority")
db = the_client.trivia_questions
the_col = db.sports_questions

gator_question = {'q': 'In what year did the Florida Gators win their last Football National Championship?', 'a': '2008'}
# the_col.insert_one(gator_question)
the_col.insert_one(Question.quest_1)

pprint.pprint(the_col.find_one())
# print(the_client.list_database_names())
# print(db.list_collection_names())
# print(the_col)
# the_time = time.ctime()
# print(the_time)
