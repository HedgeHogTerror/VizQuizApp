from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class TestCreateForm(Form):
    title = StringField('', validators=[DataRequired()])
    description = StringField('', validators=[DataRequired()])
    
class QuestionCreateForm(Form):
    question = StringField('', validators=[DataRequired()])
    answerone = StringField('', validators=[DataRequired()])
    answertwo = StringField('', validators=[DataRequired()])
    answerthree = StringField('', validators=[DataRequired()])
    answerfour = StringField('', validators=[DataRequired()])

class TestTakeForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


