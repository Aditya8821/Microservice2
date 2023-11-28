from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Use environment variables or default values
API1_URL = os.environ.get('API1_URL', 'http://localhost:5000')
PORT = int(os.environ.get('PORT', 5001))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculateprice', methods=['POST'])
def calculate_price():
    product_id = request.form['product_id']
    quantity = int(request.form['quantity'])

    # Make a request to the first API to get product details
    api1_url = f'{API1_URL}/getprice/{product_id}'
    response = requests.get(api1_url)

    if response.status_code == 200:
        price = response.json().get('price')
        total_price = price * quantity
        return render_template('result.html', total_price=total_price)
    else:
        return render_template('result.html', error="Failed to fetch product details from API1")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)


# from flask import Flask, render_template, request, jsonify
# import requests

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/calculateprice', methods=['POST'])
# def calculate_price():
#     product_id = request.form['product_id']
#     quantity = int(request.form['quantity'])

#     # Make a request to the first API to get product details
#     api1_url = 'http://localhost:5000/getprice/' + product_id  # Replace with the actual IP or domain
#     response = requests.get(api1_url)

#     if response.status_code == 200:
#         price = response.json().get('price')
#         total_price = price * quantity
#         return render_template('result.html',total_price=total_price)
#     else:
#         return render_template('result.html', error="Failed to fetch product details from API1")

# if __name__ == '__main__':
#     app.run(debug=True, port=5001)
