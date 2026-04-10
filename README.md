# Eneagrama Esencial — Diagnóstico inicial profesional

App Flask con pago por Mercado Pago, test de eneagrama y generación de PDF.

Un diagnóstico claro para comenzar tu camino de autoconocimiento.

¿Para quién es?

* Personas que desean conocerse mejor
* Quienes repiten patrones y no saben por qué
* Personas en búsqueda vocacional
* Profesionales en proceso de crecimiento personal

Conocerte es el primer paso para transformarte.
Te invito a un maravilloso viaje hacia el centro de tu alma a través de esta técnica basada en 9 modelos de personalidad.

El Eneagrama no te encasilla.
Te revela.

En solo 15–20 minutos de cuestionario recibirás un informe profesional y personalizado en PDF.

¿Qué incluye?

✔ Eneatipo principal con descripción profunda
✔ Tu ala dominante
✔ Orientación vocacional base
✔ Gráfico radial personalizado
✔ Documento profesional descargable

¿Qué no incluye?

Este diagnóstico inicial no aborda análisis evolutivos profundos ni estructura mental completa.
Si luego deseas profundizar, podrás acceder al Informe Evolutivo Integral.

⏱ Cuestionario: 15–20 minutos
📩 Entrega automática en PDF

🎯 Lanzamiento 72 hs: $9.999 ARS
✨ Precio especial Marzo: $15.000 ARS
💰 Valor regular: $18.000 ARS
---

## Estructura de carpetas

```
eneagrama_esencial/
├── app.py
├── Procfile
├── requirements.txt
├── .python-version
├── .gitignore
├── extract_excel_to_json.py
├── data/
│   └── source.xlsx          ← tu Excel (NO se sube a git)
├── static/
│   ├── style.css
│   └── img/
│       └── logo_az.png
└── templates/
    ├── base.html
    ├── index.html
    ├── quiz.html
    ├── result.html
    ├── pago_fallido.html
    └── pago_pendiente.html
```

---

## Paso 1 — Generar questions.json (una sola vez en local)

Antes de subir a Heroku necesitás generar el archivo `data/questions.json`
a partir del Excel:

```bash
cd eneagrama_esencial
python extract_excel_to_json.py
```

Esto crea `data/questions.json`. **Incluilo en git** (está excluido por defecto
en .gitignore; quitá esa línea si querés incluirlo, o añadilo manualmente).

---

## Paso 2 — Crear repositorio en GitHub

```bash
cd eneagrama_esencial
git init
git add .
git commit -m "Initial commit - Eneagrama Esencial"
```

Crear repo en GitHub (sin README, sin .gitignore), luego:

```bash
git remote add origin https://github.com/TU_USUARIO/eneagrama-esencial.git
git branch -M main
git push -u origin main
```

---

## Paso 3 — Crear app en Heroku

```bash
heroku create eneagrama-esencial
```

O desde el dashboard de Heroku:
1. New → Create new app
2. Nombre: `eneagrama-esencial`
3. Region: United States (o el más cercano)

---

## Paso 4 — Agregar base de datos PostgreSQL

```bash
heroku addons:create heroku-postgresql:essential-0 --app eneagrama-esencial
```

Heroku setea automáticamente `DATABASE_URL` en las variables de entorno.

---

## Paso 5 — Configurar variables de entorno en Heroku

```bash
heroku config:set MP_ACCESS_TOKEN="TU_ACCESS_TOKEN_DE_MERCADO_PAGO" --app eneagrama-esencial
heroku config:set APP_URL="https://eneagrama-esencial.herokuapp.com" --app eneagrama-esencial
heroku config:set SECRET_KEY="una-clave-secreta-larga-y-aleatoria" --app eneagrama-esencial
```

También podés configurarlas desde el dashboard:
Settings → Config Vars → Reveal Config Vars

---

## Paso 6 — Vincular GitHub con Heroku y deployar

### Opción A: Deploy manual desde Heroku CLI
```bash
heroku git:remote -a eneagrama-esencial
git push heroku main
```

### Opción B: Deploy automático desde GitHub (recomendado)
1. En el dashboard de Heroku → Deploy → Deployment method → GitHub
2. Conectar con tu cuenta de GitHub
3. Buscar el repo `eneagrama-esencial`
4. Enable Automatic Deploys (desde `main`)
5. Deploy Branch → Deploy

---

## Paso 7 — Verificar que funciona

```bash
heroku open --app eneagrama-esencial
heroku logs --tail --app eneagrama-esencial
```

---

## Variables de entorno requeridas

| Variable         | Descripción                              |
|-----------------|------------------------------------------|
| `MP_ACCESS_TOKEN` | Access token de Mercado Pago (producción) |
| `APP_URL`         | URL pública de la app en Heroku          |
| `SECRET_KEY`      | Clave secreta para sesiones Flask        |
| `DATABASE_URL`    | Seteada automáticamente por Heroku       |

---

## Precio configurado

- **Producto:** Eneagrama Esencial — Diagnóstico inicial profesional
- **Precio:**
- Modificable en `app.py` → función `crear_preferencia` → `unit_price`

---

## Notas

- El archivo `data/questions.json` debe estar presente en el servidor.
  Si usás Git para deploymient, **no lo excluyas del .gitignore** o generalo
  como parte del build (ver Heroku buildpacks).
- Para actualizar el Excel: modificar `source.xlsx`, correr `extract_excel_to_json.py`,
  hacer commit y push.
