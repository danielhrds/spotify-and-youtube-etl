import pandas as pd

def transform_spotify_data(tracks):
    data = []
    for item in tracks:
        track = item['track']
        data.append({
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'popularity': track['popularity'],
            'duration_min': round(track['duration_ms'] / 60000, 2),
            'album': track['album']['name'],
            'id': track['id']
        })
    return pd.DataFrame(data)

def transform_youtube_data(videos):
    data = []
    for v in videos:
        snippet = v['snippet']
        stats = v.get('statistics', {})
        data.append({
            'title': snippet['title'],
            'channel': snippet['channelTitle'],
            'categoryId': snippet.get('categoryId', ''),
            'views': int(stats.get('viewCount', 0)),
            'likes': int(stats.get('likeCount', 0)),
            'comments': int(stats.get('commentCount', 0)),
            'id': v['id']
        })
    return pd.DataFrame(data)
