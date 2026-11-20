#!/usr/bin/env python3
"""Genera las páginas estáticas de arboladoyjardinzaragoza.es (cabecera y pie comunes)."""
"""Uso: python herramientas/generar_paginas.py .   (desde la raíz del repositorio). Rehace index.html, servicios/, las páginas legales, sitemap.xml, robots.txt y llms.txt."""
import sys, html, json
from datetime import date
from pathlib import Path

OUT = Path(sys.argv[1])
# Medidas de cada foto; las apunta herramientas/preparar_fotos.py
MEDIDAS = json.loads((OUT / "img" / "fotos" / "medidas.json").read_text(encoding="utf-8"))
# Municipios de alrededor de Zaragoza donde se trabaja. Sale en la portada, en las
# preguntas frecuentes, en los datos para buscadores y en llms.txt.
ZONA = ["Cuarte de Huerva", "Cadrete", "María de Huerva", "La Muela", "Utebo", "Villanueva de Gállego",
        "Zuera", "San Mateo de Gállego", "La Puebla de Alfindén", "Pastriz", "Alfajarín", "El Burgo de Ebro"]
ZONA_TXT = ", ".join(ZONA[:-1]) + " y " + ZONA[-1]
MARCA = "Arbolado y Jardín Zaragoza"
MARCA_A, MARCA_B = "Arbolado y Jardín", " Zaragoza"
DOM = "https://arboladoyjardinzaragoza.es"
TEL, TEL_TXT = "+34876657235", "876 65 72 35"
EMAIL = "info@arboladoyjardinzaragoza.es"
DIR = "Calle Riglos 9, 50012 Zaragoza"
WA = ("https://wa.me/34876657235?text=%5BJARDINERIA%5D%20Hola%2C%20vengo%20de%20"
      "arboladoyjardinzaragoza.es.%20Os%20cuento%20qu%C3%A9%20necesito%20y%20d%C3%B3nde%3A%20")
MAILTO = ("mailto:" + EMAIL + "?subject=Presupuesto%20de%20jardiner%C3%ADa&body=Hola%2C%20os%20escribo%20"
          "desde%20arboladoyjardinzaragoza.es.%0A%0AQu%C3%A9%20necesito%3A%20%0AD%C3%B3nde%20(municipio%20o%20urbanizaci%C3%B3n)%3A%20%0ATel%C3%A9fono%3A%20")

SERVICIOS = [
    ("mantenimiento-de-jardines", "Mantenimiento de jardines"),
    ("riego-automatico", "Riego automático"),
    ("poda-de-arboles", "Poda y arboricultura"),
    ("tala-y-destoconado", "Tala y destoconado"),
    ("desbroce-y-prevencion-de-incendios", "Desbroce y prevención de incendios"),
]

def cabecera(titulo, desc, ruta, raiz, schema=""):
    canon = DOM + "/" + ruta
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titulo)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#14532d">
<link rel="icon" href="{raiz}img/verdalia-favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="{MARCA}">
<meta property="og:title" content="{html.escape(titulo)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{DOM}/img/compartir.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Quicksand:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{raiz}css/styles.css">
<script src="{raiz}js/cookies.js"></script>
{schema}</head>
<body>

<header class="site-header">
  <div class="container header-inner">
    <a class="logo" href="{raiz}" aria-label="{MARCA}, inicio">
      <img class="logo-mark" src="{raiz}img/verdalia-hoja.svg" alt="" aria-hidden="true">
      <span class="logo-text">{MARCA_A}<span>{MARCA_B}</span></span>
    </a>
    <nav class="nav" id="nav">
      <a href="{raiz}#servicios">Servicios</a>
      <a href="{raiz}#expres">Urgencias</a>
      <a href="{raiz}#zona">Zona</a>
      <a href="{raiz}#contacto">Contacto</a>
    </nav>
    <div class="header-actions">
      <a class="btn btn-primary btn-header" href="{WA}" target="_blank" rel="noopener">WhatsApp</a>
      <button class="nav-toggle" id="nav-toggle" aria-label="Abrir menú" aria-controls="nav" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>

<main>
"""

def contacto(titulo="Hablemos de su jardín"):
    return f"""
  <section id="contacto" class="section section-cta">
    <div class="container contacto-inner">
      <h2>{titulo}</h2>
      <p>Cuéntenos qué necesita y dónde, y le preparamos un presupuesto sin compromiso. Si nos manda una foto, mejor.</p>
      <div class="hero-cta">
        <a class="btn btn-primary" href="{WA}" target="_blank" rel="noopener">Escribir por WhatsApp</a>
        <a class="btn btn-ghost" href="tel:{TEL}">Llamar: {TEL_TXT}</a>
        <a class="btn btn-ghost" href="{MAILTO}">Escribir un correo</a>
      </div>
      <p class="contacto-direccion">{DIR} (España)</p>
    </div>
  </section>
