from flask import flash, render_template, jsonify
import requests

from app_formulaire import app
from app_formulaire.forms import ProjetForm


# Creation d'un projet
@app.route('/', methods=['GET', 'POST'])
def formulaire():
    projet_form = ProjetForm()
    if projet_form.validate_on_submit():

        # Construire l'URL pour la requête GET
        service_url = f'http://127.0.0.1:5000/projets'


        # Creer le corps de la requete avec les donnees du formulaire
        donnees = {
            'codeProjet': projet_form.codeProjet.data,
            'description': projet_form.description.data,
        }

        response = requests.post(service_url, json=donnees)


        if response.status_code == 201:
            flash(f'Le projet {projet_form.codeProjet.data} est cree avec success')
        else:
            flash('Erreur de la creation de projet.')
    return render_template('formulaire.html', form=projet_form)

