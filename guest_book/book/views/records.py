from django.shortcuts import render, redirect, get_object_or_404


from book.models import Record, StatusChoices

from book.forms import RecordForm


def index_view(request):
    if request.method == 'GET':
        records = Record.objects.all().order_by('-created_at')
        form = RecordForm()
        context = {
            'records': records,
            'choices': StatusChoices.choices,
            'form': form
        }
        return render(request, 'index.html', context)


def add_record_view(request):
    form = RecordForm()
    if request.method == 'GET':
        context = {'form': form}
        return render(request, 'add_record.html', context)
    form = RecordForm(request.POST)
    if not form.is_valid():
        context = {
            'form': form
        }
        return render(request, 'add_record.html', context)
    record = Record.objects.create(**form.cleaned_data)
    return redirect('index')


def edit_record_view(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'GET':
        form = RecordForm(initial={
            'author_name': record.author_name,
            'author_email': record.author_email,
            'text': record.text,
        })
        return render(request, 'edit_record.html', context={'form': form, 'record': record})
    form = RecordForm(request.POST)
    if not form.is_valid():
        context = {
            'form': form,
            'record': record
        }
        return render(request, 'edit_record.html', context)
    record = Record.objects.filter(pk=pk).update(**form.cleaned_data)
    return redirect('index')


def delete_view(request, pk):
    record = get_object_or_404(Record, pk=pk)
    context = {
        'record': record
    }
    return render(request, 'delete_confirm.html', context)


def confirm_delete(request, pk):
    Record.objects.filter(pk=pk).update(
        status=StatusChoices.Неактивно)
    return redirect('index')
