import os
import streamlit as st
import telebot
from openai import OpenAI
from dotenv import load_dotenv

# 1. Configuración de la página web
st.set_page_config(page_title="Sweat Factory AI Agent", page_icon="🏋️‍♂️", layout="centered")
st.title("🏋️‍♂️ Max - Sweat Factory AI")
st.subheader("Asistente Virtual de Ventas y Atención al Cliente")

# 2. Cargar credenciales de forma segura (Local o Streamlit Cloud)
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") or st.secrets.get("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")

if not TELEGRAM_BOT_TOKEN or not OPENAI_API_KEY:
    st.error("❌ Error: Faltan configurar las credenciales en las variables de entorno o Secrets.")
    st.stop()

# 3. Inicializar clientes
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# Intentar inicializar Telegram en segundo plano (Opcional si solo quieres la web)
try:
    bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
except Exception as e:
    st.warning(f"⚠️ No se pudo enlazar Telegram: {e}")

# 4. Cargar instrucciones de Max
PROMPT_PATH = os.path.join("agent-config", "system_prompt.txt")
if os.path.exists(PROMPT_PATH):
    with open(PROMPT_PATH, "r", encoding="utf-8") as file:
        system_prompt = file.read()
else:
    system_prompt = "Eres Max, asistente de Sweat Factory. Usa emojis (🏋️‍♂️, 🔥). Precios: Básico $399, Premium $599. Sé enérgico y vende."

# 5. Historial de chat en la interfaz Web (Memoria de Streamlit)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "¡Hola! 🔥 Soy Max, el entrenador virtual de Sweat Factory. ¿Listo para construir tu mejor versión? Pregúntame sobre nuestros planes, horarios o reglamentos. 🏋️‍♂️"}
    ]

# Mostrar los mensajes anteriores en la pantalla
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. Capturar la interacción del usuario en la web
if user_input := st.chat_input("Escribe tu pregunta aquí... (ej. ¿Cuánto cuesta la mensualidad?)"):
    # Mostrar el mensaje del usuario en la web
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generar la respuesta de Max con OpenAI
    with st.chat_message("assistant"):
        with st.spinner("Max está pensando... ⚡"):
            try:
                # Construir el contexto histórico completo para la IA
                contexto = [{"role": "system", "content": system_prompt}]
                for m in st.session_state.messages:
                    contexto.append({"role": m["role"], "content": m["content"]})

                response = openai_client.chat.completions.create(
                    model="gpt-4o",
                    messages=contexto,
                    temperature=0.5
                )
                respuesta_max = response.choices[0].message.content
                st.markdown(respuesta_max)
                
                # Guardar en el historial interno
                st.session_state.messages.append({"role": "assistant", "content": respuesta_max})
            except Exception as e:
                st.error(f"Hubo un calambre en mis circuitos: {e}")