"""

def pie(raiz):
    servicios = " · ".join(f'<a href="{raiz}servicios/{s}.html">{n}</a>' for s, n in SERVICIOS)
    return f"""
</main>

<footer class="site-footer">
  <div class="container footer-inner">
    <p class="footer-firma">
      <span class="logo-text">{MARCA_A}<span>{MARCA_B}</span></span>
      <span class="footer-sep">·</span>Jardinería, arbolado y prevención de incendios
    </p>
    <p class="footer-contacto"><a href="tel:{TEL}">{TEL_TXT}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a> · {DIR}</p>
  </div>
  <div class="container footer-inner footer-links">
    <p>{servicios}</p>
    <p><a href="{raiz}aviso-legal.html">Aviso legal</a> · <a href="{raiz}privacidad.html">Privacidad</a> · <a href="{raiz}cookies.html">Cookies</a> · <a href="#" data-cookies-config>Configurar cookies</a></p>
  </div>
</footer>

<script>
  (function () {{
    var toggle = document.getElementById('nav-toggle');
    var nav = document.getElementById('nav');
    if (!toggle || !nav) return;
    function closeNav() {{
      nav.classList.remove('open');
      toggle.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    }}
    toggle.addEventListener('click', function () {{
      var abierto = nav.classList.toggle('open');
      toggle.classList.toggle('open', abierto);
      toggle.setAttribute('aria-expanded', abierto ? 'true' : 'false');
    }});
    nav.querySelectorAll('a').forEach(function (a) {{ a.addEventListener('click', closeNav); }});
  }})();
</script>

