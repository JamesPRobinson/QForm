
from flask import Flask, render_template, request, abort
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, \
                SubmitField, SelectField
from wtforms import TextAreaField
from wtforms.validators import ValidationError, DataRequired, \
                Email, EqualTo, Length, Optional
from questions import generate_questions
import lang_config

def factory(code = 'EN'):
    # This form class is created in a local scope, so a new class object
    # is made each time factory is called
    class QForm(FlaskForm):
        pass
    question_fields = generate_questions(code)
    setattr(QForm, 'q1',  SelectField( u"Question 1", [Optional()], choices=question_fields[1]))
    setattr(QForm, 'a1', TextAreaField(validators=[Length(min=2, message=lang_config.ERRORLEN[code].format(question_fields[0][0], 2))]))
    setattr(QForm, 'q2', SelectField( u"Question 2", [Optional()], choices=question_fields[2]))
    setattr(QForm, 'a2', TextAreaField(validators=[Length(min=2, message=lang_config.ERRORLEN[code].format(question_fields[0][1], 2))]))
    setattr(QForm, 'submit', SubmitField(label=('Submit')))
    return QForm

"""
class SuperForm(FlaskForm):
    code = None
    question_fields = generate_questions(code)
    q1 = SelectField( u"Question 1", [Optional()], choices=question_fields[1])
    a1 = TextAreaField(validators=[Length(min=2, message=lang_config.ERRORLEN[code].format(question_fields[0][0], 2))])
    q2 = SelectField( u"Question 2", [Optional()], choices=question_fields[2])
    a2 = TextAreaField(validators=[Length(min=2, message=lang_config.ERRORLEN[code].format(question_fields[0][1], 2))])

    submit = SubmitField(label=('Submit'))
class ENForm(SuperForm):
    code = 'EN'
"""
    