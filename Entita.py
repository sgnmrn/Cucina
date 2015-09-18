__author__ = 'marino'

DEFAULT_USER_NAME = 'anonimo'


class Utente():

    def __init__(self, nome, pwd):
        self.nome = nome
        self.pwd = pwd

class Cinema():
     def __init__(self, nome):
        self.nome = nome


class Film():
    def __init__(self, titolo):
        self.titolo = titolo

def creaRecensione(login , passwd , title , cine, rat, commento):
    # recupera user
    ute = Utente.query(Utente.nome == login).get()
    if ute:
        if ute.password != passwd:
            return ute.nome, 'password errata'
        ute = ute.key
    else:
        ute = Utente(nome=login,password=passwd).put()
    mov = Film.query(Film.titolo == title).get()
    if mov:
        mov = mov.key
    else:
        mov = Film(titolo=title).put()
    cin = Cinema.query(Cinema.nome == cine).get()
    if cin:
        cin = cin.key
    else:
        cin = Cinema(nome =cine).put()
    rece= Recensione(author=ute, movie = mov, cinema=cin, rating = rat,testo=commento).put()
    return 'inserito', 'rece'


class Recensione():

    def __init__(self, author ,movie ,cinema ,rating ,testo ,date):
        self.author =author
        self.movie = movie
        self.cinema = cinema
        self.rating = rating
        self.testo = testo
        self.date = date

    def __str__(self):
        return self.testo #str(self.author)
