#!/usr/bin/env python3
"""Prepara las fotos para la web: las pasa a WebP, sin datos GPS ni de cámara.

Uso (desde la raíz del repositorio):

    python herramientas/preparar_fotos.py CARPETA_CON_FOTOS

De cada foto de la carpeta (jpg, png o webp) saca dos ficheros en img/fotos/:
`nombre.webp` (1200 px de lado mayor como máximo) y `nombre-600.webp` (para
móviles y miniaturas). El nombre del fichero es el que se usa luego en
`generar_paginas.py`. Sin carpeta, solo repasa las que ya hay en img/fotos/.

Al final apunta las medidas de todas en img/fotos/medidas.json, que es de donde
las lee `generar_paginas.py`.
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageOps

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "img" / "fotos"
LADO_MAX, ANCHO_MINI = 1200, 600
COMPARTIR = "jardin-chalet"


def guardar(im, ruta, calidad):
    # Imagen nueva sin metadatos: así no viajan el GPS ni el modelo del móvil.
    limpia = Image.new("RGB", im.size)
    limpia.paste(im)
    limpia.save(ruta, "WEBP", quality=calidad, method=6)


def mini(im, nombre):
    m = im.copy()
    if m.width > ANCHO_MINI:
        m = m.resize((ANCHO_MINI, round(m.height * ANCHO_MINI / m.width)), Image.LANCZOS)
    guardar(m, DESTINO / f"{nombre}-600.webp", 74)


def main():
    DESTINO.mkdir(parents=True, exist_ok=True)
    if len(sys.argv) > 1:
        for f in sorted(Path(sys.argv[1]).iterdir()):
            if f.suffix.lower() not in (".jpg", ".jpeg", ".png", ".webp"):
                continue
            im = ImageOps.exif_transpose(Image.open(f)).convert("RGB")
            im.thumbnail((LADO_MAX, LADO_MAX), Image.LANCZOS)
            guardar(im, DESTINO / f"{f.stem}.webp", 76)
            mini(im, f.stem)
            print(f"{f.stem}: {im.width} x {im.height}")

    medidas = {}
    for f in sorted(DESTINO.glob("*.webp")):
        if f.stem.endswith("-600"):
            continue
        im = Image.open(f).convert("RGB")
        if not (DESTINO / f"{f.stem}-600.webp").exists():
            mini(im, f.stem)
        medidas[f.stem] = [im.width, im.height]
    (DESTINO / "medidas.json").write_text(json.dumps(medidas, indent=1) + "\n", encoding="utf-8")
    print(f"{len(medidas)} fotos en img/fotos/")

    # La foto que enseñan WhatsApp y las redes al pegar el enlace de la web (en JPG, 1200 x 630).
    origen = DESTINO / f"{COMPARTIR}.webp"
    if origen.exists():
        im = ImageOps.fit(Image.open(origen).convert("RGB"), (1200, 630), Image.LANCZOS, centering=(0.5, 0.6))
        im.save(RAIZ / "img" / "compartir.jpg", "JPEG", quality=84, optimize=True)


if __name__ == "__main__":
    main()
