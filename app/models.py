from app import db

# User db model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    tests = db.relationship('Test', backref='author', lazy='dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.nickname)

# Test db model
class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    description = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    questions = db.relationship('Question', backref='test', lazy='dynamic')

    def __repr__(self):
        return '<Test %r>' % (self.title)

# Question db model, all fields must be entered atm.
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200))
    video_url = db.Column(db.String(300))
    answer_one = db.Column(db.String(200))
    answer_two = db.Column(db.String(200))
    answer_three = db.Column(db.String(200))
    answer_four = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime)
    test_id = db.Column(db.Integer, db.ForeignKey('test.id'))

    def __repr__(self):
        return '<Question %r>' % (self.question)