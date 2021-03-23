from werkzeug.utils import redirect
from models import *

from flask import Flask
from flask.globals import request, session
from blueprints.login import bp as LoginBlueprint
from blueprints.admin import bp as AdminBlueprint
from blueprints.pharm import bp as PharmBlueprint



app = Flask(__name__)
app.register_blueprint(LoginBlueprint, url_prefix='/login')
app.register_blueprint(AdminBlueprint, url_prefix='/admin')
app.register_blueprint(PharmBlueprint, url_prefix='/pharm')
app.config['SECRET_KEY'] = 'aoaoaoaooaoaoaoaoao'

@app.route('/')
def Hello():
    if not 'username' in session:
        return redirect('/login/')
    
    return redirect('/admin/')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5009',  debug=True)