</body>
</html>
"""

def imagen(raiz, nombre, alt, tamanos, clase="", primera=False, arriba=False):
    """Foto en dos tamaños (600 px y la grande), para que el móvil baje la pequeña."""
    ancho, alto = MEDIDAS[nombre]
    base = f"{raiz}img/fotos/{nombre}"
    # primera: la foto principal de la portada. arriba: fotos que se ven casi al abrir la página (no se retrasan).
    carga = ' fetchpriority="high"' if primera else (' decoding="async"' if arriba else ' loading="lazy" decoding="async"')
    return (f'<img{f" class={chr(34)}{clase}{chr(34)}" if clase else ""} src="{base}.webp" '
            f'srcset="{base}-600.webp 600w, {base}.webp {ancho}w" sizes="{tamanos}" '
            f'alt="{html.escape(alt)}" width="{ancho}" height="{alto}"{carga}>')

def galeria(raiz, fotos):
    """Fotos de una página de servicio, como (nombre, texto alternativo, pie). Pocas: una, o dos como mucho."""
    if not fotos:
        return ""
    tamanos = "(max-width: 800px) 100vw, 760px" if len(fotos) == 1 else "(max-width: 560px) 100vw, 380px"
    figuras = "".join(f"""<figure class="foto">
          <a href="{raiz}img/fotos/{n}.webp">{imagen(raiz, n, alt, tamanos, arriba=True)}</a>
          <figcaption>{pie_foto}</figcaption>
        </figure>""" for n, alt, pie_foto in fotos)
    return f'<div class="galeria galeria-{len(fotos)}">{figuras}</div>'

# ---------- Datos para buscadores y asistentes de IA (schema.org) ----------
NEGOCIO_ID = DOM + "/#negocio"
DESC_NEGOCIO = ("Empresa de jardinería y arbolado de Zaragoza: mantenimiento de jardines, riego automático, poda de árboles, tala controlada, "
                "destoconado y desbroce de parcelas y fincas en Zaragoza y los municipios de alrededor, desde los permisos "
                "hasta la retirada de los restos.")
DIRECCION_LD = {"@type": "PostalAddress", "streetAddress": "Calle Riglos 9", "postalCode": "50012",
                "addressLocality": "Zaragoza", "addressRegion": "Zaragoza", "addressCountry": "ES"}
ZONA_LD = [{"@type": "City", "name": m} for m in ["Zaragoza"] + ZONA]

def ld(*nodos):
    return ('<script type="application/ld+json">\n'
            + json.dumps({"@context": "https://schema.org", "@graph": list(nodos)}, ensure_ascii=False, indent=1)
            + "\n</script>\n")

def faq_ld(faq):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}

def faq_html(faq):
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)

NEGOCIO_LD = {
    "@type": "HomeAndConstructionBusiness", "@id": NEGOCIO_ID, "name": MARCA, "description": DESC_NEGOCIO,
    "url": DOM + "/", "telephone": TEL, "email": EMAIL, "address": DIRECCION_LD, "areaServed": ZONA_LD,
    "image": [DOM + "/img/compartir.jpg", DOM + "/img/fotos/siega-cesped-jardin.webp"],
    "contactPoint": {"@type": "ContactPoint", "telephone": TEL, "contactType": "customer service",
                     "availableLanguage": "es", "areaServed": "ES"},
    "knowsAbout": ["Jardinería", "Mantenimiento de jardines", "Riego automático", "Arboricultura", "Poda de árboles", "Poda en altura",
                   "Tala controlada", "Destoconado", "Desbroce de parcelas y fincas", "Prevención de incendios"],
    "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Servicios", "itemListElement": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n, "url": f"{DOM}/servicios/{s}.html"}}
        for s, n in SERVICIOS]},
}
# En las páginas de servicio, el negocio va resumido y enlazado al de la portada por su @id.
NEGOCIO_CORTO_LD = {k: NEGOCIO_LD[k] for k in ("@type", "@id", "name", "url", "telephone", "address")}

FAQ_PORTADA = [
    ("¿Qué trabajos hacen?", "Mantenimiento de jardines (siega, setos y limpieza), instalación y reparación de riego automático, poda de árboles, también en altura, tala controlada, destoconado y desbroce de parcelas y fincas. Al terminar nos llevamos los restos."),
    ("¿En qué zona trabajan?", f"En Zaragoza capital y en los municipios y urbanizaciones de alrededor: {ZONA_TXT}, entre otros."),
    ("¿Se ocupan de los permisos?", "Sí. Si la poda, la tala o el desbroce necesitan permiso del ayuntamiento o de Medio Ambiente, lo tramitamos nosotros."),
    ("¿Atienden urgencias?", "Sí. Si un árbol o una rama pueden caer tras un temporal, avísenos: si es posible, vamos el mismo día."),
    ("¿Cómo pido presupuesto?", f"Por WhatsApp o por teléfono en el {TEL_TXT}, o por correo. Cuéntenos qué necesita y dónde y, si puede, mándenos una foto. El presupuesto es sin compromiso."),
]

SCHEMA = ld({"@type": "WebSite", "@id": DOM + "/#web", "url": DOM + "/", "name": MARCA, "inLanguage": "es",
             "publisher": {"@id": NEGOCIO_ID}},
            NEGOCIO_LD, faq_ld(FAQ_PORTADA))

# ---------- Portada ----------
def tarjeta(slug, titulo, texto, img, alt):
    return f"""<a class="card card-link" href="servicios/{slug}.html">
            {imagen("", img, alt, "(max-width: 560px) 100vw, (max-width: 980px) 50vw, 370px", "card-img")}
            <div class="card-body">
              <h3>{titulo}</h3>
              <p>{texto}</p>
              <span class="card-mas">Ver el servicio →</span>
            </div>
          </a>"""

portada = cabecera("Jardinería, poda y tala en Zaragoza | " + MARCA,
    "Mantenimiento de jardines, riego, poda, tala, destoconado y desbroce de fincas en Zaragoza y alrededores. Nos ocupamos de todo, desde los permisos hasta la retirada de los restos.",
    "", "", SCHEMA) + f"""
  <section id="inicio" class="hero">
    <div class="container hero-inner">
      <div class="hero-text">
        <h1>Su jardín, sus árboles y su finca, en buenas manos</h1>
        <p class="hero-sub">Jardinería, riego, poda, tala y desbroce en Zaragoza y alrededores, para chalets, comunidades y fincas rústicas. Nos ocupamos de todo: desde pedir los permisos hasta llevarnos los restos.</p>
        <div class="hero-cta">
          <a class="btn btn-primary" href="{WA}" target="_blank" rel="noopener">Pedir presupuesto por WhatsApp</a>
          <a class="btn btn-ghost" href="tel:{TEL}">Llamar: {TEL_TXT}</a>
        </div>
      </div>
      {imagen("", "siega-cesped-jardin", "Jardinero segando el césped de un jardín con setos altos y un árbol de sombra", "(max-width: 900px) 100vw, 480px", "hero-image", primera=True)}
    </div>
  </section>

  <section class="highlight">
    <div class="container highlight-inner">
      <img class="highlight-icon" src="img/verdalia-hoja.svg" alt="" aria-hidden="true">
      <p><strong>Usted se despreocupa.</strong> Si el trabajo necesita permiso del ayuntamiento o de Medio Ambiente, lo tramitamos nosotros, y al terminar dejamos la zona limpia.</p>
    </div>
  </section>

  <section id="servicios" class="section">
    <div class="container">
      <h2>Servicios</h2>
      <p class="section-sub">De forma periódica o para un trabajo puntual.</p>
      <div class="cards cards-5">
          {tarjeta(SERVICIOS[0][0], SERVICIOS[0][1], "Siega, setos, riego y limpieza con visitas programadas. También plantación y reforma de zonas del jardín.", "jardin-chalet", "Jardín de un chalet con el césped cuidado, un seto alto y un parterre de flores junto a la casa")}
          {tarjeta(SERVICIOS[1][0], SERVICIOS[1][1], "Instalación y reparación de riego automático: aspersores, goteo, electroválvulas y programador.", "riego-arqueta-electrovalvulas", "Arqueta de riego abierta en el césped, con tres electroválvulas y sus llaves de paso")}
          {tarjeta(SERVICIOS[2][0], SERVICIOS[2][1], "Poda de formación, de limpieza y en altura. Revisamos si el árbol tiene grietas, pudriciones o ramas con riesgo.", "poda-en-altura-cuerdas", "Rama con cortes de poda limpios, cuerdas de trepa y una motosierra de poda colgada")}
          {tarjeta(SERVICIOS[3][0], SERVICIOS[3][1], "Tala controlada de árboles junto a casas, muros o cables, y retirada del tocón para recuperar el espacio.", "tala-tocon-motosierra", "Motosierra apoyada en el tocón de un árbol recién talado en un jardín")}
          {tarjeta(SERVICIOS[4][0], SERVICIOS[4][1], "Desbroce de parcelas y fincas para cumplir la normativa y reducir el riesgo de incendio.", "desbroce-tractor", "Tractor con desbrozadora limpiando el matorral junto a unas encinas")}
      </div>
    </div>
  </section>

  <section id="expres" class="section section-alt">
    <div class="container">
      <div class="panel">
        <div class="panel-intro">
          <span class="panel-badge">Respuesta rápida</span>
          <h2>Urgencias y trabajos exprés</h2>
          <p>Cuando algo no puede esperar, avísenos. Si es posible, vamos el mismo día.</p>
        </div>
        <ul class="lista-check">
          <li>Árboles o ramas que pueden caer tras un temporal.</li>
          <li>Recogida rápida de restos de poda o de ramas caídas.</li>
          <li>Poda o tala que no puede esperar por seguridad.</li>
          <li>Puesta a punto del jardín antes de una fecha señalada.</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="nosotros" class="section">
    <div class="container">
      <h2>Cómo trabajamos</h2>
      <div class="features">
        <div class="feature">
          <h3>Una sola persona de contacto</h3>
          <p>Habla siempre con la misma persona, del presupuesto al final del trabajo.</p>
        </div>
        <div class="feature">
          <h3>Trabajo seguro</h3>
          <p>Poda en altura y talas con técnica y equipo de seguridad, protegiendo su casa y sus árboles.</p>
        </div>
        <div class="feature">
          <h3>Presupuesto claro</h3>
          <p>Antes de empezar le decimos qué vamos a hacer y cuánto cuesta. Sin sorpresas.</p>
        </div>
      </div>
    </div>
  </section>

  <section id="zona" class="section section-alt">
    <div class="container zona-inner">
      <h2>Zona de servicio</h2>
      <p>Zaragoza capital y los municipios y urbanizaciones de alrededor: {ZONA_TXT}. Si no sabe si llegamos a su zona, pregúntenos sin compromiso.</p>
      <div class="mapa-embed" data-mapa="https://maps.google.com/maps?q=Calle%20Riglos%209%2C%2050012%20Zaragoza&amp;z=11&amp;output=embed">
        <button type="button" class="mapa-cargar">Ver el mapa (Google Maps)</button>
      </div>
    </div>
  </section>

  <section id="preguntas" class="section">
    <div class="container prosa prosa-centro">
      <h2>Preguntas frecuentes</h2>
      <div class="faq">{faq_html(FAQ_PORTADA)}</div>
    </div>
  </section>
