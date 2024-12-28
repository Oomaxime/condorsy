from flask import Flask, render_template, request, url_for, redirect, g

from pymongo import MongoClient

from bson.objectid import ObjectId # type: ignore

import time, datetime

global_data = {}

from app import global_data

client = MongoClient("mongodb://localhost:27017/")
db = client.projet_1com

user_collection = db.User
questions_collection = db.Questions

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('page.html')



#
#
#Fonction de création d'utilisateur
def creationUser():

    pseudo_= str(request.form.get('pseudo'))
    password_= str(request.form.get('password'))
    age_= int(request.form.get('age'))
    address_= str(request.form.get('address'))
    job_= str(request.form.get('job'))

    pseudo_existant = user_collection.find_one({ "pseudo": pseudo_ })

    if pseudo_existant and (str(pseudo_existant['pseudo']) == pseudo_):
        return render_template('page.html')

    else:

        user_collection.insert_one({ "pseudo": pseudo_, 
                                      "password":password_, 
                                      "age":age_, 
                                      "addresse":address_, 
                                      "job":job_,
                                      "admin": 0, 
                                      "role": 'visitor'})
        
        global_data['pseudo'] = pseudo_
        global_data['password'] = password_
    
        return render_template('modif.html')
    



#
#
#Fonction de supprésion d'utilisateur
def killUser():

    user_collection.update_one({ 'pseudo': global_data['pseudo']},
                                            { "$unset": { "addresse": "",
                                                          "age": "", 
                                                          "job": "", 
                                                          "password":""}})

    return render_template('login.html')



#
#
#Fonction de modification d'utilisateur
def modUser():

    password_= str(request.form.get('password'))
    age_= int(request.form.get('age'))
    address_= str(request.form.get('address'))
    job_= str(request.form.get('job'))


    password_existant = user_collection.find_one({ "pseudo": global_data['pseudo'] })

    if (str(password_existant['password']) == password_):
        return render_template('modif.html')
    
    else:
        user_collection.update_one({ 'pseudo': global_data['pseudo']},
                                    { "$set": { "addresse": address_,
                                                "age": age_, 
                                                "job": job_, 
                                                "password":password_}})
        return 'données modifiées'



#
#
#Fonction de création de survey
#
# ATTENTION !!! Bien penser à changer la valeur du champ 'champschoix' par la variable contenant 
# le nombre de réponses possibles 
def creationSurvey():

    champs_choix_ = 7

    if (champs_choix_>2):
        creator_ = str(global_data['pseudo'])
        question_ = str(request.form.get('question'))
        description_ = str(request.form.get('description'))
        date_ = time.strftime("%d:%m:%Y à %H:%M:%S", time.localtime())
        date_start_ = str(request.form.get('date_start'))
        date_end_ = str(request.form.get('date_end'))

        questions_collection.insert_one({ "creator": creator_, 
                                            "question":question_, 
                                            "description":description_, 
                                            "date.create":date_, 
                                            "date.start":date_start_,
                                            "date.end": date_end_})

            
        for k in range(champs_choix_):
            choix = str(request.form.get(f'{k}'))
            questions_collection.update_one({ "creator": creator_},{"$push" : {"choix": choix}})

            
            return render_template('page.html')
    
    else:
        return render_template('creationForm.html')



#
#
#Fonction de modification du survey
#
#ATTENTION !!! Dans la fonction, l'id_ correspond à un bouton ayant pour nom 'button_id'. 
# Le bouton devra porter ce nom, et avoir pour value l'id du survey
def modificationSurvey():


    id_ = request.form.get('button_id')
    document = questions_collection.find_one({"_id": ObjectId(id_)})
    champs_choix_ = len(document.get("choix", []))


    question_ = str(request.form.get('question'))
    description_ = str(request.form.get('description'))

    questions_collection.update_one({ '_id': id_},  { "$set": { "question": question_,
                                                                  "description": description_}})
    
    questions_collection.update_one({ "_id": id_},{"$unset" : {"choix": ""}})

    for k in range(champs_choix_):
                choix = str(request.form.get(f'{k}'))

                questions_collection.update_one({ "_id": id_},{"$push" : {"choix": choix}})


    return render_template('survey.html')



