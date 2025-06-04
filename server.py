from flask import Flask, request, jsonify
import random
import os

app = Flask(__name__)

@app.route('/get_action', methods=['POST'])
def get_action():
    data = request.json
    # فرض بر اینکه data شامل اطلاعاتی مثل موقعیت بازیکن و توپ باشه
    # برای ساده‌سازی، فقط یک جهت تصادفی انتخاب می‌کنیم
    directions = ['up', 'down', 'left', 'right', 'up-left', 'up-right', 'down-left', 'down-right']
    action = random.choice(directions)
    return jsonify({'action': action})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # برای Render یا دیگر سرورها
    app.run(host="0.0.0.0", port=port)
