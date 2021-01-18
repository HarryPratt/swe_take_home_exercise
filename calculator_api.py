from flask import Flask, render_template, request
from calculator import get_result

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def welcome():
    # Initiated calculator page
    return render_template('index.html', entered=None, result=None, calc=None)


@app.route('/result_json', methods=['POST'])
def result_json():
    # If we want to do a post request and receive the result in json format
    inp = request.form.get("inp", type=str)
    response = get_result(inp)
    return response


@app.route('/result', methods=['POST'])
def result():
    # Update the index page with the output
    inp = request.form.get("inp", type=str)
    response = get_result(inp)
    return render_template('index.html', entered=inp, result=response["result"], calc=response["calc"])


app.run()