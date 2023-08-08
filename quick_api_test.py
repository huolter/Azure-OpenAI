import json
import openai

# start by getting some keys
def read_keys_from_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        endpoint_name = data.get('ENDPOINT_NAME')
        key = data.get('KEY')
        deployment_name = data.get('DEPLOYMENT_NAME')
        print (endpoint_name, key, deployment_name)
        return endpoint_name, key, deployment_name

file_path = 'keys.json'
endpoint_name, key, deployment_name = read_keys_from_json(file_path)

openai.api_key = key
openai.api_base =  endpoint_name 
openai.api_type = 'azure' # Necessary for using the OpenAI library with Azure OpenAI

# https://learn.microsoft.com/en-US/azure/ai-services/openai/reference
openai.api_version = '2023-05-15' # Latest / target version of the API

deployment_name = deployment_name # SDK calls this "engine", but naming
                                           # it "deployment_name" for clarity



# test the completion
prompt = 'One, two, three, hey hey... '
response = openai.Completion.create(engine=deployment_name, prompt=prompt)
print ("prompt:", prompt)
print("completion:" ,response.choices[0].text)

# test the ChatCompletion

messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Azure OpenAI? Reply with 50 words or less"}
    ]

response = openai.ChatCompletion.create(
    engine=deployment_name,
    messages=messages
)
print ("--")
print ("[user]", messages[1]["content"])
print("[response]",response['choices'][0]['message']['content'])

