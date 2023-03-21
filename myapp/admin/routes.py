from flask import Flask, Blueprint, render_template, request, url_for, redirect
from flask_login import current_user
from models import Categories, Products, db
import forms

admin = Blueprint('admin', __name__)

#----------------------RUTAS-------------------------------------------------------------------------------------------------------------------------------------#

@admin.route('/admin/index', methods=['GET'])
def get_products():
    products_Form = forms.ProductForm(request.form)
    productos = Products.query.all()
    categorias = Categories.query.all()
    return render_template('admin_index.html', name = 'Admin', user = current_user, productos = productos, categorias = categorias, form = products_Form)

#Categorías
@admin.route('/admin/categorias', methods=['GET'])
def get_category():
    categories_form = forms.CategoryForm(request.form)
    categorias = Categories.query.all()
    return render_template('admin_category.html', name = 'Admin', user = current_user, categorias = categorias, form = categories_form)

@admin.route('/admin/register/categoria', methods=['POST'])
def register_category():
    categories_form = forms.CategoryForm(request.form)
    catego = Categories(
        name = categories_form.name.data
    )
    db.session.add(catego)
    db.session.commit()
    return redirect(url_for('admin.get_category'))

@admin.route('/admin/update/categoria', methods=['POST'])
def update_category():
    categories_form = forms.CategoryForm(request.form)
    categoria = db.session.query(Categories).filter(Categories.id == request.form.get('id')).first()
    categoria.name = categories_form.name.data
    db.session.add(categoria)
    db.session.commit()
    return redirect(url_for('admin.get_category'))

@admin.route('/admin/delete/categoria', methods=['POST'])
def delete_category():
    categories_form = forms.CategoryForm(request.form)
    categoria = db.session.query(Categories).filter(Categories.id == request.form.get('id')).first()
    categoria.name = categories_form.name
    db.session.delete(categoria)
    db.session.commit()
    return redirect(url_for('admin.get_category'))