import requests
import json
URL = "http://127.0.0.1:8000/stuupdate/"



def createobj(data):
    json_data = json.dumps(data)
    r = requests.post(url=URL, data = json_data)

    data = r.json()
    print(data)
#createobj({'name':'Nowshin','roll': 3 ,'city':'Dhaka'})

def getdata(id = None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL,data=json_data)

    data = r.json()
    print(data)
getdata(1)

def update(data):
    json_data = json.dumps(data)
    r = requests.put(url=URL, data = json_data)

    data = r.json()
    print(data)
#update({'id':8,'name':'Jolil','roll': 3 ,'city':'Dhaka'})

def delete(data):
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data = json_data)

    data = r.json()
    print(data)
#delete({'id':7})