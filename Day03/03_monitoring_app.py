from flask import Flask, render_template, jsonify # type: ignore
import psutil # type: ignore

app = Flask(__name__)

# Initialize CPU percent calculation
psutil.cpu_percent(interval=None)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/usage")
def get_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    ram_percent = psutil.virtual_memory().percent
    return jsonify(cpu_percent=cpu_percent, ram_percent=ram_percent)

if __name__ == '__main__':
    app.run(debug=True)