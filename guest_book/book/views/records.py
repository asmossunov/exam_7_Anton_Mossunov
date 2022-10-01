from django.shortcuts import render, redirect, get_object_or_404


from book.models import Record, StatusChoices

from book.forms import RecordForm, FindForm


def index_view(request):
    if request.method == 'GET':
        records = Record.objects.filter(status='ACTIVE').order_by('-created_at')
        form = RecordForm()
        find_form = FindForm()
        context = {
            'records': records,
            'choices': StatusChoices.choices,
            'find_form': find_form,
            'form': form
        }
        return render(request, 'index.html', context)


def add_record_view(request):
    form = RecordForm(request.POST)
    if not form.is_valid():
        records = Record.objects.filter(status='ACTIVE').order_by('-created_at')
        find_form = FindForm()
        context = {
            'records': records,
            'choices': StatusChoices.choices,
            'find_form': find_form,
            'form': form
        }
        return render(request, 'index.html', context)
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


def find_view(request):
    if request.POST.get('author_name'):
        author_name = request.POST.get('author_name')
        records = Record.objects.filter(author_name=author_name)
        if records:
            form = RecordForm()
            find_form = FindForm()
            context = {
                'records': records,
                'choices': StatusChoices.choices,
                'find_form': find_form,
                'form': form
            }
            return render(request, 'index.html', context)
        else:
            form = RecordForm()
            find_form = FindForm()
            context = {
                'answer': 'записи этого автора не найдены!',
                'choices': StatusChoices.choices,
                'find_form': find_form,
                'form': form
            }
        return render(request, 'index.html', context)
