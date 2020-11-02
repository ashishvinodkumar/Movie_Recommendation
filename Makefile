install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

test:
	python -m pytest -vv test_movie_rec.py

lint:
	pylint --disable=R,C,W app/app.py

all: install lint test
