# OC-DataScientist-P7
Dépôt dédié au projet "Implémentez un modèle de scoring" du parcours DataScientist sur OpenClassrooms

Contenu :

------------------------------------------
app.py
requirements.txt
models/
static/
templates/

Script et ressources de l'API Flask qui possède 2 endpoints :
- endpoint n°1 : page d'accueil de l'API qui contient les consignes d'utilisation
- endpoint n°2 : retourne le score et la classe prédite par le modèle lorsqu'on lui soumet les variables décrivant un client

------------------------------------------
project/
	scripts/
	submission_files/
	tdb_streamlit/

Ces répertoires contiennent les éléments mis en oeuvre au cours du projet autour de cette API.
- le notebook qui permet la création, l'évaluation et le référencement d'un modèle d'apprentissage est dans scripts/
- les fichiers générés au format adapté pour être soumis dans le cadre de la compétition Kaggle sont dans submission_files/
- un tableau de bord streamlit fournit une interface locale pour tester l'API ; sa configuration est dans tdb_streamlit/

------------------------------------------
Projet réalisé en mai 2024