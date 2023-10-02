from flask import jsonify, request

from model import Projet, db, create_app

app = create_app()

# Ajout d'un projet
@app.route('/projets/insert-data', methods=['POST'])
def insert_projet():
    try:
        data = request.json

        new_entry = Projet(codeProjet=data['codeProjet'],
                           description=data['description'])

        db.session.add(new_entry)
        db.session.commit()

        return jsonify(status="success", message="Données ajoutées avec succès."), 200
    except Exception as e:

        app.logger.error(f"Erreur d'ajout des données: {str(e)}")
        return jsonify(status="error", message=str(e)), 500

# Recherche d"un projet par son code
@app.route('/projets/<string:codeProjet>', methods=['GET'])
def get_projet(codeProjet):
    projet =Projet.query.filter_by(codeProjet=codeProjet).first()
    if projet is None:
        return jsonify({'erreur':'Le code du projet est incorrect'}), 404
    return jsonify({'projet':{
        'codeProjet': projet.codeProjet,
        'description': projet.description
    }})

if __name__ == '__main__':
    app.run(port=5001, debug=True)