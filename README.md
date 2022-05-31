# Asistente virtual en Python


## ¿Qué es?
Implementación de un asistente virtual en Python que no necesite recibir comandos de voz para la activación. Detecta cuando un dispositivo bluetooth (Mi Band) está cerca a través de un barrido bluetooth y notifica sobre nuevos correos electrónicos, eventos en el calendario... 

También puede interpretar comandos, diferenciando entre verbos y sustantivos, para poder interpretar la misma orden dicha con diferentes palabras y darle la capacidad de interpretar diferentes parámetros para un mismo comando.

## Características:

 - Comprobar el correo electrónico y notificarlo.
 - Comprobar los eventos en Google Calendar y notificar cuando sea necesario.
 - Añadir eventos a Google Calendar.
 - Hacer una copia de seguridad en un disco externo.
 - Abrir el explorador de archivos en una ruta específica.
 - Abrir el terminal en una ruta específica.
 - Por la noche, sugerir una alarma para el día siguiente en función de los eventos en el calendario (no terminado).
 - Reproducir música de Spotify y controlar el volumen.
 - Ejecutar una aplicación específica.
 - Comprobar cada vez que la Mi Band está cerca mediante el escaneo de Bluetooth para notificar nuevos eventos, haciendo un buffer de notificaciones aún no notificadas.

## Instalación
### Clonar repositorio
`$ git clone https://github.com/DiegoMartindeAndres/pyAssistant.git`

### Entrar en el directorio
`$ cd pyAssistant`

### Instalar dependencias
`$ pip install -r requirements.txt`

### Ejecutar clase principal
`$ python3 main.py`
