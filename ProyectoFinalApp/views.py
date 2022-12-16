from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .models import *
from ProyectoFinalApp.forms import *

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, r'ProyectoFinalApp\inicio.html', {})

def about(request):
    return render(request, r'ProyectoFinalApp\about.html', {})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contra)
            
            if user is not None:
                login(request, user)
                return render(request, 'ProyectoFinalApp\inicio.html', {'mensaje':f'Bienvenido {usuario}'})
            
            else:
                return render(request, 'ProyectoFinalApp\inicio.html', {'mensaje': 'Error, datos incorrectos'})
            
        else:
            return render(request, 'ProyectoFinalApp\inicio.html', {'mensaje': 'Error, formulario incorrecto'})
    
    form = AuthenticationForm()
    return render(request, 'ProyectoFinalApp\login.html', {'form':form})
    

def registro(request):
    
    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            informacion = form.cleaned_data
            username = informacion.get('username')
            password = informacion.get('password1')
            
            form.save()
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                return redirect('login')
            
        return render(request, r'ProyectoFinalApp\registro.html', {'form':form})
    
    form = UserRegisterForm()

    return render(request, r'ProyectoFinalApp\registro.html', {'form':form})

def logout_request(request):
    logout(request)
    return redirect('inicio')

@login_required
def editarPerfil(request):
    
    user = request.user
    
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user.username = informacion['username']
            user.email = informacion['email']
            user.save()
            return redirect('inicio')
    else:
        form = UserEditForm(initial={"email":user.email, "username":user.username})
    
    return render(request, r'ProyectoFinalApp\editar-perfil.html', {'form':form})
    
@login_required
def aregarAvatar(request):
    
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            avatar = Avatar(usuario=user, bio=form.cleaned_data['bio'], imagen=form.cleaned_data['imagen'])
            avatar.save()
            return redirect('inicio')
    else:
        form = AvatarForm()
        
    return render(request, r'ProyectoFinalApp\agregar-avatar.html', {'form':form})

@login_required
def enviarMensaje(request):
    if request.method == 'POST':
        form = CrearMensajeForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            mensaje = Mensaje(origen=request.user, destinatario=User.objects.get(email=informacion["destinatario"]), 
                              mensaje = informacion["mensaje"])
            mensaje.save()
            messages.success(request, "Mensaje enviado!")
            return redirect('inicio')
        else:
            messages.success(request, "Mensaje no enviado, error")
            return redirect('inicio')
    else:
        form = CrearMensajeForm()
        return render(request, r'ProyectoFinalApp\enviar-mensaje.html', {'form':form})
    
@login_required
def bandejaEntrada(request):
    user = request.user
    mensajes = Mensaje.objects.filter(destinatario=user)
    
    
    return render(request, r'ProyectoFinalApp\bandeja-entrada.html', {'mensajes':mensajes})
        

@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            info = form.cleaned_data
            post = Post(autor=user, titulo=info['titulo'], descripcion=info['descripcion'], 
                        imagen=info['imagen'], contenido=info['contenido'])
            
            post.save()
            
            return redirect('listado de posts')

        return render(request, r'ProyectoFinalApp\crear-post.html', {'form':form})
            
    form = PostForm()
    
    return render(request, r'ProyectoFinalApp\crear-post.html', {'form':form})

def todos_posts(request):
    post = Post.objects.all()
    return render(request, r'ProyectoFinalApp\listado-posts.html', {'posts':post})

@login_required
def perfil(request):
    return render(request, r'ProyectoFinalApp\perfil.html', {})

@login_required
def avatar(request):
    return render(request, r'ProyectoFinalApp\avatar.html', {})

@login_required
def editar_avatar(request):
    user = request.user
    
    avt = Avatar.objects.filter(usuario=user)

    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            info = form.cleaned_data
            avt.bio = info['bio']
            avt.imagen = info['imagen']
            avt.save()
            return redirect('inicio')
    form = AvatarForm(initial={'bio':avt.bio, 'imagen':avt.imagen})
    
    return render(request, r'ProyectoFinalApp\editar-avatar.html', {'form':form})

@login_required
def eliminar_avatar(request):
    return render(request, r'ProyectoFinalApp\eliminar-avatar.html', {})