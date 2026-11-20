# arboladoyjardinzaragoza.es

Web de Arbolado y Jardín Zaragoza (jardinería, poda, tala, destoconado y desbroce).
Se publica con GitHub Pages desde la rama `main` (dominio en `CNAME`).

## Qué hay

| Ruta | Qué es |
|---|---|
| `index.html` | Portada |
| `servicios/` | Una página por servicio |
| `aviso-legal.html`, `privacidad.html`, `cookies.html` | Páginas legales |
| `js/cookies.js` | Aviso de cookies: Google Analytics solo se carga si se acepta; el mapa solo al pulsar |
| `img/fotos/` | Fotos en WebP, cada una en dos tamaños (1200 y 600 px), sin datos GPS. Unas son reales y otras, ilustrativas hechas con IA |
| `img/compartir.jpg` | La foto que enseñan WhatsApp y las redes al pegar el enlace |
| `herramientas/generar_paginas.py` | Genera todas las páginas con la misma cabecera y pie, y también `sitemap.xml`, `robots.txt` y `llms.txt` |
| `herramientas/preparar_fotos.py` | Convierte fotos nuevas al formato de la web |
| `llms.txt` | Resumen de la web en texto llano para los asistentes de IA |

## Cambiar textos

Los textos están en `herramientas/generar_paginas.py`. Después de cambiarlo:

    python herramientas/generar_paginas.py .

## Poner una foto nueva

1. Dejar la foto (jpg o png) en una carpeta, con el nombre que tendrá en la web, por ejemplo `seto-recortado.jpg`.
2. `python herramientas/preparar_fotos.py CARPETA` la pasa a `img/fotos/`.
3. Ponerla en `herramientas/generar_paginas.py` con `foto(...)` o `tarjeta(...)` y volver a generar las páginas.

Los originales están fuera del repositorio, en la carpeta `fotos-web` de al lado.

Vista previa: `python -m http.server 8199` y abrir http://localhost:8199
