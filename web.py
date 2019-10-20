from flask import Flask, request, render_template
from app import eb_api_query
import json

app = Flask(__name__)


@app.route('/form-example', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST':
        return;

    # uncomment the line below after finishing the form-example demo    
    # return render_template('index.html')


if __name__ == '__main__':
    app.run()
