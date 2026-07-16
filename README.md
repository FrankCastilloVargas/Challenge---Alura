# 🏋️‍♂️ Sweat Factory AI Agent MAX — Atención al Cliente y Ventas

¡Bienvenido al repositorio oficial del Agente de Inteligencia Artificial de **Sweat Factory**! 🚀 Este proyecto combina tecnología de lenguaje natural (IA) con estrategias de conversión para ofrecer atención al cliente 24/7 y potenciar las ventas de nuestra comunidad fitness.

---

## 🎯 ¿Para qué es este Repositorio?
El propósito de este repositorio es centralizar, respaldar y versionar toda la arquitectura lógica, la configuración del sistema y la base de conocimientos que dan vida a nuestro agente de IA. 

El agente tiene dos misiones principales:
1. **Atención al Cliente Impecable:** Resolver de forma inmediata y automática cualquier duda de los socios actuales sobre horarios, reglamento interno, uso de instalaciones y políticas.
2. **Cerrador de Ventas Efectivo:** Guiar a los prospectos (no-socios) a través de nuestros planes, manejar objeciones de precio de manera persuasiva y motivarlos a agendar una visita o inscribirse directamente.

---

## 📁 ¿Qué contiene este Repositorio?

Este espacio está organizado de manera limpia y modular para facilitar cualquier actualización técnica o de contenido:

*   **`agent-config/`**
    *   `sweat_factory_agent.json`: Archivo maestro con el flujo conversacional estructurado, nodos de decisión y conexiones API listo para ser importado en la plataforma de desarrollo.
    *   `system_prompt.txt`: Las instrucciones de personalidad, tono enérgico/motivador y directrices de venta que moldean el comportamiento del asistente.
*   **`knowledge-base/`**
    *   `Manual_Operativo_Sweat_Factory.pdf`: El cerebro de datos del bot. Contiene el reglamento oficial, políticas de reembolso detalladas, guías de seguridad para el uso de equipos y respuestas a preguntas frecuentes (FAQs).
*   **`README.md`**: Esta guía de bienvenida y documentación general del proyecto.

---

## 🔥 ¡Únete a la Comunidad Sweat Factory! (Promoción del Gimnasio)

En **Sweat Factory** no solo construimos cuerpos, ¡forjamos disciplina y comunidad! Si estás listo para llevar tu entrenamiento al siguiente nivel, tenemos el plan perfecto para ti.

### 📋 Nuestros Planes Mensuales
*   **Plan Básico (\$399 MXN):** Acceso total a zonas de peso libre, peso integrado y nuestra moderna área de cardio. *(Inscripción: \$250 MXN)*.
*   **Plan Premium (\$599 MXN):** Todo lo del Plan Básico **+** Clases grupales ilimitadas (Spinning, Yoga, Zumba) **+** ¡1 pase de invitado gratis al mes para entrenar con quien quieras! *(Inscripción: GRATIS)*.
*   **Plan VIP Anual (\$5,400 MXN):** El pase definitivo. Todos los beneficios Premium **+** Evaluación nutricional mensual incluida. Pago único anual donde **¡te ahorras 2 meses completos de mensualidad!** *(Inscripción: GRATIS)*.

### 🤝 Programa de Referidos: "Entrena con Amigos"
¡Entrenar acompañado paga bien! Si ya eres socio de Sweat Factory, invita a tus amigos:
*   Por **1 amigo** inscrito en el mes: Te llevas **50% de descuento** en tu próxima mensualidad.
*   Por **2 amigos** inscritos en el mismo mes: ¡Tu siguiente mes es **100% GRATIS**!
*   **¿Y tu amigo?** Al ingresar recomendado por ti, recibe de inmediato un **50% de descuento en su inscripción**.

---

## 🚀 Cómo Replicar o Desplegar este Agente
1. Descarga el archivo `.json` ubicado en la carpeta `agent-config/`.
2. Impórtalo en tu plataforma de automatización (Voiceflow, Botpress o ManyChat).
3. Sube el archivo `Manual_Operativo_Sweat_Factory.pdf` de la carpeta `knowledge-base/` como la fuente primaria de información del bot.
4. Conecta tu API Key de OpenAI (GPT-4o recomendado), vincula tu canal de salida (WhatsApp/Instagram) y ¡deja que la IA trabaje por ti!

---
*Sweat Factory — Construyendo tu mejor versión, una repetición a la vez.* 💪🔥
