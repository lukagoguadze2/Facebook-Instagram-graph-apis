from define import getCreds, makeApiCall

def create_container(params, video_url, caption):
    """
    POST https://graph.facebook.com/{api-version}/{ig-user-id}/media
        ?media_type=REELS
        &video_url={reel-url}
        &caption={caption}
        &share_to_feed={share-to-feed}
        &collaborators={collaborator-usernames}
        &cover_url={cover-url}
        &audio_name={audio-name}
        &user_tags={user-tags}
        &location_id={location-id}
        &thumb_offset={thumb-offset}
        &share_to_feed={share-to-feed}
        &access_token={access-token}

    Returns:
        data: creation id
    """
    endpointParams = dict()
    endpointParams["media_type"] = "REELS"
    endpointParams["video_url"] = video_url
    endpointParams["caption"] = caption
    endpointParams["share_to_feed"] = "true"
    endpointParams["access_token"] = params["page_access_token"]

    url = params["endpoint_base"] + params["instagram_business_id"] + "/media"

    return makeApiCall(url, endpointParams, debug="no", type="POST")

def publish_content(params, creation_id):
    """
    POST "https://graph.facebook.com/{api-version}/{ig-user-id}/media_publish
            ?creation_id={creation-id}
            &access_token={access-token}"
    """
    endpointParams = dict()
    endpointParams["creation_id"] = creation_id
    endpointParams["access_token"] = params["page_access_token"]

    url = params["endpoint_base"] + params["instagram_business_id"] + "/media_publish"

    return makeApiCall(url, endpointParams, debug="no", type="POST")

def get_status(params, creation_id):
    """
    GET "https://graph.facebook.com/{api-version}/{creation-id}
            ?fields=status_code
            &access_token={access-token}"
    """
    endpointParams = {
        "fields": "status_code",
        "access_token": params["page_access_token"]
    }

    url = params["endpoint_base"] + creation_id

    return makeApiCall(url, endpointParams, debug="no", type="GET")

def upload_reels(video_url, caption):
    from time import sleep
    import os
    params = getCreds()
    creation_id = create_container(params, video_url, caption)["json_data"]["id"] # creating a container

    # sending a get requests for status
    status = ""
    while True:
        status = get_status(params, creation_id)["json_data"]["status_code"].upper()
        if status in ["FINISHED", "ERROR", "EXPIRED"]:
            os.system("cls")
            print(f"\n ---- STATUS_CODE ----\npreperation status: {status}\n\n")
            break
        else:
            os.system("cls")
            print(f"\n ---- STATUS_CODE ----\npreperation status: {status}\n\n")
        sleep(5)

    sleep(2)
    if status == "FINISHED":
        invidid = publish_content(params, creation_id)
        while True:
            status = get_status(params, creation_id)["json_data"]["status_code"].upper()
            if status != "PUBLISHED":
                os.system("cls")
                print(f"\n ---- STATUS_CODE ----\nvideo status: {status}\n\n")
            else:
                os.system("cls")
                print(f"\n ---- STATUS_CODE ----\nuploading status: {status}\n\n")
                break
            sleep(5)
        return {"Uploaded": True, "MediaId": invidid}
    else:
        return {"Uploaded": False, "MediaId": None}
    
        
# upload_reels(VideoUrl, Caption)
    