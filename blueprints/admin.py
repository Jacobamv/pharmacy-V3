from models import *

from flask import Blueprint, render_template, request, redirect, session


bp = Blueprint('admin', __name__ )

def check_session():
    if not 'username' in session:
        return redirect('/login/')


@bp.route('/', methods=['GET'])
def Get():
    check_session()

    return render_template('admin/index.html')
    
    
@bp.route('/pharmacies', methods = ['GET'])
def GetPharhmacies():
    check_session()

    networkid = session.get('networkid')
    pharm = Pharmacy.select().where(Pharmacy.network == networkid)
    return render_template('admin/pharmacylist.html', data=pharm, length=len(pharm))

# Выведение списка аптек (na-sa)
@bp.route('/drugs', methods=['GET'])
def GetDrugsNetwork():
    check_session()

    networks = Network.select()
    return render_template('admin/drugsNetwork.html', data=networks, length=len(networks))

# Вывод списка лекарств выбранной аптеки (na-sa)
@bp.route('drugs/show/<id>', methods=['GET'])
def GetDrugs(id):
    check_session()

    # Фильтрация по id сети аптеки
    drugs = Drugs.select().where(Drugs.network == id)
    return render_template('admin/drugsDrugs.html', data=drugs, length=len(drugs))