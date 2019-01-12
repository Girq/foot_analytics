from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np

# Create your views here.

def test(request):
    template = loader.get_template('test1/index.html')
    #return HttpResponse(template.render({}, request))

    # Token

    headers = {'X-Auth-Token': '06558c656e394bc6ad30546af2801d27'}

    # Request --> Filter /teams

    URL1 = 'http://api.football-data.org/v2/competitions/PL/teams'

    r = requests.get(url=URL1, headers=headers)

    rr = r.json()['teams']

    # Premiere Tableau teams PL

    dd = []
    dc = []
    da = []
    dg = []

    for i in range(len(rr)):
        dd.append(rr[i]['name'])
        dc.append(rr[i]['founded'])
        da.append(rr[i]['website'])
        dg.append(rr[i]['clubColors'])

    mylist = zip(dd, dc, da, dg)

    # ddd={'toto': mylist}

    # Histogram

    nor = []
    nor1 = []
    nor2 = []

    for t in range(len(dd)):
        x = dd[t]
        j = x.split()
        nor.append(j)

    for z in nor:
        nor1.append(z[0])

    for m in nor1:
        nor2.append(m[0:2])

    f, ax = plt.subplots(1)
    ax.set_ylim(1870, max(dc))
    ax.set_xlabel('Teams')
    ax.set_ylabel('Year of Foundation')

    ax.bar(nor2, dc)

    #plt.savefig('/home/grig/PycharmProjects/untitled/test1/static/test1/images/pic.png')
     plt.savefig('/home/Grig117/foot_analytics/test1/static/test1/images/pic.png')

    # Request --> Filter /standings

    URL2 = 'http://api.football-data.org/v2/competitions/PL/standings'

    a = requests.get(url=URL2, headers=headers)

    aa = a.json()['standings']

    ppp = aa[0]['table']

    # Classement PL --->

    point = []
    posit = []
    clubs = []
    games = []
    won = []
    draw = []
    lost = []
    goalfor = []
    goalag = []
    goaldif = []

    for i in range(len(ppp)):
        posit.append(ppp[i]['position'])
        point.append(ppp[i]['points'])
        clubs.append(ppp[i]['team']['name'])
        games.append(ppp[i]['playedGames'])
        won.append(ppp[i]['won'])
        lost.append(ppp[i]['lost'])
        draw.append(ppp[i]['draw'])
        goalfor.append(ppp[i]['goalsFor'])
        goalag.append(ppp[i]['goalsAgainst'])
        goaldif.append(ppp[i]['goalDifference'])

    mylist1 = zip(posit, clubs, games, won, draw, lost, goalfor, goalag, goaldif, point)

    logos = []
    for j in range(len(ppp)):
        logos.append(ppp[j]['team']['crestUrl'])

    # mylogo=zip(logos)

    # Template ---->

    context = {

        'picture': {"name": 'Histograme', 'filename': 'test1/images/pic.png'},

        'toto': {'elem': mylist},

        'tata': {'position': mylist1},

        'teamlogo': {'logo1': logos}

    }

    return HttpResponse(template.render(context, request))


def foot(request):
    template = loader.get_template('test1/footdata.html')

 # Token

    headers = {'X-Auth-Token': '06558c656e394bc6ad30546af2801d27'}


# Request --> Filter /teams

    URL1 = 'http://api.football-data.org/v2/competitions/PL/teams'

    r = requests.get(url=URL1, headers=headers)

    rr = r.json()['teams']


# Premiere Tableau teams PL

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

    #ddd={'toto': mylist}


# Histogram

    nor=[]
    nor1=[]
    nor2=[]

    for t in range(len(dd)):
        x = dd[t]
        j = x.split()
        nor.append(j)

    for z in nor:
        nor1.append(z[0])

    for m in nor1:
        nor2.append(m[0:2])

    f, ax = plt.subplots(1)
    ax.set_ylim(1870, max(dc))
    ax.set_xlabel('Teams')
    ax.set_ylabel('Year of Foundation')

    ax.bar(nor2, dc)

    #plt.savefig('/home/grig/PycharmProjects/untitled/test1/static/test1/images/pic.png')
    plt.savefig('/home/Grig117/foot_analytics/test1/static/test1/images/pic.png')


# Request --> Filter /standings

    URL2 = 'http://api.football-data.org/v2/competitions/PL/standings'

    a = requests.get(url=URL2, headers=headers)

    aa = a.json()['standings']

    ppp = aa[0]['table']


# Classement PL --->

    point = []
    posit = []
    clubs = []
    games = []
    won = []
    draw = []
    lost = []
    goalfor = []
    goalag = []
    goaldif = []

    for i in range(len(ppp)):
        posit.append(ppp[i]['position'])
        point.append(ppp[i]['points'])
        clubs.append(ppp[i]['team']['name'])
        games.append(ppp[i]['playedGames'])
        won.append(ppp[i]['won'])
        lost.append(ppp[i]['lost'])
        draw.append(ppp[i]['draw'])
        goalfor.append(ppp[i]['goalsFor'])
        goalag.append(ppp[i]['goalsAgainst'])
        goaldif.append(ppp[i]['goalDifference'])


    mylist1=zip(posit, clubs, games, won, draw, lost, goalfor, goalag, goaldif, point)


    logos = []
    for j in range(len(ppp)):
        logos.append(ppp[j]['team']['crestUrl'])

    #mylogo=zip(logos)

    # Template ---->

    context = {

                'picture': {"name": 'Histograme', 'filename': 'test1/images/pic.png'},

                'toto': {'elem': mylist},

                'tata': {'position': mylist1},

                'teamlogo': {'logo1': logos}

    }




    return HttpResponse(template.render(context, request))

