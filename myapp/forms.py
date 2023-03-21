from wtforms import Form, StringField, SubmitField, EmailField, PasswordField, validators, TextAreaField, DecimalRangeField, HiddenField

class LoginForm(Form):
    name = StringField('Nombre', [
        validators.DataRequired(message='El nombre es obligatorio'),
        validators.length(min=4, max=50, message='Excede los límites de este campo')
    ])
    username = StringField('Nombre de Usuario', [
        validators.DataRequired(message='El nombre de usuario es obligatorio'),
        validators.length(min=6, max=15, message='Excede los límites de este campo')
    ])
    email = EmailField('Email', [
        validators.DataRequired(message='El correo electrónico es obligatorio'),
        validators.Email('Tienes que proporcionar una dirección de correo electrónico'),
        validators.length(min=6, max=50, message='Excede los límites de este campo')
    ])
    password = PasswordField('Contraseña', [
        validators.DataRequired(message='Se necesita crear una contraseña'),
        validators.length(min=4, max=15, message='La contraseña debe tener mínimo 4 carácteres y máximo 15')
    ])

class ProductForm(Form):
    name = StringField('Nombre', [
        validators.DataRequired(message='El nombre es obligatorio'),
        validators.length(min=4, max=50, message='Excede los límites de este campo')
    ])
    short_desc = StringField('Descripción Corta', [
        validators.DataRequired(message='La descripción corta es obligatoria'),
        validators.length(min=4, max=50, message='Excede los límites de este campo')
    ])
    long_desc = TextAreaField('Descripción Larga', [
        validators.DataRequired(message='La descripción larga es obligatoria')
    ])
    category = StringField('Categoría', [
        validators.DataRequired(message='Categoría obligatoria'),
    ])
    photo_url = StringField('URL de Foto', [
        validators.DataRequired(message='URL de foto obligatoria')
    ])
    price = DecimalRangeField('Precio', [
        validators.DataRequired(message='Precio obligatorio')
    ])

class CategoryForm(Form):
    id = HiddenField("id")
    name = StringField('Nombre', [
        validators.DataRequired(message='El nombre es obligatorio'),
        validators.length(min=4, max=50, message='Excede los límites de este campo')
    ])