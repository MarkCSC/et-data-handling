import requests
import json
import logging

APP_ID = "edtorch_project_8d7e91_0e1a52"
APP_API_KEY = "5d19e69eae6de933aa7b86654cb97e4dc04f42c2a5c2df20aedda1b56a86a817"

class Mathpix:
    def __init__(self, app_id=APP_ID, app_key_api=APP_API_KEY):
        self.app_id = app_id
        self.app_api_key = app_key_api
    
    def sendOne(self, file=None):
        if file == None:
            logging.error("Cropped image doesn't exist, can't send to mathpix")
            print("File doesn't exist")
            return
        
        with open(file, 'rb') as img: 
            r = requests.post("https://api.mathpix.com/v3/text", 
                files={"file": img},
                data={
                    "options_json": json.dumps({
                        "math_inline_delimiters": ["$", "$"],
                        "rm_spaces": True
                    })
                },
                headers={
                    "app_id": self.app_id,
                    "app_key": self.app_api_key
                }
            )
            print(json.dumps(r.json(), indent=4, sort_keys=True))