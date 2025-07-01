# Prodity AI Risk Detection

Este repositorio contiene la API de detección de riesgos laborales basada en inteligencia artificial para el software Prodity de Grupo Espiral. Utiliza un modelo YOLOv8 re-entrenado para analizar imágenes de entornos laborales, detectando personas y evaluando el uso de protección en la cabeza (cascos de seguridad, otros elementos o ausencia de estos).

La API se construye con FastAPI y está diseñada para ser desplegada como un contenedor Docker.

## Estructura del Proyecto
```
prodity-risk-detection/
├── api/                  # Lógica de la API FastAPI
│   ├── main.py           # Punto de entrada de la aplicación
│   ├── models.py         # Definiciones de modelos Pydantic (Request/Response)
│   └── utils.py          # Funciones auxiliares (procesamiento de imagen, dibujo)
├── model/                # Modelos entrenados
│   ├── detect_best.pt    # Modelo YOLOv8 re-entrenado
│   └── args.yaml         # Archivo de configuración del entrenamiento
├── Dockerfile            # Configuración para construir el contenedor Docker
├── requirements.txt      # Dependencias de Python
├── README.md             # Este archivo
└── .gitignore            # Archivos y directorios a ignorar por Git
```

## Clases Detectadas

El modelo ha sido entrenado para detectar las siguientes 4 clases:

* `person`: Personas en la imagen.
* `hard_hat`: Casco de seguridad en la cabeza de una persona.
* `no_hard_hat`: Algo en la cabeza de una persona que no es un casco de seguridad.
* `no_head_wear`: Ausencia de cualquier elemento en la cabeza de una persona.

## Uso

### Requisitos

* Python 3.10+
* Docker (para despliegue en contenedor)
* `pip`

### 1. Clonar el Repositorio

```bash
git clone [https://github.com/Especializacion-IA/prodity-risk-detection.git](https://github.com/Especializacion-IA/prodity-risk-detection.git)
cd prodity-risk-detection
```
Proyecto creado con ❤️ por el equipo de especialización en IA de la promoción Techcamp de Factoría F5

<img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="20" height="20" alt="GitHub icon"> [Naudelyn Lucena](https://github.com/NaudelynLucena), <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="20" height="20" alt="GitHub icon"> [Eva G. Muñoz](https://github.com/Emagmunioz), <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="20" height="20" alt="GitHub icon"> [Grigory Pereira](https://github.com/Grigory-Vladimiro), <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="20" height="20" alt="GitHub icon"> [Jesús Enjamio](https://github.com/JesusEnjamio), <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="20" height="20" alt="GitHub icon"> [Mabel Rincón](https://github.com/MabelRincon)
