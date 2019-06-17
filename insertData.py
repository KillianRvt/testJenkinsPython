#Import des modules nécessaires
import mysql.connector as mariadb
import glob
import os
import json

#Récupération de la liste de fichiers
list_of_files = glob.glob('*')

#Récupération du dernier fichier créé
latest_file = max(list_of_files, key=os.path.getctime)

#Connexion à la base de données
mariadb_connection = mariadb.connect(host='192.168.213.128', port=3306, user='devops', password='bournigal', database='TPDevOps')

#Création du curseur pour exécuter des requetes
cursor = mariadb_connection.cursor()

#Récupération des données du fichier json
with open(latest_file) as json_file:  
    data = json.load(json_file)

    #Pour chaque mesure, insertion des données dans la base
    for p in data['mesure']:
        insert = "INSERT INTO MesuresAutomates (numUnite, numAutomate, typeAutomate, tempCuve, tempExterieure, poidsLaitCuve, poidsProduitFini, pH, ionPotassium, chlorureDeSodium, niveauSalmonelle, niveauEColi, niveauListeria, dateMesure) VALUES ("+str(p['numUnite'])+", "+str(p['numAutomate'])+", '"+str(p['typeAutomate'])+"', "+str(p['tempCuve'])+", "+str(p['tempExterieure'])+", "+str(p['poidsLaitCuve'])+", "+str(p['poidsProduitFini'])+", "+str(p['pH'])+", "+str(p['ionPotassium'])+", "+str(p['chlorureDeSodium'])+", "+str(p['niveauSalmonelle'])+", "+ str(p['niveauEColi'])+", "+str(p['niveauListeria'])+", '"+str(p['dateMesure'])+"');"
        #print(insert)
        cursor.execute(insert)

#Commit des données 
mariadb_connection.commit()
