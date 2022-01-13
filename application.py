from flask import Flask, render_template, request, jsonify
import pandas as pd
import requests

from functools import lru_cache
from flask import send_file

application = Flask(__name__)
application.config['SECRET_KEY']='some_random_key'

database = {'admin': 'admin'}


@application.route("/downloadTaluk", methods=["POST", "GET"])
def hello():
    url = "https://www.kaushalkar.com/webservices/ws/getDistrictsByStateId"
    payload = {'stateId': '29'}
    files = []
    headers = {'api': 'c726736ed6a469e5e713118332558b54', 'Cookie': 'PHPSESSID=hpt5eenuebn5d28a07aligkbol'}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    dict = {}
    response = response.json()

    for x in range(len(response)):
        temp_dct = response[x]
        tt = temp_dct.values()
        list = []
        for v in tt:
            list.append(v)
        dict[list[0]] = list[1]

    list1 = dict.values()
    return render_template('index.html', list1=list1)


@application.route("/downlaodDistrict", methods=["POST", "GET"])
def hello1():
    url = "https://www.kaushalkar.com/webservices/ws/getDistrictsByStateId"
    payload = {'stateId': '29'}
    files = []
    headers = {'api': 'c726736ed6a469e5e713118332558b54', 'Cookie': 'PHPSESSID=hpt5eenuebn5d28a07aligkbol'}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    dict = {}
    response = response.json()

    for x in range(len(response)):
        temp_dct = response[x]
        tt = temp_dct.values()
        list = []
        for v in tt:
            list.append(v)
        dict[list[0]] = list[1]

    list1 = dict.values()
    return render_template('indexone.html', list1=list1)


@application.route("/get_child_categories", methods=["POST", "GET"])
def get_child_categories():
    if request.method == 'POST':
        url2 = "https://www.kaushalkar.com/webservices/ws/getDistrictsByStateId"
        payload2 = {'stateId': '29'}
        files2 = []
        headers2 = {'api': 'c726736ed6a469e5e713118332558b54', 'Cookie': 'PHPSESSID=hpt5eenuebn5d28a07aligkbol'}
        response2 = requests.request("POST", url2, headers=headers2, data=payload2, files=files2)
        dict2 = {}
        response2 = response2.json()

        for x2 in range(len(response2)):
            temp_dct2 = response2[x2]
            tt2 = temp_dct2.values()
            list2 = []
            for v2 in tt2:
                list2.append(v2)
            dict2[list2[0]] = list2[1]

        parent_id = request.form["parent_id"]
        url = "https://www.kaushalkar.com/webservices/ws/getTaluksByDistrictId"
        pp = get_key(parent_id, dict2)
        payload = {'districtId': pp}
        files = []
        headers = {
            'api': 'c726736ed6a469e5e713118332558b54',
            'Cookie': 'PHPSESSID=hpt5eenuebn5d28a07aligkbol'
        }

        response1 = requests.request("POST", url, headers=headers, data=payload, files=files)
        dict = {}
        response1 = response1.json()

        for x in range(len(response1)):

            temp_dct = response1[x]
            tt = temp_dct.values()
            list = []
            for v in tt:
                list.append(v)
            dict[list[0]] = list[1]
        list_1 = dict.values()
        
    return jsonify({'htmlresponse': render_template('response.html', list_1=list_1)})


@application.route("/thank-you", methods=["POST", "GET"])
def result():
    url = "https://www.kaushalkar.com/webservices/ws/getDistrictsByStateId"
    payload = {'stateId': '29'}
    files = []
    headers = {'api': 'c726736ed6a469e5e713118332558b54', 'Cookie': 'PHPSESSID=hpt5eenuebn5d28a07aligkbol'}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    dict = {}
    response = response.json()

    for x in range(len(response)):
        temp_dct = response[x]
        tt = temp_dct.values()
        list = []
        for v in tt:
            list.append(v)
        dict[list[0]] = list[1]
    
    output = request.form.get("search_category")
    output1 = request.form.get("sub_category")
    for key, value in dict.items():
        if value == output:
            disID = key

    url11 = "https://www.kaushalkar.com/webservices/ws/getTaluksByDistrictId"
    payload11 = {'districtId': disID}
    files11 = []
    headers11 = {'api': 'c726736ed6a469e5e713118332558b54', 'Cookie': 'PHPSESSID=hpt5eenuebn5d28a07aligkbol'}
    response11 = requests.request("POST", url11, headers=headers11, data=payload11, files=files11)
    dict11 = {}
    response11 = response11.json()

    for x11 in range(len(response11)):
        temp_dct11 = response11[x11]
        tt11 = temp_dct11.values()
        list11 = []
        for v11 in tt11:
            list11.append(v11)
        dict11[list11[0]] = list11[1]

    for key, value in dict11.items():
        if value == output1:
            talkID = key

    

    l1 = giveDetailsOfTaluk(talkID, disID)
    pd.DataFrame(l1).to_excel("static/output.xlsx")
    return send_file('static/output.xlsx', as_attachment=True)


