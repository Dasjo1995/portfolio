from flask import Flask, render_template, redirect, url_for, flash, abort, request
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
import stripe



app = Flask(__name__)
app.config['SECRET_KEY'] = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf' # used for securely signing the session cookie
ckeditor = CKEditor(app)
Bootstrap(app)


app.config['STRIPE_PUBLIC_KEY'] = 'pk_test_51NJIASHrBw1AU6YAuFmtwvw01qCqFuSf1FTpZohfhfHF9RIxJ2DtUEw8WmgIa0YlbOyxDcmYdEPkiXcfHAKA6zcu00syJpaKM5'
app.config['STRIPE_SECRET_KEY'] = 'sk_test_51NJIASHrBw1AU6YAqjan5ZYDOKM3xGIZ51opLUEXaByfcU3uLP8Uo0653FKPshOlhhrPTfwRdbte4h8tvk5NX6KA00a7Xsp33Z'



@app.route('/')
def home():
    return render_template('index.html', public_key=app.config['STRIPE_PUBLIC_KEY'])

@app.route('/payment', methods=['GET', 'POST'])
def payment():

    stripe.api_key = app.config['STRIPE_SECRET_KEY']

    customer = stripe.Customer.create(
        email=request.form['stripeEmail'],
        source=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=200,
        currency='usd',
        description='Price'
    )

    return redirect(url_for('thankyou'))

@app.route('/thankyou')
def thankyou():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)