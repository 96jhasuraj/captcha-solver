from flask import Flask, request, jsonify
from PIL import Image
import pytesseract

app = Flask(__name__)

@app.route("/solve", methods=["POST"])
def solve():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    image = Image.open(file.stream)
    text = pytesseract.image_to_string(image)
    return jsonify({"text": text.strip()})

@app.route("/")
def index():
    return {"status": "ok", "message": "CAPTCHA solver API. Use /solve"}, 200
