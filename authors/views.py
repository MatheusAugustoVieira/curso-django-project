from django.shortcuts import render
from .forms import RegisteForm

# Create your views here.
def register_view(request):
    if request.POST:
        form = RegisteForm(request.POST)
    else:
        form = RegisteForm()
    return render(request, 'authors/pages/register_view.html', {
        'form': form,
    })