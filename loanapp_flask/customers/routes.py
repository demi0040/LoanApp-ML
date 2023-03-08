import pickle
import numpy as np
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from loanapp_flask import db
from loanapp_flask.models import Customer, LoanApplication
from loanapp_flask.customers.forms import CustomerForm, LoanApplicationForm

customers = Blueprint('customers', __name__)

@customers.route("/customer/new", methods=['GET', 'POST'])
@login_required
def new_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        customer = Customer(customer_name=form.customer_name.data, content=form.content.data, author=current_user)
        db.session.add(customer)
        db.session.commit()
        flash('New customer has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_customer.html', title='New Customer',
                           form=form, legend='New Customer')


@customers.route("/customer/<int:customer_id>")
def customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    return render_template('customer.html', customer_name=customer.customer_name, customer=customer)


@customers.route("/customer/<int:customer_id>/update", methods=['GET', 'POST'])
@login_required
def update_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    if customer.author != current_user:
        abort(403)
    form = CustomerForm()
    if form.validate_on_submit():
        customer.customer_name = form.customer_name.data
        customer.content = form.content.data
        db.session.commit()
        flash('Your customer has been updated!', 'success')
        return redirect(url_for('customers.customer', customer_id=customer.id))
    elif request.method == 'GET':
        form.customer_name.data = customer.customer_name
        form.content.data = customer.content
    return render_template('create_customer.html', title='Update Customer',
                           form=form, legend='Update Customer')


@customers.route("/customer/<int:customer_id>/delete", methods=['POST'])
@login_required
def delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    if customer.author != current_user:
        abort(403)
    db.session.delete(customer)
    db.session.commit()
    flash('Your customer has been deleted!', 'success')
    return redirect(url_for('main.home'))

@customers.route("/customer/<int:customer_id>/create_loan_application", methods=['GET', 'POST'])
@login_required
def new_loan_application(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    if customer.author != current_user:
        abort(403)
    form = LoanApplicationForm()
    if form.validate_on_submit():
        loanapp = LoanApplication(
            gender=form.gender.data,
            married=form.married.data,
            dependents=int(form.dependents.data),
            education=form.education.data,
            self_employment=form.self_employment.data,
            applicant_income=form.applicant_income.data,
            coapplicant_income=form.coapplicant_income.data,
            loan_amount=form.loan_amount.data,
            loan_term=form.loan_term.data,
            credit_history=form.credit_history.data,
            prop_area=form.prop_area.data,
            customer=customer
        )
        db.session.add(loanapp)
        db.session.commit()

        # Use the trained model to predict the loan status
        with open('loanapp_flask\mlpredict\model.pkl', 'rb') as file:
            rfc = pickle.load(file)
        gender = int(form.gender.data)
        married = int(form.married.data)
        dependents = int(form.dependents.data)
        education = int(form.education.data)
        self_employment = int(form.self_employment.data)
        applicant_income = float(form.applicant_income.data)
        coapplicant_income = float(form.coapplicant_income.data)
        loan_amount = float(form.loan_amount.data)
        loan_term = float(form.loan_term.data)
        credit_history = float(form.credit_history.data)
        prop_area = int(form.prop_area.data)

        prediction = rfc.predict([[gender, married, dependents, education, self_employment,
                           applicant_income, coapplicant_income, loan_amount,
                           loan_term, credit_history, prop_area]])
        
        # Map the predicted class to a loan status
        loan_status = "Approved" if prediction == 1 else "Rejected"

        customer = Customer.query.get_or_404(customer_id)
        if loan_status == 'Approved':
            customer.res_loan = 1
        else:
            customer.res_loan = 0
        db.session.commit()

        flash(f'New loan application has been created! Loan status: {loan_status}', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_loan_application.html', title='New Loan Application',
                           form=form, legend='New Loan Application')
