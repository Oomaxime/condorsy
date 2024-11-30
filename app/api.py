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
@app.route('/submit', methods=['POST'])
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
@app.route('/kill', methods=['POST'])
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
@app.route('/modif', methods=['POST'])
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
                                    { "$unset": { "addresse": address_,
                                                "age": age_, 
                                                "job": job_, 
                                                "password":password_}})
        return 'données modifiées'



#
#
#Fonction de création de survey
#
# ATTENTION !!! Bien penser à changer la valeur du champ 'champschoix' par la variable contenant le nombre de réponses possibles 
@app.route('/creationForm', methods=['POST'])
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
#ATTENTION !!! Dans la fonction, l'id_ correspond à un bouton ayant pour nom 'button_id'. Le bouton devra porter ce nom, et avoir pour value l'id du survey
@app.route('/modificationForm', methods=['POST'])
def modificationSurvey():


    id_ = request.form.get('button_id')
    champs_choix_ = len(questions_collection.keys())

    question_ = str(request.form.get('question'))
    description_ = str(request.form.get('description'))

    questions_collection.update_one({ '_id': id_},  { "$unset": { "question": question_,
                                                                  "description": description_}})

    for k in range(champs_choix_):
                choix = str(request.form.get(f'{k}'))
                questions_collection.update_one({ "creator": creator_},{"$push" : {"choix": choix}})


    return render_template('survey.html')



#
#
#Fonction de gestion des formulaires
#
#ATTENTION !!! La fonction pseudo contient le name de la zone de texte. Elle doit obligatoirement se trouver dans un form pour être analysée
@app.route('/gestionForm', methods=['POST'])
def gestionForm():
    pseudo_ = request.form.get('pseudo')
    survey_ = questions_collection.find({pseudo_})
    survey_['dépouillage'] = True

    
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



if __name__ == "__main__":
    app.run(debug=True, port=4000)