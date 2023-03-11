from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, RadioField, FloatField
from wtforms.validators import DataRequired

class CustomerForm(FlaskForm):
    customer_name = StringField('Customer Name', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Create')

class LoanApplicationForm(FlaskForm):
    gender = RadioField('Gender', choices=[(0, 'Male'), (1, 'Female')], coerce=bool)
    married = RadioField('Married', choices=[(0, 'No'), (1, 'Yes')], coerce=bool)
    dependents = RadioField('Dependents', choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3+')])
    education = RadioField('Education', choices=[(0, 'Not Graduate'), (1, 'Graduate')], coerce=bool)
    self_employment = RadioField('Self Employment', choices=[(0, 'No'), (1, 'Yes')], coerce=bool)
    applicant_income = IntegerField('Applicant Income', validators=[DataRequired()])
    coapplicant_income = IntegerField('Co-Applicant Income', validators=[DataRequired()])
    loan_amount = IntegerField('Loan Amount', validators=[DataRequired()])
    loan_term = IntegerField('Loan Term', validators=[DataRequired()])
    credit_history = RadioField('Credit History', choices=[(0, '0'), (1, '1')], coerce=bool)
    prop_area = RadioField('Property Area', choices=[(0, 'Rural'), (1, 'Semiurban'), (2, 'Urban')])
    submit = SubmitField('Create')

class InsurancePremiumForm(FlaskForm):
    gender = RadioField('Gender', choices=[(0, 'Male'), (1, 'Female')], validators=[DataRequired()], coerce=bool)
    smoker = RadioField('Married', choices=[(0, 'No'), (1, 'Yes')], validators=[DataRequired()], coerce=bool)
    age = IntegerField('Age', validators=[DataRequired()])
    children = IntegerField('Age', validators=[DataRequired()])
    bmi = FloatField('BMI', validators=[DataRequired()])
    submit = SubmitField('Create')
