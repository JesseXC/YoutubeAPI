from pyyoutube import Api

class YTstats:
  def __init__(self,apikey,channel_id):
    self.api = Api(api_key=f"{apikey}")
    self.channel_id = channel_id
    self.channel_statistics = None

  def get_channel_statistics(self):
    channel_by_id = self.api.get_channel_info(channel_id="UC_x5XG1OV2P6uZZ5FSM9Ttw")
    #print(url)
    statistics = channel_by_id.items[0].to_dict()
    return statistics
  
  def get_description(self):
    dictionary = self.get_channel_statistics()
    return dictionary['snippet']['description']
