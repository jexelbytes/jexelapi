import os
import firebase_admin
from firebase_admin import credentials, messaging

# Configuracion de Firebase para envio de notificaciones al movil

path_simp = f"./services/creds.json"

try:
    cred = credentials.Certificate(os.path.abspath(path_simp))
    conn = firebase_admin.initialize_app(cred)
except Exception as err:
    print(err)

def send_notification(title, content, image, token, data=None):
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=content,
            image=image,
        ),
        data=data,
        tokens=[token],
    )
    res = messaging.send_multicast(message)
    print("notificacion enviada exitosamente:", str(res))
    return res