from django.db import models
from django.core.exceptions import ValidationError
class Tarefa(models.Model):
    STATUS_CHOISES = [
        ('PENDENTE', 'pendente'),
        ('CONCLUIDA', 'concluida'),
    ]

    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    status = models.CharField(
        max_length = 10,
        choices = STATUS_CHOISES,
        default = 'PENDENTE'
    )
    
    criada_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.tituto
    
    def clean(self):
        if len(self.titulo.strip()) < 3:
            raise ValidationError('o titulo deve conter mais de 3 caracteres')