from models import *

from flask import Blueprint, render_template, request, redirect, session

bp = Blueprint('admin', __name__ )

@bp.route('/', methods=['GET'])
def Get():
    if not 'username' in session:
        return redirect('/login/')
    return render_template('admin/index.html')
    
    
@bp.route('/pharmacy', methods = ['GET'])
def GetPharhmacies():
    if not 'username' in session:
        return redirect('/login/')
    networkid = session.get('networkid')
    pharm = Pharmacy.select().where(Pharmacy.network == networkid)
    return render_template('admin/pharmacylist.html', data=pharm, length=len(pharm))

@bp.route('/pharmacy/add', methods = ['GET'])
def AddPharmacy():
    if not 'username' in session:
        return redirect('/login/')
    return render_template('admin/pharmacy_add.html')

@bp.route('/pharmacy/add', methods = ['POST'])
def product_create():
    _name = request.form.get('name')
    _address = request.form.get('address')
    phar = Pharmacy(name = _name, network = 1, address=_address).save()
    return redirect('/admin/pharmacy')

@bp.route('pharmacy/edit/<id>')
def EditPharmacy(id):
    phar = Pharmacy.get(Pharmacy.id == id)
    return render_template('/admin/pharmacy_edit.html', phar=phar)

@bp.route('pharmacy/edit/<id>', methods = ['POST'])
def EditPharmacyPost(id):
    phar = Pharmacy.get(Pharmacy.id == id)
    phar.name = request.form['name']
    phar.address = request.form['address']
    phar.save()
    return redirect('/admin/pharmacy')


@bp.route('/pharmacy/<id>/departments')
def GetDepartments(id):
    dp = Department.select().where(Department.pharmacy == id)
    return render_template('/admin/department_list.html',data = dp, length=len(dp))