""" + contacto() + pie("")
(OUT / "index.html").write_text(portada, encoding="utf-8")

# ---------- Páginas de servicio ----------
def pagina_servicio(slug, titulo_seo, desc, h1, intro, bloques, fotos, faq):
    raiz = "../"
    url = f"{DOM}/servicios/{slug}.html"
    nombre = dict(SERVICIOS)[slug]
    schema = ld(
        {"@type": "Service", "@id": url + "#servicio", "name": h1, "serviceType": nombre, "description": desc,
         "url": url, "provider": NEGOCIO_CORTO_LD, "areaServed": ZONA_LD},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": DOM + "/"},
            {"@type": "ListItem", "position": 2, "name": nombre, "item": url}]},
        faq_ld(faq))
    cuerpo = "".join(f"<h2>{t}</h2>{c}" for t, c in bloques)
    otros = "".join(f'<li><a href="{s}.html">{n}</a></li>' for s, n in SERVICIOS if s != slug)
    return cabecera(titulo_seo + " | " + MARCA, desc, f"servicios/{slug}.html", raiz, schema) + f"""
  <section class="page-hero">
    <div class="container prosa">
      <p class="migas"><a href="../">Inicio</a> › <a href="../#servicios">Servicios</a></p>
      <h1>{h1}</h1>
      <p class="hero-sub">{intro}</p>
      <div class="hero-cta">
        <a class="btn btn-primary" href="{WA}" target="_blank" rel="noopener">Pedir presupuesto por WhatsApp</a>
        <a class="btn btn-ghost" href="tel:{TEL}">Llamar: {TEL_TXT}</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container prosa">
      {galeria(raiz, fotos)}
      {cuerpo}
      <h2>Preguntas frecuentes</h2>
      <div class="faq">{faq_html(faq)}</div>
      <h2>Otros servicios</h2>
      <ul class="otros">{otros}</ul>
    </div>
  </section>
