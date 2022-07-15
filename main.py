from youtubeAPI import YTstats
from pyyoutube import Api

yt = YTstats("AIzaSyCrqPhwI-0t28ejuQzHrTfrh89_S_g9Gg8","UC_x5XG1OV2P6uZZ5FSM9Ttw")

print(yt.get_description())
#video_by_id = api.get_video_by_id(video_id="CvTApw9X8aA")
#print(channel_by_id.items[0].to_dict())
#channel_by_id.items[Channel(kind='youtube#channel', id='UC_x5XG1OV2P6uZZ5FSM9Ttw')]
#channel_by_id.items[0].to_dict()

#API_KEY = "AIzaSyCrqPhwI-0t28ejuQzHrTfrh89_S_g9Gg8"
#channel_id = "UCTZRcDjjkVajGL6wd76UnGg"

#yt = YTstats(API_KEY,channel_id)
#yt.get_channel_statistics()