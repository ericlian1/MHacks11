import requests
import json
import numpy as np
import pandas as pd

# import matplotlib.pyplot as plt
def get_data(ticker,startDate,endDate):
    client_id = '9f096dbb7c2742c8ae3e596c4f388835'
    client_secret = 'b97b003435c9c538accd86fa81f65d320056a63110a726e2882a50e3042cceb0'

    auth_data = {
        "grant_type"    : "client_credentials",
        "client_id"     : client_id,
        "client_secret" : client_secret,
        "scope"         : "read_product_data read_financial_data read_content"
    }

    # create session instance
    session = requests.Session()

    auth_request = session.post("https://idfs.gs.com/as/token.oauth2", data = auth_data)
    access_token_dict = json.loads(auth_request.text)
    access_token = access_token_dict["access_token"]

    # update session headers with access token
    session.headers.update({"Authorization":"Bearer "+ access_token})

    request_url = "https://api.marquee.gs.com/v1/data/USCANFPP_MINI/query"

    request_query = {
            "where": {
                    "ticker" : ticker
                    },
            "startDate": startDate,
            "endDate": endDate
    }
    req = session.post(url = request_url, json = request_query)
    data = json.loads(req.text)
    data = data['data']
    df = pd.DataFrame(data)
    print(df)
    return df

assets = pd.read_csv("marquee_companies.csv")
tickers = assets['ticker']
gsids = assets['gsid']

#og = pd.DataFrame.from_csv("marquee_data.csv")

og = pd.DataFrame()
#tickers[67] not working
for i in range(0,len(tickers)):
    print(i)
    if(i == 67):
        break
    df = get_data(tickers[i],"2000-01-01","2018-06-30")
    og = pd.concat([og,df])
og.to_csv("marquee_data.csv")

# results = json.loads(request.text)
# print(len(results['data']))
# for i in results['data']:
#     print(i)
