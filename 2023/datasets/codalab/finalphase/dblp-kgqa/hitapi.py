import requests
import json


d = json.loads(open('dblp.heldout.500.questionsonly.json').read())

models = ['t5-small','t5-base']
embeddings = ['transe','complex','distmult']


urlbase = "https://ltdemos.informatik.uni-hamburg.de/dblplinkapi/api/entitylinker/"  # Replace with the actual API URL

for model in models:
    for embedding in embeddings:
        url = urlbase+model+'/'+embedding
        print(url)
        for item in d:
            data1 = {'question': item['question']}
            data2 = {'question': item['paraphrase']}
            # Convert the data to JSON format
            json_data1 = json.dumps(data1)
            json_data2 = json.dumps(data2)
        
            # Set the headers for the request
            headers = {
                "Content-Type": "application/json"  # Specify that we are sending JSON data
            }
        
            # Make the POST request
            response1 = requests.post(url, data=json_data1, headers=headers)
            response2 = requests.post(url, data=json_data2, headers=headers)
        
            # Check the response status code
            print("======================")
            print(item)
            if response1.status_code == 200:
                print("POST request successful")
                print("Response1 data:", response1.json())
            else:
                print(f"POST request failed with status code {response.status_code}")
                print("Response1 content:", response1.text)
            if response2.status_code == 200:
                print("POST request successful")
                print("Response1 data:", response2.json())
            else:
                print(f"POST request failed with status code {response.status_code}")
                print("Response1 content:", response2.text)
