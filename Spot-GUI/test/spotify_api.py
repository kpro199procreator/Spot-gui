# spotify_api.py
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Tus claves de Spotify
CLIENT_ID = "f4c5e329458f4053801b0d87e7d89579"
CLIENT_SECRET = "507cb5a339fb4acdb8658bcd22d6ea5f"

# Autenticación
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)


def buscar(query: str, limit: int = 10):
    """Busca canciones, álbumes, playlists y podcasts."""
    try:
        resultados = sp.search(q=query, type="track,album,playlist,show", limit=limit)

        datos = {
            "tracks": [],
            "albums": [],
            "playlists": [],
            "shows": [],
        }

        for track in resultados.get("tracks", {}).get("items", []):
            if track:
                datos["tracks"].append({
                    "tipo": "track",
                    "titulo": track.get("name", "Desconocido"),
                    "artista": ", ".join([a.get("name", "Artista desconocido") for a in track.get("artists", [])]),
                    "imagen": track.get("album", {}).get("images", [{}])[0].get("url", None),
                    "url": track.get("external_urls", {}).get("spotify", "")
                })

        for album in resultados.get("albums", {}).get("items", []):
            if album:
                datos["albums"].append({
                    "tipo": "album",
                    "titulo": album.get("name", "Desconocido"),
                    "artista": ", ".join([a.get("name", "Artista desconocido") for a in album.get("artists", [])]),
                    "imagen": album.get("images", [{}])[0].get("url", None),
                    "url": album.get("external_urls", {}).get("spotify", "")
                })

        for playlist in resultados.get("playlists", {}).get("items", []):
            if playlist:
                datos["playlists"].append({
                    "tipo": "playlist",
                    "titulo": playlist.get("name", "Desconocido"),
                    "artista": playlist.get("owner", {}).get("display_name", "Desconocido"),
                    "imagen": playlist.get("images", [{}])[0].get("url", None),
                    "url": playlist.get("external_urls", {}).get("spotify", "")
                })

        for show in resultados.get("shows", {}).get("items", []):
            if show:
                datos["shows"].append({
                    "tipo": "podcast",
                    "titulo": show.get("name", "Desconocido"),
                    "artista": show.get("publisher", "Desconocido"),
                    "imagen": show.get("images", [{}])[0].get("url", None),
                    "url": show.get("external_urls", {}).get("spotify", "")
                })

        return datos

    except Exception as e:
        print(f"[ERROR] No se pudo buscar en Spotify: {e}")
        return {
            "tracks": [],
            "albums": [],
            "playlists": [],
            "shows": [],
        }
