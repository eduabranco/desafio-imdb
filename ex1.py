import csv
from imdb import Cinemagoer

ia = Cinemagoer()

columns=['imdbID','title','year','genres','kind']
lista_filmes=[['20880628'],['10872600'],['3501632'],['9419884'],['7131622']]

for i in range(len(lista_filmes)):
    search=ia.get_movie(lista_filmes[i][0])
    for j in range(1,len(columns)):
        dados=search.data[columns[j]]
        if columns[j]=='genres':dados=', '.join(dados)
        if columns[j]=='kind':dados=dados.capitalize()
        lista_filmes[i].append(dados)

for i in range(1, len(columns)): columns[i]=columns[i].capitalize()

with open('dados-de-filmes.csv','w') as f:
    write=csv.writer(f)
    write.writerow(columns)
    write.writerows(lista_filmes)