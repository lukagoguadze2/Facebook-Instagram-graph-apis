from define import getCreds, makeApiCall

def get_permalink(params, mediaid):
    """"
    GET https://graph.facebook.com/{graph-version}/{media-id}
        ?fields={fields}
        &access_token={access-token}

    Returns:
        permalink
    """
    endpointParams = dict()
    endpointParams["fields"] = "permalink"
    endpointParams["access_token"] = params["page_access_token"]

    url = params["endpoint_base"] + mediaid

    return makeApiCall(url, endpointParams, debug="no", type="GET")["json_data"]

params = getCreds()
response = get_permalink(params, "your_media_id")
print(f'Permalink: {response["permalink"]}\nMediaId: {response["id"]}')