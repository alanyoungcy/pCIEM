import requests
import json
import webbrowser
#import pandas as pd



apiStrings = [
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20201203-1251',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20210107-1258',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20210204-1327',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20210303-1406',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20210417-1226',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20210505-1227',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20210604-1313',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20210706-1356',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20210805-1321',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20210903-1242',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20211007-1343',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20211104-1316',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20211203-1323',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20220105-2021',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20220211-1337',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20220314-1355',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20220406-1703',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20220510-1657',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20220607-1723',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20220706-1451',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20220805-1324',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20220903-1308',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20221006-1336',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20221104-1334',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20221206-1330',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20230107-1353',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20230203-1358',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20230306-1346',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20230404-1411',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20230504-1330',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20230603-1313',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20230704-1312',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20230808-1427',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20230905-1407',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20231004-1450',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20231102-1438',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20231206-1423',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20240104-1417',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20240203-1352',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20240307-1437',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20240406-1348',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20240509-1041',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20240607-1025',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20240704-1054',
'https://app.data.gov.hk/v1/historical-archive/get-file?url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time=20240725-1048'
]

i = 0
import codecs
import csv


with open('test.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    #writer.writerows([])
    writer.writerow(['Date','No. of Internet mails received','No. of Internet mails filtered','No. of Internet mails sent'])
    for iurl in apiStrings:
        print("getting from " + iurl)
        r = requests.get(iurl)

        decoded_data = codecs.decode(r.text.encode(), 'utf-8-sig')
        data = json.loads(decoded_data)

        for record in data:
            date = str(record['year']) + '/' + str(record['month'])
            mailrecevied = str(record['types'][0]['number'])
            mailfiltered = str(record['types'][1]['number'])
            mailsent = str(record['types'][2]['number'])

            writer.writerow([date, mailrecevied,mailfiltered,mailsent])
           # print(" Time ", record['year'], " ",record['month'], " percentatge ", record['types'][0]['type'],' ',record['types'][0]['number'])

