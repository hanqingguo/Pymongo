from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
import datetime

client = MongoClient()
db = client.test_database
collection1 = db.test_collection
#post = {"author":"hanqing","date":datetime.datetime.now(),"page":"Hello World!"}
#collection1.insert_one(post)


def index(request):

    return HttpResponse("Hello, world. You're at the polls index"+collection1.find_one()['author'])


# Create your views here.
