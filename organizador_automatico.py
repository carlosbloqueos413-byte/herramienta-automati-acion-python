import os
import shutil
def organizar_carpeta(ruta_carpeta)
# Definimos las carpetas de destino para cada tipo de archivo
extensiones= {
  "Documentos_PDF": {".pdf"},
  "Imagene":{".jpg". ".png", ".gif},
  "Documentos_Texto":{".docx", ",xlsx"}
}
# Creamos las carpetas si no existen y movemos los archivos
for archivo in os.listdir(ruta_carpeta):
  ruta_archivo= os.path.join(ruta_carpeta,archivo
                             if os.path.isfile(ruta_archivo):
                             _, ext = os.path.splitext(archivo)
                             for carpeta, exts in extensiones.items():
                               if ext.lower() in exts:
                                 ruta_destino = os.path.join(ruta_carpeta, carpeta)
                                 os.makedirs(ruta_destino, exist_ok=True)
                                 shutil.move(ruta_archivo, os.path.join(ruta_destino,archivo))
                                 print("Movido: {archivo} -> {carpeta}")
                                 # Ejemplo de uso para el cliente
                                 if _name_ == "_main_":
                                   print(Iniciando el organizador automatico de archivos...")
                                   
