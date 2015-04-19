from django.shortcuts import render
from django.http import HttpResponse

from os import listdir
from os.path import isfile, join

# Create your views here.


def home(request):
    return render(request, 'DetectionAnomalie/home.html')


def formulaire(request):
    return render(request, 'DetectionAnomalie/formulaire.html', {'files': files(), 'files_name': files_name()})


def files():
    file = [f for f in listdir("files/") if isfile(join("files/", f))]

    return file


def files_name():
    file = [f for f in listdir("files/name/") if isfile(join("files/name/", f))]

    array = []
    for fil in file:
        array.append(read_file("files/name/"+fil))
    return array


def read_file(path):
    fichier = open(path, 'r+')
    infos = fichier.read().split()
    return infos


def traiter(request):
    return render(request, 'DetectionAnomalie/affichage.html')
    #return HttpResponse("waiting for "+request.POST.get('files', 'derp')+" with "+request.POST.get('k', '0')+
    #                    " clusters and "+request.POST.get('N', '0')+" % error")