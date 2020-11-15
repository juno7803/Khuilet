from django.shortcuts import render
import os

data_path = os.path.abspath("static/toilet_daejeon.csv")
# "/Users/ijunho/desktop/junho/2020-2학기/web-python/khuilet/static/toilet_daejeon.csv"
file = open(data_path,'r')
toliet_list = []

lines = file.readlines()
for line in lines:
    toliet_list.append(line.split(','))
file.close()

data = toliet_list[1:80]

def index(request):
    return render(request,'main/index.html',{'data':data});