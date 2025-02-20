from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    nota1 = models.DecimalField(max_digits=5, decimal_places=1)
    nota2 = models.DecimalField(max_digits=5, decimal_places=1)
    nota3 = models.DecimalField(max_digits=5, decimal_places=1)
    nota4 = models.DecimalField(max_digits=5, decimal_places=1)
    media = models.DecimalField(max_digits=5, decimal_places=1, editable=False)
    situacao = models.CharField(max_length=10, editable=False)

    def save(self, *args, **kwargs):
        # Calculando a média
        self.media = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4
        # Definindo a situação
        if self.media >= 6.0:
            self.situacao = 'APROVADO'
        else:
            self.situacao = 'REPROVADO'
        super(Aluno, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome
