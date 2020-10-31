import urllib.request, os
from api.models import User, Comment, Genre, Movie, CommentPage
from django.core.files import File

genres = ['Adventure', 'Action', 'Animation', 'Comedy', 'Drama', 'Fantasy', 'Family', 'Science Fiction', 'Spy',
          'Superhero', 'Mystery', 'War', 'Thriller']
movies = [
    {
        'title': 'Peter Rabbit 2',
        'release_date': '27th Mar 2020',
        'director': 'Will Gluck',
        'cast': 'James Corden, Margot Robbie, Rose Byrne, Domhnall Gleeson',
        'background': 'http://127.0.0.1:8000/media/images/movie_backgrounds/1.jpg',
        'poster': 'http://127.0.0.1:8000/media/images/movie_posters/1.jpg',
        'synopsis': 'Peter Rabbit and his bunny buddies are back, along with Bea and new husband Thomas McGregor. ' +
                    'But Peter is tired of his reputation for mischief and runs away from the'
                    + ' countryside where he bumps into an old, adventure-loving friend of his father’s. ' +
                    'James Corden, Rose Byrne, Margot Robbie, and Domhnall Gleeson reprise their roles in ' +
                    'this funny new part-animated adventure, directed by Will Gluck, ' +
                    'based on the stories by Beatrix Potter.',
        'genres': ['Family', 'Animation', 'Adventure', 'Fantasy', 'Comedy', 'Action']
    },
    {
        'title': 'Mulan',
        'background': 'http://127.0.0.1:8000/media/images/movie_backgrounds/2.jpg',
        'poster': 'http://127.0.0.1:8000/media/images/movie_posters/2.jpg',
        'release_date': '27th Mar 2020',
        'director': 'Niki Caro',
        'cast': 'Yifei Liu',
        'synopsis': 'When the Emperor of China issues a decree that one man per family must' +
                    ' serve in the Imperial Army to defend the ' +
                    'country from Northern invaders, Hua Mulan,' +
                    ' the eldest daughter of an honored warrior, steps in to take the place of her ailing father.' +
                    ' Masquerading as a man, Hua Jun, she is tested every step of the way and must harness her ' +
                    'inner-strength and embrace her true potential. It is an epic journey that will ' +
                    'transform her into an honored warrior and earn her the respect of a grateful nation...' +
                    ' and a proud father. "Mulan" features a celebrated international cast that ' +
                    'includes: Yifei Liu as Mulan; Donnie Yen as Commander Tung; Jason Scott Lee as Bori' +
                    ' Khan; Yoson An as Cheng Honghui; with Gong Li as Xianniang and Jet Li as the Emperor. The film ' +
                    'is directed by Niki Caro from a screenplay by Rick Jaffa & Amanda Silver and Elizabeth Martin &' +
                    ' Lauren Hynek based on the narrative poem "The Ballad of Mulan.',
        'genres': ['Animation', 'War', 'Family', 'Drama']
    },
    {
        'title': 'Black Widow',
        'background': 'http://127.0.0.1:8000/media/images/movie_backgrounds/3.jpg',
        'poster': 'http://127.0.0.1:8000/media/images/movie_posters/3.jpg',
        'release_date': '1st May 2020',
        'director': 'Cate Shortland',
        'cast': 'Scarlett Johansson, Rachel Weisz, FLorence Pugh, David Harbour',
        'synopsis': 'At birth the Black Widow (aka Natasha Romanova) is given to the KGB, ' +
                    'which grooms her to become its ultimate operative. When the U.S.S.R. breaks up, ' +
                    'the government tries to kill her as the action moves to present-day New York,' +
                    ' where she is a freelance operative.',
        'genres': ['Action', 'Superhero', 'Science Fiction', 'Fantasy', 'Adventure'],
    },
    {
        'title': 'Wonder Woman 1984',
        'background': 'http://127.0.0.1:8000/media/images/movie_backgrounds/4.jpg',
        'poster': 'http://127.0.0.1:8000/media/images/movie_posters/4.jpg',
        'release_date': '1st May 2020',
        'director': 'Patty Jenkins',
        'cast': 'Gal Gadot, Chris Pine, Connie Nielsen, Kristen Wiig, Pedro Pascal',
        'synopsis': 'Wonder Woman squares off against the Cheetah,' +
                    ' a villainess who possesses superhuman strength and agility.',
        'genres': ['Action', 'Superhero', 'Fantasy', 'Adventure'],
    },
    {
        'title': 'Soul',
        'background': 'http://127.0.0.1:8000/media/images/movie_backgrounds/5.jpg',
        'poster': '',
        'release_date': '19th Jun 2020',
        'director': 'Pete Docter',
        'cast': 'Jamie Foxx, Tina Fey, Questlove, Phylicia Rashad',
        'synopsis': 'Joe is a middle-school band teacher whose life hasnt quite ' +
                    'gone the way he expected. His true passion is jazz -- and hes good. But ' +
                    'when he travels to another realm to help someone find their passion, he soon discovers ' +
                    'what it means to have soul.',
        'genres': ['Animation', 'Comedy', 'Drama', 'Adventure', 'Fantasy'],
    },
    {
        'title': 'No time to die',
        'background': 'http://127.0.0.1:8000/media/images/movie_backgrounds/6.jpg',
        'poster': 'http://127.0.0.1:8000/media/images/movie_posters/6.jpg',
        'release_date': '12th Nov 2020',
        'director': 'Cary Joji Fukunaga',
        'cast': 'Daniel Craig, Lashana Lynch, Ana de Armas, Rami Malek, Jeffrey Wright, Naomie Harris, ' +
                'Lea Seydoux, Ben Whishaw, Ralph Fiennes',
        'synopsis': 'Recruited to rescue a kidnapped scientist, globe-trotting spy James ' +
                    'Bond finds himself hot on the trail of a mysterious villain, whos armed ' +
                    'with a dangerous new technology.',
        'genres': ['Action', 'Thriller', 'Adventure', 'Spy', 'Mystery'],
    },
    {
        'title': 'Minions 2: the rise of gru',
        'background': 'http://127.0.0.1:8000/media/images/movie_backgrounds/7.jpg',
        'poster': 'http://127.0.0.1:8000/media/images/movie_posters/7.jpg',
        'release_date': '2nd Jul 2021',
        'director': 'Kyle Balda',
        'cast': 'Steve Carell',
        'synopsis': 'The further adventures of Gru and his Minions.',
        'genres': ['Animation', 'Comedy', 'Family'],
    },
    {
        'title': 'Tenet',
        'background': 'http://127.0.0.1:8000/media/images/movie_backgrounds/8.jpg',
        'poster': '',
        'release_date': '17th Jul 2020',
        'director': 'Christopher Nolan',
        'cast': 'Robert Pattinson, John David Washington, Elizabeth Debicki, Aaron Taylor-Johnson',
        'synopsis': 'An action epic film evolving from the world of international espionage.',
        'genres': ['Thriller', 'Adventure', 'Action'],
    },

]


def add_genres():
    for genre in genres:
        temp = Genre()
        temp.name = genre
        temp.save()


def add_movies():
    for movie in movies:
        temp_movie = Movie()
        temp_movie.title = movie.get('title')
        temp_movie.release_date = movie.get('release_date')
        temp_movie.cast = movie.get('cast')
        temp_movie.background = movie.get('background')
        temp_movie.poster = movie.get('poster')
        temp_movie.director = movie.get('director')
        temp_movie.synopsis = movie.get('synopsis')
        new_page = CommentPage()
        new_page.save()
        temp_movie.comment_page = new_page
        temp_movie.save()

        for genre in movie.get('genres'):
            try:
                temp_genre = Genre.objects.get(name=genre)
                temp_genre.movies.add(temp_movie)
            except Genre.DoesNotExist:
                print(genre)


def run():
    print('here')
    add_genres()
    add_movies()