#
#
#Fonction de gestion des formulaires
#
#ATTENTION !!! La fonction text_id contient le name de la zone de texte ('<text area name="...">). Ce texte aura pour valeur l'id du survey. 
# Elle doit obligatoirement se trouver dans un form pour être analysée
def gestionForm():

    id_ = request.form.get('text_id')
    survey_ = questions_collection.find({"id": id_})
    survey_['dépouillage'] = False

    
    for surveys_ in survey_:
        if datetime.now() > surveys_['date.start'] and datetime.now() < surveys_['date.end']:
            surveys_['avancement'] = "en cours"
        elif datetime.now() < surveys_['date.start']:
            surveys_['avancement'] = "n'a toujours pas commencé"
        elif datetime.now() > surveys_['date.end'] and surveys_['dépouillage'] == False:
            surveys_['avancement'] = "fermé"
        else:
            surveys_['avancement'] = "résultats disponibles"        

    return survey_



#
#
#Fonction de gestion des formulaires
#
# Même règle que pour la fonction gestionForm concernant le button_id. La fonction fait ici le retour 
# dans une chaine de caractères les choix de l'utilisateur en fonction de l'ordre choisi. 
# L'ordre sera afficher sous cet ordre dans la variable document['ordre']: x>y>z>p=s>c
def affichageReponses():

    id_u = user_collection.find_one({'pseudo': global_data['pseudo']})

    id_ = request.form.get('button_id')
    document = questions_collection.find_one({"_id": ObjectId(id_), "reponses.user_id": id_u})

    for reponse in document['reponse']:
        if isinstance(reponse, list):
            for egalite in reponse:
                if document['ordre']:
                    document['ordre'] += '='
                document['ordre'] += egalite
        else:
            if document['ordre']:
                document['ordre'] += '>'
            document['ordre'] += reponse
            
    
    return document



#
#
#Fonction de participation aux sondages
#
#Même règle que pour la fonction gestionForm concernant le button_id. 'classement' correspond au name de la textarea. La fonction récupère ici 
#une zone de texte contenant les préférences de l'utilisateur en terme de choix.
def participationReponses():

    id = request.form.get('button_id')
    classement = request.form.get('classement')
    classement = classement.replace(" ", "")
    reponseU = questions_collection.find_one({'pseudo': global_data['pseudo']}, {"id": 1})

    resultat = []

    rep = classement.split('>')

    for reps in rep:
        if '=' in reps:
            resultat.append([str(reps) for reps in reps.split('=')])
        else:
            resultat.append(str(reps))

    questions_collection._update({"_id": ObjectId(id)}, {"reponses.user_id": reponseU, "reponse": resultat})




# Fonction d'affichage des reponses
#
#Même règle que pour la fonction gestionForm concernant le button_id. La fonction fait ici le retour des réponses de l'utilisateur
def affichageReponses():

    id_u = user_collection.find_one({'pseudo': global_data['pseudo']})

    id_ = request.form.get('button_id')
    document = questions_collection.find_one({"_id": ObjectId(id_), "reponses.user_id": id_u})

    for reponse in document['reponse']:
        if isinstance(reponse, list):
            for egalite in reponse:
                if document['ordre']:
                    document['ordre'] += '='
                document['ordre'] += egalite
        else:
            if document['ordre']:
                document['ordre'] += '>'
            document['ordre'] += reponse
            
    
    return document


if __name__ == "__main__":
    app.run(debug=True, port=4000)




# Fonction d'envoi des réponses de l'utilisateur
#
# Cette fonction récupère les réponses de l'utilisateur et les envoie dans la base de données, 
# lors de sa première participation à un sondage. 'choix' correspond au name de la zone de texte.

def participationForm():

    id = request.form.get('choix')
    id = id.replace(" ", "")

    resultat = []

    rep = id.split('>')

    for reps in rep:
        if '=' in reps:
            resultat.append([str(reps) for reps in reps.split('=')])
        else:
            resultat.append(str(reps))

    questions_collection.insert_one({"reponses": {
            "user_id": global_data['id'], 
            "reponse": resultat
        }})
