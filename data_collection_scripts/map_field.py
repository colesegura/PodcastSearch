# import requests
# import json

# # Replace with your service name
# service_name = "cwseguracogsearch"

# # Replace with your admin key
# api_key = "jtysr61P8EyVTaJmhQj7ldQMCZbYuzweDDtdqoDEHGAzSeDnKFd2"

# # The name of your data source and index
# data_source_name = "blobstoragesource"
# index_name = "podcast-index"

# # The API version
# api_version = "2020-06-30"

# # The URL of the Create Indexer API
# url = f"https://{service_name}.search.windows.net/indexers?api-version={api_version}"

# # The headers of the HTTP request
# headers = {
#     "Content-Type": "application/json",
#     "api-key": api_key
# }

# # The body of the HTTP request
# body = {
#     "name": "main-indexer",
#     "dataSourceName": data_source_name,
#     "targetIndexName": index_name,
#     "fieldMappings": [
#         {
#             "sourceFieldName": "id",
#             "targetFieldName": "id",
#             "mappingFunction": { "name": "base64Encode" }
#         },
#         { "sourceFieldName": "podcast_id", "targetFieldName": "podcast_id" },
#         { "sourceFieldName": "episode_id", "targetFieldName": "episode_id" },
#         { "sourceFieldName": "transcript", "targetFieldName": "transcript" },
#         { "sourceFieldName": "title", "targetFieldName": "title" },
#         { "sourceFieldName": "date", "targetFieldName": "date" }
#     ]
# }

# # Send the HTTP request
# response = requests.post(url, headers=headers, json=body)

# # Print the response
# print(json.dumps(response.json(), indent=4))

import requests
import json

# Replace with your service name
service_name = "cwseguracogsearch"

# Replace with your admin key
api_key = "jtysr61P8EyVTaJmhQj7ldQMCZbYuzweDDtdqoDEHGAzSeDnKFd2"

# The name of your data source and index
data_source_name = "blobstoragesource"
index_name = "podcast-index"

# The API version
api_version = "2020-06-30"

# The URL of the Create Indexer API
url = f"https://{service_name}.search.windows.net/indexers?api-version={api_version}"

# The headers of the HTTP request
headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}

# The body of the HTTP request
body = {
    "name": "main-indexer",
    "dataSourceName": data_source_name,
    "targetIndexName": index_name,
    "parameters": {
        "configuration": {
            "parsingMode": "delimitedText",
            "delimitedTextDelimiter": "^",
            "firstLineContainsHeaders": True
        }
    },
    "fieldMappings": [
        {
            "sourceFieldName": "id",
            "targetFieldName": "id",
            "mappingFunction": { "name": "base64Encode" }
        },
        { "sourceFieldName": "podcast_id", "targetFieldName": "podcast_id" },
        { "sourceFieldName": "episode_id", "targetFieldName": "episode_id" },
        { "sourceFieldName": "transcript", "targetFieldName": "transcript" },
        { "sourceFieldName": "title", "targetFieldName": "title" },
        { "sourceFieldName": "date", "targetFieldName": "date" }
    ]
}

# Send the HTTP request
response = requests.post(url, headers=headers, json=body)

# Print the response
print(json.dumps(response.json(), indent=4))
