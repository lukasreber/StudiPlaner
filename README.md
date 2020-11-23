# StudiPlaner

Django Webapplikation für die Kompetenz wet im Studiengang Data Science @ FHNW

## Installation

Repository kopieren

    git clone https://github.com/lukasreber/StudiPlaner.git

Neues Virtual Environment erstellen

    python -m venv studiplaner

Virtual Environment aktivieren

    source studiplaner/bin/activate

Dependencies installieren

    pip install -r requirements.txt

Webserver starten

    python manage.py runserver

Die Webseite ist anschliessend unter [http://127.0.0.1:8000](http://127.0.0.1:8000) erreichbar

## Testausführung

Virtual Environment aktivieren

    source studiplaner/bin/activate

Testausführung mit pytest

    pytest

## User Management

Admin erstellen

    python manage.py createsuperuser

Passwort zurücksetzen

    python manage.py changepassword <username>
