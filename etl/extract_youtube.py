from googleapiclient.discovery import build



import os
from dotenv import load_dotenv
load_dotenv()


def get_youtube_client():
    return build('youtube', 'v3', developerKey=os.getenv('YOUTUBE_API_KEY'))

def fetch_youtube_videos(region='BR', max_results=20):
    yt = get_youtube_client()
    req = yt.videos().list(
        part="snippet,statistics",
        chart="mostPopular",
        regionCode=region,
        maxResults=max_results
    )
    return req.execute()['items']
