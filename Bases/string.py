import pickle

lista_nombres = ['Ana', 'Juan', '010101', 'Alejandro']
fichero_binario=open("lista_nombres","wb")
pickle.dump(lista_nombres, fichero_binario)
fichero_binario.close()

with open("lista_nombres","rb") as file:
    print(pickle.load(file))
