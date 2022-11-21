import os
import json
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']

db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Project(db.Model):
   __tablename__ = "projects"    
   id = db.Column("id", db.Integer, primary_key=True)   
   name = db.Column("name", db.String)
   owner = db.Column("owner", db.String)
   tech_stack = db.Column("tech_stack", db.String)
   github_link = db.Column("github_link", db.String)
   description = db.Column("description", db.String)
   contact_info = db.Column("contact_info", db.String)

   @property
   def serialized(self):
      return {
         "id" : self.id,
         "name" : self.name,
         "owner" : self.owner,
         "tech_stack" : self.tech_stack,
         "github_link" : self.github_link,
         "description" : self.description,
         "contact_info": self.contact_info
      }    


@app.route("/")
def index():
   return "Welcome to the Software Project Finder Database"

@app.route("/projectsAll")
def getAllProjects():
   
   projects = Project.query.all()

   return jsonify ({
      "projects" : [project.serialized for project in projects]
   })

@app.route("/projects/<int:id>")
def getProjectById(id):
   return "need to implement"

if __name__ == '__main__':
   app.run(debug=True)
