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
| `img/fotos/` | Fotos reales en WebP (máx. 1200 px, sin datos GPS) |
| `herramientas/generar_paginas.py` | Genera todas las páginas con la misma cabecera y pie |

## Cambiar textos

Los textos están en `herramientas/generar_paginas.py`. Después de cambiarlo:

    python herramientas/generar_paginas.py .

Vista previa: `python -m http.server 8199` y abrir http://localhost:8199
