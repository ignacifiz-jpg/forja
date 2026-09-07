out="$HOME/Desktop/serra-s-check3.txt"
UA='Mozilla/5.0 (Macintosh) Sultox-check'
{
  echo "Comprobacion 3  $(date '+%Y-%m-%d %H:%M')"
  echo; echo "### venta.php de serra-s.es"
  curl -sSL --max-time 30 -A "$UA" -H 'Accept-Language: es-ES,es' https://www.serra-s.es/venta.php | perl -0777 -ne 'while (/<title[^>]*>[^<]*<\/title>|<meta[^>]+name=["\x27]description["\x27][^>]*>|<link[^>]+canonical[^>]*>/ig) { my $m = $&; $m =~ s/\s+/ /g; print substr($m, 0, 250), "\n" }'
  echo; echo "### ENLACES a fichas encontrados en venta.php"
  links=$(curl -sSL --max-time 30 -A "$UA" -H 'Accept-Language: es-ES,es' https://www.serra-s.es/venta.php | perl -ne 'while (/href=["\x27]([^"\x27]*(ficha|codigo=)[^"\x27]*)["\x27]/ig) { print "$1\n" }' | sort -u | head -5)
  echo "$links"
  first=$(echo "$links" | head -1)
  case $first in
    http*) u=$first;;
    /*) u="https://www.serra-s.es$first";;
    *) u="https://www.serra-s.es/$first";;
  esac
  echo; echo "### PRIMERA FICHA VIVA: $u"
  curl -sSL --max-time 30 -A "$UA" -H 'Accept-Language: es-ES,es' "$u" | perl -0777 -ne 'while (/<title[^>]*>[^<]*<\/title>|<meta[^>]+name=["\x27]description["\x27][^>]*>|<meta[^>]+og:title[^>]*>|<link[^>]+canonical[^>]*>|<h1[^>]*>.*?<\/h1>|application\/ld\+json/ig) { my $m = $&; $m =~ s/\s+/ /g; print substr($m, 0, 250), "\n" }'
  echo; echo "### /en/ de la web corporativa"
  curl -sSL --max-time 30 -A "$UA" https://www.serra-s.com/en/ | perl -0777 -ne 'while (/<title[^>]*>[^<]*<\/title>|<meta[^>]+name=["\x27](description|robots)["\x27][^>]*>|<link[^>]+canonical[^>]*>|<link[^>]+hreflang=[^>]*>|<h1[^>]*>.*?<\/h1>/ig) { my $m = $&; $m =~ s/\s+/ /g; print substr($m, 0, 250), "\n" }'
  echo; echo "Listo. Archivo: $out"
} 2>&1 | tee "$out"
open -e "$out"
