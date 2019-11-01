from django.db import models
from image_cropping import ImageRatioField

# Definição do model 'Depoimento'
class Depoimento(models.Model):
    nome = models.CharField(max_length=35, null=False, default='Nome')
    profissao = models.CharField(max_length=70, null=False, default='Profissão')
    depoimento = models.TextField(max_length=560, null=False, default='Depoimento')
    alt = models.CharField(max_length=40, null=False, default='Descrição para o arquivo da foto')
    imagem = models.ImageField(upload_to='_galeria/_depoimentos/', blank=True)
    cropped = ImageRatioField('imagem', '150x150') # Campo que armazena as dimensões da imagem

    # Método que diz que cada model 'Depoimento' vai ser chamada pelo seu campo 'nome'
    def __str__(self):
        return self.nome

    # Método que busca o path da imagem, caso não encontre, retorna ""
    def get_image_path(self):
        try:
            return self.imagem.url
        except:
            return ""

# Definição do model 'Foto'
class Foto(models.Model):
    alt = models.CharField(max_length=40, null=False, default='Descrição para o arquivo da foto')
    imagem = models.ImageField(upload_to='_galeria/_fotos/', blank=True)
    cropped = ImageRatioField('imagem', '350x300') # Campo que armazena as dimensões da imagem

    # Método que diz que cada model 'Foto' vai ser chamada pelo seu campo 'alt'
    def __str__(self):
        return self.alt

    # Método que busca o path da imagem, caso não encontre, retorna ""
    def get_image_path(self):
        try:
            return self.imagem.url
        except:
            return ""