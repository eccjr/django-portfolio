from django.shortcuts import render
from django.contrib import messages
from django.core import mail
from django.core.mail import EmailMessage, BadHeaderError, get_connection
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from produtos.models import Produto
from .models import Depoimento, Foto


# Define a view da página inicial
def home_page(request):
    # Define as variáveis com os respectivos objetos necessários
    products = Produto.objects.filter(mostrar_na_pagina_inicial = True)
    reviews = Depoimento.objects.all()
    images = Foto.objects.all()

    # Configurações do form de contato
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                sender_name = form.cleaned_data['name']
                sender_email = form.cleaned_data['email']
                message = "{0} te enviou a seguinte mensagem:\n\n{1}\n\nResponda pelo email {2}".format(sender_name, form.cleaned_data['message'], sender_email)
                connection = mail.get_connection()
                connection.open()
                email = EmailMessage('Nova mensagem - www.website.com', message, 'no_reply@eccjr.com.br', ['a@a.com'], connection=connection)
                email.send()
                connection.close()
            except BadHeaderError:
                messages.error('Cabeçalho inválido!')
            messages.success(resquest, 'Obrigado por entrar em contato!')

    # Salva essas variáveis em um dicionário 'context'
    context = {
        'products': products,
        'reviews': reviews,
        'images': images,
        'form': form,
    }

    # Renderiza a página do site passando 'context'
    return render(request, 'index.html', context)

