from models import *

from flask import Flask
from blueprints.login import bp as LoginBlueprint
from blueprints.admin import bp as AdminBlueprint



app = Flask(__name__)
app.register_blueprint(LoginBlueprint, url_prefix='/login')
app.register_blueprint(AdminBlueprint, url_prefix='/admin')
app.config['SECRET_KEY'] = 'aoaoaoaooaoaoaoaoao'

@app.route('/')
def Hello():
    return "Hello WOrld"
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5009', debug=True)