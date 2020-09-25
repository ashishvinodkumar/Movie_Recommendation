install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

test:
	python -m pytest -vv test_movie_rec.py

lint:
	python movie_rec.py --title "Jumanji"

all: install lint test
