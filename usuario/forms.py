from django import forms
from .models import Usuario
from django.core.validators import validate_email
import re


class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['nome', 'login', 'senha', 'rg', 'cpf', 'email', 'celular', 'data_nascimento',
                  'cep', 'logradouro', 'complemento', 'bairro',
                  'localidade', 'uf']

    def is_valid(self):

        valid = True

        if not super(UsuarioForm, self).is_valid():
            valid = False

        valid_senha = Usuario.objects.filter(senha=self.data['senha'])
        user_exists = Usuario.objects.filter(login=self.data['login']).exists()
        cpf_exists = Usuario.objects.filter(cpf=self.data['cpf']).exists()
        email_exists = Usuario.objects.filter(
            email=self.data['email']).exists()

        if user_exists:
            self.adiciona_erro('Usuário já existente')
            valid = False

        if cpf_exists:
            self.adiciona_erro('CPF já existente')
            valid = False

        if email_exists:
            self.adiciona_erro('E-mail já existente')
            valid = False

        return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(
            forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)
