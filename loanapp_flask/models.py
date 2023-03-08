from datetime import datetime
from itsdangerous import Serializer
from flask import current_app
from loanapp_flask import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    customers = db.relationship('Customer', backref='author', lazy=True)

    def get_reset_token(self):
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.id})


    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    res_ins = db.Column(db.Integer, default=2)
    res_mor = db.Column(db.Integer, default=2)
    res_loan = db.Column(db.Integer, default=2)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    applications = db.relationship('LoanApplication', backref='customer', lazy=True)

    def __repr__(self):
        return f"Customer('{self.customer_name}', '{self.date_created}')"

class LoanApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    gender = db.Column(db.Boolean, default=0)
    married = db.Column(db.Boolean, default=0)
    dependents = db.Column(db.Integer, default=0)
    education = db.Column(db.Boolean, default=0)
    self_employment = db.Column(db.Boolean, default=0)
    applicant_income = db.Column(db.Integer, default=0)
    coapplicant_income = db.Column(db.Integer, default=0)
    loan_amount = db.Column(db.Integer, default=0)
    loan_term = db.Column(db.Integer, default=0)
    credit_history = db.Column(db.Boolean, default=0)
    prop_area = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"LoanApplication('{self.gender}', '{self.married}', '{self.dependents}', '{self.education}', '{self.self_employment}', '{self.applicant_income}', '{self.coapplicant_income}'), '{self.loan_amount}', '{self.loan_term}', '{self.credit_history}', '{self.prop_area}'"