""" + contacto("Pídanos presupuesto") + pie(raiz)

r = "../"
(OUT / "servicios").mkdir(exist_ok=True)
paginas = {
"mantenimiento-de-jardines": pagina_servicio("mantenimiento-de-jardines",
    "Mantenimiento de jardines en Zaragoza",
    "Mantenimiento de jardines de chalets y comunidades en Zaragoza: siega, setos, riego, limpieza y plantación, con visitas programadas o trabajos puntuales.",
    "Mantenimiento de jardines en Zaragoza",
    "Cuidamos el jardín de su chalet o de su comunidad con visitas programadas, para que usted no tenga que pensar en él.",
    [("Qué incluye", "<ul class='lista-check'><li>Siega y perfilado del césped.</li><li>Recorte de setos y arbustos.</li><li>Poda ligera de árboles pequeños y frutales.</li><li>Revisión y ajuste del <a href='riego-automatico.html'>riego automático</a>, y arreglo de goteros y aspersores.</li><li>Limpieza de hojas, malas hierbas y restos, que nos llevamos.</li></ul>"),
     ("Visitas periódicas o trabajos sueltos", "<p>Puede contratar visitas cada semana, cada quince días o cada mes, según el tamaño del jardín y la época del año. También hacemos trabajos sueltos: una limpieza a fondo antes del verano, poner el jardín a punto antes de una celebración o cambiar una zona de césped por plantas que necesiten menos agua.</p>"),
     ("Plantación y reforma", "<p>Plantamos árboles, arbustos y césped nuevo, y rehacemos zonas del jardín pensando en el clima de Zaragoza: verano seco, cierzo y heladas. Le aconsejamos especies que aguanten bien y gasten poca agua.</p>")],
    [("jardin-chalet", "Jardín de un chalet con el césped cuidado, un seto alto y un parterre de flores junto a la casa", "Césped cuidado y parterre de flores."),
     ("restos-de-poda-saca", "Saca llena de ramas y restos de poda en un jardín", "Nos llevamos los restos.")],
    [("¿Cada cuánto conviene la visita?", "En primavera y verano el césped crece rápido y suele hacer falta una visita cada una o dos semanas. En otoño e invierno basta con una al mes."),
     ("¿Se llevan los restos?", "Sí. Al terminar recogemos hojas, ramas y césped cortado y nos los llevamos."),
     ("¿Trabajan para comunidades de vecinos?", "Sí, tanto para chalets particulares como para zonas verdes de comunidades y urbanizaciones.")]),
"riego-automatico": pagina_servicio("riego-automatico",
    "Riego automático en Zaragoza: instalación y reparación",
    "Instalación, reparación y puesta a punto de riego automático en jardines de Zaragoza: aspersores, goteo, electroválvulas y programadores. Arreglamos fugas y averías.",
    "Riego automático en Zaragoza",
    "Instalamos riego automático en jardines nuevos o ya hechos, y reparamos el que tiene: fugas, aspersores rotos, electroválvulas que no abren o programadores que fallan.",
    [("Instalación", "<ul class='lista-check'><li>Aspersores y difusores para el césped.</li><li>Goteo para setos, arbustos, árboles y huerto.</li><li>Electroválvulas en arqueta y programador, para que cada zona reciba el agua que necesita.</li><li>En jardines ya hechos abrimos zanjas estrechas, metemos la tubería y volvemos a tapar.</li></ul>"),
     ("Reparación y puesta a punto", "<p>Buscamos y arreglamos fugas, cambiamos aspersores, goteros y electroválvulas, y dejamos el programador ajustado. En primavera ponemos el riego en marcha y lo revisamos zona por zona; antes del invierno lo dejamos preparado para las heladas.</p>"),
     ("Regar bien con menos agua", "<p>En Zaragoza el verano es seco y el cierzo se lleva buena parte del agua de los aspersores. Programamos el riego de noche o de madrugada, ponemos goteo donde se puede y ajustamos los tiempos según la época del año.</p>")],
    [("riego-arqueta-electrovalvulas", "Arqueta de riego abierta en el césped, con tres electroválvulas y sus llaves de paso", "Arqueta con las electroválvulas."),
     ("riego-zanja-tuberia", "Zanja en el césped con una tubería de riego de polietileno y una pieza de conexión", "Tubería nueva en zanja.")],
    [("¿Se puede poner riego automático en un jardín ya hecho?", "Sí. Abrimos zanjas estrechas, metemos la tubería y volvemos a tapar. El césped se recupera en unas semanas."),
     ("¿A qué hora conviene regar?", "De noche o de madrugada. Se evapora menos agua y suele haber menos viento, que con los aspersores se nota mucho."),
     ("¿Qué hay que hacer con el riego en invierno?", "Con las heladas conviene cerrar el agua y vaciar la instalación, o al menos proteger las electroválvulas y el programador. Lo dejamos preparado en otoño y lo ponemos en marcha en primavera."),
     ("¿Arreglan un riego que ha instalado otra empresa?", "Sí. Reparamos fugas, aspersores y electroválvulas aunque la instalación no sea nuestra.")]),
"poda-de-arboles": pagina_servicio("poda-de-arboles",
    "Poda de árboles en Zaragoza",
    "Poda de árboles en Zaragoza: poda de formación, de limpieza y en altura, y revisión del estado del árbol (grietas, pudriciones y ramas con riesgo).",
    "Poda de árboles en Zaragoza",
    "Podamos árboles de jardín, de calle y de finca, también en altura. Antes de podar miramos el estado del árbol para saber qué necesita.",
    [("Tipos de poda", "<ul class='lista-check'><li><strong>De formación</strong>, en árboles jóvenes, para que crezcan con una buena estructura.</li><li><strong>De limpieza</strong>: ramas secas, rotas o enfermas.</li><li><strong>De seguridad</strong>: ramas que tocan el tejado, la fachada o los cables, o que pueden caer.</li><li><strong>En altura</strong>, con técnica de trepa cuando no llega una plataforma.</li></ul>"),
     ("Antes de podar, miramos el árbol", "<p>Muchos problemas no se ven a simple vista: grietas en la base, pudriciones dentro del tronco o heridas que sueltan resina. Revisamos el árbol y le decimos si basta con una poda o si conviene hacer algo más. Podar de más debilita el árbol, así que cortamos solo lo necesario.</p>"),
     ("Pinos y árboles protegidos", "<p>En algunos municipios hace falta permiso para podar o talar ciertos árboles. Si es su caso, lo tramitamos nosotros.</p>")],
    [("poda-en-altura-cuerdas", "Rama con cortes de poda limpios, cuerdas de trepa y una motosierra de poda colgada", "Poda en altura, con cuerdas.")],
    [("¿Cuándo es mejor podar?", "La mayoría de árboles se podan mejor en invierno, con la savia parada. Las ramas peligrosas o secas se pueden quitar en cualquier época."),
     ("¿Un árbol inclinado es peligroso?", "No siempre. Depende de si la inclinación es antigua, de cómo está la base y de si el suelo se ha levantado. Lo mejor es que lo veamos."),
     ("¿Se llevan las ramas?", "Sí. Troceamos y retiramos todos los restos, o los dejamos triturados si los quiere para el jardín.")]),
"tala-y-destoconado": pagina_servicio("tala-y-destoconado",
    "Tala de árboles y destoconado en Zaragoza",
    "Tala controlada de árboles junto a casas, muros o cables en Zaragoza, y destoconado para quitar el tocón y recuperar el espacio del jardín.",
    "Tala de árboles y destoconado en Zaragoza",
    "Talamos árboles en sitios difíciles, junto a casas, muros, coches o cables, bajándolos por partes cuando no hay sitio para que caigan enteros. Después quitamos el tocón si lo necesita.",
    [("Tala controlada", "<p>Cuando no hay espacio para que el árbol caiga entero, lo desmontamos por trozos desde arriba y los bajamos con cuerdas. Así no se daña nada alrededor. Si hace falta cortar la calle o pedir permiso al ayuntamiento, nos ocupamos nosotros.</p>"),
     ("Destoconado", "<p>El tocón que queda después de una tala estorba, vuelve a echar brotes y puede levantar el suelo. Lo quitamos con una destoconadora, que lo tritura por debajo del nivel del suelo, y dejamos el hueco listo para plantar, poner césped o pavimentar.</p>"),
     ("Qué nos llevamos", "<p>Tronco, ramas, serrín y restos del tocón. Si quiere quedarse la leña, se la dejamos cortada.</p>")],
    [("tala-tocon-motosierra", "Motosierra apoyada en el tocón de un árbol recién talado en un jardín", "Árbol talado: queda el tocón, que también quitamos.")],
    [("¿Necesito permiso para talar un árbol?", "Depende del municipio, de la especie y de si el terreno es urbano o rústico. Se lo decimos al ver el árbol y, si hace falta, lo pedimos nosotros."),
     ("¿Qué pasa si no quito el tocón?", "Muchos árboles vuelven a brotar desde el tocón y las raíces, y con los años se pudre y atrae hongos e insectos."),
     ("¿Se puede plantar en el mismo sitio?", "Sí. Después del destoconado rellenamos el hueco con tierra y ya se puede plantar.")]),
"desbroce-y-prevencion-de-incendios": pagina_servicio("desbroce-y-prevencion-de-incendios",
    "Desbroce de parcelas y fincas en Zaragoza",
    "Desbroce de parcelas, solares y fincas rústicas en Zaragoza para cumplir la normativa municipal y reducir el riesgo de incendio. Retirada de restos incluida.",
    "Desbroce de parcelas y fincas en Zaragoza",
    "Limpiamos parcelas, solares y fincas de hierba seca y matorral. Así cumple con el ayuntamiento y reduce el riesgo de que un fuego llegue a su casa.",
    [("Por qué desbrozar", "<p>La hierba seca y el matorral arden con mucha facilidad en verano. Muchos ayuntamientos obligan a tener las parcelas limpias y pueden multar si no lo están. En las urbanizaciones junto al monte, una franja limpia alrededor de las casas es la mejor protección frente a un incendio.</p>"),
     ("Qué hacemos", "<ul class='lista-check'><li>Desbroce de hierba y matorral, a mano o con la máquina que pida el terreno.</li><li>Poda de las ramas bajas de los árboles, para que el fuego no suba a las copas.</li><li>Franjas de protección alrededor de casas y vallas.</li><li>Retirada o triturado de todos los restos.</li></ul>"),
     ("Cuándo hacerlo", "<p>Lo mejor es desbrozar a finales de primavera, cuando la hierba ya ha crecido y antes de que se seque. En fincas grandes conviene repasar a finales de verano.</p>")],
    [("desbroce-tractor", "Tractor con desbrozadora limpiando el matorral junto a unas encinas", "Desbroce con tractor y desbrozadora.")],
    [("¿Me pueden multar si no desbrozo?", "Sí. Muchas ordenanzas municipales obligan a mantener limpios los solares y parcelas, sobre todo en verano."),
     ("¿Queman los restos?", "No. Los retiramos o los trituramos y los dejamos en el terreno, que protege el suelo."),
     ("¿Trabajan en fincas grandes?", "Sí. Díganos la superficie y le preparamos el presupuesto; en los bordes y junto a los árboles siempre se repasa a mano.")]),
}
for slug, contenido in paginas.items():
    (OUT / "servicios" / f"{slug}.html").write_text(contenido, encoding="utf-8")

# ---------- Páginas legales ----------
PEND = '<mark class="pendiente">[PENDIENTE: {}]</mark>'
def legal(slug, titulo, cuerpo):
    return cabecera(titulo + " | " + MARCA, titulo + " de " + MARCA + ".", slug + ".html", "") + f"""
  <section class="section">
    <div class="container prosa">
      <h1>{titulo}</h1>
      {cuerpo}
    </div>
  </section>
