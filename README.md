# linkedin-imagenes

Imágenes de los posts de LinkedIn de Iker Pereira. Las prepara Claude con la skill `imagenes-linkedin`.

- `fondo/fondo-arboles.png`: fondo de árboles con niebla (el mismo del perfil).
- `plantilla/pantalla.py`: ayudas de dibujo (colores, fuentes Inter, tarjeta, texto).
- `plantilla/componer.py`: pone la pantalla al 82 % sobre el fondo, con sombra.
- `ejemplos/`: pantallas de prueba del 14/11/2026 (chat de IA, Excel, calendario, suscripciones).
- `posts/`: imágenes publicadas, `AAAA-MM-DD-tema.png` (1200×1200).

Uso:

```
python3 ejemplos/p1_chat.py /tmp/plano.png
python3 plantilla/componer.py /tmp/plano.png fondo/fondo-arboles.png posts/2026-11-16-ia-que-da-la-razon.png 0.82
```

Enlace público de una imagen (para Buffer):
`https://raw.githubusercontent.com/<usuario>/linkedin-imagenes/main/posts/<archivo>.png`
