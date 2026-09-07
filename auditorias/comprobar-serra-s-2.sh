out="$HOME/Desktop/serra-s-check2.txt"
UA='Mozilla/5.0 (Macintosh) Sultox-check'
{
  echo "Comprobacion 2 serra-s.com  $(date '+%Y-%m-%d %H:%M')"
  echo; echo "### ESTADO DE URLS"
  for u in https://www.serra-s.com/en/ https://www.serra-s.com/es/inicio/ https://www.serra-s.com/es/contacto/ https://www.serra-s.com/es/compra/terrenos/barcelona/premia-de-dalt/528 https://serra-s.com/es/content/certif-energetico https://www.serra-s.es/es https://www.serra-s.es/ca https://www.serra-s.es/en; do
    printf '%s : ' "$u"; curl -sS -o /dev/null -w '%{http_code} -> %{redirect_url}\n' --max-time 20 -A "$UA" "$u" 2>&1
  done
  for sm in page post category; do
    echo; echo "### SITEMAP $sm"
    curl -sS --max-time 20 -A "$UA" "https://www.serra-s.com/$sm-sitemap.xml" | perl -ne 'while (/<loc>([^<]+)<\/loc>/g) { print "$1\n" }'
  done
  echo; echo "### SERRA-S.ES en castellano"
  curl -sSL --max-time 30 -A "$UA" -H 'Accept-Language: es-ES,es;q=0.9' https://www.serra-s.es/ | perl -0777 -ne 'while (/<title[^>]*>[^<]*<\/title>|<meta[^>]+name=["\x27]description["\x27][^>]*>|<link[^>]+canonical[^>]*>|<link[^>]+hreflang=[^>]*>|<html[^>]*>|<meta[^>]+generator[^>]*>/ig) { my $m = $&; $m =~ s/\s+/ /g; print substr($m, 0, 250), "\n" }'
  echo; echo "### FICHA de serra-s.es (Canet)"
  curl -sSL --max-time 30 -A "$UA" -H 'Accept-Language: es-ES,es;q=0.9' 'https://www.serra-s.es/ficha/index.php?codigo=12449_23982185' | perl -0777 -ne 'while (/<title[^>]*>[^<]*<\/title>|<meta[^>]+name=["\x27]description["\x27][^>]*>|<link[^>]+canonical[^>]*>|<h1[^>]*>.*?<\/h1>|application\/ld\+json/ig) { my $m = $&; $m =~ s/\s+/ /g; print substr($m, 0, 250), "\n" }'
  echo; echo "### ENLACES de www.serra-s.com hacia serra-s.es y menu"
  curl -sSL --max-time 30 -A "$UA" https://www.serra-s.com/ | perl -ne 'while (/href=["\x27](https?:\/\/[^"\x27]*serra-s\.es[^"\x27]*|[^"\x27]*(compra|venda|lloguer|venta|alquiler|inmuebles|immobles|propietats|serveis|servicios)[^"\x27]*)["\x27]/ig) { print "$1\n" }' | sort -u | head -40
  echo; echo "### PISTAS del proveedor de serra-s.es"
  curl -sSL --max-time 30 -A "$UA" https://www.serra-s.es/ | perl -ne 'while (/(generator|powered|copyright|desarrollad|dise[nñ]ad|inmovilla|witei|mobilia|inmoweb|habitania|sooprema|idealista|api\.[a-z0-9.-]+\.[a-z]+|https?:\/\/[a-z0-9.-]+\.(com|es|net|cat)\/[^"\x27 <>]*\.js)[^"\x27<>]{0,80}/ig) { print "$&\n" }' | sort -u | head -40
  echo; echo "Listo. Archivo: $out"
} 2>&1 | tee "$out"
open -e "$out"
