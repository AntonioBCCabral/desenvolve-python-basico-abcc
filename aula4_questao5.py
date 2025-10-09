#A extensão ".csv" significa "comma-separated values" ou "valores separados por vírgula".
# É a extensão utilizada por sistemas de gerência de tabelas como o Microsoft Excel ou
# Google Sheets. Nesse exercício vamos criar uma planilha com dados sobre livros que você já leu
# ou gostaria de ler. Siga as instruções.

# Selecione pelo menos 10 livros que você leu ou gostaria de ler. Você deve reunir
# as seguintes informações: título, autor, ano de publicação e número de páginas.
# No Python, crie um arquivo chamado "meus_livros.csv", aberto para escrita.
# Na primeira linha escreva os títulos da planilha separados por vírgula (sem espaço em branco).
# Os títulos são: "Título", "Autor", "Ano de publicação" e "Número de páginas".
# Lembre de finalizar a linha com uma quebra de linha.
# A partir da segunda linha escreva as informações de cada livro que você levantou,
# separando cada informação por uma vírgula (sem espaço em branco).
# Lembre de finalizar cada linha com uma quebra de linha.
# Feche o arquivo para salvá-lo e abra com a ferramenta de planilhas de sua escolha.
# Como você já tem conta no Google, sugiro abrir com o Google Sheets.
# Seu arquivo deve ser aberto como uma planilha parecida com essa:
# Título             Autor                Ano de publicação  Número de páginas
# O Caçador de Pipas Khaled Hosseini      2003               368
# Torto Arado        Itamar Vieira Junior 2019               264

import os
import random
# Criar o arquivo meus_livros.csv e escrever os dados dos livros
with open("meus_livros.csv", "w") as arquivo:
    arquivo.write("Título          da          Obra,Nome    do    Autor,Ano   de   publicação,Número   de   páginas\n")
    arquivo.write("Ascensão e Queda do III Reich,William L. Shirer,1975,1600\n")
    arquivo.write("Les Misérables,Victor Hugo,1973,1910\n")
    arquivo.write("1984,George Orwell,1949,328\n")
    arquivo.write("O Estado no Estado,Benício Cabral,2021,239\n")
    arquivo.write("Grande Sertão: Veredas,João Guimarães Rosa,1956,496\n")
    arquivo.write("Cem Anos de Solidão,Gabriel García Márquez,1967,417\n")
    arquivo.write("A Metamorfose,Franz Kafka,1915,201\n")
    arquivo.write("O Pequeno Príncipe,Antoine de Saint-Exupéry,1943,96\n")
    arquivo.write("Memórias Póstumas de Brás Cubas,Machado de Assis,1881,216\n")
    arquivo.write("Sapiens,Yuval Noah Harari,2018,459\n")
# Fechar o arquivo
arquivo.close()
# Agora abra o arquivo "meus_livros.csv" com a ferramenta de planilhas de sua escolha.



