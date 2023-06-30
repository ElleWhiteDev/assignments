from flask import Flask, render_template, request, redirect, flash
import requests
from forex_python.converter import CurrencyCodes
from validation import validate_currency_code, is_valid_amount


app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def currency_form():
    return render_template("index.html")

@app.route('/convert', methods=['POST'])
def converted_currency():

    convert_from = request.form["convert-from"].upper().strip()
    convert_to = request.form["convert-to"].upper().strip()
    amount = request.form["amount"]

    if not is_valid_amount(amount):
        flash("Invalid amount: please enter positive a number")
        return redirect("/")
    
    amount = float(amount)
    amount = round(amount, 2)

    if not validate_currency_code(convert_from):
        flash("Invalid base currency code")
        return redirect("/")
    if not validate_currency_code(convert_to):
        flash("Invalid converted currency code")
        return redirect("/")

    url = f"https://api.exchangerate.host/convert?from={convert_from}&to={convert_to}&amount={amount}&places=2"
    response = requests.get(url)
    data = response.json()
    converted_amount = data["result"]
    convert_from_symbol = CurrencyCodes().get_symbol(convert_from)
    convert_to_symbol = CurrencyCodes().get_symbol(convert_to)

    return render_template("converted_result.html", convert_from_symbol=convert_from_symbol, convert_to_symbol=convert_to_symbol,
    amount=amount, 
    convert_from=convert_from, 
    convert_to=convert_to, 
    converted_amount=converted_amount)
