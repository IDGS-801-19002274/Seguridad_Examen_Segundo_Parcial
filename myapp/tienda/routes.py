from flask import Blueprint, render_template, request
from flask_login import current_user

tienda = Blueprint('tienda', __name__)

#----------------------RUTAS-------------------------------------------------------------------------------------------------------------------------------------#

@tienda.route('/tienda/index', methods=['GET'])
def index():
    tienda = [  "https://picsum.photos/500/500",  "https://picsum.photos/800/600",  "https://picsum.photos/700/900"]
    return render_template('index.html', name = 'Inicio', user=current_user, images = tienda, want_footer = True)
