
"""
Get a user by id
"""
# Path to lib directory which contains pytan package
PYTAN_LIB_PATH = '../lib'

# connection info for Tanium Server
USERNAME = "Tanium User"
PASSWORD = "T@n!um"
HOST = "172.16.31.128"
PORT = "444"

# Logging conrols
LOGLEVEL = 2
DEBUGFORMAT = False

import sys, tempfile
sys.path.append(PYTAN_LIB_PATH)

import pytan
handler = pytan.Handler(
    username=USERNAME,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    loglevel=LOGLEVEL,
    debugformat=DEBUGFORMAT,
)

print handler

# setup the arguments for the handler method
kwargs = {}
kwargs["objtype"] = u'user'
kwargs["id"] = 1

# call the handler with the get method, passing in kwargs for arguments
response = handler.get(**kwargs)

print ""
print "Type of response: ", type(response)

print ""
print "print of response:"
print response

print ""
print "length of response (number of objects returned): "
print len(response)

print ""
print "print the first object returned in JSON format:"
print response.to_json(response[0])


'''Output from running this:
Handler for Session to 172.16.31.128:444, Authenticated: True, Version: 6.2.314.3258

Type of response:  <class 'taniumpy.object_types.user_list.UserList'>

print of response:
UserList, len: 1

length of response (number of objects returned): 
1

print the first object returned in JSON format:
{
  "_type": "user", 
  "deleted_flag": 0, 
  "group_id": 0, 
  "id": 1, 
  "last_login": "2014-12-08T19:28:09", 
  "name": "Jim Olsen", 
  "permissions": {
    "_type": "permissions", 
    "permission": "admin"
  }, 
  "roles": {
    "_type": "roles", 
    "role": [
      {
        "_type": "role", 
        "description": "Administrators can perform all functions in the system, including creating other users, viewing the System Status, changing Global Settings, and creating Computer Groups.", 
        "id": 1, 
        "name": "Administrator", 
        "permissions": {
          "_type": "permissions", 
          "permission": "admin"
        }
      }
    ]
  }
}

'''
