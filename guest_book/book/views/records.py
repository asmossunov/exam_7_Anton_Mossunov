from django.shortcuts import render, redirect, get_object_or_404


from book.models import Record, StatusChoices

# from market.forms import ProductForm


def index_view(request):
    if request.method == 'GET':
        # products = Product.objects.all()
        records = Record.objects.all().order_by('-created_at')
        context = {
            'records': records,
            'choices': StatusChoices.choices
        }
        return render(request, 'index.html', context)
