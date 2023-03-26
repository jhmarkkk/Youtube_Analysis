#!/usr/bin/env python
# coding: utf-8

# In[1]:


import constants

API_KEY = constants.API_KEY

from googleapiclient.discovery import build

import time

# In[2]:


while True:

    import datetime

    current_datetime = datetime.datetime.now()
    print(current_datetime.time())

    #We run this before 12am SGT each day
        
    dataset_name = 'yt_dataset_{}.csv'.format(str(current_datetime.date()))
    print(dataset_name)


    # In[3]:


    youtube = build('youtube', 'v3', developerKey=API_KEY) #this is a Service


    # # Video Id of Trending videos
    # We will create an array trending_id containing the video Ids of trending videos.

    # In[4]:


    request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            chart="mostPopular",
            regionCode="US",
            maxResults=50
        )

    trending = request.execute()
    print(trending)


    # In[5]:


    trending_id = []

    for video in trending["items"]:
        trending_id.append(video["id"])
        
    trending_id = list(set(trending_id))
    print(trending_id)
    print(len(trending_id))


    # # Gathering info on videos in past 72 hours

    # In[6]:


    #This is in UTC

    start_date = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=3)
    start_date = start_date.isoformat()

    #This ensures our search is limited to past 72 hours


    # In[7]:


    request = youtube.search().list(
            part="snippet",
            maxResults=50,
            regionCode="US",
            relevanceLanguage="en",
            safeSearch="moderate",
            type="video",
            publishedAfter=start_date
        ) #request for a service

    search_result = request.execute() #execute the request


    # In[8]:


    print(search_result)


    # In[9]:


    print(search_result["items"][0])


    # In[10]:


    video_id = []


    # In[11]:


    for video in search_result["items"]:
        video_id.append(video["id"]["videoId"])


    # In[12]:


    if "nextPageToken" in search_result:
        next_page = search_result["nextPageToken"]
        
    else:
        next_page = None


    # In[13]:


    count = 1 #just so we don't overload the API call quota

    while next_page and count < 10: #we will let it run for maximum 20 cycles
        request = youtube.search().list(
            part="snippet",
            pageToken=next_page,
            maxResults=50,
            regionCode="US",
            relevanceLanguage="en",
            safeSearch="moderate",
            type="video",
            publishedAfter=start_date
        ) #request for a service

        search_result = request.execute() #execute the request
        
        for video in search_result["items"]:
            video_id.append(video["id"]["videoId"])
            
        if "nextPageToken" in search_result:
            next_page = search_result["nextPageToken"]
        
        else:
            next_page = None
        
        count += 1


    # In[14]:


    video_id = list(set(video_id))
    print(video_id, len(video_id))


    # In[15]:


    #to get more info on each video, we make a request of each videoId
    current_videoId = video_id[0]

    request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=current_videoId
        )

    video_info = request.execute()


    # In[16]:


    print(video_info)


    # In[17]:


    import csv
        
    header = ['id', 'publishedAt', 'channelId', 'title', 'description', 'channelTitle', 'categoryId', 'duration', 'dimension',           'definition', 'caption', 'viewCount', 'likeCount', 'commentCount', 'Trending']

    #There is no trending tag from the API

    with open(dataset_name, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        
        writer.writerow(header)
        
        #For each videoId, we add its details to the csv file
        
        for current_videoId in video_id:
            
            #Get info of video with matching Id
            request = youtube.videos().list(
                part="snippet,contentDetails,statistics",
                id=current_videoId
            )

            video_info = request.execute()
        
            vi_items = video_info["items"][0]
            snippet = vi_items["snippet"]
            contentDetails = vi_items["contentDetails"]
            statistics = vi_items["statistics"]


            if "viewCount" not in statistics:
                statistics["viewCount"] = "None"

            if "likeCount" not in statistics:
                statistics["likeCount"] = "None"
                
            if "commentCount" not in statistics:
                statistics["commentCount"] = "None"
                

            data = [current_videoId, snippet["publishedAt"], snippet["channelId"], snippet["title"], snippet["description"],                snippet["channelTitle"], snippet["categoryId"], contentDetails["duration"], contentDetails["dimension"],                contentDetails["definition"], contentDetails["caption"], statistics["viewCount"], statistics["likeCount"],                statistics["commentCount"]]


            #We need to manually check if a video is trending

            if current_videoId in trending_id:
                data.append(1)
                trending_id.remove(current_videoId)

            else:
                data.append(0)

            writer.writerow(data)
            
        #Add the rest of the trending videos to the csv
        for current_videoId in trending_id:
            
            request = youtube.videos().list(
                part="snippet,contentDetails,statistics",
                id=current_videoId
            )

            video_info = request.execute()
        
            vi_items = video_info["items"][0]
            snippet = vi_items["snippet"]
            contentDetails = vi_items["contentDetails"]
            statistics = vi_items["statistics"]


            if "viewCount" not in statistics:
                statistics["viewCount"] = "None"

            if "likeCount" not in statistics:
                statistics["likeCount"] = "None"
                
            if "commentCount" not in statistics:
                statistics["commentCount"] = "None"

            data = [current_videoId, snippet["publishedAt"], snippet["channelId"], snippet["title"], snippet["description"],                snippet["channelTitle"], snippet["categoryId"], contentDetails["duration"], contentDetails["dimension"],                contentDetails["definition"], contentDetails["caption"], statistics["viewCount"], statistics["likeCount"],                statistics["commentCount"]]
            
            data.append(1)

            writer.writerow(data)
        
        


    # In[ ]:

    time.sleep(60 * 60 * 24)



    # In[ ]:




