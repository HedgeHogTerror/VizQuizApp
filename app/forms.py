from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class TestCreateForm(Form):
    title = StringField('title', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    
class QuestionCreateForm(Form):
    question = StringField('question', validators=[DataRequired()])
    answerone = StringField('answerone', validators=[DataRequired()])
    answertwo = StringField('answertwo', validators=[DataRequired()])
    answerthree = StringField('answerthree', validators=[DataRequired()])
    answerfour = StringField('answerfour', validators=[DataRequired()])

class TestTakeGetForm(Form):
    testid = StringField('testid', validators=[DataRequired()])

class TestTakeForm(Form):
	answerselect = StringField('answerone', validators=[DataRequired()])
 


