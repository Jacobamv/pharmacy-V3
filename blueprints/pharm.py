from models import *

from flask import Blueprint, render_template, request, redirect, session


bp = Blueprint('pharm', __name__ )



@bp.route('/', methods=['GET'])
def Get():
    return 'Вы в странице аптекаря'