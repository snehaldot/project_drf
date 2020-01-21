1) Create virtual env:

    python3 -m venv env

2) Install python packages:

    pip install -r requirement.txt

3) Make migrations:

    python manage.py makemigrations

4) Run Migrations:

    python manage.py migrate

5) Run development server:

    python manage.py runserver

6) URL's for project:

    admin: http://127.0.0.1:8000/admin/
    jwt: http://127.0.0.1:8000/api-token-auth/
    api: 
        api's: http://127.0.0.1:8000/
        image: http://127.0.0.1:8000/image/<int:id>
        images: http://127.0.0.1:8000/image/
