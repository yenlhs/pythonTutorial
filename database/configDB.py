import configparser

config = configparser.ConfigParser()

config.read("/Users/Adrian/Documents/pythonTutorial/database/database.properties")

# username = config['Mariadb']['user']
# password = config['Mariadb']['password']
# host     = config['Mariadb']['host']
# db       = config['Mariadb']['db']
dbsys='Mariadb'
username = config[dbsys]['user']
password = config[dbsys]['password']
host     = config[dbsys]['host']
db       = config[dbsys]['db']


