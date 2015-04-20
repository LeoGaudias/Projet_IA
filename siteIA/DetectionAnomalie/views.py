from django.shortcuts import render, redirect
from django.http import HttpResponse

from os import listdir
from os.path import isfile, join

from kmean import KMeanClusterer

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

    return array[0]


def read_file(path):
    fichier = open(path, 'r+')

    next(fichier)
    infos = []
    for line in fichier:
        infos.append(line.split(':')[0])

    return infos


def traiter(request):
    try:
        file = request.POST['files']
        N = int(request.POST['N'])
        k = int(request.POST['k'])

        kMeanClusterer = KMeanClusterer(k, "files/"+file, N)
        kMeanClusterer.performClustering()

        text = ""

        for obs in kMeanClusterer.getCluster(0).getObservations():
            for obj in obs:
                text += obj


    except(KeyError):
        return redirect('formulaire')

    #return render(request, 'DetectionAnomalie/affichage.html')
    return HttpResponse(text)