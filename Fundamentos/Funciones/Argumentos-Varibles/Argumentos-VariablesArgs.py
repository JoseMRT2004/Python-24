print('*** Argumentos Variables ***')

def superheroeSuperpoderes(superheroe, nombre, *args):
    print(f'Superheroe: {superheroe} - {nombre} - {args}')
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')

superheroeSuperpoderes('Spiderman', 'Peter Parker', 'Instinto Arácnido', 'Teleraña')
superheroeSuperpoderes('Ironam', 'Tony Stark', 'Armadura','Playboy','Millonario')

superheroeSuperpoderes('Mi vecino', 'Juan Perez')