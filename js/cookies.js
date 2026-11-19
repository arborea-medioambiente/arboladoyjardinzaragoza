/* Cookies y analítica: Google Analytics solo se activa si el visitante lo acepta.
   La decisión se guarda en localStorage ("ajz_cookies" = "si" | "no"). */
(function () {
  var GA_ID = 'G-3S94ZZ80TG';
  var CLAVE = 'ajz_cookies';

  function leer() { try { return localStorage.getItem(CLAVE); } catch (e) { return null; } }
  function guardar(v) { try { localStorage.setItem(CLAVE, v); } catch (e) {} }

  window.dataLayer = window.dataLayer || [];
  function gtag() { dataLayer.push(arguments); }
  window.gtag = gtag;
  gtag('consent', 'default', { analytics_storage: 'denied', ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied' });

  var cargado = false;
  function activarAnalitica() {
    gtag('consent', 'update', { analytics_storage: 'granted' });
    if (cargado) return;
    cargado = true;
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(s);
    gtag('js', new Date());
    gtag('config', GA_ID);
  }

  if (leer() === 'si') activarAnalitica();

  // Clics en llamar, WhatsApp o correo, con su motivo (para clasificar los contactos)
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    if (a.hasAttribute('data-cookies-config')) { e.preventDefault(); mostrarAviso(); return; }
    var h = a.getAttribute('href'), m = null;
    if (/^tel:/i.test(h)) m = 'telefono';
    else if (/wa\.me\//i.test(h)) m = 'whatsapp';
    else if (/^mailto:/i.test(h)) m = 'correo';
    if (m && cargado) gtag('event', 'contact_click', { method: m, motivo: 'jardineria' });
  });

  function mostrarAviso() {
    if (document.getElementById('aviso-cookies')) return;
    var raiz = document.querySelector('link[rel="stylesheet"][href$="css/styles.css"]');
    var base = raiz ? raiz.getAttribute('href').replace('css/styles.css', '') : '';
    var d = document.createElement('div');
    d.id = 'aviso-cookies';
    d.className = 'aviso-cookies';
    d.setAttribute('role', 'dialog');
    d.setAttribute('aria-label', 'Aviso de cookies');
    d.innerHTML = '<p>Usamos Google Analytics para contar las visitas, solo si usted lo acepta. ' +
      '<a href="' + base + 'cookies.html">Más información</a>.</p>' +
      '<div class="aviso-botones"><button type="button" class="btn btn-ghost" data-v="no">Rechazar</button>' +
      '<button type="button" class="btn btn-primary" data-v="si">Aceptar</button></div>';
    d.addEventListener('click', function (e) {
      var v = e.target.getAttribute && e.target.getAttribute('data-v');
      if (!v) return;
      guardar(v);
      if (v === 'si') activarAnalitica();
      else gtag('consent', 'update', { analytics_storage: 'denied' });
      d.remove();
    });
    document.body.appendChild(d);
  }

  // Mapa de Google: solo se carga al pulsar el botón
  document.addEventListener('click', function (e) {
    var b = e.target.closest && e.target.closest('.mapa-cargar');
    if (!b) return;
    var cont = b.parentNode;
    var f = document.createElement('iframe');
    f.src = cont.getAttribute('data-mapa');
    f.title = 'Zona de servicio en Zaragoza';
    f.loading = 'lazy';
    f.referrerPolicy = 'no-referrer-when-downgrade';
    cont.innerHTML = '';
    cont.appendChild(f);
  });

  document.addEventListener('DOMContentLoaded', function () {
    var v = leer();
    if (v !== 'si' && v !== 'no') mostrarAviso();
  });
})();
