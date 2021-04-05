import os
import sys

import requests

working_proj_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(working_proj_dir)
from scripts.to_json import solve


class JsonBlob:
    def __init__(self, json_data, blob_id_location=os.path.join(working_proj_dir, "scripts", "blob_id")):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        self.base_url = 'https://jsonblob.com/api'
        self.path = "marcodong/caspita_srl/lucca"

        self.blob_id_location = blob_id_location
        self.data = json_data

        self.url = f"{self.base_url}/{self.path}"
        try:
            self.blob_id = self._read()
        except FileNotFoundError:
            self.post()
            self.put()

    def post(self):
        response = requests.post("https://jsonblob.com/api/jsonBlob", headers=self.headers, data=self.data)
        print(response.status_code)
        self.blob_id = self._write(response)

    def put(self):
        response = requests.put(f'{self.url}/{self.blob_id}', headers=self.headers, data=self.data)
        return response.json()

    def get(self):
        return requests.get(f'{self.url}/{self._read()}', headers=self.headers).json()

    def _write(self, response):
        print(response.headers)
        blob_id = response.headers["Location"].split("/")[-1]
        with open(self.blob_id_location, "w") as f:
            f.write(blob_id)
        return blob_id

    def _read(self):
        with open(self.blob_id_location, "r") as f:
            return f.read()


if __name__ == '__main__':
    data = solve(os.path.join(working_proj_dir, "src", "assets", "img", "products"))
    json_blob = JsonBlob(data)

    print(json_blob.get())
