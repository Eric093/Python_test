# coding=utf-8

import mysql.connector
from mysql.connector import errorcode

# Configuration dans un dictionnaire
config = {
  'user': 'qstdo',
  'password': 'qstdocdg',
  'host': 'siam5.tech.cdg',
  'database': 'siam.v28',
  'raise_on_warnings': True,
}

try:
    # Connexion à l'aide du dictionnaire de configuration
    cnx = mysql.connector.connect(**config)
    print("Connexion réussie !")

    # Handle d'accès à la base
    cursor = cnx.cursor()

    # Requete
    query = ("SELECT login FROM param_utilisateur WHERE id BETWEEN 0 AND 10")

    # Execution de la requete
    cursor.execute(query)

    # Affichage du résultat

    for (login) in cursor:
        name = cursor.fetchone()[0]
        print(name)



except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

else:
    cursor.close()
    cnx.close()
    print("Connexion cloturée.")

