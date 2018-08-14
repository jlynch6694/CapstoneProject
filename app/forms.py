from flask_wtf import FlaskForm #flask form class all forms will inherit this
from wtforms import IntegerField, SelectField, SubmitField, validators #importing different types of fields to allow us to easily create input fields


class currencyForm (FlaskForm):
    language = SelectField('Currency', choices=[ ('US Dollar', 'US Dollar'), ( 'Chinese Yuan', 'Chinese Yuan'), ('Canadian Dollar', 'Canadian Dollar'), ( 'Mexican Peso', 'Mexican Peso'), ('Japanese Yen', 'Japanese Yen'), ('Euro', 'Euro'), ('South Korean Won', 'South Korean Won'), ('British Pound', 'British Pound'), ('Indian Rupee', 'Indian Rupee'), ('New Taiwan Dollar', 'New Taiwan Dollar')])
    submit = SubmitField('Submit')

class InputGDP (FlaskForm):
    num1 = IntegerField('Market Capitalization', [validators.DataRequired()])
    num2 = IntegerField('Debt', [validators.DataRequired()])
    num3 = IntegerField('Preferred Shares', [validators.DataRequired()])
    num4 = IntegerField('Cash/Cash Expenditures', [validators.DataRequired()])
    num5 = IntegerField('Annual Sales', [validators.DataRequired()])
    submit2 = SubmitField('Submit')
