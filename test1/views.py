from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests

# Create your views here.

def test(request):
    template = loader.get_template('test1/index.html')
    return HttpResponse(template.render({}, request))



def foot(request,):
    template = loader.get_template('test1/footdata.html')



    headers = {'X-Auth-Token': '06558c656e394bc6ad30546af2801d27'}



    URL = 'http://api.football-data.org/v2/competitions/PL/teams'

    r = requests.get(url=URL, headers=headers)

    rr = r.json()['teams']


    dd=[]
    dc=[]
    da=[]
    dg=[]



    for i in range(len(rr)):

        dd.append(rr[i]['name'])
        dc.append(rr[i]['founded'])
        da.append(rr[i]['website'])
        dg.append(rr[i]['clubColors'])



    mylist=zip(dd,dc,da,dg)

    ddd={'toto': mylist}


    return HttpResponse(template.render(ddd, request))

