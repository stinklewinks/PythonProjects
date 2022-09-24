# Console Trivia
# 
# A Terminal Game built with Python
import os
import sys
import time
import random
import math
import pymongo

the_client = pymongo.MongoClient("mongodb+srv://stinkledb:GMCie0ScYKbv1cZq@cluster0.5whmq9z.mongodb.net/?retryWrites=true&w=majority")
db = the_client["Cluster0"]

print(the_client.list_database_names())
the_time = time.ctime()
print(the_time)
