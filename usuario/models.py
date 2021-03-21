from django.db import models
# Create your models here.


class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    rg = models.CharField(max_length=15, blank=True)
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=255)
    celular = models.CharField(max_length=20)
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    cep = models.CharField(max_length=10)
    logradouro = models.CharField(max_length=150)
    complemento = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100)
    localidade = models.CharField(max_length=100,  verbose_name='Cidade')
    uf = models.CharField(
        max_length=2,
        default='',
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )

    def __str__(self):
        return f"{self.pk}"
