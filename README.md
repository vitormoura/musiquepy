# Musiquepy

Projet labo pour explorer le développement des applications web python en utilisant Flask.

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