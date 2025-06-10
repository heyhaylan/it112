from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm

def index(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guestbook:index')
    else:
        form = EntryForm()

    entries = Entry.objects.order_by('-timestamp')
    return render(request, 'guestbook/index.html', {'form': form, 'entries': entries})
