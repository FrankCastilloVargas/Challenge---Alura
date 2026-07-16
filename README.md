# 🏋️‍♂️ Sweat Factory AI Agent — Atención al Cliente y Ventas (Pure Python Edition)

¡Bienvenido al repositorio oficial del Agente de Inteligencia Artificial de **Sweat Factory**! 🚀 Este proyecto combina la potencia de los modelos de lenguaje natural (LLMs) con una arquitectura ligera basada exclusivamente en **Python**, garantizando un despliegue rápido, eficiente y de alta disponibilidad.

---

## 🎯 ¿Para qué es este Repositorio?
El propósito de este repositorio es centralizar, respaldar y versionar toda la arquitectura lógica, la configuración del sistema y la base de conocimientos que dan vida a nuestro agente de IA. 

El agente tiene dos misiones principales:
1. **Atención al Cliente Impecable:** Resolver de forma inmediata y automática cualquier duda de los socios actuales sobre horarios, reglamento interno, uso de instalaciones y políticas.
2. **Cerrador de Ventas Efectivo:** Guiar a los prospectos (no-socios) a través de nuestros planes, manejar objeciones de precio de manera persuasiva y motivarlos a agendar una visita o inscribirse directamente.

---

## 🏗️ Arquitectura del Sistema (Despliegue en OCI Compute con Python)

El agente está diseñado para ejecutarse directamente sobre el entorno de ejecución de Python en una máquina virtual de **Oracle Cloud Infrastructure (OCI)**

[ Usuario (Telegram App) ]
│
▼ (Servidores de Telegram)
▲
│  (Long Polling Seguro / Puerto Abierto de Salida)
[ OCI Compute Instance (Windows Server) ] ◄── Monitoreado por ──► [ Windows Task Scheduler ]
│
└── (Entorno Virtual Python)
│
├──► Lee Configuración ──► [ agent-config/ & knowledge-base/ ]
│
└──► Procesa Consulta ───► [ OpenAI API (GPT-4o) ]

### Componentes Clave:
* **OCI Compute Instance (Windows Server):** Una instancia de cómputo flexible ejecutando Windows Server. Puede operar eficientemente con recursos mínimos (1 o 2 OCPUs) asignados en la plataforma de Oracle Cloud.
* **Telegram Bot API:** El canal oficial de comunicación. Los mensajes de los usuarios son procesados por el script mediante la librería `pyTelegramBotAPI` o `python-telegram-bot`.
* **Windows Task Scheduler (Programador de Tareas):** Configuramos un disparador para que el script de Python se inicie automáticamente cada vez que el servidor Windows se encienda o se reinicie por mantenimiento, garantizando disponibilidad 24/7.

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

---## 💬 Ejemplos de Preguntas y Respuestas en Telegram

El agente interactúa con los usuarios utilizando el contexto del manual de Sweat Factory de la siguiente manera:

### 1. Escenario de Ventas (Prospecto pregunta por precios)
* **Usuario:** *Hola, ¿cuánto cuesta la mensualidad?*
* **Max (IA):** *¡Excelente que preguntes! En **Sweat Factory** tenemos opciones que se adaptan a ti: 1️⃣ **Plan Básico ($399 MXN/mes):** Acceso total a pesas y cardio. 2️⃣ **Plan Premium ($599 MXN/mes):** ¡Inscripción GRATIS, clases grupales ilimitadas y 1 pase de invitado al mes! 🚴‍♂️ 3️⃣ **Plan VIP Anual ($5,400 MXN):** ¡Te ahorras 2 meses enteros! ¿Cuál de estos planes se acomoda mejor a tus objetivos actuales? 💪 ¡Escribe /visita para agendar un recorrido gratis por nuestras instalaciones!*

### 2. Escenario de Reglamento (Socio actual)
* **Usuario:** *¿Se puede entrenar en sandalias?*
* **Max (IA):** *¡Hola! Por tu propia seguridad y para evitar lesiones en la zona de pesas, es estrictamente obligatorio entrenar con ropa deportiva y calzado cerrado adecuado (tenis limpios) 👟 No se permite el acceso en sandalias, calzado de calle o sin playera. ¡Cuidemos tu cuerpo y el de todos! 🔥*

---


