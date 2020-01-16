import sys
import os


urlSite = "https://www.mangapanda.com/"
urls = list()
chemins = list()
if len(sys.argv) < 3:
    sys.exit("Ce programme nécessite au moins 2 arguments")
else:
    #recuperation du nom du manga 
    nomManga = sys.argv[1].lower()
    #On concatène le nom du manga à l'url du site
    urlSite = urlSite + nomManga + "/"
    if "," in sys.argv[2]:
        chapitres = sys.argv[2].split(',')
        for chapitre in chapitres:
            #On ajoute les différents chapitres donnés en paramètre
            urls.append(urlSite + chapitre + "/")
    else:
        if "-" in sys.argv[2]:
            chapitres = sys.argv[2].split("-")
            #On ajoute les différents chapitres donnés en paramètre
            for chapitre in range(int( chapitres[0] ) , int( chapitres[1] ) + 1 ):           
                urls.append(urlSite + str(chapitre) + "/")
        else:
            #Dans ce cas on a un seul chapitre donne en parametre
            urls.append( urlSite + sys.argv[2] + "/")

