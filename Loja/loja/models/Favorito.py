from django.db import models
from django.contrib.auth.models import User

class Favorito(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favoritos')
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'produto') # Evita duplicados para o mesmo usuário