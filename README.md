Install

    npm i

    pip install -r requirements.txt

Before run

    ./manage.py migrate --settings=config.settings.local

Run

	./manage.py runserver 0.0.0.0:8000 --settings=config.settings.local

Collect static files

    ./manage.py collectstatic --settings=config.settings.local