from define import getCreds, makeApiCall

def getInstagramAccount(params):
    """
    Get instagram account

    API Endpoint:

    https://graph.facebook.com/{graph-api-version}/me?access_token={page_access_token}&fields=instagram_business_account

    Returns:
        object: data from the endpoint
    """

    endpointParams = dict()
    endpointParams['access_token'] = params['page_access_token']

    url = params['endpoint_base'] + "me?fields=instagram_business_account"

    return makeApiCall(url, endpointParams , params['debug'])

params = getCreds()
params['debug'] = "no"
response = getInstagramAccount(params)

print(f"\n---- INSTAGRAM ACCOUNT INFO ----\nINSTAGRAM BUSINESS ACCOUNT ID: {response['json_data']['instagram_business_account']['id']}")
print(f"\nPAGE ID: {response['json_data']['id']}\n")
