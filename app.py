from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({"message": "Welcome to LET Innovations API"})

if __name__ == "__main__":
    app.run(debug=True)