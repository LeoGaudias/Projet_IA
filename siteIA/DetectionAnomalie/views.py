from django.shortcuts import render, redirect
from django.http import HttpResponse

from os import listdir
from os.path import isfile, join

from DetectionAnomalie.kmean import KMeanClusterer
import json
from math import *

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

        values = []
        names = []
        for i in request.POST:
            if i not in ['N', 'k', 'files', 'csrfmiddlewaretoken']:
                values.append(i.split('p')[1])
                names.append(request.POST[i])

        kMeanClusterer = KMeanClusterer(k, "files/"+file, N, values)
        kMeanClusterer.performClustering()

        '''json_data = []
        for i in range(kMeanClusterer.getClusterNumber()):
            cluster = {'number': i, 'obs': kMeanClusterer.getCluster(i).getObservations()}
            json_data.append(cluster)

        tab = {'names': names, 'values': json_data}'''

        tab = []
        centroids = []
        nodes = []
        links = []
        total_obs = 0
        num_col = len(kMeanClusterer.getCluster(0).getCentroid())
        for i in range(kMeanClusterer.getClusterNumber()):
            tab_col_x = 0
            tab_col_y = 0
            for column in kMeanClusterer.getCluster(i).getCentroid():
                if num_col <= len(kMeanClusterer.getCluster(i).getCentroid())/2:
                    tab_col_x += trunc(pow(float(column), 2))
                else:
                    tab_col_y += trunc(pow(float(column), 2))
            centroids.append({'number': i, 'x': sqrt(tab_col_x), 'y': sqrt(tab_col_y)})
            num_obs = 0
            for obs in kMeanClusterer.getCluster(i).getObservations():
                tab_col_x = 0
                tab_col_y = 0

                for column in obs:
                    if num_col <= len(obs)/2:
                        tab_col_x += trunc(pow(float(column), 2))
                    else:
                        tab_col_y += trunc(pow(float(column), 2))
                tab.append({'number': i, 'x': sqrt(tab_col_x), 'y': sqrt(tab_col_y)})

                nodes.append({'name': 'obs '+str(num_obs), 'group': i})
                links.append({'source': total_obs + num_obs, 'target': total_obs+len(kMeanClusterer.getCluster(i).getObservations())+1, 'value': kMeanClusterer.computeDistance(obs, kMeanClusterer.getCluster(i).getCentroid())})
                num_obs += 1
            total_obs += len(kMeanClusterer.getCluster(i).getObservations())

            nodes.append({'names': 'centroid '+str(i), 'group': i})

        json1 = {'obs': tab, 'centroid': centroids}

        json2 = {'nodes': nodes, 'links': links}


        json_data = kMeanClusterer.extractValuesGraph()
        tab = {'names' : names, 'values' : json_data}

    except(KeyError):
        return redirect('formulaire')

    return render(request, 'DetectionAnomalie/affichage.html', {'tab': tab, 'json': json.dumps(json1), 'json2': json.dumps(json2)})
    #return render(request, 'DetectionAnomalie/affichage.html', tab)
    #return HttpResponse(request)
