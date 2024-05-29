import os


#### Carpeta dataset ####
location = 'C:/Users/Luigui/Desktop/CERTUS/3.DataOPS/proyecto_parcial/python/dataset'

#### Validar si existe carpeta ####
if not os.path.exists(location): #Carpeta no exixte#
    ## Creo la carpeta ##
    os.mkdir(location)
else: ##Carpeta existe
    ## Borrar contenido ##
    for root, dirs, files in os.walk(location, topdown = False):
        for name in files:
            os.remove(os.path.join(root, name)) # Eliminar los archivos #
        for name in dirs:
            os.rmdir(os.path.join(root, name)) # Eliminar las carpetas #

#Importar libreria API Kaggle#
from kaggle.api.kaggle_api_extended import KaggleApi

#Autenticarnos en la API#
api = KaggleApi()
api.authenticate()

#Descargar DataSet#
#print(api.dataset_list(search=''))# Sirve para listar Datasets disponibles

#api.dataset_download_file('dem0nking/video-game-ratings-dataset','Video_Game_Information.csv',path=location,force=True,quiet=False)
#api.dataset_download_file('rahulvyasm/netflix-movies-and-tv-shows','netflix_titles.csv',path=location,force=True,quiet=False)
api.dataset_download_files('rahulvyasm/netflix-movies-and-tv-shows',path=location,force=True,quiet=False,unzip=True)