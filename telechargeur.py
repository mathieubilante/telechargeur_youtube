from pytubefix import YouTube
from pytubefix.cli import on_progress
url = input("Enter le lien video youtube: ")
print("Telechargement en cours...")
print("\n")
youtube_lien=YouTube(url, on_progress_callback=on_progress)
#affichade des truc du lien 
print("Titre: ", youtube_lien.title)
print("Auteur: ", youtube_lien.author)
print("Nombre de vues: ", youtube_lien.views)
print("Durée: ", youtube_lien.length, "secondes")
print("Description: ", youtube_lien.description)
print("\n")
stream = youtube_lien.streams.get_highest_resolution()
stream.download()
print("Telechargement terminé!")


