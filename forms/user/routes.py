
from forms.user.modules import UserRegistration
from forms import db,app
from flask import redirect,flash,url_for,render_template,request




@app.route('/', methods=['GET','POST'])
def addStudent():
    # form = UserInputForm()
    if request.method == 'POST':
        register = UserRegistration(first_name=request.form.get('firstName'),last_name=request.form.get('lastName'),other_name=request.form.get('otherName'),
                                    gender=request.form.get('gender'),date_of_birth=request.form.get('dateOfBirth'),
                                    jamb_registration_no = request.form.get('JambRegistrationNo'),
                                    college=request.form.get('College'),email=request.form.get('Email'),phone_no=request.form.get('PhoneNo'),
                                    nationality=request.form.get('Nationality'),state_of_origin =request.form.get('stateOfOrigin'),
                                    local_government=request.form.get('localGovernment'),guardian_name=request.form.get('guardianName'),
                                    guardian_number=request.form.get('guardianNumber'),guardian_address=request.form.get('guardianAddress'),
                                    postal_address=request.form.get('postalAddress'))
        db.session.add(register)
        flash(f"Welcome {request.form.get('firstName')}. Thank you for registering",'success')
        db.session.commit()
        return redirect(url_for('addStudent'))
    return render_template('add.html')


