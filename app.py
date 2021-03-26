from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS, cross_origin
from fire import Base
import time


app = Flask(__name__)
CORS(app, support_credentials=True)

data_base = Base("./titato-8a7f4-firebase-adminsdk-cacno-b118cf5928.json")
free_games = []

@app.route('/add_match', methods=['POST'])
@cross_origin(supports_credentials=True)
def add_match():
    request_data = request.get_json()
    uid = int(request_data['ID'])
    if (len(free_games) == 0):
        name = data_base.create_game(uid,True)
        free_games.append(name)
    else:
        name = free_games.pop(0)
        data_base.add_to_game(uid,name)

    return jsonify(RID=name)

app.run(port=3000)