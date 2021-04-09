import os
import sys

working_proj_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(working_proj_dir)
from scripts.jsonblob import JsonBlob
from scripts.to_json import solve

if __name__ == '__main__':
    products_json = solve(os.path.join(working_proj_dir, "src", "assets", "img", "products"))
    json_blob = JsonBlob(products_json)
    json_blob.put()
