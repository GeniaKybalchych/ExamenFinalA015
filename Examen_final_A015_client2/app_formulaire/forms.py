from flask_wtf import  FlaskForm
from wtforms import SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired


class ProjetForm(FlaskForm):
    codeProjet=StringField("CodeProjet:", validators=[DataRequired()])
    submit=SubmitField("Rechercher")