import http.client
import json


connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': '06558c656e394bc6ad30546af2801d27' }

connection.request('GET', '/v2/competitions/PL/teams', None, headers )


response = json.loads(connection.getresponse().read().decode())

c=response['teams']


print(c)



