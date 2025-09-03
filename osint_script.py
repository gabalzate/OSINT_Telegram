from telethon import TelegramClient
from config import API_ID, API_HASH

# El nombre de la sesión es el nombre del archivo de la sesión
# que se creará. Puedes elegir cualquier nombre.
session_name = 'mi_sesion'

# Crea el cliente de Telegram usando las credenciales del archivo de configuración
client = TelegramClient(session_name, API_ID, API_HASH)

async def main():
    # Conéctate a Telegram
    await client.start()

    # Si el cliente no está autorizado, pide al usuario
    # su número de teléfono y el código de verificación.
    if not await client.is_user_authorized():
        print("Necesitas iniciar sesión. Por favor, ingresa tu número de teléfono (con código de país, por ejemplo, +573001234567):")
        phone = input()
        await client.send_code_request(phone)

        print("Por favor, ingresa el código de verificación que llegó a tu teléfono:")
        code = input()
        await client.sign_in(phone, code)

    print("¡Conexión exitosa! 🎉")

# Ejecuta el código principal
with client:
    client.loop.run_until_complete(main())
