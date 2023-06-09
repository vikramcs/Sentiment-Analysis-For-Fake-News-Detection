# Sentiment-Analysis-For-Fake-News-Detection

**Description:**
This repository contains a Python application that performs sentiment analysis for fake news detection. The application uses natural language processing techniques to analyze the sentiment of textual content and determine the likelihood of it being fake or misleading.

**Features:**
Sentiment Analysis: The application utilizes a pre-trained sentiment analysis model to determine the sentiment of news articles or textual content.

**Fake News Detection:** Based on the sentiment analysis results, the application applies a classification algorithm to identify whether the given content is likely to be fake or genuine.

**User Interface:** The application provides a user-friendly interface for users to input text and receive the analysis results.

**Data Visualization:** The application generates visualizations such as sentiment distribution and classification results to aid in understanding the analysis.

The LIAR extension is enhanced and expanded even more in our Sentimental LIAR dataset. In our dataset, half-true, false, barely-true, and pants-fire labels are changed to False, while the remaining labels are changed to True, converting the multi-class labeling of LIAR to a binary annotation. Furthermore, in order to remove bias associated with the textual representation of names, we turn the speaker names into numerical IDs. The sentiments obtained by utilizing the Google NLP API are then included, expanding the binary-label dataset. 
Using a numerical score, sentiment analysis evaluates the text's general attitude (i.e., whether it is positive or negative). Positive is applied to the sentiment attribute if the sentiment score is positive; otherwise, Negative is given. We also added a further enhancement by include emotion ratings for each claim that were retrieved using the IBM NLP API. These scores indicate the degree to which anger, sorrow, contempt, fear, and pleasure were recognized. Each emotion has a score that falls between 0 and 1.




