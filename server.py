from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/get_move', methods=['POST'])
def get_move():
    data = request.get_json()
    x1 = data.get('x1')  # بازیکن ۱
    y1 = data.get('y1')
    x2 = data.get('x2')  # بازیکن ۲ (خود AI)
    y2 = data.get('y2')
    ball_x = data.get('ball_x')
    ball_y = data.get('ball_y')

    # اینجا من فقط یک حرکت تصادفی برمی‌گردونم (۰ تا ۷)
    # بهتره هوش مصنوعی خودت رو جایگزین کنی
    move = random.randint(0,7)

    return jsonify({'move': move})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
