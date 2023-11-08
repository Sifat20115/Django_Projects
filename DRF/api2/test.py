import requests
import json
URL = "http://127.0.0.1:8000/stuget/"



def createobj(data):
    json_data = json.dumps(data)
    r = requests.post(url=URL, data = json_data)

    data = r.json()
    print(data)
#createobj({'name':'Rif','roll': 3 ,'city':'Dhaka'})
def getdata(id = None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL,data=json_data)

    data = r.json()
    print(data)
getdata(8)