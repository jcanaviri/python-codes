import log

# Constante que contiene el nombre del archivo de log a utilizar
ARCHIVO_LOG = "mi_log.txt"

def main():
    # Al comenzar, abrir el log
    archivo_log = log.abrir_log(ARCHIVO_LOG)
    # Error de recurso no encontrado
    try:
        open("ARCHIVO_LOG")
    except FileNotFoundError:
        error = 'no se pudo acceder al recurso'

    if error:
        log.guardar_log(archivo_log, "ERROR: "+error)
    
    # Usando un formato invalido
    try:
        open(ARCHIVO_LOG, 'no-valid')
    except ValueError:
        error = 'formato de entrada invalido'
        log.guardar_log(archivo_log, "ERROR: "+error)

    # Finalmente cerrar el archivo
    log.cerrar_log(archivo_log)

main()
