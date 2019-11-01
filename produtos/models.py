import uuid
import itertools
from django.db import models
from django.db.models import Q
from django.utils.text import slugify
from image_cropping import ImageRatioField
from embed_video.fields import EmbedVideoField

# Definição do model 'Produto'
class Produto(models.Model):
    nome = models.CharField(max_length=16, null=False, default='Nome do produto')
    detalhes_da_pagina_inicial = models.CharField(max_length=80, null=False, default='Detalhes que serão exibidos na página inicial')
    imagem_da_pagina_inicial = models.ImageField(upload_to='_galeria/_produtos/', blank=True)
    cropped = ImageRatioField('imagem_da_pagina_inicial', '286x180') # Campo que armazena as dimensões da imagem
    mostrar_na_pagina_inicial = models.BooleanField(default=True)
    video_em_gravacao = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, default=uuid.uuid4, max_length=255)
    detalhes = models.TextField(max_length=2000, null=False, default='Descrição do produto')
    preco = models.DecimalField(null=False, decimal_places=2, max_digits=6, default=0.00)
    link_video_demo = EmbedVideoField() # Campo do objeto EmbedVideo
    link_botao_de_compra = models.URLField(max_length=300, null=False, default='https://')

    # Método que diz que cada model 'Produto' vai ser chamada pelo seu campo 'nome'
    def __str__(self):
        return self.nome

    # Método que busca o path da imagem, caso não encontre, retorna ""
    def get_image_path(self):
        try:
            return self.imagem_da_pagina_inicial.url
        except:
            return ""

    # Método que realiza sucessivas verificações na slug do produto para que ela seja inicialmente
    # o título do produto "slugificado" (slugify) com alterações aleatórias caso haja outro produto
    # com uma slug semelhante.
    def save(self, *args, **kwargs):
        max_length = Produto._meta.get_field('slug').max_length
        self.slug = orig = slugify(self)[:max_length]

        for x in itertools.count(1):
            if self.id:
                if Produto.objects.filter(Q(slug=self.slug), Q(nome=self.nome), Q(id=self.id),).exists():
                    break
            if not Produto.objects.filter(slug=self.slug).exists():
                break

            # Truncate & Minus 1 for the hyphen.
            self.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)

        super(Produto, self).save(*args, **kwargs)