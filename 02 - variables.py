
#agrego libreria para objeto date
import datetime

#Variables String
libro_favorito = 'Los Miserables'
cancion_favorita = 'Iba acabandose el vino'
ultimo_que_comi = 'Papardellis caseros con salsa arrabiata'

#Variables Int
año_libro = 1862
año_canción = 1976
día_comida_objeto = datetime.date(2020,11,13)

#Variables float
importe_libro = 132.99
importe_disco = 39.99
presupuesto_comida = 75.50

#Variables Bool
leido = True
escuchado = True
comido = True

#impresión en consola de los distintos tipos de variables
print(f'Mi libro favorito es: {libro_favorito} del año {año_libro} y cuando lo compré me costó {importe_libro} pesos')
print(f'Mi canción favorita es: {cancion_favorita} del año {año_canción} y el disco me costó {importe_disco} pesos')
print(f'Lo último que comí fue: {ultimo_que_comi} el día {día_comida_objeto} y me costó prepararlos {presupuesto_comida} pesos')