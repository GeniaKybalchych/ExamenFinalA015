from flask import flash, render_template, request
import requests

from app_formulaire import app
from app_formulaire.forms import ProjetForm



# Recherche d'un projet
@app.route('/', methods=['GET', 'POST'])
def formulaire():
    projet_form = ProjetForm()
    projet = None

    codeProjet = request.args.get('codeProjet')

    if codeProjet:

            # Construire l'URL pour la requête GET
        service_url = f'http://127.0.0.1:5000/projets/{codeProjet}'


        response = requests.get(service_url)


        if response.status_code == 200:
                 projet = response.json().get('projet')
        else:
                 flash('Erreur de la recherche de projet.')
    return render_template('formulaire.html',  form=projet_form, projet=projet)