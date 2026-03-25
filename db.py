import pymysql
import redis
from pymongo import MongoClient

#MySQL Connection
mysql_conn = pymysql.connect(
    host="localhost",
    user="root",
    password="HAri@12345",
    database="project_db",
    cursorclass=pymysql.cursors.DictCursor
)

#Redis Connection
r = redis.Redis(host="localhost", port=6379, decode_responses=True)

#MongoDB Connection
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["project_db"]
profile_collection = mongo_db["profiles"]