import http.client
import json
import requests

import matplotlib

matplotlib.use('agg')
import matplotlib.pyplot as plt

#from IPython import get_ipython
#get_ipython().run_line_magic('matplotlib', 'inlune')

#from IPython import get_ipython
#ipython = get_ipython()
import numpy as np




#connection = http.client.HTTPConnection('api.football-data.org')
#connection2 = http.client.HTTPConnection('api.football-data.org')

#headers = { 'X-Auth-Token': '06558c656e394bc6ad30546af2801d27' }

#connection.request('GET', '/v2/competitions/PL/teams', None, headers )

#connection2.request('GET', '/v2/competitions/PL/standings', None, headers )


#response = json.loads(connection.getresponse().read().decode())
#response2 = json.loads(connection2.getresponse().read().decode())

#c=response['teams']
#pp=response['standings']


#print(c)

#Token

headers = { 'X-Auth-Token': '06558c656e394bc6ad30546af2801d27' }

# Request --> filter /teams

URL1 = 'http://api.football-data.org/v2/competitions/PL/teams'

cc = requests.get(url=URL1, headers=headers)

c = cc.json()['teams']



# Request --> filter /standings


URL2 = 'http://api.football-data.org/v2/competitions/PL/standings'

p = requests.get(url=URL2, headers=headers)

pp = p.json()['standings']

ppp=pp[0]['table']


#print(ppp)


point=[]
posit=[]
clubs=[]

for i in range(len(ppp)):

        posit.append(ppp[i]['position'])
        point.append(ppp[i]['points'])
        clubs.append(ppp[i]['team']['name'])

print(posit)
print(point)
print(clubs)


#year=[]
#nn=[]
#for i in range(len(c)):

    #print(c[i]['founded'])

    #year.append(c[i]['founded'])
    #nn.append(c[i]['name'])

#print(year)
#print(nn)

#nor=[]
#nor1=[]
#nor2=[]

#for t in range(len(nn)):
#    x=nn[t]
#    j=x.split()
#    nor.append(j)


#for z in nor:
#    nor1.append(z[0])

#for m in nor1:
#    nor2.append(m[0:2])



#print(nor2)
#print(year)

#f, ax = plt.subplots(1)
#ax.set_ylim(1870, max(year))
#ax.set_xlabel('Teams')
#ax.set_ylabel('Year of Foundation')

#ax.bar(nor2, year)




#plt.bar(nor2, year)
#axs[1].scatter(nor2, year)
#axs[2].plot(nor2, year)
#fig.suptitle('Categorical Plotting')

#plt.hist([nor2, year], density= )
#plt.ylabel('Founded');
#plt.xlabel('Teams')
#plt.savefig('/home/grig/PycharmProjects/untitled/test1/static/test1/images/pic.png')
