import os
import telebot
from openai import OpenAI
from dotenv import load_dotenv

# 1. Cargar las variables de entorno desde el archivo .env
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Validar que las credenciales existan antes de arrancar
if not TELEGRAM_BOT_TOKEN or not OPENAI_API_KEY:
    print("❌ ERROR: Falta configurar TELEGRAM_BOT_TOKEN o OPENAI_API_KEY en el archivo .env")
    exit(1)

# 2. Inicializar los clientes de Telegram y OpenAI
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# 3. Cargar las instrucciones de personalidad (System Prompt) de Max
PROMPT_PATH = os.path.join("agent-config", "system_prompt.txt")

try:
    with open(PROMPT_PATH, "r", encoding="utf-8") as file:
        system_prompt = file.read()
    print("💪 Base de conocimientos e instrucciones de Max cargadas correctamente.")
except FileNotFoundError:
    # Respaldo por si no encuentra el archivo en la carpeta estructurada
    system_prompt = "Eres Max, el entrenador virtual de Sweat Factory. Usa emojis (🏋️‍♂️, 🔥), sé enérgico, motivador y ayuda a vender membresías."
    print("⚠️ ADVERTENCIA: No se encontró 'agent-config/system_prompt.txt'. Usando prompt de respaldo.")

print("🚀 El agente de IA de Sweat Factory está encendido y escuchando en Telegram...")

# 4. Capturar y responder los mensajes de Telegram
@bot.message_handler(func=lambda message: True)
def responder_cliente(message):
    chat_id = message.chat.id
    user_text = message.text
    
    # Mostrar en la consola del servidor lo que escribe el usuario para monitoreo
    print(f"📩 Mensaje recibido de [{message.from_user.first_name}]: {user_text}")

    try:
        # Indicar al usuario en Telegram que Max está "escribiendo..."
        bot.send_chat_action(chat_id, 'typing')

        # Consultar al cerebro de OpenAI (GPT-4o) mandando las reglas del gimnasio
        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_text}
            ],
            temperature=0.7 # Balance ideal entre creatividad de ventas y precisión de reglas
        )
        
        # Extraer la respuesta generada por la IA
        respuesta_max = response.choices[0].message.content

        # Enviar la respuesta de vuelta al cliente en Telegram
        bot.send_message(chat_id, respuesta_max, parse_mode="Markdown")
        print(f"📤 Respuesta de Max: {respuesta_max[:50]}...")

    except Exception as e:
        error_msg = "❌ Hola. Mi circuito de entrenamiento sufrió un calambre temporal. Por favor, intenta de nuevo en unos segundos. 🔥"
        bot.send_message(chat_id, error_msg)
        print(f"💥 Ocurrió un error al procesar el mensaje: {e}")

# 5. Mantener el bot corriendo indefinidamente (Long Polling)
if __name__ == "__main__":
    bot.infinity_polling()
