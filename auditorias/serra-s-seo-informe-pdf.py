# -*- coding: utf-8 -*-
"""Genera el informe de auditoría Serra-S en PDF ligero (fuentes base-14, sin incrustar)."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                KeepTogether, ListFlowable, ListItem, HRFlowable)

ACC = colors.HexColor('#0E5A6B'); ACC_SOFT = colors.HexColor('#E1EEF0')
INK = colors.HexColor('#172029'); MUTED = colors.HexColor('#5B6770'); LINE = colors.HexColor('#D8DEDC')
CRIT = colors.HexColor('#B3382C'); HIGH = colors.HexColor('#B8741B'); MED = colors.HexColor('#4A6FA5')
CRIT_S = colors.HexColor('#F7E6E3'); HIGH_S = colors.HexColor('#F8EEDC'); MED_S = colors.HexColor('#E4EBF5')

def st(name, **kw):
    base = dict(fontName='Helvetica', fontSize=10, leading=14, textColor=INK, alignment=TA_LEFT)
    base.update(kw); return ParagraphStyle(name, **base)

S = {
    'eyebrow': st('eyebrow', fontName='Helvetica-Bold', fontSize=7.5, leading=10, textColor=MUTED),
    'h1': st('h1', fontName='Helvetica-Bold', fontSize=21, leading=25, textColor=INK, spaceAfter=4),
    'h2': st('h2', fontName='Helvetica-Bold', fontSize=15, leading=18, textColor=INK, spaceBefore=14, spaceAfter=4),
    'h3': st('h3', fontName='Helvetica-Bold', fontSize=11.5, leading=14, textColor=INK),
    'lede': st('lede', fontSize=11, leading=15.5),
    'body': st('body'),
    'small': st('small', fontSize=9, leading=12.5, textColor=MUTED),
    'cell': st('cell', fontSize=8.5, leading=11),
    'cellbad': st('cellbad', fontSize=8.5, leading=11, textColor=CRIT),
    'th': st('th', fontName='Helvetica-Bold', fontSize=7.5, leading=10, textColor=MUTED),
    'fix': st('fix', fontSize=9.5, leading=13),
    'rank': st('rank', fontName='Helvetica-Bold', fontSize=22, leading=24, textColor=INK),
    'price': st('price', fontName='Helvetica-Bold', fontSize=20, leading=23, textColor=INK),
}

def P(t, s='body'): return Paragraph(t, S[s])

def pill(label, col, soft):
    t = Table([[Paragraph(f'<font color="{col.hexval()}"><b>{label}</b></font>', S['eyebrow'])]], colWidths=[22*mm])
    t.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), soft), ('LEFTPADDING', (0,0), (-1,-1), 5),
                           ('RIGHTPADDING', (0,0), (-1,-1), 5), ('TOPPADDING', (0,0), (-1,-1), 3), ('BOTTOMPADDING', (0,0), (-1,-1), 3)]))
    return t

def fixbox(text):
    t = Table([[Paragraph(f'<font color="{ACC.hexval()}"><b>SOLUCIÓN</b></font><br/>{text}', S['fix'])]], colWidths=[142*mm])
    t.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), ACC_SOFT), ('LINEBEFORE', (0,0), (0,-1), 2.2, ACC),
                           ('LEFTPADDING', (0,0), (-1,-1), 9), ('RIGHTPADDING', (0,0), (-1,-1), 9),
                           ('TOPPADDING', (0,0), (-1,-1), 7), ('BOTTOMPADDING', (0,0), (-1,-1), 7)]))
    return t

def bullets(items, style='body'):
    return ListFlowable([ListItem(P(i, style), leftIndent=10) for i in items], bulletType='bullet', bulletFontSize=7, leftIndent=12, bulletOffsetY=-1)

def finding(n, sev, title, body_flow, fix):
    col, soft = {'crit': (CRIT, CRIT_S), 'high': (HIGH, HIGH_S), 'med': (MED, MED_S)}[sev]
    label = {'crit': 'CRÍTICO', 'high': 'ALTO', 'med': 'MEDIO'}[sev]
    left = [P(str(n), 'rank'), Spacer(1, 3), pill(label, col, soft)]
    right = [P(title, 'h3'), Spacer(1, 4)] + body_flow + [Spacer(1, 5), fixbox(fix)]
    t = Table([[left, right]], colWidths=[26*mm, 146*mm])
    t.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LINEABOVE', (0,0), (-1,0), 0.6, LINE),
                           ('TOPPADDING', (0,0), (-1,-1), 9), ('BOTTOMPADDING', (0,0), (-1,-1), 9),
                           ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    return KeepTogether(t)

def grid_table(rows, widths, bad_cols=()):
    data = [[Paragraph(h, S['th']) for h in rows[0]]]
    for r in rows[1:]:
        data.append([Paragraph(c, S['cellbad'] if i in bad_cols else S['cell']) for i, c in enumerate(r)])
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F3F5F4')), ('LINEBELOW', (0,0), (-1,-1), 0.4, LINE),
                           ('BOX', (0,0), (-1,-1), 0.4, LINE), ('VALIGN', (0,0), (-1,-1), 'TOP'),
                           ('TOPPADDING', (0,0), (-1,-1), 5), ('BOTTOMPADDING', (0,0), (-1,-1), 5),
                           ('LEFTPADDING', (0,0), (-1,-1), 6), ('RIGHTPADDING', (0,0), (-1,-1), 6)]))
    return t

def plan(title, sub, price, items, term, lead=False):
    inner = [P(title, 'h3'), P(sub, 'small'), Spacer(1, 4), P(f'{price} <font size="8" color="{MUTED.hexval()}">IVA no incluido</font>', 'price'), Spacer(1, 4),
             bullets(items, 'cell'), Spacer(1, 4), P(term, 'small')]
    t = Table([[inner]], colWidths=[54*mm])
    t.setStyle(TableStyle([('BOX', (0,0), (-1,-1), 1.6 if lead else 0.5, ACC if lead else LINE), ('BACKGROUND', (0,0), (-1,-1), colors.white),
                           ('LEFTPADDING', (0,0), (-1,-1), 8), ('RIGHTPADDING', (0,0), (-1,-1), 8), ('TOPPADDING', (0,0), (-1,-1), 9), ('BOTTOMPADDING', (0,0), (-1,-1), 9), ('VALIGN', (0,0), (-1,-1), 'TOP')]))
    return t

def footer(canvas, doc):
    canvas.saveState(); canvas.setFont('Helvetica', 7.5); canvas.setFillColor(MUTED)
    canvas.drawString(19*mm, 11*mm, 'Auditoría SEO · SERRA-S Immobiliàries · Sultox · 7 de septiembre de 2026')
    canvas.drawRightString(A4[0]-19*mm, 11*mm, f'Página {doc.page}')
    canvas.restoreState()

doc = SimpleDocTemplate('auditoria-serra-s.pdf', pagesize=A4, leftMargin=19*mm, rightMargin=19*mm, topMargin=17*mm, bottomMargin=18*mm,
                        title='Auditoría SEO Serra-S', author='Sultox', subject='Auditoría SEO de serra-s.com')
F = []
# Cabecera
F += [HRFlowable(width='100%', thickness=3, color=ACC, spaceAfter=10), P('AUDITORÍA SEO RÁPIDA · SIN COSTE', 'eyebrow'), Spacer(1, 4),
      P('Qué le falta a serra-s.com para salir cuando alguien busca una inmobiliaria en Santa Susanna', 'h1'), Spacer(1, 6)]
meta = Table([[P('PARA', 'eyebrow'), P('WEB ANALIZADA', 'eyebrow'), P('FECHA', 'eyebrow'), P('PREPARADO POR', 'eyebrow')],
              [P('<b>SERRA-S Immobiliàries</b>'), P('<b>www.serra-s.com</b>'), P('<b>7 de septiembre de 2026</b>'), P('<b>Nacho · Sultox</b>')]], colWidths=[43*mm]*4)
meta.setStyle(TableStyle([('LINEABOVE', (0,0), (-1,0), 0.5, LINE), ('LINEBELOW', (0,-1), (-1,-1), 0.5, LINE), ('LEFTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 5), ('BOTTOMPADDING', (0,0), (-1,-1), 5)]))
F += [meta, Spacer(1, 10), P('Hemos comprobado vuestra web página a página, lo que Google tiene indexado de serra-s.com y serra-s.es, cómo aparecéis en los portales y cómo salen vuestros competidores directos en Santa Susanna. Este documento recoge lo que falla, en qué orden arreglarlo y cuánto cuesta si queréis que lo hagamos nosotros.', 'lede')]

# Resumen
F += [P('Resumen en tres líneas', 'h2'), ListFlowable([
    ListItem(P('La web corporativa está bien montada por dentro (redirecciones, mapa del sitio, caché), pero <b>Google no sabe qué sois ni dónde estáis</b>: la portada se titula "Inici", ninguna página tiene descripción y el plugin de SEO está instalado sin configurar.')),
    ListItem(P('<b>Los inmuebles no están en la web.</b> Viven en serra-s.es, vuestra web de Inmovilla, donde el listado tiene el mismo título que la portada y cada ficha se titula con el titular comercial del agente, sin marca ni "en venta". De más de 100 inmuebles, en nuestras búsquedas Google solo muestra uno, y ya retirado.')),
    ListItem(P('Lo primero se arregla en <b>una semana sin tocar el diseño</b>. Lo segundo tiene solución conocida porque Inmovilla lo permite: plantilla actual o conexión con la web.')),
], bulletType='1', bulletFontName='Helvetica-Bold', bulletColor=ACC, leftIndent=14)]

# Hallazgos
F += [P('Hallazgos, por orden de prioridad', 'h2'), P('Comprobados directamente sobre la web el 7 de septiembre de 2026. Los dos primeros explican la mayor parte del problema.', 'small'), Spacer(1, 6)]

t1 = grid_table([['Página', 'Título real', 'Descripción'],
                 ['www.serra-s.com/', 'Inici', 'Ninguna'],
                 ['/es/serra-s-inmobiliaries-compraventa-de-inmuebles/', 'Inicio', 'Ninguna'],
                 ['/contacte/', 'Contacte - SERRA-S inmobiliàries | Compraventa de inmuebles, Alquiler', 'Ninguna'],
                 ['/es/noticias/', 'Noticias - SERRA-S inmobiliàries | Compraventa de inmuebles, Alquiler', 'Google lo corta'],
                 ['www.serra-s.es/ (y todas sus páginas)', 'SERRA-S inmobiliàries | Compraventa de inmuebles, Alquil...', 'Lista de servicios, sin localidad']],
                [50*mm, 60*mm, 32*mm], bad_cols=(1, 2))
F.append(finding(1, 'crit', 'Los títulos no dicen a qué os dedicáis ni dónde, y no hay descripciones', [
    P('El título es lo primero que Google lee y lo que la gente ve en azul en los resultados. La descripción es el texto gris de debajo. Esto es lo que tiene cada página ahora mismo:'), Spacer(1, 4), t1, Spacer(1, 5),
    P('Ni "inmobiliaria" ni "Santa Susanna" aparecen en ningún título. Google intenta arreglarlo por su cuenta: a veces muestra la portada como "SERRA-S inmobiliàries" en vez de "Inici". En serra-s.es el título ya viene cortado con puntos suspensivos desde el propio código.'), Spacer(1, 4),
    P('Para comparar: la página de inmuebles en venta de VirtuaHome, vuestra competencia directa, sale con el título <i>"La Mejor Inmobiliaria de Santa Susana | VirtuaHome.es"</i>. Su portada, en cambio, se titula "INICIO - VIRTUA HOME": la mayoría de agencias de la zona tienen el mismo problema que vosotros, y quien lo arregle primero se lleva las búsquedas. En Santa Susanna hay 47 agencias dadas de alta en idealista.')],
    'Tenéis Yoast SEO instalado y funcionando: solo hay que rellenarlo. Un título y una descripción por página, en catalán y castellano. Ejemplo para la portada: <b>"Inmobiliaria en Santa Susanna · Compra, venta y alquiler en el Maresme | SERRA-S"</b>. Es trabajo de configuración, no de programación.'))

F.append(finding(2, 'crit', 'Los inmuebles viven fuera de la web y Google no los ve', [bullets([
    'La web corporativa www.serra-s.com tiene 15 páginas y ninguna ficha de inmueble ni página de comprar, vender o alquilar. El menú envía a serra-s.es/venta.php.',
    'serra-s.es es vuestra web de Inmovilla. La página de listado tiene el mismo título y la misma descripción que la portada: la página que debería salir por "pisos en venta en Santa Susanna" no dice ni "venta" ni "Santa Susanna".',
    'Cada ficha se titula con el titular comercial que escribe el agente, por ejemplo <i>"VIVE DE VACACIONES TODO EL AÑO: PARCELA con DOS módulos..."</i>: en mayúsculas, cortado a 60 caracteres, sin "en venta", sin precio y sin la marca. Y el encabezado principal de la ficha no es el inmueble, es "Encuentra la casa de tus sueños".',
    'Las direcciones antiguas de las fichas (formato ficha/index.php?codigo=...), que son las que Google conoce, muestran la portada en vez de llevar a la ficha nueva o avisar de que el inmueble ya no está.',
    '7 de las 16 fotos de la portada de serra-s.es no tienen texto alternativo, y la portada tiene 15 encabezados principales en vez de uno.']), Spacer(1, 4),
    P('Resultado: tenéis 85 inmuebles en idealista y 111 en habitaclia, y en nuestras búsquedas Google solo muestra una ficha vuestra, y ya retirada. Cada búsqueda de "casa en venta en Canet de Mar" o "terreno en Premià de Dalt" se la llevan los portales, donde pagáis por aparecer.')],
    'Título automático estructurado en cada ficha (tipo, "en venta", municipio, zona, metros, precio y marca) delante del titular comercial; el inmueble como encabezado principal; listado con título y descripción propios; redirección de las direcciones antiguas; datos estructurados; y páginas de comprar, vender y alquilar en la web corporativa que enlacen a las fichas. Estas plantillas las gestiona Inmovilla y se ajustan a través de ellos; la alternativa es el conector Inmovilla a WordPress para tener todo bajo www.serra-s.com.'))

F.append(finding(3, 'high', 'Las fichas antiguas de serra-s.com dan error', [
    P('Google todavía muestra direcciones de vuestro buscador anterior, como /es/compra/terrenos/barcelona/premia-de-dalt/528 (un terreno en Premià de Dalt a 660.000 €). Quien hace clic ve "Page not found". Es lo que pasa cuando se cambia de plataforma sin redirigir las direcciones viejas: se pierde el tráfico y la confianza de Google en el dominio.')],
    'Redirección permanente de todas las direcciones antiguas del buscador a su ficha equivalente o a la página de compra. Enviar a Google la lista para que limpie el índice.'))

F.append(finding(4, 'med', 'Google recibe páginas que no debería ver', [
    P('El mapa del sitio que la web envía a Google incluye páginas de plantilla que no son para el público: /qality/, /excellence/, /es/footer-esp/, /es/qality-esp/ y /es/excellence-2/ son bloques de diseño del tema, no páginas. Incluye también los 19 archivos de categoría del blog, y Google tiene indexado el archivo vacío "Sense categoria". Todo eso diluye la calidad del sitio a ojos de Google.')],
    'Marcar como no indexables las páginas de plantilla y los archivos de categoría, etiqueta, autor y adjuntos, y sacarlos del mapa del sitio. Diez minutos en Yoast.'))

F.append(finding(5, 'med', 'Señalización de idiomas incompleta', [
    P('La web sí le indica a Google qué versión es catalana y cuál castellana (etiquetas hreflang). Pero la portada catalana declara además una versión inglesa en /en/ que está vacía: muestra "Nothing Found" y aun así es indexable. Las páginas en catalán llevan la coletilla del título en castellano ("Contacte - ... Compraventa de inmuebles, Alquiler"), y la portada de noticias en catalán tiene la dirección en castellano (/noticias/).')],
    'Etiquetas de idioma coherentes, coletilla en el idioma de cada versión, y una de dos con el inglés: versión real (portada, comprar, contacto) para captar al comprador extranjero, que en Santa Susanna es mucho, o retirar la página vacía del índice.'))

F.append(finding(6, 'med', 'La marca está escrita de tres maneras', [
    P('En los títulos de la web predomina "SERRA-S <b>inmobiliàries</b>" (mezcla de castellano y catalán); en idealista y en vuestro logo, "SERRA-S <b>immobiliàries</b>"; y en habitaclia y en vuestra firma de correo, "SERRA-S <b>Gestions Immobiliàries</b>". Para Google son tres nombres distintos.')],
    'Elegir una forma y usarla igual en web, portales, Google Maps, Facebook y firma de correo.'))

F.append(finding(7, 'med', 'La portada en castellano tiene una dirección larga y tres saltos', [
    P('Para llegar a la portada en castellano, serra-s.com/es salta a www.serra-s.com/es, luego a /es/inicio/, y de ahí a /es/serra-s-inmobiliaries-compraventa-de-inmuebles/, que es la que Google indexa. Funciona, pero cada salto resta velocidad y claridad.')],
    'Portada castellana directamente en www.serra-s.com/es/ y un solo salto desde las demás direcciones.'))

F.append(finding(8, 'med', 'Datos de contacto distintos según dónde se mire', [
    P('En los portales vuestra dirección aparece como "Carretera N-II km 673, Centro Comercial Carrefour" y también como "N-2, 11, 08398 Santa Susanna". Google Maps cruza estos datos: si no coinciden, baja la confianza en vuestra ficha de empresa y salís peor en el mapa.')],
    'Mismo nombre, dirección, teléfono y horario en web, ficha de Google, idealista, habitaclia y Facebook.'))

F.append(finding(9, 'med', 'Mucho blog, nada local', [
    P('Tenéis 45 artículos publicados en catalán y castellano, y eso es un activo. Pero todos son noticias generales del sector (euríbor, IBI, decoración, normativa de ascensores) y solo uno habla del Maresme. Ninguno menciona Santa Susanna, Malgrat, Pineda, Calella ni Canet. Google posiciona por lo que se escribe: hoy el blog no os trae ni una búsqueda local.')],
    'Cinco páginas de zona (una por municipio donde tenéis cartera) y un artículo local al mes rinden más que cuarenta noticias nacionales.'))

# Lo que está bien / comprobaciones
def checklist(items):
    return ListFlowable([ListItem(P(i)) for i in items], bulletType='bullet', start='□', bulletFontSize=8, bulletColor=ACC, leftIndent=12)
F += [P('Lo que ya está bien', 'h2'), P('Para que se vea que no todo falla. Esto lo hemos comprobado y no hay que tocarlo.', 'small'), Spacer(1, 4), checklist([
    'Redirecciones de http a https y de serra-s.com a www: correctas', 'robots.txt y mapa del sitio generados por Yoast: correctos', 'Etiqueta canonical en cada página de la web corporativa',
    'Todas las fotos de la web corporativa tienen texto alternativo', 'Un solo encabezado principal por página en la web corporativa', 'Idioma declarado en cada página (catalán / castellano)',
    'Caché de servidor activa (W3 Total Cache con Redis)', 'Blog activo con 45 artículos en dos idiomas'])]
F += [P('Comprobaciones técnicas incluidas', 'h2'), P('Se revisan y corrigen dentro de la Fase 1. No se cobran aparte.', 'small'), Spacer(1, 4), checklist([
    'Velocidad de carga en móvil y escritorio', 'Datos estructurados de empresa (nombre, dirección, horario, zona)', 'Ficha de Google Maps revisada y unificada',
    'Google Search Console configurado y mapa del sitio enviado', 'Fotos sin texto alternativo en serra-s.es', 'Versión móvil y botones de llamada y WhatsApp'])]

# Plan
plans = Table([[
    plan('Fase 1 · Base', 'Arregla los hallazgos 1, 3, 4, 5, 6, 7 y 8', '450 €', [
        'Títulos y descripciones de todas las páginas en catalán y castellano', 'Redirecciones de las direcciones antiguas del buscador', 'Páginas de plantilla y archivos fuera del índice y del mapa del sitio',
        'Etiquetas de idioma coherentes y página inglesa vacía resuelta', 'Portada castellana en /es/ con un solo salto', 'Marca unificada, ficha de Google Maps y Search Console',
        'Propuesta cerrada para los inmuebles (plantilla Inmovilla o conexión con la web)'], 'Plazo: 1 semana', lead=True),
    plan('Fase 2 · Inmuebles y zona', 'Arregla los hallazgos 2 y 9 y abre nuevas búsquedas', '890 €', [
        'Título, descripción y datos estructurados automáticos en todas las fichas', 'Listado con título propio y redirección de las fichas antiguas', 'Páginas de comprar, vender y alquilar en la web corporativa',
        '5 páginas de zona: Santa Susanna, Malgrat, Pineda, Calella y Canet', 'Versión inglesa mínima (portada, comprar, contacto)', 'Mejora de velocidad'], 'Plazo: 2 semanas'),
    plan('Fase 1 + 2', 'Todo lo anterior, en un solo encargo', '1.190 €', [
        'Ahorro de 150 € frente a contratar por separado', 'Un único interlocutor y una única entrega', 'Informe de resultados a los 30 días'], 'Plazo: 3 semanas'),
]], colWidths=[57*mm]*3)
plans.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 1.5), ('RIGHTPADDING', (0,0), (-1,-1), 1.5), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
F += [KeepTogether([P('Plan de acción y precios cerrados', 'h2'), P('Sin cuotas mensuales. Precio fijo por fase, con informe de antes y después en Google Search Console.', 'small'), Spacer(1, 8), plans, Spacer(1, 8),
      P('Si para los inmuebles se opta por conectar Inmovilla con la web corporativa, la licencia del conector se paga aparte al proveedor, a su precio, sin recargo nuestro. Si preferís hacerlo con vuestro proveedor actual, este documento sirve como lista de tareas. No hay ningún compromiso por haber pedido la auditoría.', 'small')])]

# Qué esperar
exp = Table([[P(f'<font color="{ACC.hexval()}"><b>Semanas 1 a 2</b></font>'), P('Google reindexa los títulos nuevos. Empezáis a aparecer por "inmobiliaria Santa Susanna" y variantes en catalán y castellano.')],
             [P(f'<font color="{ACC.hexval()}"><b>Meses 1 a 2</b></font>'), P('Las fichas de inmuebles empiezan a recibir visitas directas desde Google, sin pasar por idealista ni habitaclia.')],
             [P(f'<font color="{ACC.hexval()}"><b>Mes 3</b></font>'), P('Con las páginas de zona, presencia en los cinco municipios del Alt Maresme donde tenéis cartera.')]], colWidths=[32*mm, 140*mm])
exp.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 3), ('BOTTOMPADDING', (0,0), (-1,-1), 3)]))
F += [KeepTogether([P('Qué esperar', 'h2'), Spacer(1, 4), exp, Spacer(1, 14), HRFlowable(width='100%', thickness=0.6, color=LINE, spaceAfter=8),
      P('<b>Nacho · Sultox</b> · Agencia digital · Maresme y Barcelona &nbsp;&nbsp;·&nbsp;&nbsp; WhatsApp <b>+34 722 83 50 57</b> · sultox.com', 'small')])]

doc.build(F, onFirstPage=footer, onLaterPages=footer)
print('ok')
