from disco.bot import Plugin
import requests, json

class TutorialPlugin(Plugin):

	@Plugin.command("hola")
	def command_ping(self, event):
		event.msg.reply("Hola papu")
	
	@Plugin.command('gif', '<content:str...>')
	def on_echo_command(self, event, content):
		url = "https://api.giphy.com/v1/gifs/random?api_key=NXZO7oebdBXRlcevidtDaS5Zn0b765qP&tag="+content+"&rating=G"
		response = requests.get(url)

		
		#result = data["data"][0]["url"]

		#print json.loads(data)
		json_data = json.loads(response.text)
		image_url = json_data["data"]["images"]["original"]["url"]
		event.msg.reply(image_url)
