# My Solution to Paisasmart's Assignment

# Sentence Classification

- For the bookstore I found that there is a need for training dataset to classify user messages into desired categories. I used ChatGPT to generate synthetic data for classification. I have personally gone through each and every data point and validated its authenticity.

- I have implemented a pipeline from `sklearn` where I used `TF-IDF` to vectorize the messages and used `Naive Bayes Algorithm` and `Support Vector Machine` to train the models.

- I have compared the accuracy scores on both the models and I found `Linear SVC` to be a better fit for classification. I achieved `95%` accuracy using SVC. Whereas with Naive Bayes, the accuracy score was `85% to 90%`.


- I have also trained a model for categorizing users query on `Store Policy` that is `Refund`, `Return`, and `Shipping`. For this model, I have also used `Linear SVC`.

-----------

# Data Extraction

* ## Book Search
    - I have used `difflib` to find the closest book match with the user query. I have used the given `books.json` to search for books.
    - I have also implement `regex` for date based book search.

* ## Order Status
    - Used `regex` to identify the order id from the classified used message.

* ## Review Submission
    - Used `spacy` to get a dictionary of english words and use them to identify reviews in user sentence. This is a `rule-based` approach, hence sometimes it returns review with the name of the book.

* ## Store Policy
    - Trained a model to classify users query related to certain policies. Generated synthetic data using ChatGPT to generate a dataset for training the model.