About
=====
Repo create a PushNotification Server

Requirements
============
1. Python3.4, pip3 and nodeJS
2. Python modules : tornado, json, requests, python-gcm  (`pip3 install <package-name>`)
3. Node modules   : rectify                              (`npm install  <package-name>`)

*use sudo if any error occurs.

Instructions
============
1. Clone mutoPush repo to local system
2. In Terminal run 'python3 pushServer.py`
 
Input/Output
============
1. Input is Json Object with Key: Value pair as {"platform" : platform, "deviceID" : deviceID } to serverUrl:8000/push
2. Output response is "{"iOS" : "OK"}, {"Android" : "OK"} or {"Status" : "FAILED" } based on the request.
 
