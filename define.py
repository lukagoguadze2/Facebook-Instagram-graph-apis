import requests
import json

def getCreds():
    creds = dict()
    creds["access_token"] = "your_short_live_token"
    creds["page_access_token"] = "your_long_live_token"
    creds["client_id"] = "your_client_id"
    creds["client_secret"] = "your_client_secret"
    creds["graph_domain"] = "https://graph.facebook.com/"
    creds["graph_version"] = "v18.0"
    creds["endpoint_base"] = creds["graph_domain"] + creds["graph_version"] + "/"
    creds["debug"] = "no"
    creds["page_id"] = "your_facebook_page_id"
    creds["instagram_business_id"] = "your_instagram_business_id"

    return creds

def makeApiCall(url, endpointParams, debug = "no", type="GET"):
    if type.lower() == "get":
        data = requests.get(url, endpointParams)
    elif type.lower() == "post":
        data = requests.post(url, endpointParams)
    
    response = dict()
    response["url"] = url
    response["endpoint_params"] = endpointParams
    response["endpoint_params_pretty"] = json.dumps(endpointParams, indent=4)
    response["json_data"] = json.loads(data.content)
    response["json_data_pretty"] = json.dumps(response["json_data"], indent=4)

    if debug == "yes":
        displayApiCallData(response)

    return response

def displayApiCallData(response):
     print(f"\nURL: {response['url']}\nEndpoint Params: {response['endpoint_params_pretty']}\nResponse: {response['json_data_pretty']}")

     