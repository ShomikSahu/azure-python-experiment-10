from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Azure Experiment 10</title>
        </head>
        <body>
            <h1>Cloud Computing Lab</h1>
            <h2>Experiment No. 10</h2>
            <p>Simple Python Web Application Deployed on Microsoft Azure</p>
            <h3>Deployment Successful!</h3>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)