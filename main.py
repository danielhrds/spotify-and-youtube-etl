from etl.extract_spotify import fetch_spotify_tracks
from etl.extract_youtube import fetch_youtube_videos
from etl.transform import transform_spotify_data, transform_youtube_data
from etl.load_mongo import save_to_mongo

SPOTIFY_PLAYLIST_ID = "62Wt2P8MII4yK8QK1rz1k3"

spotify_raw = fetch_spotify_tracks(SPOTIFY_PLAYLIST_ID)
spotify_df = transform_spotify_data(spotify_raw)
save_to_mongo("spotify_tracks", spotify_df)

youtube_raw = fetch_youtube_videos()
youtube_df = transform_youtube_data(youtube_raw)
save_to_mongo("youtube_videos", youtube_df)

print("ETL finalizado com sucesso.")
