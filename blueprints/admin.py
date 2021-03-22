from models import *

from flask import Blueprint, render_template, request, redirect, session


bp = Blueprint('admin', __name__ )



@bp.route('/', methods=['GET'])
def Get():
    return render_template('admin/index.html')
    
    
@bp.route('/pharmacies', methods = ['GET'])
def GetPharhmacies():
    pharm = Pharmacy.select()
    return render_template('admin/pharmacylist.html', ph)