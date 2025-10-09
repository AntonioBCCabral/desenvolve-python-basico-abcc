# Vamos descobrir as músicas mais populares do Spotify nos últimos 10 anos! 
# Abrir o arquivo spotify-2023.csv e ler os dados
import os
import random
with open("spotify-2023.csv", "r", encoding="latin-1") as arquivo:
    linhas = arquivo.readlines()
# Abrir o arquivo para leitura só até a linha 10
    dados = [linha.strip().split(",") for linha in linhas[0:11:]]
    print(dados)
# Filtrar as 10 músicas mais tocadas entre 2012 e 2022
# Apenas track_name, artist_name, artist_count, release_date, streams
    musicas_filtradas = []
    for linha in dados[1:]:
        ano = int(linha[4].split("-")[0])
        if 2012 <= ano <= 2022:
            musica = {
                "track_name": linha[1],
                "artist_name": linha[2],
                "artist_count": linha[3],
                "release_date": linha[4],
                "streams": int(linha[5])
            }
            musicas_filtradas.append(musica)
# Criar um arquivo chamado top10_musicas_spotify.csv e escrever os dados filtrados
with open("top10_musicas_spotify.csv", "w", encoding="latin-1") as arquivo_saida:
    arquivo_saida.write("track_name,artist_name,artist_count,release_date,streams\n")
    for musica in musicas_filtradas:
        linha = f"{musica['track_name']},{musica['artist_name']},{musica['artist_count']},{musica['release_date']},{musica['streams']}\n"
        arquivo_saida.write(linha)
    

