from flask import Flask, request, jsonify
import math

app = Flask(__name__)

@app.route("/ai-move", methods=["POST"])
def ai_move():
    data = request.get_json()

    x = data["x"]   # موقعیت توپ
    y = data["y"]
    x2 = data["x2"] # موقعیت مهره بازیکن دوم (AI)
    y2 = data["y2"]

    dx = x - x2
    dy = y - y2

    if dx == 0 and dy == 0:
        jahat = None
    else:
        angle = math.degrees(math.atan2(dy, dx))
        if angle < 0:
            angle += 360

        if 22.5 <= angle < 67.5:
            jahat = 7  # راست بالا
        elif 67.5 <= angle < 112.5:
            jahat = 1  # بالا
        elif 112.5 <= angle < 157.5:
            jahat = 6  # چپ بالا
        elif 157.5 <= angle < 202.5:
            jahat = 0  # چپ
        elif 202.5 <= angle < 247.5:
            jahat = 5  # چپ پایین
        elif 247.5 <= angle < 292.5:
            jahat = 3  # پایین
        elif 292.5 <= angle < 337.5:
            jahat = 4  # راست پایین
        else:  # 337.5 <= angle < 22.5
            jahat = 2  # راست

    return jsonify({"jahat": jahat})

if __name__ == "__main__":
    app.run(debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
