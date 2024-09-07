import os
import numpy as np
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.errors import HttpError
import pandas as pd
import json

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"

    # This file needs to be registered and downloaded by yourself
    client_secrets_file = "client_secret_56381008278-5gk503lqdkonqtghaeb82m3jbep43ve6.apps.googleusercontent.com.json"
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    videoId = '9bqFjcDeVIg'
    request = youtube.commentThreads().list(
        part="snippet,replies",
        videoId=videoId,
        maxResults=10000
    )
    response = request.execute()

    totalResults = int(response['pageInfo']['totalResults'])

    count = 0
    nextPageToken = ''
    comments = []
    first = True
    further = True
    while further:
        halt = False
        if first == False:
            print('..')
            try:
                response = youtube.commentThreads().list(
                    part="snippet,replies",
                    videoId=videoId,
                    maxResults=100,
                    textFormat='plainText',
                    pageToken=nextPageToken
                ).execute()
                totalResults = int(response['pageInfo']['totalResults'])
            except HttpError as e:
                print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
                halt = True

        if halt == False:
            count += totalResults
            for item in response["items"]:
                # This is only a part of the data. 
                # You can choose what you need. You can print the data information you can get and crawl it as needed.
                comment = item["snippet"]["topLevelComment"]
                author = comment["snippet"]["authorDisplayName"]
                text = comment["snippet"]["textDisplay"]
                likeCount = comment["snippet"]['likeCount']
                publishtime = comment['snippet']['publishedAt']
                comments.append([author, publishtime, likeCount, text])
            if totalResults < 100:
                further = False
            else:
                further = True
                first = False
                try:
                    nextPageToken = response["nextPageToken"]
                except KeyError as e:
                    print("An KeyError error occurred: %s" % (e))
                    further = False
    print('get data count: ', str(count))

    ### write to csv file
    data = np.array(comments)
    df = pd.DataFrame(data, columns=['author', 'publishtime', 'likeCount', 'comment'])
    df.to_csv('google_comments.csv', index=0, encoding='utf-8')
