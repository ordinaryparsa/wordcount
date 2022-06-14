from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home/home.html")

@app.route("/result", methods=["POST"])
def result():
    words = request.form.get("text").split()
    wordCounter = dict()
    for word in words:
        if word in wordCounter:
            wordCounter[word] += 1
        else:
            wordCounter[word] = 1
    wordNumber = len(wordCounter.keys())
    return render_template("result/result.html", wordNumber=wordNumber, wordCounter=wordCounter, words=list(set(words)))

    



if __name__ == "__main__":
    app.run(debug=True)