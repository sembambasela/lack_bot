import os
import requests  
import datetime 
from googleapiclient.discovery import build
from  google_auth_oauthlib.flow import InstalledAppFlow  
from google.auth.transport.requests import Request 
from google.oauth2.credentials import Credentials 
from requests.structures import CaseInsensitiveDict 

#import pandas as pd 
import json 



# if modifying these scopes, delete the file token.json
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly','https://www.googleapis.com/auth/calendar','https://www.googleapis.com/auth/calendar.event.readonly','https://www.googleapis.com/auth/calendar.event']
all_events = []

def main(): 
  creds=None 
  if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json',SCOPES)
  if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token: 
        creds.refresh(Request())
      else: 
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json',SCOPES)
        creds =  flow.run_local_server(port = 0) 
      with open('token.json','w') as token: 
        token.write(creds.to_json())

  service = build('calendar','v3', credentials = creds) 
  now = datetime.datetime.utcnow().isoformat() + 'Z'
  events = service.events().list(calendarId = 'primary',timeMin = now, singleEvents=True, orderBy = 'startTime').execute() 
  all_events.append(events)
  print(all_events)
 
main() 
