WIP

A simple python3 tool to get the external ip address of your Raspberry Pi (tested on my 3B+) and sync it to onedrive.

This only works in desktop environment because it will open the browser to authenticate.

# 1. Create a Miscrosoft graph app
You need to [create a microsoft graph app](https://docs.microsoft.com/en-us/onedrive/developer/rest-api/getting-started/app-registration?view=odsp-graph-online) first so you can gain access to your onedrive content.

After creating your microsoft graph app, assign your clent_id and client_secret in `settings.py`.

# 2. Install packages
## 2.1 Create a virtual environment (optional, recommended)

## 2.2 Install packages
`pip install --upgrade pip`

`pip install onedrivesdk`

# 3. Set parameters and run
You can set the intervals for uploading and how many days you want the program keep running in `settings.py`.

`python3 sync.py` to run.
