from flask import Flask, render_template
from log_parser import parse_auth_log

app = Flask(__name__)

@app.route("/")
def index():
    log_path = "sample_logs/auth.log"
    df = parse_auth_log(log_path)
    failed = df[df["Status"] == "Failed"]
    suspicious = failed["IP"].value_counts()
    return render_template("index.html", tables=[df.to_html(classes='data')], suspicious=suspicious)

if __name__ == "__main__":
    app.run(debug=True)
