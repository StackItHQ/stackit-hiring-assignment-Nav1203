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
if 'df' not in st.session_state:
    st.session_state.df=None
if 'file_id' not in st.session_state:
    st.session_state.file_id=None
if 'file_change' not in st.session_state:
    st.session_state.file_change=False
# def get_delimiter(file, bytes = 4096):
#     sniffer = csv.Sniffer()
#     data = str(file.read())
#     delimiter = sniffer.sniff(data).delimiter
#     return delimiter
# def reload_file():
#     if (file.name!=)
#         st.session_state.df=None
def upload_data_to_sheets(df,row,num,unfil,url,sname):
    pts=url.split('/')
    for i in range(0,len(pts)):
        if pts[i]=='d':
            file_id=pts[i+1]
            break
    # file_id=pts[i]
    if num:
        new_df=df.iloc[:,start-1:end-1]
        cols=[list(new_df.columns)]
        cols.extend(new_df.values.tolist())
        request=sheet.values().update(spreadsheetId=file_id,
                                range=f'{sname}',valueInputOption='USER_ENTERED',body={'values':cols}).execute()
        
    elif row:
        dropped=[]
        for i in vals:
            if vals[i]==False:
                dropped.append(i)
        new_df=df.drop(dropped,axis=1)
        cols=[list(new_df.columns)]
        cols.extend(new_df.values.tolist())
        request=sheet.values().update(spreadsheetId=file_id,
                                range=f'{sname}',valueInputOption='USER_ENTERED',body={'values':cols}).execute()
    elif unfil:
        cols=[list(df.columns)]
        cols.extend(df.values.tolist())
        # print(len(cols),cols[0])
        request=sheet.values().update(spreadsheetId=file_id,
                                    range=f'{sname}',valueInputOption='USER_ENTERED',body={'values':cols}).execute()

    st.success(f'Success!:  {str(request)}')
st.header('CSV to Google Sheets Importer :memo:')
st.write('Hey :wave:')
st.write('Instructions are simple, You create a new Google sheet add the following email as a user in the shared members after clicking on the share button.')
st.write('')
st.write('Email to Add:')
st.code('sheetapi@sheetsapidemo-400606.iam.gserviceaccount.com')
width=50
side=((100-width)/2)
_,container,_=st.columns([side,width,side])
with container:
    st.video('instruction.mp4')
file=st.file_uploader('Upload CSV files',accept_multiple_files=False,type='csv')
print(file)
if file.file_id != st.session_state.file_id:
    st.session_state.df=None
    st.session_state.file_id=file.file_id
if file is not None:
    # delim=get_delimiter(file)
    if type(st.session_state.df)=="<class 'NoneType'>":
        st.session_state.df=pd.read_csv(file,on_bad_lines='skip',sep=None)
    st.write("Preview Dataset")
    st.write(st.session_state.df)
    vals={}
    url=st.text_input('Paste the URL of the Google sheet you want the data in: ')
    sname=st.text_input('Sheet Name in the file of where the data has to be pasted (has to be created manually):')
    '''
     You can use the below methods to modify
     your dataset
    '''
    
    '''
    Filtering can be done column-wise as well as row-wise
    '''
    filter_method=st.selectbox('How to filter dataset?',options=['By Column Names','By Indexing','No filter'],index=2)
    # filter_names=st.checkbox('Filter By Column Names')
    # filter_number=st.checkbox('Filter By Indexes')
    row,num,unfil=False,False,False
  
    if filter_method=='By Column Names':
        row=True
        for i in st.session_state.df.columns:
            temp=st.checkbox(str(i))
            vals[i]=temp
        # agreed=st.button('Click to choose')
        # if agreed:
        #     for i in vals:
        #         if vals[i]:
        #             st.write(i)
    elif filter_method=='By Indexing':
        num=True
        start,end=st.select_slider('Include Range of Columns',options=[i+1 for i in range(0,st.session_state.df.shape[1])],value=(1,st.session_state.df.shape[1]))
    elif filter_method=='No filter':
        unfil=True
    '''
    Value based formatting
    '''
    row_wise=st.selectbox('Filters based on row values',options=['No filter','Conditional Range filter','Filter Values Out'])
    
    if row_wise=='Conditional Range filter':
        st.warning('Click Apply filter to apply row wise filtering!')
        col=st.selectbox('Column to filter:',options=st.session_state.df.columns)
        s1=st.text_input('Starting from:')
        s2=st.text_input('Ending to:')
        click=st.button('Apply filter')
        if click:
            if s1==None or s1==' ':
                st.warning('Enter Start Value')
            elif s2==None or s2==' ':
                st.warning('Enter End Value')
            else:
                with st.status('Running'):
                    st.session_state.df=st.session_state.df[(st.session_state.df[col]>=int(s1)) & (st.session_state.df[col]<=int(s2))]
                st.success('Filter Applied!')
                st.write(st.session_state.df)

    elif row_wise=='Filter Values Out':
        st.warning('Click Apply filter to apply row wise filtering!')
        col=st.selectbox('Column to filter:',options=st.session_state.df.columns)
        s1=st.text_input('Value:')
        click=st.button('Apply filter')
        if click:
            if s1==None or s1==' ':
                st.warning('Enter Start Value')
            else:
                with st.status('Running'):
                    st.write('running')
                    st.session_state.df=st.session_state.df[st.session_state.df[col]!=s1]
                st.success('Filter Applied!')
                st.write(st.session_state.df)


    tap=st.button('Upload to sheet')
    if tap:
        if url==None or url =='':
            st.warning('Provide Sheet URL')
        else:
            with st.status('Running!'):
                upload_data_to_sheets(st.session_state.df,row,num,unfil,url,sname)
