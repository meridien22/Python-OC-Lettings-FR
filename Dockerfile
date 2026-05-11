# Image de base légère
FROM python:3.13-slim

# Variables d'environnement pour Python
# Empêche la création de fichiers .pyc et des dossiers __pycache__
# Evite la présence de fichier inutile dans le conteneur
ENV PYTHONDONTWRITEBYTECODE=1
# Dsactive le buffering des sorties standard (stdout) et d’erreur (stderr)
# Assure un affichage direct des logs
ENV PYTHONUNBUFFERED=1

# Définition du répertoire de travail/répertoire courant du conteneur
# Si /app n’existe pas, il est créé automatiquement
# Toutes les instructions suivantes s’exécutent dans /app
WORKDIR /app

# Installation des dépendances système (nécessaires pour certains packages Python)
# apt-get update : Met à jour la liste des paquets disponibles depuis les dépôts Debian/Ubuntu
# apt-get install -y : Installe des dépendances système sans demander de confirmation
# build-essential : compilateur C/C++ + outils (gcc, make…), utile pour compiler certaines dépendances Python
# libpq-dev : bibliothèques de développement pour PostgreSQL, nécessaire pour certaines libs PostgreSQL comme psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Installer Poetry
RUN apt-get update && apt-get install -y curl
# Installation de curl car absent de la version slim de python
RUN curl -sSL https://install.python-poetry.org | python3
# Le répertoire d'intallation de curl n'est pas dans le PATH des couches Docker, il faut l'ajouter
ENV PATH="/root/.local/bin:$PATH"
# Copier uniquement les fichiers de dépendances
COPY pyproject.toml poetry.lock* /app/
# Installer les dépendances sans créer de venv
# --no-interaction : Désactive toute interaction utilisateur, pas de questions (“Do you want to continue ?”)
# --no-ansi : Désactive les couleurs et caractères spéciaux terminal
# --no-root : N'installe pas le projet courant comme package, installe uniquement les dépendances
# --without dev : N’installe pas les dépendances de développement
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root --without dev

# Copie du reste du projet
COPY . /app/

# Collecte des fichiers statiques (nécessaire pour la prod)
# Utilise la constance STATIC_ROOT de settings.py
RUN python manage.py collectstatic --noinput

# Exposition du port (8000 par défaut pour Django)
EXPOSE 8000

# Lancement de l'application
# On utilise gunicorn pour la production au lieu de runserver
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]