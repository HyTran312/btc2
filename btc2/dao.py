import json
from btc2 import app

def load_json():
    with open(f'{app.root_path}/data/categories.json', encoding='utf-8') as f:
        return json.load(f)