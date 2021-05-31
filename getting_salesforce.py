import json
import pandas
from simple_salesforce import Salesforce, SalesforceLogin, SFType

logininfo= json.load(open('login.json'))
username= logininfo['username']
password= logininfo['password']
security_token= logininfo['security_token']
domain= 'login'

# sf= Salesforce(username= username,password=password,security_token=security_token, domain=domain)
# print(sf)

session_id, instance= SalesforceLogin(username= username,password=password,security_token=security_token, domain=domain)
sf= Salesforce(session_id=session_id, instance=instance)

for element in dir(sf):
    if not element.startswith('_'):
        if isinstance(getattr(sf, element),str):
            print('Property Name: {0} ; Value: {1}'.format(element, getattr(sf, element)))

metadata_org= sf.describe()

print(metadata_org["encoding"])
print(metadata_org["maxBatchSize"])
print(type(metadata_org["sobjects"]))

account= sf.account