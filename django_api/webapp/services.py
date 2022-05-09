import os
import requests

def get_employee_data():
    url = "http://127.0.0.1:8000/dsl-api/employee/"
    
    payload={}
    headers = {}
    
    response = requests.request("GET", url, headers=headers, data=payload)
    
    r = response.json()
    datalist = []
    
    
    for i in range(len(r)):
        datalist.append(r[i])

    print(datalist)
    return datalist

def get_project_data():
    url = "http://127.0.0.1:8000/dsl-api/project/"
    payload={}
    headers = {}
    
    response = requests.request("GET", url, headers=headers, data=payload)
    
    r = response.json()
    datalist = []
    
    
    for i in range(len(r)):
        datalist.append(r[i])

    print(datalist)
    return datalist