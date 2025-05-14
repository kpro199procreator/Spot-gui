import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = "f4c5e329458f4053801b0d87e7d89579"
client_secret = "507cb5a339fb4acdb8658bcd22d6ea5f"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

def buscar(query):
    resultados = {"canciones": [], "albums": [], "playlists": []}
    if not query: return resultados

    try:
        tracks = sp.search(q=query, type="track", limit=5)
        for item in tracks["tracks"]["items"]:
            resultados["canciones"].append({
                "tipo": "track",
                "titulo": item["name"],
                "artista": item["artists"][0]["name"],
                "imagen": item["album"]["images"][0]["url"] if item["album"]["images"] else None,
                "url": item["external_urls"]["spotify"]
            })

        albums = sp.search(q=query, type="album", limit=3)
        for item in albums["albums"]["items"]:
            resultados["albums"].append({
                "tipo": "album",
                "titulo": item["name"],
                "artista": item["artists"][0]["name"],
                "imagen": item["images"][0]["url"] if item["images"] else None,
                "url": item["external_urls"]["spotify"]
            })

        playlists = sp.search(q=query, type="playlist", limit=2)
        for item in playlists["playlists"]["items"]:
            resultados["playlists"].append({
                "tipo": "playlist",
                "titulo": item["name"],
                "artista": item["owner"]["display_name"],
                "imagen": item["images"][0]["url"] if item["images"] else None,
                "url": item["external_urls"]["spotify"]
            })

    except Exception as e:
        print("Error en búsqueda:", e)

    return resultados
