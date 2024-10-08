import requests
import json
import plotly.graph_objects as go

# Initialize lists to store the data
months = []
mails_received = []
mails_filtered = []

# Define the base URL and the common part of the query string
base_url = "https://app.data.gov.hk/v1/historical-archive/get-file"
query_string = "url=https%3A%2F%2Fwww.digitalpolicy.gov.hk%2Fopen_data%2Fcis%2Fimx-statistics-en.json&time="

# Define the list of timestamps
timestamps = [
    "20201203-1251", "20210107-1258", "20210204-1327", "20210303-1406",
    "20210417-1226", "20210505-1227", "20210604-1313", "20210706-1356",
    "20210805-1321", "20210903-1242", "20211007-1343", "20211104-1316",
    "20211203-1323", "20220105-2021", "20220211-1337", "20220314-1355",
    "20220406-1703", "20220510-1657", "20220607-1723", "20220706-1451",
    "20220805-1324", "20220903-1308", "20221006-1336", "20221104-1334",
    "20221206-1330", "20230107-1353", "20230203-1358", "20230306-1346",
    "20230404-1411", "20230504-1330", "20230603-1313", "20230704-1312",
    "20230808-1427", "20230905-1407", "20231004-1450", "20231102-1438",
    "20231206-1423", "20240104-1417", "20240203-1352", "20240307-1437",
    "20240406-1348", "20240509-1041", "20240607-1025", "20240704-1054",
    "20240725-1048"
]

# Generate the list of URLs
apiStrings = [f"{base_url}?{query_string}{timestamp}" for timestamp in timestamps]

# Loop through each URL to fetch data
for iurl in apiStrings:
    print(iurl)
    r = requests.get(iurl).content
    response_list = json.loads(r)
  
    # Loop through each dictionary in the response list

    for response_dict in response_list:
        
        # Extract the month and year
        month = response_dict.get("month")
        year = response_dict.get("year")
        
        # Find the required types
        received = next((item['number'] for item in response_dict['types'] if item['type'] == 'No. of Internet mails received'), 0)
        filtered = next((item['number'] for item in response_dict['types'] if item['type'] == 'No. of Internet mails filtered'), 0)
        
        # Append the data to the lists
        months.append(f"{year}-{month:02d}")  # Format as "YYYY-MM"
        mails_received.append(received)
        mails_filtered.append(filtered)

# Create a bar chart using Plotly
fig = go.Figure(data=[
    go.Bar(name='No. of Internet mails received', x=months, y=mails_received),
    go.Bar(name='No. of Internet mails filtered', x=months, y=mails_filtered)
])

# Update the layout
fig.update_layout(
    title='Internet Mails Statistics',
    xaxis_title='Month',
    yaxis_title='Number of Mails',
    barmode='group'
)

# Show the plot
fig.show()