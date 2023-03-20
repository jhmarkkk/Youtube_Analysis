import constants

API_KEY = constants.API_KEY

from googleapiclient.discovery import build

search_result = []
trending_result = []

youtube = build('youtube', 'v3', developerKey=API_KEY) #this is a Service

request = youtube.search().list(
        part="snippet",
        maxResults=10,
        regionCode="SG",
        relevanceLanguage="en",
        safeSearch="moderate",
        type="video"
    ) #request for a service

search_result = request.execute() #execute the request

print(search_result)

youtube.close()