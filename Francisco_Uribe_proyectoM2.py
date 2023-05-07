#CODIGO QUE SE ENCARGA DE VERIFICAR QUE LA PALABRA DADA POR EL USARIO SEA DE 4 A 8 CARACTERES
palabra=""
while palabra=="": #AQUI CREAMOS EL CICLO PARA SI HAY ERROR REPITA LA OPERACION EL USUARIO
    palabra=input("Por favor deme la palabra: ") #AQUI PEDIMOS AL USUARIO LA PALABRA A VERIFICAR
    if len(palabra)<4: #CONDICION PARA VERIFICAR QUE LA PALABRA NO SEA MENOR DE 4 CRACTERES
        print("Hacen falta letras. Solo tiene " + str (len(palabra)) + " letras.") #MENSAJE AL USUARIO DONDE DICE QUE ESTA INCORRECTA SU PALABRA
        palabra="" #DEVOLVEMOS EL VALOR A LA VARIABLE PARA QUE SE REPITA EL CICLO
    elif len(palabra)>8: #SUBCONDICION DONDE VERIFICAMOS QUE LA PALABRA NO TENGA MAS DE 8 CARACTERES
        print("Sobran letras. Tiene " + str(len(palabra)) + " letras.") #MENSAJE AL USUARUIO INDICANDO EL ERROR
        palabra="" #DEVOLVEMOS EL VALOR A LA VARIABLE PARA QUE SE REPITA EL CICLO
    else: #SI NO SE CUMPLEN LAS CONDICIONALES SALE DEL CICLO
        print("Palabra correcta") #MOSTRAMOS AL USUARUIO QUE TODO ESTA CORRECTO

#CODIGO QUE SE ENCARGA DE ENCONTRAR EN QUE CUADRANTE ESTÁ UNA CORDENADA
x=0 #DECLARAMOS LAS VARIABLES EN 0 PARA EL CICLO
y=0 
while x==0 and y==0: #AÑADIMOS EL CICLO PARA EL ERROR QUE NOS PUEDA DAR
    x= int (input("Deme la cordenada x: ")) #PEDIMOS AL USUARIO EL PRIMER DATO
    y= int (input("Deme la cordenada y: ")) #PEDIMOS AL USARIO EL SEGUNDO DATO
if x==0 or y==0: #CREAMOS LA CONDICION PARA QUE EN NINGUNA COORDENADA HAYA UN CERO COMO VALOR
    print("No debe de haber ninguna coordenada en 0") #MANDAMOS EL MENSAJE DE ERROR AL USUARIO
    x=0 #DECLARAMOS LAS VARIABLES EN 0 PARA QUE SE REPITA EL CICLO
    y=0    
elif x>0 and y>0: #CREAMOS LAS CONDICIONES PARA PODER 
    print("Su cordenada está en el cuadrante I.")
elif x<0 and y<0:
    print("Su cordenada está en el cuadrante III")
elif x<0 and y>0:
    print("Su cordenada está en el cuadrante II")
elif x>0 and y<0:
    print("Su cordenada está en el cuadrante IV")