@application.route("/thank-you1", methods=["POST", "GET"])
def result1():
    url = "https://www.kaushalkar.com/webservices/ws/getDistrictsByStateId"
    payload = {'stateId': '29'}
    files = []
    headers = {'api': 'c726736ed6a469e5e713118332558b54', 'Cookie': 'PHPSESSID=hpt5eenuebn5d28a07aligkbol'}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    dict = {}
    response = response.json()

    for x in range(len(response)):
        temp_dct = response[x]
        tt = temp_dct.values()
        list = []
        for v in tt:
            list.append(v)
        dict[list[0]] = list[1]
    
    output = request.form.get("search_category1")
    # output1 = request.form.get("sub_category")
    for key, value in dict.items():
        if value == output:
            disID = key

    l1 = giveDetailsOfDistrict(disID)
    pd.DataFrame(l1).to_excel("static/output.xlsx")
    return send_file('static/output.xlsx', as_attachment=True)


def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key


@application.route('/', methods=["POST", "GET"])
def logIn():
    return render_template("login.html")


@application.route('/form_login', methods=['POST', 'GET'])
def login():
    name1 = request.form['username']
    pwd = request.form['password']
    if name1 not in database:

        return render_template('login.html', info='Invalid User')
    else:
        if database[name1] != pwd:
            return render_template('login.html', info='Invalid Password')
        else:
            return render_template('home.html')


@application.route('/downlaodAll', methods=['POST', 'GET'])
def downlaodAll():
    l1 = getDataOfAllStudents()
    pd.DataFrame(l1).to_excel("static/output.xlsx")
    return send_file('static/output.xlsx', as_attachment=True)


@lru_cache(maxsize=1000000)
def giveDetailsOfTaluk(talukID, districtID):
    url = "https://www.kaushalkar.com/webservices/ws/getStudentsData/"
    payload = {'districtId': districtID, 'talukId': talukID}
    files = []
    headers = {'api': 'c726736ed6a469e5e713118332558b54', 'Cookie': 'PHPSESSID=hpt5eenuebn5d28a07aligkbol'}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return response.json()


@lru_cache(maxsize=10000)
def giveDetailsOfDistrict(districtId):
    url = "https://www.kaushalkar.com/webservices/ws/getTaluksByDistrictId"
    payload = {'districtId': districtId}
    files = []
    headers = {'api': 'c726736ed6a469e5e713118332558b54', 'Cookie': 'PHPSESSID=hpt5eenuebn5d28a07aligkbol'}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    dict = {}
    response = response.json()
    data_t = []

    for x in range(len(response)):
        temp_dct = response[x]
        tt = temp_dct.values()
        list = []
        for v in tt:
            list.append(v)
        dict[list[0]] = list[1]
    for keys in dict.keys():
        a = (giveDetailsOfTaluk(keys, districtId))
        data_t = data_t + a

    return data_t


@lru_cache(maxsize=10000)
def getDataOfAllStudents():
    url = "https://www.kaushalkar.com/webservices/ws/getDistrictsByStateId"
    payload = {'stateId': '29'}
    files = []
    headers = {'api': 'c726736ed6a469e5e713118332558b54', 'Cookie': 'PHPSESSID=hpt5eenuebn5d28a07aligkbol'}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    dict = {}
    response = response.json()
    data_t = []

    for x in range(len(response)):
        temp_dct = response[x]
        tt = temp_dct.values()
        list = []
        for v in tt:
            list.append(v)
        dict[list[0]] = list[1]

    for keys in dict.keys():
        temp_storage = giveDetailsOfDistrict(keys)
        data_t = data_t + temp_storage
    return data_t


if __name__ == '__main__':
    application.run(host='0.0.0.0',port=8080)
