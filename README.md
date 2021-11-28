# Musiquepy

Projet labo pour explorer le développement des applications web python en utilisant Flask.

## Des fonctionnalités à explorer

- [ ] Configuration des nouveux environnements
- [ ] Struture des projets Python et Flask
- [ ] Contenu dynamique `text/html` (pages web en utilisant de templates)
- [ ] Contenu statique (fichiers css, js, imgs, etc.)
- [ ] Requêtes et validation des formulaires HTML
- [ ] Téléchargement/Téléversement des fichiers binaires
- [ ] Requêtes/Réponses `application/json`
- [ ] Utilisation des sessions utilisateur
- [ ] CORS
- [ ] Configuration
- [ ] Journalisation
- [ ] Request filters
- [ ] Traitement des erreurs
- [ ] Build et déployement


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

Pour finir, vous pouvez desormais lancer le projet website ou api avec:

```shell
> cd musiquepy/website
> flask run --port 5000
```

```shell
> cd musiquepy/api
> flask run --port 5001
```

## Paquet de distribuition

Exécutez:

```shell
> python setup.py sdist
```

## Quelques références utiles

- La doc officielle: https://flask.palletsprojects.com/en/2.0.x/
- Un bon tuto à regarder : https://hackersandslackers.com/your-first-flask-application