# Gaviria Fajardo — Sitio Web Corporativo

Sitio web institucional desarrollado a la medida para una firma jurídica en Colombia. Presenta los servicios legales, el equipo de abogados, y la identidad corporativa (misión, visión, valores) de la firma. Construido como un monolito con Wagtail CMS sobre Django, lo que permite al cliente gestionar todo el contenido de forma autónoma desde un panel de administración.

> 🏢 Proyecto desarrollado por **[EnocDev](https://github.com/enocdev)** como parte de los servicios de desarrollo web a la medida para empresas del sector privado.

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.1-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Wagtail](https://img.shields.io/badge/Wagtail-2.12-43B1B0?logo=wagtail&logoColor=white)](https://wagtail.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-11-336791?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)

---

## 🎯 Contexto

La firma necesitaba un sitio web profesional que transmitiera confianza y seriedad, y que pudiera ser actualizado por personal no técnico sin depender de un desarrollador para cada cambio de texto o imagen. Wagtail fue la elección ideal: ofrece un panel de administración intuitivo sobre la robustez de Django, con un sistema de páginas jerárquico que se adapta naturalmente a la estructura de un sitio corporativo.

## ✨ Funcionalidades

- ✅ **Páginas de contenido dinámico** — servicios legales, equipo de abogados, misión y visión, editables desde el admin de Wagtail
- ✅ **Panel de administración** — interfaz amigable para que el cliente gestione contenido sin conocimientos técnicos
- ✅ **Sistema de páginas jerárquico** — estructura de contenido organizada por secciones con navegación automática
- ✅ **Assets optimizados con Webpack** — bundling de JS y CSS para carga eficiente en producción
- ✅ **Despliegue con Dokku** — configuración production-ready con deploy vía `git push`
- ✅ **Contenedores Docker** — entorno de desarrollo reproducible y consistente

## 🧱 Stack técnico

| Capa | Tecnología |
|------|-----------|
| **CMS / Backend** | Wagtail 2.12 · Django 3.1 · Python 3.x |
| **Base de datos** | PostgreSQL 11 |
| **Frontend** | Webpack (bundling de assets JS/CSS) |
| **Contenedores** | Docker · Docker Compose |
| **Deploy** | Dokku (compatible Heroku) |

## 🏗️ Arquitectura

```
├── main/                    # App principal: templates base, statics, rutas raíz
│   ├── fixtures/            # Datos iniciales (carga automática al iniciar)
│   ├── static/              # Archivos estáticos principales
│   ├── templates/           # Templates base del sitio
│   ├── models.py            # Modelos compartidos (Config, etc.)
│   └── urls.py              # URLs raíz (home page)
│
├── assets/                  # JS y CSS fuente → procesados por Webpack
│
├── gaviriafajardo/          # Configuración del proyecto Django
│   ├── settings/
│   │   ├── common.py        # Settings compartidos entre entornos
│   │   ├── development.py   # Settings de desarrollo (DEBUG, etc.)
│   │   └── production.py    # Settings de producción (seguridad, allowed hosts)
│   ├── urls.py
│   └── wsgi.py
│
├── scripts/                 # Scripts de soporte (wait-for-it, comandos post-start)
├── Dockerfile               # Imagen de producción
├── docker-compose.yml       # Orquestación para desarrollo local
├── Makefile                 # Comandos de utilidad
├── Procfile                 # Configuración Dokku/Heroku
└── requirements.txt         # Dependencias Python
```

Decisiones de diseño relevantes:

- **Wagtail como CMS** en lugar de WordPress o un SPA + headless CMS: el cliente necesitaba autonomía para editar contenido sin soporte técnico. Wagtail ofrece un admin superior al de Django y un modelo de páginas jerárquico que se ajusta naturalmente a sitios corporativos.
- **Monolito** en lugar de microservicios: para un sitio institucional, la simplicidad de un monolito reduce costos de infraestructura y mantenimiento. Un solo proceso sirve el CMS, el frontend y el admin.
- **Settings por entorno** (`development.py` / `production.py`): separación clara que evita errores de configuración al desplegar. Cada entorno hereda de `common.py` y sobrescribe lo necesario.
- **Webpack para assets**: permite usar SCSS, ES6+ y optimización de bundles para producción, sin sacrificar la experiencia de desarrollo con live reload.

---

## ⚡ Quickstart (desarrollo local)

```bash
# 1. Clonar el repositorio
git clone https://github.com/camiloquintero771/web-site-gaviriafajardo.git
cd web-site-gaviriafajardo

# 2. Configurar variables de entorno
cp .env.example .env   # editar con tus valores

# 3. Levantar los contenedores
docker-compose up
```

> En el primer arranque puede fallar la conexión con PostgreSQL mientras se inicializa.
> Simplemente ejecuta `docker-compose up` de nuevo.

El sitio estará disponible en `http://localhost:8000`.

### Compilar assets con Webpack

Después de levantar los contenedores, es necesario generar el bundle de assets:

```bash
# Generar bundle una vez
make webpack-dev

# O con live reload (recomendado durante desarrollo)
make webpack-dev-server
```

## 🔐 Variables de entorno

```bash
cp .env.example .env
```

Estructura del `.env.example`:

```env
# Django
ENVIRONMENT=development
DJANGO_SECRET_KEY=change-me-generate-a-real-key
DEBUG=True

# PostgreSQL
POSTGRES_DB=gaviriafajardo_db
POSTGRES_USER=gaviriafajardo_user
POSTGRES_PASSWORD=change-me-use-a-strong-password
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

# Email (producción)
EMAIL_PASSWORD=change-me
```

> 💡 Para generar un `DJANGO_SECRET_KEY` seguro:
> ```bash
> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
> ```

> ⚠️ **Importante:** asegúrate de que `.env` esté en tu `.gitignore`. Solo el `.env.example` con placeholders debe estar versionado.

---

## 🛠️ Comandos disponibles

| Comando | Descripción |
|---------|-------------|
| `docker-compose up` | Levanta los servicios (Django + PostgreSQL) |
| `docker-compose up --build` | Reconstruye imágenes tras cambios en dependencias |
| `docker-compose down` | Detiene y elimina contenedores (incluye DB) |
| `make webpack-dev` | Genera el bundle de assets (una vez) |
| `make webpack-dev-server` | Webpack con live reload para desarrollo |

---

## 🚀 Deploy (producción)

El proyecto está configurado para despliegue en **Dokku** (compatible con Heroku). El flujo de deploy es:

1. Configurar la app y la base de datos en el servidor Dokku.
2. Definir las variables de entorno de producción (`ENVIRONMENT=production`, `DJANGO_SECRET_KEY`, `EMAIL_PASSWORD`).
3. Desplegar con `git push production master`.

> La documentación detallada de deploy se mantiene internamente por seguridad del servidor.

---

## 👤 Autor

**Camilo Quintero** — Backend Developer · Fundador de [EnocDev](https://github.com/enocdev)
[LinkedIn](https://www.linkedin.com/in/camlo2021) · [GitHub](https://github.com/camiloquintero771)
