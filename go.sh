#!/bin/bash
option="$1"

if [ "${option}" == "install" ]; then
	echo -e "\n[AUTOMATIC_SUMMARIZER] Installing prerequisite..."
    sudo apt-get install python
	sudo apt-get install pip

	sudo apt-get install screen

	pip install Django==1.11
	pip install django-cleanup

	sudo apt-get install mysql-server libmysqlclient-dev
	echo "CREATE DATABASE AUTOMATIC_SUMMARIZER CHARACTER SET UTF8;" | mysql -u root -p

	pip install mysql-python

	pip install pdfminer

	pip install gensim

	pip install -U textblob
	python -m textblob.download_corpora

	echo -e "[AUTOMATIC_SUMMARIZER] Done.\n"

elif [ "${option}" == "run" ]; then
	echo -e "\n[AUTOMATIC_SUMMARIZER] Starting..."

	python manage.py makemigrations
	python manage.py migrate
	screen -XS automatic_summarizer quit
	screen -dmS automatic_summarizer python manage.py runserver

	echo -e "[AUTOMATIC_SUMMARIZER] Running.\n[AUTOMATIC_SUMMARIZER] To see it, use the command: \$ screen -r automatic_summarizer\n"

else
	echo -e "\n[AUTOMATIC_SUMMARIZER] Wrong argument ${option}! Use only run or install parameters.\n"
fi