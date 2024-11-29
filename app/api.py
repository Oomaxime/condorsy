from flask import Flask, render_template, request, url_for, redirect, g

from pymongo import MongoClient

from bson.objectid import ObjectId # type: ignore

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
    

@app.route('/kill', methods=['POST'])
def killUser():

    user_collection.update_one({ 'pseudo': global_data['pseudo']},
                                            { "$unset": { "addresse": "",
                                                          "age": "", 
                                                          "job": "", 
                                                          "password":""}})

    return render_template('login.html')


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

if __name__ == "__main__":
    app.run(debug=True, port=4000)