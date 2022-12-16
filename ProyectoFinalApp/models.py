from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='profilePics/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
            return self.usuario.username
    
class Mensaje(models.Model):
        origen = models.ForeignKey(User, on_delete=models.CASCADE, related_name='origen')
        destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='destinatario')
        mensaje = models.TextField(max_length=1000, blank=True, null=True)
        actualizado = models.DateTimeField(auto_now=True)
        creado = models.DateTimeField(auto_now_add=True)
        
        def __str__(self):
                return self.mensaje

class Post(models.Model):
        titulo = models.CharField(max_length=300, blank=False, null=False)
        descripcion = models.CharField(max_length=100, blank=True, null=True)
        imagen = models.ImageField(upload_to='postImg/', blank=True, null=True)
        autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='autor')
        fechaCreacion = models.DateField(auto_now=False, auto_now_add=True)
        contenido = models.TextField(max_length=1000, blank=False, null=False)
        class Meta:
                verbose_name = 'Post'
                verbose_name_plural = 'Posts'
        
        def __str__(self):
                return self.titulo