import sys
import requests
import os
import shutil
from tqdm import tqdm
from bs4 import BeautifulSoup as bs


def telechargerChapitreManga(url, repertoire):
    """
        Telecharge toutes les pages d'un chapitre donne par son url `url` et 
        stocke les pages dans le repertoire `repertoire`
    """
    ### Creation du repertoire sous la forme nomManga/numChapitre ###
    os.makedirs(repertoire)
    ##############################
    j=1
    continu = True
    while continu:
        urlfinal= url + str(j)
        ### Extraction de l'url de l'image dans l'url donne en parametre ###
        reponse1=requests.get(urlfinal)
        if reponse1.ok:
            soup = bs(reponse1.content, "html.parser")
            for img in tqdm(soup.find_all("img"), "Extracting images"):
                img_url = img.attrs.get("src")

                if not img_url or "mangapanda.com/" not in img_url:
                    # Donc ce n'est pas la photo du manga
                    continue
            ###############################################

            reponse2 = requests.get(img_url, stream=True)
            reponse2.raw.decode_content = True 

            ### Nom du fichier ###
            ext= str(j) + ".jpg"
            filename = os.path.join(repertoire, ext )
            ######################
            with open(filename, "wb") as f:
                shutil.copyfileobj(reponse2.raw, f)
            j += 1
        else:
            continu = False
       

urlSite = "https://www.mangapanda.com/"
urls = list()
if len(sys.argv) < 3:
    sys.exit("Ce programme nécessite 2 arguments")
else:
    #recuperation du nom du manga 
    nomManga = sys.argv[1].lower()
    #On concatène le nom du manga à l'url du site
    urlSite = urlSite + nomManga 
    if "," in sys.argv[2]:
        chapitres = sys.argv[2].split(',')
        for chapitre in chapitres:
            #On ajoute les différents chapitres donnés en paramètre
            urls.append(urlSite + "/" + chapitre + "/")
    else:
        if "-" in sys.argv[2]:
            chapitres = sys.argv[2].split("-")
            #On ajoute les différents chapitres donnés en paramètre
            for chapitre in range(int( chapitres[0] ) , int( chapitres[1] ) + 1 ):           
                urls.append(urlSite + "/" + str(chapitre) + "/")
        else:
            #Dans ce cas on a un seul chapitre donne en parametre
            urls.append( urlSite + "/" + sys.argv[2] + "/")
    
testManga = requests.get(urlSite)
if testManga.ok: ### Le manga donne en parametre existe ###
    ##Telechargement des differents chapitres
    for url in urls:
            #pour obtenir le chemin d'un repertoire on enleve le debut jusqu'a ".com/"
            #ainsi le nom du repertoire sera le 2e element de la liste retournee par url.split('.com/')
        telechargerChapitreManga( url, url.split(".com/")[1] )

    print("Téléchargement reussi!")
else:
    sys.exit("Ce manga n'existe pas!")


