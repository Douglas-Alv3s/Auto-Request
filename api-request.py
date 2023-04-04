import requests
import time

url = 'https://api-logic-lqttb.run-us-west2.goorm.site/api-logic/arguments/1/1/MP/1'
headers = {'User-Agent': 'User-desktop'}

while True:
    response = requests.get(url, headers=headers)
    print(response.text)  # Apenas para fins de depuração; remova ou comente isso em produção
    time.sleep(900)  # Espera 900 segundos (15 minutos)
