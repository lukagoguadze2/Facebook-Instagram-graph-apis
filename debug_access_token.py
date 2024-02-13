from define import getCreds, makeApiCall
import datetime

def debugAccessToken(params):
    """" Get info on an access token

    API Endpoint:
    https://graph.facebook.com/
    debug_token?input_token={input-token}&Beeessmtoken={valid-access-token}

    Returns:
        object: data from the endpoint
    """
    endpointParams = dict()
    endpointParams["input_token"] = params["access_token"]
    endpointParams["access_token"] = params["access_token"]

    url = params["graph_domain"] + "/debug_token"

    return makeApiCall(url, endpointParams, params["debug"])

params = getCreds()
params["debug"] = "no"
response = debugAccessToken(params)

print(f'\nData Excpires at: {datetime.datetime.fromtimestamp(response["json_data"]["data"]["data_access_expires_at"])}')
if response["json_data"]["data"]["expires_at"]:
    print(f'\nToken Excpires at: {datetime.datetime.fromtimestamp(response["json_data"]["data"]["expires_at"])}')
else:
    print(f'\nToken Excpires at: Never')
