from spotify_api import buscar

resultados = buscar("milo j")

for tipo, lista in resultados.items():
    print(f"\n== {tipo.upper()} ==")
    for item in lista:
        print(f"{item['titulo']} - {item['artista']} ({item['url']})")
