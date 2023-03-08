from flask import Blueprint, render_template, request
from loanapp_flask.models import Customer

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    customers = Customer.query.order_by(Customer.date_created.desc()).paginate(page=page, per_page=8)
    return render_template('home.html', customers=customers)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
