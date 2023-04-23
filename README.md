# Welcome to our SC1015 Mini Project on Youtube_Analysis!

## Introduction
Our project uses the official [Youtube Data API](https://developers.google.com/youtube/v3) to form datasets on videos in the past 3 days.

Based on the datasets, we use machine learning models to predict:
1. Whether a video will trend or not
2. What Youtube video category (e.g. Gaming, Sports, Music) a video belongs to based on its title

These problem statements can give us insight into maximising Trending potential of Youtube videos, as well as allow us to explore natural language processing potential using titles and categories of video hosting platforms.

We cover the following topics in the following sections:
- [Members](#members)
- [Dataset Information](#dataset-information)
- [Machine Learning Models Used](#machine-learning-models-used)
- [Explanatory Data Analysis (EDA)](#exploratory-data-analysis)
- [Youtube Category Prediction Process](#youtube-category-prediction-process)
- [Conclusion](#conclusion)
- [References](#references)

## Members
- Chin Jun Hao, Mark
- Tan Kuan Kiat
- Chelson Chong

## Dataset Information

The YT_Dataset_Creation.ipynb file generates a dataset.

![image](https://user-images.githubusercontent.com/93315900/233829093-ed45503b-7200-40f7-94f8-ffc4aa2f97a2.png)

First, we get Youtube to list the videos currently on trending. 

We then obtain the video ID of these trending videos and store them in a trending_id variable.

![image](https://user-images.githubusercontent.com/93315900/233829116-1b93e0ba-767a-4a13-8986-a2cf974c6310.png)

Next, we do a general search for videos.

We do not want to search for videos from too long ago, as trending videos are those that are released more recently. Hence, we set a start_date variable of datetime 72 hours before our program runs.

Then, we do a search of videos published after this start_date variable. 

![image](https://user-images.githubusercontent.com/93315900/233829132-42792188-dea5-473e-b6aa-d9f7d0cf491a.png)

Our searches give us a list of videos. But the information given is quite lacking. We currently only get videoID, channelID, and publishTiming. We would want more factors that could possibly influence if a video trends.

![image](https://user-images.githubusercontent.com/93315900/233829148-66b6220e-1e4d-48c8-a4af-a9ffdf3f2243.png)

To accomplish this, we make an API request for each individual videoID. This gives us more information about each video.

Now, we have access to information like categoryId, video duration, viewcounts, likecounts, and commentcounts.

![image](https://user-images.githubusercontent.com/93315900/233829407-1d9e2a36-76c9-4137-823c-eee624af1a0c.png)

We add all these videoIds to a video_id variable (unless they are in trending_id too as we do not want to double-count).

Giving the videos in trending_id a trending value of 1 and videos in video_id a trending value of 0, we get a compiled dataset below.

![Capture](https://user-images.githubusercontent.com/93315900/233765193-0c01da46-aa47-48bc-ace3-7805e49c91f9.PNG)

- id: A string for the Youtube id of the video.

- publishedAt: A datetime (in UTC) the video was published at.

- channelId: A string for the Youtube id of the publishing channel.

- title: A string for the title of the video.

- description: A string for the description of the video.

- channelTitle: A string for the title of the publishing channel.

- categoryId: A categorial integer denoting what video category a video belongs to (e.g. Gaming, Sports, Music).

- liveBroadcastContent: integer 0 if it is NOT an active/upcoming live broadcast, and 1 if it is.

- duration: A string denoting hour-minute-second duration format of the video, after "PT".

- dimension: A string denoting if a video is in "2d" or "3d".

- definition: A string denoting if a video is in "hd" (high definition) or "sd" (standard definition).

- caption: A boolean denoting if a video has captions.

- viewCount: An integer representing number of views the video has. (contains a string "None" if the video has a paywall, e.g. paid movies)

- likeCount: An integer representing number of likes the video has. (contains a string "None" if the video has likes disabled)

- commentCount: An integer representing number of comments the video has. (contains a string "None" if the video has comments disabled)

- Trending: integer 0 if the video is NOT trending at search time, and 1 if it is.

The YT_Dataset_Creation.py file does the same as the YT_Dataset_Creation.ipynb file, but generates a dataset once every 12 hours.

We then compiled these csv files into one YT_dataset.csv file.

## Machine Learning Models Used
1. Decision Tree
2. Random Forest
    - The Random Forest classifier consists of many individual decision trees that make use of different sets of data and different features to classify them. The model chooses the class most predicted by the trees as its prediction.
3. Naïve Bayes
    - The Naïve Bayes classifier is a supervised machine learning algorithm, which is used for classification tasks, like text classification. It is also part of a family of generative learning algorithms, meaning that it seeks to model the distribution of inputs of a given class or category.

## Exploratory Data Analysis
### Categories Sorted By Video Count / Trending Videos Sorted By Video Count
<img width="567" alt="image" src="https://user-images.githubusercontent.com/79626294/233766870-d210cdf2-7c33-4813-a74b-33360f0de0ed.png">

### Videos Posted Per Hour / Trending Videos Posted Per Hour
<img width="578" alt="image" src="https://user-images.githubusercontent.com/79626294/233766897-1e6c99ea-45df-4ce9-8308-610054974982.png">

### Videos Posted Throughout The Week / Trending Videos Posted Throughout The Week
<img width="579" alt="image" src="https://user-images.githubusercontent.com/79626294/233766906-9e484522-5a30-407a-956e-7cb10f615516.png">

### Decision Tree

## Random Forest

## Youtube Category Prediction Process
In this Youtube Category Prediction Model, we made use of Naïve Bayes Classifier. By inputing in hypothetical video titles, the Prediction Model will produce for us the predicted category to place this vidoes in. There are 3 dataset that we have tested on, firstly a Pre-Dataset which is a smaller dataset which we used to work on while we collect more data from the YouTube API, secondly, the Full-Dataset and lastly the cleaned version of the Full-Dataset.
### Part 1: Getting the data
<img width="765" alt="image" src="https://user-images.githubusercontent.com/79626294/233765603-42228515-1cc1-4f55-a4e3-919f7b43b8d6.png">


### Part 2: Training the model
<img width="764" alt="image" src="https://user-images.githubusercontent.com/79626294/233765584-9b818dde-7704-4020-9959-77c6bc73fa43.png">
The Model was train and tested in a ratio of 80:20 (80 being the training set and 20 being the test set)

### Part 3: Testing phase
<img width="327" alt="image" src="https://user-images.githubusercontent.com/79626294/233765576-1d2ab293-1a5d-4627-b135-8faf300570d0.png">
Here we provide hypothetical video titles, in which the model will then provide us with the predicted category these video titles will be categorised in.

### Additional: Cleaning of Data to increase accuracy
<img width="453" alt="image" src="https://user-images.githubusercontent.com/79626294/233828219-fe81d0ac-a61d-494b-860a-3934e8d7ea79.png">
Some of the process that was done to clean the data included removing unnecessary spaces, cleaning the numbers, correction of the misspelled words, correction of rare words, cleaning bad case words, cleaning the repeat words, cleaning the emojis, unnecessary, punctuations, characters as seen in our preprocess function. These uncleaned data would affect the models efficency even if it is by the slightest margin.

<img width="744" alt="image" src="https://user-images.githubusercontent.com/79626294/233765549-568e37b0-ba70-499e-9986-1cf934afbfb1.png">
As seen in the chart above, there are 140k texts after cleaning the data in comparison to what it was which was at 167k texts.

## Conclusion
Our project has answered both of our problem statements. However, perhaps we need larger datasets for greater accuracy.

Especially for the video category predictor model, our datasets may still be too small to make accurate classifications due to the huge number of video categories.

One possible extension is to examine data across other regions. We only observed Youtube data in the US region for this dataset. Maybe regions like Singapore and Europe will provide different results.

A second possible extension is to examine the data across more days. Maybe on days like public holidays, the data may differ.


## References
1. https://www.ibm.com/topics/naive-bayes#:~:text=The%20Na%C3%AFve%20Bayes%20classifier%20is,a%20given%20class%20or%20category
2. https://towardsdatascience.com/understanding-random-forest-58381e0602d2
3. https://developers.google.com/youtube/v3
