import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer
from requests import get
import settings
from time import sleep
from datetime import datetime


def auth():
    # authentication
    redirect_uri = 'http://localhost:8080/'
    client_secret = settings.CLIENT_SECRET
    scopes = ['wl.signin', 'wl.offline_access', 'onedrive.readwrite']
    client = onedrivesdk.get_default_client(
        client_id=settings.CLIENT_ID, scopes=scopes)
    auth_url = client.auth_provider.get_auth_url(redirect_uri)
    code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)
    client.auth_provider.authenticate(code, redirect_uri, client_secret)
    return client


def get_ip():
    # get external ip address and save it in 'ip.txt'
    ext_ip = get('https://ipapi.co/ip/').text
    with open('ip.txt', 'w') as f:
        f.write(ext_ip)


def upload_file():
    # upload file
    returned_item = client.item(
        drive='me', id='root').children['Raspberry_Pi_IP.txt'].upload('./ip.txt')


sync_interval = max(5*60, settings.SYNC_INTERVAL*60) # limit sync every 5 minutes
sync_days = settings.SYNC_DAYS

start_time = datetime.now()

while not sync_days or (datetime.now() - start_time).days <= sync_days:
    client = auth()
    get_ip()
    upload_file()
    sleep(sync_interval)
