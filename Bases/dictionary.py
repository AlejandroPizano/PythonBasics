def cartelera():    
    current_movies = {'The grinch':'11:00 am',
                    'The incredibles':'12:00 am',
                    'The frosty':'1:00 pm',
                    'Harry Potter':'4:00 pm'}


    for title, time in current_movies.items():
        print(title,"-------->", time)


    pelicula=input("Que pelicula quieres ver?")
    if current_movies.get(pelicula):
        print(pelicula," se esta reproduciendo a las ",current_movies.get(pelicula) )
    else:
        print("Esa pelicula no esta dentro de la cartelera\n")
        cartelera()
cartelera()