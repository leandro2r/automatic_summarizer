sudo apt-get install python
sudo apt-get install pip

pip install Django==1.11
pip install django-cleanup

sudo apt-get install mysql-server libmysqlclient-dev
mysql -u root -p
-ex CREATE DATABASE AUTOMATIC_SUMMARIZER CHARACTER SET UTF8;

pip install mysql-python

pip install pdfminer

pip install gensim
# pip install sumy
# python -c "import nltk; nltk.download('punkt')"

pip install -U textblob
python -m textblob.download_corpora