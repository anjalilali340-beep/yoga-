from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    pose = request.form.get("pose")

    # simple logic (prototype)
    if pose.lower() == "tree":
        result = "Correct Pose ✅"
    else:
        result = "Try Again ❌"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run()