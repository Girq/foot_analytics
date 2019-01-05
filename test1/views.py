from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import http.client
import json

# Create your views here.

def test(request):
    template = loader.get_template('test1/index.html')
    return HttpResponse(template.render({}, request))



def foot(request,):
    template = loader.get_template('test1/footdata.html')


    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': '06558c656e394bc6ad30546af2801d27'}

    connection.request('GET', '/v2/competitions/PL/teams', None, headers)

    response = json.loads(connection.getresponse().read().decode())

    c = response['teams']
    dd=[]
    dc=[]
    da=[]
    dg=[]



    for i in range(len(c)):

        dd.append(c[i]['name'])
        dc.append(c[i]['founded'])
        da.append(c[i]['website'])
        dg.append(c[i]['clubColors'])



    mylist=zip(dd,dc,da,dg)

    ddd={'toto': mylist}


    return HttpResponse(template.render(ddd, request))

