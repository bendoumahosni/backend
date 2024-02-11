                                         Projet7 : Implémentez un modèle de scoring 
# Problématique:
Une société financière, nommée "Prêt à dépenser", qui propose des crédits à la consommation pour des personnes souhaite mettre en œuvre un outil de “scoring crédit” pour calculer la probabilité qu’un client rembourse son crédit, puis classifie la demande en crédit accordé ou refusé​

# Travail demande:​
* Construire un modèle de scoring​
* Analyse des features qui contribuent le plus au modèle​
* Mettre en production le modèle de scoring  (API et interface de test)​
* Tracking des expérimentations et analyse du data drift​
# Données Kaggle : [Home Credit Default](https://www.kaggle.com/c/home-credit-default-risk/data)
# creation d'un depot pour api (avec fastapi)
# creation d'un depot pour l'interface cree avec streamlit : [interface](https://github.com/bendoumahosni/strprojet7/tree/master)
# bibliothèques python a ajouter au fichier: requirements.txt
* fastapi == 0.109.0
* gunicorn
* uvicorn
* python_multipart
* pandas
* joblib
* scikit_learn
* pydantic
* lightgbm
* pytest
* httpx
# Outils utilisés:
* jupyter notebook
* Mlflow
* Aws 
