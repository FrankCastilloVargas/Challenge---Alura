# 🏋️‍♂️ Sweat Factory AI Agent — Atención al Cliente y Ventas (Pure Python Edition)

¡Bienvenido al repositorio oficial del Agente de Inteligencia Artificial de **Sweat Factory**! 🚀 Este proyecto combina la potencia de los modelos de lenguaje natural (LLMs) con una arquitectura ligera basada exclusivamente en **Python**, garantizando un despliegue rápido, eficiente y de alta disponibilidad.

---

## 🎯 ¿Para qué es este Repositorio?
El propósito de este repositorio es centralizar, respaldar y versionar toda la arquitectura lógica, la configuración del sistema y la base de conocimientos que dan vida a nuestro agente de IA. 

El agente tiene dos misiones principales:
1. **Atención al Cliente Impecable:** Resolver de forma inmediata y automática cualquier duda de los socios actuales sobre horarios, reglamento interno, uso de instalaciones y políticas.
2. **Cerrador de Ventas Efectivo:** Guiar a los prospectos (no-socios) a través de nuestros planes, manejar objeciones de precio de manera persuasiva y motivarlos a agendar una visita o inscribirse directamente.

---

## 📁 ¿Qué contiene este Repositorio?

* **`agent-config/`**
    * `sweat_factory_agent.json`: Archivo maestro con el flujo conversacional estructurado, nodos de decisión e intenciones predefinidas listo para ser importado.
    * `system_prompt.txt`: Las instrucciones de personalidad, tono enérgico/motivador y directrices de venta que moldean el comportamiento de Max.
* **`Base-Conocimiento/`**
    * `Manual_Operativo_Sweat_Factory.pdf`: El cerebro de datos del bot (Reglamento, precios, políticas de reembolso y guías de seguridad).
* **`app.py`**: El script principal de Python que conecta el API de Telegram con el cerebro de OpenAI.
* **`requirements.txt`**: Lista de librerías de Python necesarias (ej: `telebot`, `openai`, `python-dotenv`).
* **`README.md`**: Esta guía de documentación.
* **`MAX Bot Evidencia I y II.jpg`**: Imagenes que demuestran que el Agente es funcional.

---## 💬 Ejemplos de Preguntas y Respuestas

El agente interactúa con los usuarios utilizando el contexto del manual de Sweat Factory de la siguiente manera:

### 1. Escenario de Ventas (Prospecto pregunta por precios)
* **Usuario:** *Hola, ¿cuánto cuesta la mensualidad?*
* **Max (IA):** *¡Excelente que preguntes! En **Sweat Factory** tenemos opciones que se adaptan a ti: 1️⃣ **Plan Básico ($399 MXN/mes):** Acceso total a pesas y cardio. 2️⃣ **Plan Premium ($599 MXN/mes):** ¡Inscripción GRATIS, clases grupales ilimitadas y 1 pase de invitado al mes! 🚴‍♂️ 3️⃣ **Plan VIP Anual ($5,400 MXN):** ¡Te ahorras 2 meses enteros! ¿Cuál de estos planes se acomoda mejor a tus objetivos actuales? 💪 ¡Escribe /visita para agendar un recorrido gratis por nuestras instalaciones!*

### 2. Escenario de Reglamento (Socio actual)
* **Usuario:** *¿Se puede entrenar en sandalias?*
* **Max (IA):** *¡Hola! Por tu propia seguridad y para evitar lesiones en la zona de pesas, es estrictamente obligatorio entrenar con ropa deportiva y calzado cerrado adecuado (tenis limpios) 👟 No se permite el acceso en sandalias, calzado de calle o sin playera. ¡Cuidemos tu cuerpo y el de todos! 🔥*

---

## 🌐 Cómo usar y probar el Agente de IA en la Web (Streamlit)

Este proyecto cuenta con una interfaz web interactiva tipo "ChatGPT" desarrollada en **Streamlit**. Esto permite que cualquier usuario o miembro del equipo pruebe las respuestas del agente **Max** directamente desde su navegador web.

Sigue estos pasos para interactuar con el bot en la plataforma:

### 🛠️ Paso 1: Acceder a la Aplicación Web
1. Haz clic en el enlace de la aplicación desplegada en Streamlit Cloud: 
   👉 *(https://challenge---alura-g6xu6e5cxmtttpxmuwymhb.streamlit.app/)*
2. Al abrir la página, verás el título **"🏋️‍♂️ Max - Sweat Factory AI"** y un mensaje de bienvenida en la pantalla de chat.

### 🔑 Paso 2: Configurar tus propias Credenciales (Si usas un fork o clon propio)
Si has clonado este repositorio y deseas correr tu propia versión en los servidores de Streamlit, debes inyectar tus llaves secretas de forma segura:
1. En tu panel de control de **Streamlit Cloud**, ve a la configuración de tu App (`Settings`).
2. Entra a la sección de **Secrets** (Llaves secretas).
3. Pega tus credenciales respetando el siguiente formato:
   ```toml
   TELEGRAM_BOT_TOKEN = "tu_token_de_botfather"
   OPENAI_API_KEY = "sk-proj-tu_clave_real_de_openai"

---

## 🏗️ Arquitectura del Sistema y Tecnologías Utilizadas

El agente de IA de **Sweat Factory** está diseñado bajo una arquitectura desacoplada, ligera y modular que prioriza la velocidad de respuesta, el control estricto de los datos del negocio y la flexibilidad de despliegue (código puro o automatización visual), evitando por completo la sobrecarga de contenedores como Docker.

### 📊 Diagrama de Flujo de Datos

```text
[ Cliente (Telegram / Web) ] 
             │
             ▼
   [ Interfaz / Trigger ] ───► (Streamlit Web App / pyTelegramBotAPI)
             │
             ▼
     [ Capa de Control ] ───► Inyección Local del 'system_prompt.txt' (Reglas del Gym)
             │
             ▼
  [ Cerebro de IA (API) ] ───► OpenAI GPT-4o (Procesamiento de Lenguaje Natural)
             │
             ▼
[ Respuesta Automatizada ] ───► Retorno con formato Markdown y Emojis al Cliente

---

## 🛠️Tecnologías Utilizadas

Este proyecto fue desarrollado utilizando un conjunto de tecnologías que permiten procesar la inteligencia artificial de forma rápida y segura, evitando la sobrecarga de contenedores pesados.

### 🐍 Tech Stack
* ![Python]**Python 3.11:**
* ![OpenAI] Google Gemini API
* ![Telegram]
* ![Streamlit]
* ![GitHub]

---
