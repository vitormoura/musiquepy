# Musiquepy

Projet labo pour explorer le développement des applications web python en utilisant Flask.

## Des fonctionnalités à explorer

- [x] Configuration des nouveaux environnements 
- [x] Structure des projets Python et Flask 
- [x] Contenu dynamique `text/html` (pages web en utilisant de templates) 
- [x] Contenu statique (fichiers css, js, imgs, etc.) 
- [x] Requêtes et validation des formulaires HTML 
- [ ] Téléchargement/Téléversement des fichiers binaires 
- [x] Requêtes/Réponses `application/json` 
- [x] Docs des APIs avec Swagger/OpenAPI
- [x] Accès aux bases des données (SQLALCHEMY)
- [x] Utilisation des sessions utilisateur 
- [x] CORS 
- [x] i18n
- [ ] Configuration 
- [ ] Journalisation 
- [ ] Request filters 
- [ ] Traitement des erreurs 
- [ ] Build et déploiement (xcopy et Docker images)

## Préparer un nouvel environnement de DEV

Créez et activez un nouvel environnement virtuel:

```shell
> python -m venv venv

> ./venv/scripts/activate
```

Ensuite, exécutez l'installation du projet en mode développement:

```shell
> pip install -e .
```

Pour finir, vous pouvez désormais lancer le projet website ou api avec:

```shell
> cd musiquepy/website
> flask run --port 5000
```

```shell
> cd musiquepy/api
> flask run --port 5001
```

## Paquet de distribution

Exécutez:

```shell
> python setup.py sdist
```

## Quelques références utiles

- La doc officielle: https://flask.palletsprojects.com/en/2.0.x/
- Un bon tuto à regarder : https://hackersandslackers.com/your-first-flask-application