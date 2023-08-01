import pickle
from flask import Flask, render_template, request
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd

app = Flask(__name__, template_folder="./templates", static_folder="./static")

# Data Loading + Pre-processing
df = pd.read_csv("./Dungent_Hunter_preprocessing.csv")

texts = df['full_text'].astype(str)
labels = df['label']
label_encoder = LabelEncoder()
labels = label_encoder.fit_transform(labels)

train_texts, test_texts, train_labels, test_labels = train_test_split(texts, labels, test_size=0.3, random_state=42)

tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(train_texts)

train_sequences = tokenizer.texts_to_sequences(train_texts)
max_sequence_length = max(len(seq) for seq in train_sequences)

model = load_model("test_model.h5")

# Predicting Function
def sentiment_analysis(news: str):

    THRESHOLD = 0.5

    print("Statement---->", news)
    news_to_list = [news]
    print("News to List ->>>",news_to_list)

    text = tokenizer.texts_to_sequences(news_to_list)
    final_text = pad_sequences(text, maxlen=max_sequence_length)
    prediction = model.predict(final_text) 

    result = (prediction> THRESHOLD).astype(int) 

    print(f"Final Prediction: {result[0][0]}")

    return result


@app.route("/")
def home():
   return render_template("index.html")

@app.route("/prediction", methods=["POST"])
def prediction():

    if request.method == "POST":
        # Get the news
        news = request.form["news"]
        print("Statement -> ",news)

        # Predicting result
        result = sentiment_analysis(news)

        if result == 1:
            result = "The news is True"
        else:
            result = "The news is False"

        return render_template("index.html", prediction_text="{}".format(result))


if __name__ == "__main__":
    app.run(debug=True)