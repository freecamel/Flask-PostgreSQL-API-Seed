from flask import Flask
from flask.ext import restful
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('settings')

rest_api = restful.Api(app)

db = SQLAlchemy(app)


from users import api as users_api


rest_api.add_resource(users_api.UserAPI, '/api/v1/user')


db.create_all()