__author__ = 'marino'

import requests
import json
from collections import namedtuple


def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)

r = requests.get('http://localhost:8181')
print r.content
pia=json2obj(r.content)
for p in pia:
    print p.costo, p.nome