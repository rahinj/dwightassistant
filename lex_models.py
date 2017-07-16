import boto3
import gmail
class LexApi:
  def __init__(self):
    self.client = boto3.client('lex-models')
  def delete_bot(self):
    response = self.client.delete_bot(name="Dwight")
    return response
  def delete_intent(self):
    self.delete_bot();
    for intent in gmail.get_intents():    
      response = self.client.delete_intent(name=intent['name'])
    return True
  def create_bot(self):
    params = gmail.get_bot()
    params["checksum"] = self.get_bot()["checksum"]
    response = self.client.put_bot(**params)
    return response
  def create_intent(self):
    res = []
    for intent in gmail.get_intents():
      intent["checksum"] = self.get_intent(intent["name"])["checksum"]
      response = self.client.put_intent(**intent)
      res.append(response)
    return res
  def get_bots(self):
    return self.client.get_bots()
  # def set_up_bot():
  #   pass
  def get_bot(self):
    return self.client.get_bot(name="Dwight",versionOrAlias="$LATEST")
  def get_bot_channel_associations(self):
    return self.client.get_bot_channel_associations(botName="Dwight",botAlias="LATEST")
  def get_intent(self, name):
    return self.client.get_intent(name=name, version="$LATEST")

class LexRunTimeApi:
  """docstring for LexRunTimeApi"""
  def __init__(self):
    self.client = boto3.client('lex-runtime')
  def send_message(self, message):
#     client.post_text(
#     botName='string',
#     botAlias='string',
#     userId='string',
#     sessionAttributes={
#         'string': 'string'
#     },
#     inputText='string'
# )
    return self.client.post_text(botName="Dwight", botAlias="$LATEST", userId="mama", inputText=message)