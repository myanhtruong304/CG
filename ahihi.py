pip install pycoingecko

from pycoingecko import CoinGeckoAPI
import time
cg = CoinGeckoAPI()
link = input('Links:')
ids = link.split('/')[-1]

while True:
    try:
        a = cg.get_coin_by_id(ids)
        break
    except:
        time.sleep(30)
        continue
      
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
sheet_id = '1nTBVXt8Aw-5S2ua21DjcBjSYrvJB5E2-tu6ShNhtg20'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
#result = sheet.values().get(spreadsheetId=sheet_id, range='Market!B1:P5000').execute()
#values = result.get('values', [])

market_data = a['market_data']

Market_Data = list([link,
             a['name'],
             a['symbol'],
             a['community_score'],
             a['liquidity_score'],
             market_data['current_price']['usd'],
             market_data['total_value_locked'],
             market_data['ath']['usd'],
             market_data['atl']['usd'],
             market_data['market_cap']['usd'],
             market_data['total_volume']['usd'],
             market_data['circulating_supply'],
             market_data['total_supply'],
             market_data['max_supply'],
             a['image']['large']])
             
        
com_list = list([[a['name']],list(a['community_data'].values())])
import itertools
Community_Data = list(itertools.chain.from_iterable(com_list))
Community_Data

platforms = list(filter(None, list(a['platforms'].keys())))
Platforms_Data = []
for p in platforms:
    Platforms_Data.append([a['name'],p, a['platforms'][p]])
    
#Market
request_market = sheet.values().append(spreadsheetId=sheet_id, range='Market!A1:P5000', valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body={'values': [Market_Data]})
response_market = request_market.execute()

#Community
request_community = sheet.values().append(spreadsheetId=sheet_id, range='Community Data!A1:H5000', valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body={'values': [Community_Data]})
response_community = request_community.execute()

#Platforms
request_platforms = sheet.values().append(spreadsheetId=sheet_id, range='Platforms!B1:C5000', valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body={'values': Platforms_Data})
response_platforms = request_platforms.execute()
