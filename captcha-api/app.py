from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import pytesseract

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

@app.route("/solve", methods=["POST"])
def solve():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    image = Image.open(file.stream)
    text = pytesseract.image_to_string(image)
    return jsonify({"text": text.strip()})

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/")
def index():
    return {"status": "ok", "message": "CAPTCHA solver API. Use /solve"}, 200
