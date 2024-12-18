import tkinter as tk
from tkinter import messagebox
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
import io


def analyze_sentiment():
    text = text_entry.get("1.0", tk.END)  # Get the text from the text box
    if not text.strip():
        messagebox.showwarning("Input Error", "Please enter some text.")
        return

    blob = TextBlob(text)
    sentiment = blob.sentiment

    if sentiment.polarity > 0:
        result = "Positive"
    elif sentiment.polarity < 0:
        result = "Negative"
    else:
        result = "Neutral"


    result_label.config(text=f"Sentiment: {result} (Polarity: {sentiment.polarity:.2f})")


    generate_wordcloud(text)



def generate_wordcloud(text):
    wordcloud = WordCloud(width=400, height=300, background_color='white').generate(text)


    image = wordcloud.to_image()


    img_data = io.BytesIO()
    image.save(img_data, format="PNG")
    img_data.seek(0)
    img = ImageTk.PhotoImage(Image.open(img_data))


    wordcloud_label.config(image=img)
    wordcloud_label.image = img  # Keep a reference



root = tk.Tk()
root.title("Sentiment Analysis and Word Cloud App")


text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=10)


analyze_button = tk.Button(root, text="Analyze Sentiment", command=analyze_sentiment)
analyze_button.pack(pady=10)


result_label = tk.Label(root, text="Sentiment: ")
result_label.pack(pady=10)


wordcloud_label = tk.Label(root)
wordcloud_label.pack(pady=10)


root.mainloop()
