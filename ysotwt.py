import requests
import logging

ysotwt = requests.get('https://siotwt.bender.sway.org/api/v1/zipcode/66219')

logging.basicConfig(level=logging.INFO)

if ysotwt.json()['youShouldOpenTheWindowsTonight']:
	data = { 'converse': True, 'command': 'broadcast message to kitchen sink, you should open the windows tonight.', 'name': 'leland'}
	braodcast = requests.post('http://192.168.1.50:3000/assistant', json=data)
	logging.info('open the windows.')	
else: 
	logging.info('don\'t open the windows.')	