""" + pie("")

TITULAR = PEND.format("nombre y apellidos o razón social")
NIF = PEND.format("NIF")
(OUT / "aviso-legal.html").write_text(legal("aviso-legal", "Aviso legal", f"""
<p>En cumplimiento de la Ley 34/2002, de servicios de la sociedad de la información y de comercio electrónico (LSSI), le informamos de quién está detrás de esta web.</p>
<h2>Titular</h2>
<ul>
<li>Titular: {TITULAR}</li>
<li>NIF: {NIF}</li>
<li>Domicilio: {DIR}</li>
<li>Teléfono: {TEL_TXT}</li>
<li>Correo: <a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li>Nombre comercial: {MARCA}</li>
</ul>
<h2>Uso de la web</h2>
<p>Esta web informa de nuestros servicios y de cómo contactar con nosotros. Quien la usa se compromete a hacerlo de buena fe y conforme a la ley.</p>
<h2>Propiedad intelectual</h2>
<p>Los textos, fotos y logotipos de esta web son de su titular o se usan con permiso. No se pueden copiar ni reutilizar sin autorización. Algunas imágenes son ilustrativas y se han creado con inteligencia artificial.</p>
<h2>Enlaces</h2>
<p>Los enlaces a otras webs (WhatsApp, Google Maps) se ofrecen para su comodidad. No respondemos del contenido de esas webs.</p>
<h2>Ley aplicable</h2>
<p>Esta web se rige por la ley española.</p>
"""), encoding="utf-8")

(OUT / "privacidad.html").write_text(legal("privacidad", "Política de privacidad", f"""
<p>Esta política explica qué datos personales tratamos cuando nos contacta y qué derechos tiene, según el Reglamento General de Protección de Datos (RGPD) y la Ley Orgánica 3/2018.</p>
<h2>Responsable</h2>
<p>{TITULAR}, NIF {NIF}, {DIR}. Correo: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Qué datos tratamos y para qué</h2>
<p>Esta web no tiene formularios. Si nos llama, nos escribe por WhatsApp o nos manda un correo, usamos su nombre, teléfono, correo, dirección del trabajo y lo que nos cuente (incluidas fotos) solo para responderle, preparar el presupuesto y, si lo acepta, hacer el trabajo y facturarlo.</p>
<h2>Base legal</h2>
<p>Su petición de presupuesto y, si lo acepta, el contrato de servicio. Los datos de facturación se guardan porque lo exige la ley fiscal.</p>
<h2>Cuánto tiempo los guardamos</h2>
<p>Los de presupuestos que no se aceptan, un año como máximo. Los de clientes, lo que exijan las obligaciones fiscales y contables (en general, seis años).</p>
<h2>Con quién los compartimos</h2>
<p>Con nadie, salvo obligación legal. Si nos escribe por WhatsApp, WhatsApp (Meta) trata también sus datos según sus propias condiciones.</p>
<h2>Sus derechos</h2>
<p>Puede pedirnos ver, corregir o borrar sus datos, limitar u oponerse a su uso y llevárselos, escribiendo a <a href="mailto:{EMAIL}">{EMAIL}</a>. Si cree que no los tratamos bien, puede reclamar ante la Agencia Española de Protección de Datos (<a href="https://www.aepd.es" rel="noopener">aepd.es</a>).</p>
<h2>Analítica</h2>
<p>Si lo acepta, usamos Google Analytics para contar visitas. Lo explicamos en la <a href="cookies.html">política de cookies</a>.</p>
"""), encoding="utf-8")

(OUT / "cookies.html").write_text(legal("cookies", "Política de cookies", f"""
<p>Una cookie es un pequeño fichero que una web guarda en su navegador. Esta web solo usa las que usted acepte, salvo la que recuerda su decisión.</p>
<h2>Qué cookies usamos</h2>
<table class="tabla">
<thead><tr><th>Cookie</th><th>De quién</th><th>Para qué</th><th>Duración</th></tr></thead>
<tbody>
<tr><td>ajz_cookies (almacenamiento local)</td><td>Esta web</td><td>Recordar si aceptó o rechazó la analítica. Es necesaria.</td><td>Hasta que la borre</td></tr>
<tr><td>_ga, _ga_*</td><td>Google Analytics</td><td>Contar visitas y ver qué páginas se leen y desde dónde llegan. Solo si la acepta.</td><td>Hasta 2 años</td></tr>
</tbody>
</table>
<p>El mapa de la zona de servicio es de Google Maps y solo se carga si pulsa «Ver el mapa». Google puede poner entonces sus propias cookies.</p>
<h2>Cómo cambiar su decisión</h2>
<p>Pulse <a href="#" data-cookies-config>Configurar cookies</a> (también está al pie de cada página). También puede borrar las cookies desde la configuración de su navegador.</p>
"""), encoding="utf-8")

# ---------- sitemap ----------
HOY = date.today().isoformat()
urls = [""] + [f"servicios/{s}.html" for s, _ in SERVICIOS] + ["aviso-legal.html", "privacidad.html", "cookies.html"]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f"  <url><loc>{DOM}/{u}</loc><lastmod>{HOY}</lastmod></url>\n" for u in urls) + "</urlset>\n"
(OUT / "sitemap.xml").write_text(sm, encoding="utf-8")

# ---------- robots.txt: buscadores y asistentes de IA, todos bienvenidos ----------
BOTS_IA = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User",
           "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot-Extended", "Bingbot"]
(OUT / "robots.txt").write_text(
    "User-agent: *\nAllow: /\n\n"
    "# Asistentes de IA (ChatGPT, Claude, Perplexity, Gemini, Copilot...): pueden leer y citar la web.\n"
    + "".join(f"User-agent: {b}\n" for b in BOTS_IA) + "Allow: /\n\n"
    f"Sitemap: {DOM}/sitemap.xml\n", encoding="utf-8")

# ---------- llms.txt: resumen de la web en texto llano, para asistentes de IA ----------
RESUMEN = {
    "mantenimiento-de-jardines": "siega, setos, riego, limpieza y plantación en chalets y comunidades, con visitas programadas o trabajos sueltos.",
    "riego-automatico": "instalación, reparación y puesta a punto de riego automático: aspersores, goteo, electroválvulas y programadores.",
    "poda-de-arboles": "poda de formación, de limpieza, de seguridad y en altura, con revisión previa del estado del árbol.",
    "tala-y-destoconado": "tala controlada junto a casas, muros o cables, y retirada del tocón con destoconadora.",
    "desbroce-y-prevencion-de-incendios": "desbroce de parcelas, solares y fincas para cumplir la normativa y reducir el riesgo de incendio.",
}
(OUT / "llms.txt").write_text(f"""# {MARCA}

> {DESC_NEGOCIO}

## Datos

- Qué es: empresa de jardinería y arbolado para chalets, comunidades de vecinos y fincas rústicas.
- Dónde trabaja: Zaragoza capital y los municipios de alrededor ({ZONA_TXT}, entre otros).
- Teléfono y WhatsApp: {TEL_TXT} ({TEL})
- Correo: {EMAIL}
- Dirección: {DIR}, España
- Web: {DOM}/
- Presupuesto sin compromiso. Si el trabajo necesita permiso del ayuntamiento o de Medio Ambiente, lo tramita la empresa. Los restos se retiran al terminar.
- Urgencias: árboles o ramas con riesgo de caída tras un temporal; si es posible, el mismo día.

## Servicios

""" + "".join(f"- [{n}]({DOM}/servicios/{s}.html): {RESUMEN[s]}\n" for s, n in SERVICIOS) + f"""
## Legal

- [Aviso legal]({DOM}/aviso-legal.html)
- [Privacidad]({DOM}/privacidad.html)
""", encoding="utf-8")
print("ok")
