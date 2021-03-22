from models import *

from flask import Blueprint, render_template, request, redirect, session


bp = Blueprint('admin', __name__ )


@bp.route('/', methods=['GET'])
def Get():
    if not 'username' in session:
        return redirect('/login/')
    return render_template('admin/index.html')
    
    
@bp.route('/pharmacies', methods = ['GET'])
def GetPharhmacies():
    if not 'username' in session:
        return redirect('/login/')

    networkid = session.get('networkid')
    pharm = Pharmacy.select().where(Pharmacy.network == networkid)
    return render_template('admin/pharmacylist.html', data=pharm, length=len(pharm))