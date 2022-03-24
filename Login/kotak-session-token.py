import json
from ks_api_client import ks_api

with open('config.json') as config_file:
    config = json.load(config_file)

client = ks_api.KSTradeApi(access_token=config['kotak_access_token'],
                           userid=config['kotak_user'],
                           consumer_key=config['kotak_consumer_key'],
                           ip="127.0.0.1", app_id="")

login_response = (client.login(password = config['kotak_password']))

#enter the received otp
otp = input('Enter access code to proceed.\n')
print(client.session_2fa(access_code =str(otp)))


config['kotak_one_time_token'] = client.one_time_token
config['kotak_session_token'] = client.session_token
config['kotak_access_code'] = otp

with open('config.json', 'w') as config_file:
    json.dump(config , config_file, sort_keys=True, indent=4)
