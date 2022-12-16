from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from pkg_resources import require
from ProyectoFinalApp.models import *

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Usuario', max_length=100, required=True)
    email = forms.EmailField(label='Email', required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        
class UserEditForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=100, required=True)
    email = forms.EmailField(label='Email')
    class Meta:
        model = User
        fields = ['username','email']
        
class AvatarForm(forms.Form):
    imagen = forms.ImageField(label='Imagen', required=False)
    bio = forms.CharField(label = 'Bio', required = False, widget=forms.Textarea)
    class Meta:
        model = Avatar
        fields = ['bio', 'imagen']
        
class CrearMensajeForm(forms.Form):
    destinatario = forms.EmailField(label='Email', required=True, 
                                    widget=forms.Select(choices=[('', 'Seleccione un destinatario')] + 
                                    [(user.email, user.email) for user in User.objects.all()]))
    mensaje = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea)
    
class PostForm(forms.Form):
    titulo = forms.CharField(label='Titulo', required=True)
    descripcion = forms.CharField(label='Descripcion', required=True)
    imagen = forms.ImageField(label='Imagen', required=False)
    contenido = forms.CharField(label='Contenido', widget=forms.Textarea, required=True)
    
    class Meta:
        model=Post
        fields=['titulo', 'descripcion', 'imagen', 'contenido']
        