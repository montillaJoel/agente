# Agente de investigación en Python

Escribe una pregunta en la terminal y recibe un resumen con las fuentes y las herramientas que el agente declara haber usado. El proyecto conecta Gemini con LangChain y le da acceso a dos herramientas de consulta: Wikipedia y la búsqueda web de DuckDuckGo.

## Una consulta de principio a fin

**Qué le pido**

> ¿Quién fue Ada Lovelace y qué relación tuvo con la máquina analítica?

**Qué hace**

Gemini recibe la pregunta y decide si necesita consultar una fuente. Para esta pregunta puede buscar «Ada Lovelace» en Wikipedia. La herramienta devuelve un extracto de hasta 1.000 caracteres del primer resultado. El agente también puede buscar en la web con DuckDuckGo si necesita más contexto.

**Qué devuelve**

Esta es una salida ilustrativa. El resumen, las fuentes y las herramientas pueden variar en cada ejecución.

```text
Tema: Ada Lovelace y la máquina analítica
Resumen: Ada Lovelace fue una matemática británica que escribió notas sobre la máquina analítica diseñada por Charles Babbage. En ellas describió un procedimiento para que la máquina calculara números de Bernoulli.
Fuentes: ['Wikipedia: Ada Lovelace']
Herramientas utilizadas: ['wikipedia']
```

## Cómo probarlo

Necesitas Python 3.14 o superior, uv y una clave de la API de Google con acceso al modelo configurado en [main.py](main.py).

1. Clona el repositorio y entra en su carpeta.

   ```sh
   git clone https://github.com/montillaJoel/agente.git
   cd agente
   ```

2. Copia `.env.example` a `.env` y asigna tu clave a `GOOGLE_API_KEY` en ese archivo local.
3. Instala las dependencias y ejecuta el agente.

   ```sh
   uv sync --locked
   uv run python main.py
   ```

4. Cuando aparezca **¿Qué deseas investigar?**, escribe una pregunta y pulsa Intro. El programa imprime la respuesta en la terminal. Para hacer otra consulta, vuelve a ejecutarlo.
