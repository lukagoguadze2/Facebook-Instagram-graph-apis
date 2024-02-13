from define import getCreds, makeApiCall

def getUserPages(params):
    """"
    Get facebook pages for a user

    API Endpoint:
    https://graph.facebook.com/{graph-api-version}/me/accounts?access_token={access-token}

    Returns:
        object: data from the endpoint

    """
    endpointParams = dict()
    endpointParams['access_token'] = params['access_token']
    
    url = params['endpoint_base'] + "me/accounts"

    return makeApiCall(url, endpointParams, params['debug'])

params = getCreds()
params['debug'] = "no"
response = getUserPages(params)

print(f"\n---- FACEBOOK PAGE INFO ----\nPage Name: {response['json_data']['data'][0]['name']}")
print(f"\nPage id: {response['json_data']['data'][0]['category']}")
print(f"\nPage id: {response['json_data']['data'][0]['id']}\n")