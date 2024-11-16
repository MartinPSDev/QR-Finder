mport cv2
from pyzbar.pyzbar import decode

#Este escript detecta que informacion tiene un codigo QR antes de escanerlo

def leer_codigo_qr(imagen_path):
    
    imagen = cv2.imread(imagen_path)
    
    
    codigos = decode(imagen)
    
    for codigo in codigos:
        tipo = codigo.type
        contenido = codigo.data.decode('utf-8')
        
        # Verifica si es un sitio web
        if contenido.startswith('http://') or contenido.startswith('https://'):
            print(f"El código QR es un sitio web: {contenido}")
        else:
            print(f"El codigo QR contiene otra informacion: {contenido}")


leer_codigo_qr('./tucodigo.jpg') # Aqui va la ruta de la imagen de tu codigo
