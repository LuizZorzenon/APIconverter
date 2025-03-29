from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    amount = 1
    url = f"https://v6.exchangerate-api.com/v6/a3268554cb8e2af283d8f776/pair/USD/BRL/{amount}"
    r = requests.get(url)

    data = r.json()
    conversion_result = data.get("conversion_result")
    result = float(conversion_result)

    real = round(result, 2)

    return render_template("index.html", result=real)

@app.route("/moeda/")
def convert_coin():
    amount = request.args.get('amount', 1)
    url = f"https://v6.exchangerate-api.com/v6/a3268554cb8e2af283d8f776/pair/USD/BRL/{amount}"
    r = requests.get(url)

    data = r.json()
    conversion_result = data.get("conversion_result")
    result = float(conversion_result)

    real = round(result,2)
    
    return str(f"R$ {real}")

if __name__ == '__main__':
    app.run(debug=True)