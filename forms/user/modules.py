from forms import db,app

class UserRegistration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name =db.Column(db.String(120),unique=False, nullable=False)
    last_name = db.Column(db.String(120), unique=False,nullable=False)
    other_name = db.Column(db.String(120),unique=False, nullable=False)
    gender = db.Column(db.String(120),unique=False, nullable=False)
    date_of_birth = db.Column(db.String(120), unique=False,nullable=True)
    jamb_registration_no = db.Column(db.String(120),unique=True, nullable=False)
    college = db.Column(db.String(120),unique=False, nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    phone_no = db.Column(db.Integer,unique=False, nullable=False)
    nationality = db.Column(db.String(120), unique=False,nullable=False)
    state_of_origin = db.Column(db.String(120), unique=False,nullable=False)
    local_government = db.Column(db.String(120),unique=False, nullable=False)
    guardian_name = db.Column(db.String(120),unique=False, nullable=False)
    guardian_number = db.Column(db.Integer,unique=False, nullable=False)
    guardian_address = db.Column(db.String(120),unique=False, nullable=False)
    postal_address = db.Column(db.String(120),unique=False, nullable=False)
with app.app_context():
    db.create_all()








