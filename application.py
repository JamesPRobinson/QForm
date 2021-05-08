from flask import Flask, render_template, request, abort, session
from form import factory

application = Flask(__name__, template_folder='templates')
application.config['SECRET_KEY']='LongAndRandomSecretKey'
application.debug = True

lang_code = 'EN'

@application.route('/result', methods=["POST"])
def submit_answers():
    code = session['code']
    form_class = factory(code)
    user_form = form_class(request.form)
    if user_form.validate_on_submit():
        answers = request.form
        print(answers)
        return render_template('success.html')
    else:
        return render_template('index.html', form=user_form)

@application.route('/', methods=('GET', 'POST'))
def index():
    lang_code = request.args.get('code')
    if not lang_code:
        abort(404)
    else:
        session['code'] = lang_code
        form_class = factory(code=lang_code)
        form = form_class(request.form)
        if form.validate_on_submit():
            print("Success!?!?")
        return render_template('index.html', form=form)