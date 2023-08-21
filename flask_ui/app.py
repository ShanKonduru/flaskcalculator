from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

# Your other routes and view functions can be added here, if needed

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, debug=True)
