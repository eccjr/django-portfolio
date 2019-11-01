from django.shortcuts import render, get_object_or_404
from .models import Produto

# Define a view da página do produto em português
def product_details(request, slug):
    # Define as variáveis com os respectivos objetos necessários
    product = get_object_or_404(Produto, slug=slug)

    # Salva essas variáveis em um dicionário 'context'
    context = {
        'product' : product
    }

    # Renderiza a página do site passando 'context'
    return render(request, 'product_br.html', context)
