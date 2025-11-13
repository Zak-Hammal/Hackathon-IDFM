"""
Application Flask pour le démonstrateur de score de mobilité
"""

from flask import Flask, render_template, request, jsonify
import json
import os
from calculateur_score import calculer_score_mobilite, charger_itineraire

app = Flask(__name__)


@app.route('/')
def index():
    """Page d'accueil"""
    return render_template('index.html')


@app.route('/api/itineraires', methods=['GET'])
def get_itineraires():
    """Récupère la liste des itinéraires disponibles"""
    itineraires = []
    fichiers = [
        'exemple_itineraire.json',
        'exemple_itineraire_voiture.json',
        'exemple_itineraire_multimodal.json',
        'exemple_itineraire_velo.json',
        'exemple_itineraire_covoiturage.json',
        'exemple_itineraire_velo_train.json'
    ]
    
    for fichier in fichiers:
        if os.path.exists(fichier):
            try:
                itineraire = charger_itineraire(fichier)
                itineraires.append({
                    'fichier': fichier,
                    'id': itineraire.get('itineraire_id', 'N/A'),
                    'depart': itineraire.get('depart', 'N/A'),
                    'arrivee': itineraire.get('arrivee', 'N/A'),
                    'distance_km': itineraire.get('distance_totale_km', 0),
                    'duree_min': itineraire.get('duree_totale_minutes', 0),
                    'co2_kg': itineraire.get('co2_total_kg', 0),
                    'tags': itineraire.get('tags', [])
                })
            except Exception as e:
                print(f"Erreur lors du chargement de {fichier}: {e}")
    
    return jsonify(itineraires)


@app.route('/api/itineraire/<path:fichier>', methods=['GET'])
def get_itineraire_detail(fichier):
    """Récupère les détails complets d'un itinéraire avec ses segments"""
    if not os.path.exists(fichier):
        return jsonify({'error': 'Fichier non trouvé'}), 404
    
    try:
        itineraire = charger_itineraire(fichier)
        return jsonify(itineraire)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/calculer', methods=['POST'])
def calculer():
    """Calcule le score de mobilité"""
    data = request.get_json()
    
    fichier = data.get('fichier')
    parametres = data.get('parametres', {})
    
    if not fichier:
        return jsonify({'error': 'Fichier non spécifié'}), 400
    
    if not os.path.exists(fichier):
        return jsonify({'error': 'Fichier non trouvé'}), 404
    
    try:
        itineraire = charger_itineraire(fichier)
        resultat = calculer_score_mobilite(
            itineraire,
            x_voiture=parametres.get('x_voiture', 50.0),
            x_marche=parametres.get('x_marche', 10.0),
            x_report_modal=parametres.get('x_report_modal', 30.0),
            x_co2=parametres.get('x_co2', 100.0),
            x_penalite_co2=parametres.get('x_penalite_co2', 2.0),
            x_tag=parametres.get('x_tag', 20.0),
            x_velo=parametres.get('x_velo', 15.0),
            x_covoiturage=parametres.get('x_covoiturage', 40.0)
        )
        return jsonify(resultat)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/upload', methods=['POST'])
def upload():
    """Upload d'un nouveau fichier d'itinéraire"""
    if 'file' not in request.files:
        return jsonify({'error': 'Aucun fichier fourni'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'Nom de fichier vide'}), 400
    
    if not file.filename.endswith('.json'):
        return jsonify({'error': 'Le fichier doit être un JSON'}), 400
    
    try:
        # Lire et valider le JSON
        content = file.read().decode('utf-8')
        itineraire = json.loads(content)
        
        # Sauvegarder le fichier
        filename = f"upload_{file.filename}"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return jsonify({
            'success': True,
            'fichier': filename,
            'message': 'Fichier uploadé avec succès'
        })
    except json.JSONDecodeError:
        return jsonify({'error': 'JSON invalide'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

