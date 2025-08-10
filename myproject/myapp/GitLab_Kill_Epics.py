import gitlab
import requests
import certifi
import csv
import time
import os

import urllib3

#connect to gitlab

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

TOKEN= "glpat-ewHR2L-evv3MCi3XyJZ6"

#GROUP_PATH = 'kuba474650'
GROUP_PATH = 'kuba474650'

# Autoryzacja
gl = gitlab.Gitlab('https://gitlab.com/', private_token=TOKEN)

# Pobranie grupy
group = gl.groups.get(GROUP_PATH)

# Pobranie epików
epics = group.epics.list(all=True)

# Usuwanie epików
for epic in epics:
    print(f"Usuwanie epika: {epic.title} (ID: {epic.id})")
    epic.delete()

print('Epics are killed')