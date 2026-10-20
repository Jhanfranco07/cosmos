# 🪐 COSMOS

**Un universo por descubrir.** Laboratorio espacial interactivo creado para una actividad de Cloud Computing con Python y Streamlit.

## Experiencia

- Exploración 3D de los ocho planetas: arrastrar para girar, rueda o botones para zoom.
- Vista de órbitas animadas. Haz clic en un planeta para explorarlo.
- Tierra con textura fotográfica; otros planetas con texturas procedurales ilustrativas y Saturno con anillos.
- Pausa, restablecimiento de cámara y modo exposición. Usa las flechas ← → para cambiar de planeta y Escape para salir del modo exposición.
- Laboratorio de peso: masa, fuerza en newtons y lectura equivalente de una balanza terrestre.
- Viaje idealizado desde la Tierra, tiempo de una señal de luz y descarga de la misión en JSON.
- Comparación proporcional de diámetros y tabla planetaria.
- Diseño adaptable a escritorio y móvil. Se respeta la preferencia de movimiento reducido al iniciar.

## Desplegar en Streamlit Community Cloud

1. Abre https://share.streamlit.io/ e ingresa con GitHub.
2. Selecciona **Create app / Deploy an app** y este repositorio.
3. Configura:
   - Repository: `Jhanfranco07/cosmos`
   - Branch: `main`
   - Main file path: `app.py`
   - Python: **3.12** en las opciones avanzadas.
4. Pulsa **Deploy** y espera la instalación de dependencias.

No requiere claves, servicios de pago ni base de datos. Publicar el repositorio no despliega automáticamente la aplicación: debes crearla en Streamlit Community Cloud.

## Ejecutar localmente

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Arquitectura y relación con Cloud Computing

El servidor Python ejecuta Streamlit y entrega la experiencia al navegador mediante un componente HTML. El navegador renderiza la escena con WebGL y calcula las interacciones. GitHub conserva el código y Streamlit Community Cloud proporciona el alojamiento gestionado. No se almacenan datos personales ni misiones; la descarga se genera en el dispositivo del usuario.

Los recursos gráficos y el motor se incluyen en `assets/` y se incrustan al servir la aplicación. No hay peticiones a CDN en tiempo de ejecución. El primer acceso requiere transferir estos recursos. Un dispositivo sin WebGL muestra un aviso y conserva disponibles el laboratorio y las comparaciones.

## Supuestos científicos

- Datos redondeados de [NASA/NSSDCA Planetary Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/), tabla actualizada el 18 de marzo de 2025. Se usa consistentemente su columna de gravedad (incluida la corrección rotacional de la tabla).
- Escena de exploración artística: tamaños, posiciones, distancias, rotaciones e inclinaciones no son una efeméride ni se representan a escala física. Las órbitas son circulares y sus velocidades relativas son ilustrativas.
- La comparación de tamaños conserva la relación entre diámetros ecuatoriales. La relación de volúmenes aproxima los cuerpos como esferas.
- Masa en kg permanece constante; peso en N = masa × gravedad. La lectura de balanza equivalente es peso / 9,8.
- Viaje: diferencia absoluta entre radios orbitales medios × 1 000 000 km, dividida entre velocidad constante. No es una predicción de viaje ni representa la distancia actual entre planetas.
- Velocidad de la luz: 299 792,458 km/s. Un año del simulador equivale a 365,25 días.
- Los gigantes no ofrecen una superficie sólida para una balanza; los valores de gravedad se refieren a un nivel atmosférico de referencia.

## Recursos y créditos

- Three.js **0.160.1**, licencia MIT en `assets/THREE-LICENSE.txt`.
- Textura terrestre distribuida en los [ejemplos oficiales de Three.js r160](https://github.com/mrdoob/three.js/blob/r160/examples/textures/planets/earth_atmos_2048.jpg); imagen terrestre NASA, recurso de visualización sin nubes.
- Texturas de otros planetas, estrellas y anillos generados por código; son representaciones artísticas.

## Guion de demostración (2 minutos)

1. Abre COSMOS y arrastra la Tierra para mostrar el modelo 3D.
2. Selecciona Saturno y muestra sus anillos.
3. Activa **Órbitas** y pausa o acerca el sistema.
4. En **Laboratorio**, cambia la masa y el destino a Júpiter.
5. Diseña un viaje a Marte y descarga la misión.
6. En **Comparar**, contrasta la Tierra con Júpiter y explica las escalas.
7. Cierra explicando que la aplicación se sirve desde la nube y puede abrirse por enlace sin instalar Python.
