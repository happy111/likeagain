from channels.consumer import SyncConsumer

class MySyncConsumer(SyncConsumer):
	def websocket_connect(self,event):
		print('Websocket Connected...')
	def websocket_receive(self,event):
		print('messaged Received')
	def websocket_disconnect(self,event):
		print('websocket DIsconnected.')