from flask import Flask, render_template, request, redirect
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

products = []

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/farmer', methods=['GET', 'POST'])
def farmer():
    if request.method == 'POST':
        name = request.form['name']
        crop = request.form['crop']
        price = request.form['price']

        data = {
            "farmer": name,
            "crop": crop,
            "price": price
        }

        blockchain.add_block(data)
        products.append(data)

        return redirect('/consumer')

    return render_template('farmer.html')


@app.route('/consumer')
def consumer():
    return render_template('consumer.html', products=products)


@app.route('/product/<int:index>')
def product(index):
    return render_template('product.html', chain=blockchain.chain)


if __name__ == '__main__':
    app.run(debug=True)