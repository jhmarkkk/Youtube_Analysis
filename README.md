# Welcome to our SC1015 Mini Project on Youtube_Analysis!

## About
Our project uses the official [Youtube Data API](https://developers.google.com/youtube/v3) to form datasets on videos in the past 3 days.

Based on the datasets, we use machine learning models to predict:
1. Whether a video will trend or not
2. What Youtube video category (e.g. Gaming, Sports, Music) a video belongs to based on its title

## Members (Team 6)
- Chin Jun Hao, Mark
- Tan Kuan Kiat
- Chelson Chong

## Dataset Information
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

### Gini Tree

## Random Forest

## Youtube Category Prediction Process
In this Youtube Category Prediction Model, we made use of Naïve Bayes Classifier. By inputing in hypothetical video titles, the Prediction Model will produce for us the predicted category to place this vidoes in. There are 3 dataset that we have tested on, firstly a Pre-Dataset which is a smaller dataset which we used to work on while we collect more data from the YouTube API, secondly, the Full-Dataset and lastly the cleaned version of the Full-Dataset.
### Part 1: Getting the data
<img width="765" alt="image" src="https://user-images.githubusercontent.com/79626294/233765603-42228515-1cc1-4f55-a4e3-919f7b43b8d6.png">


### Part 2: Training the model
<img width="764" alt="image" src="https://user-images.githubusercontent.com/79626294/233765584-9b818dde-7704-4020-9959-77c6bc73fa43.png">


### Part 3: Testing phase
<img width="327" alt="image" src="https://user-images.githubusercontent.com/79626294/233765576-1d2ab293-1a5d-4627-b135-8faf300570d0.png">


### Additional: Cleaning of Data to increase accuracy
<img width="744" alt="image" src="https://user-images.githubusercontent.com/79626294/233765549-568e37b0-ba70-499e-9986-1cf934afbfb1.png">


## References
1. https://www.ibm.com/topics/naive-bayes#:~:text=The%20Na%C3%AFve%20Bayes%20classifier%20is,a%20given%20class%20or%20category
2. https://towardsdatascience.com/understanding-random-forest-58381e0602d2
3. 
