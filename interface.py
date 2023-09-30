from __future__ import print_function
import streamlit as st
import pandas as pd
import csv
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'credentials.json'

credentials=None
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('sheets', 'v4', credentials=credentials)
sheet = service.spreadsheets()

# def get_delimiter(file, bytes = 4096):
#     sniffer = csv.Sniffer()
#     data = str(file.read())
#     delimiter = sniffer.sniff(data).delimiter
#     return delimiter
def upload_data_to_sheets(dataframe,row,num,unfil,url,sname):
    file_id='1vgIhl4taJWmI97rgZU_A-KDNNZzZXtEeL5rNHaoVJvI'

    if num:
        new_df=dataframe.iloc[:,start-1:end-1]
        cols=[list(new_df.columns)]
        cols.extend(new_df.values.tolist())
        request=sheet.values().update(spreadsheetId=file_id,
                                range=f'{sname}',valueInputOption='USER_ENTERED',body={'values':cols}).execute()
        
    elif row:
        dropped=[]
        for i in vals:
            if vals[i]==False:
                dropped.append(i)
        new_df=dataframe.drop(dropped,axis=1)
        cols=[list(new_df.columns)]
        cols.extend(new_df.values.tolist())
        request=sheet.values().update(spreadsheetId=file_id,
                                range=f'{sname}',valueInputOption='USER_ENTERED',body={'values':cols}).execute()
    elif unfil:
        cols=[list(dataframe.columns)]
        cols.extend(dataframe.values.tolist())
        # print(len(cols),cols[0])
        request=sheet.values().update(spreadsheetId=file_id,
                                    range=f'{sname}',valueInputOption='USER_ENTERED',body={'values':cols}).execute()

    st.success(f'Success!:  {str(request)}')
st.header('CSV to Google Sheets Importer')
st.write('Hey :wave:')
st.write('Instructions are simple, You create a new Google sheet add the following email as a user in the shared members after clicking on the share button.')
st.code('sheetapi@sheetsapidemo-400606.iam.gserviceaccount.com')
file=st.file_uploader('Upload CSV files',accept_multiple_files=False,type='csv')
if file is not None:
    # delim=get_delimiter(file)
    dataframe=pd.read_csv(file,on_bad_lines='skip',sep=None)
    st.write("Preview Dataset")
    st.write(dataframe)
    vals={}
    url=st.text_input('Paste the URL of the Google sheet you want the data in: ')
    sname=st.text_input('Sheet Name in the file of where the data has to be pasted')
    filter_method=st.selectbox('How to filter dataset?',options=['By Row Names','By Indexing','No filter'])
    # filter_names=st.checkbox('Filter By Column Names')
    # filter_number=st.checkbox('Filter By Indexes')
    row,num,unfil=False,False,False
  
    if filter_method=='By Row Names':
        row=True
        for i in dataframe.columns:
            temp=st.checkbox(str(i))
            vals[i]=temp
        agreed=st.button('Click to choose')
        if agreed:
            for i in vals:
                if vals[i]:
                    st.write(i)
    elif filter_method=='By Indexing':
        num=True
        start,end=st.select_slider('Include Range of Rows',options=[i+1 for i in range(0,dataframe.shape[1])],value=(1,dataframe.shape[1]))
    elif filter_method=='No filter':
        unfil=True
    tap=st.button('Upload to sheet')
    if tap:
        if url==None or url =='':
            st.warning('Provide Sheet URL')
        else:
            with st.status('Running!'):
                upload_data_to_sheets(dataframe,row,num,unfil,url,sname)