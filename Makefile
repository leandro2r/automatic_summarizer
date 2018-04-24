
PROJECT_DIR:=/opt/automatic_summarizer/

#---------------------------------------------------------------------------------
# Install
#---------------------------------------------------------------------------------

install:
	@echo Installing ...
	@sudo apt-get install python
	@sudo apt-get install python-pip
	@sudo apt-get install mysql-server libmysqlclient-dev
	@echo "CREATE DATABASE AUTOMATIC_SUMMARIZER CHARACTER SET UTF8;" | mysql -u root -p
	@pip install -r requirements.txt
	@python -m textblob.download_corpora
	@sudo mkdir -p $(PROJECT_DIR)
	@sudo cp -Rf * $(PROJECT_DIR)
	@sudo ln -sf $(PROJECT_DIR)daemons/* /etc/init.d/
	@echo Installation complete.

