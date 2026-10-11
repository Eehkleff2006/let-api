from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({"message": "Welcome to LET Innovations API"})

# --- new code goes here ---
device = {"name": "ESP32-01", "status": "offline", "location": "Lab"}

@app.get("/device")
def get_device():
    return jsonify(device)

@app.patch("/device")
def update_device():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Send JSON data"}), 400
    for key, value in data.items():
        if key in device:
            device[key] = value
    return jsonify(device)
# --- end of new code ---

if __name__ == "__main__":
    app.run(debug=True)