# SISTEMA DE IA Y ANÁLISIS DE DATOS
## Prompts, Automatizaciones y Framework de Datos

---

## 1. PROMPTS PARA GITHUB COPILOT / CHATGPT

### 1.1 Generación de Presentaciones

#### Prompt Maestro para Presentación Completa

```
Genera una presentación de Google Slides para una clase de francés.

CONTEXTO:
- Nivel: [A1.1 / A1.2 / A2.1 / A2.2 / B1.1]
- Semana: [número]
- Día: [Martes / Jueves]
- Alumnos: 12-15 años, mexicanos, clase online vía Zoom
- Duración: 50 minutos

CONTENIDO DE ESTA CLASE (del plan de estudios):
- Vocabulario: [copiar del plan]
- Gramática: [copiar del plan]
- Práctica: [copiar del plan]

ESTRUCTURA REQUERIDA (10 slides aprox):
1. Slide de bienvenida con pregunta del día en francés
2. Repaso de clase anterior (1-2 slides, actividad interactiva)
3. Vocabulario nuevo con imágenes (2-3 slides, máx 5 palabras por slide)
4. Gramática explicada de forma simple (2 slides, ejemplos visuales)
5. Actividad de práctica (instrucciones claras)
6. Tarea y cierre

ESTILO:
- Visual: más imágenes que texto
- Poco texto: máximo 30 palabras por slide
- Ejemplos con personajes/referencias que conocen adolescentes mexicanos
- Colores azul, blanco, rojo (bandera francesa)
- Fuente legible: mínimo 24pt

DATOS DE CLASES ANTERIORES (si hay):
- Actividad mejor recibida: [tipo]
- Tema que costó trabajo: [tema]
- Nivel de participación: [alto/medio/bajo]

Genera el contenido textual de cada slide, indicando:
- Título del slide
- Contenido (texto, bullet points)
- Notas del presentador (qué decir/hacer)
- Sugerencia de imagen
```

#### Prompt para Adaptar Dificultad

```
Tengo esta actividad para nivel [A1.1]:

[Pegar actividad]

Los datos de mi grupo muestran que:
- El [X]% tuvo dificultades con [aspecto específico]
- La actividad de [tipo] funcionó mejor que [otro tipo]
- Los alumnos [observación específica]

Adapta la actividad para:
1. Reducir/aumentar la dificultad en [aspecto]
2. Mantener el objetivo de aprendizaje: [objetivo]
3. Hacerla más interactiva/dinámica
4. Incluir andamiaje (scaffolding) para alumnos con dificultades
```

#### Prompt para Crear Kahoot/Quizizz

```
Crea 10 preguntas para un Kahoot sobre:
- Nivel: [nivel]
- Tema: [vocabulario/gramática de la semana]

Formato para cada pregunta:
1. Pregunta (en francés o español según complejidad)
2. 4 opciones de respuesta (1 correcta, 3 distractores plausibles)
3. Respuesta correcta marcada
4. Tiempo sugerido (10, 20, o 30 segundos)

Criterios:
- Dificultad progresiva (fácil → difícil)
- Incluir 2 preguntas de audio si es posible (indicar texto a leer)
- Los distractores deben ser errores comunes, no absurdos
- Incluir al menos 2 preguntas de imagen
```

### 1.2 Generación de Guías del Profesor

```
Genera una guía del profesor para:
- Nivel: [nivel]
- Semana: [número]
- Día: [Martes/Jueves]
- Tema: [título]

Contenido de la clase (del plan):
[Copiar contenido léxico y gramatical del plan]

La guía debe incluir:
1. Objetivos (léxicos, gramaticales, comunicativos)
2. Preparación previa (checklist)
3. Desarrollo minuto a minuto (50 min total):
   - 0-5: Bienvenida (script en francés)
   - 5-15: Repaso (actividad detallada)
   - 15-30: Contenido nuevo (vocabulario + gramática)
   - 30-40: Práctica (instrucciones paso a paso)
   - 40-48: Producción (actividad creativa)
   - 48-50: Cierre (resumen, tarea)
4. Posibles problemas y soluciones (tabla)
5. Datos a recolectar después de clase
6. Mensaje para padres (copiar/pegar)

Tono: Profesional pero cercano, como si fuera un colega dando consejos.
```

### 1.3 Análisis y Recomendaciones

```
Analiza estos datos de mi grupo de francés [nivel]:

DATOS DE LAS ÚLTIMAS 4 SEMANAS:
[Pegar datos en formato CSV o tabla]

Columnas: semana, asistencia_promedio, participacion, comprension_tema, 
dudas_frecuentes, actividad_mejor_recibida

PREGUNTAS:
1. ¿Qué patrones observas?
2. ¿Qué temas necesitan refuerzo?
3. ¿Qué tipo de actividades funcionan mejor?
4. ¿Hay alumnos específicos que necesiten atención?
5. ¿Qué ajustes recomiendas para las próximas semanas?

Responde con:
- Insights principales (3-5 bullets)
- Recomendaciones concretas (acciones específicas)
- Ajustes sugeridos al plan (si aplica)
```

---

## 2. FRAMEWORK DE RECOLECCIÓN DE DATOS

### 2.1 Formulario Post-Clase (Google Form)

**Campos obligatorios:**

```
Profesor: [dropdown]
Grupo: [dropdown]
Fecha: [date picker]
Semana: [número]
Día: [Martes/Jueves]

Asistencia: [número] de [total]

Participación general (1-5):
[ ] 1 - Muy baja (nadie participaba)
[ ] 2 - Baja (solo 2-3 alumnos)
[ ] 3 - Media (la mitad del grupo)
[ ] 4 - Alta (mayoría participó)
[ ] 5 - Muy alta (todos participaron activamente)

Comprensión del tema (1-5):
[ ] 1 - No entendieron
[ ] 2 - Entendieron poco
[ ] 3 - Entendieron lo básico
[ ] 4 - Entendieron bien
[ ] 5 - Dominaron el tema

Actividad mejor recibida: [dropdown]
- Kahoot/Quizizz
- Trabajo en parejas
- Juego de roles
- Video
- Ejercicio escrito
- Otra: [texto]

Dudas más frecuentes: [texto largo]

Alumnos que necesitan seguimiento: [texto]
(Nombre + razón breve)

Notas para próxima clase: [texto]

Tiempo real por actividad: [opcional, texto]
```

### 2.2 Seguimiento Semanal por Alumno

**Estructura de Google Sheet:**

```
| alumno_id | nombre | grupo | semana | asistencia_martes | asistencia_jueves | 
| participacion | tareas_entregadas | calidad_tareas | errores_frecuentes | 
| fortalezas | comentarios |
```

**Escala de calidad de tareas:**
- 1: No entregada
- 2: Incompleta o con muchos errores
- 3: Completa con errores menores
- 4: Bien hecha
- 5: Excelente, superó expectativas

### 2.3 Evaluaciones

**Estructura:**

```
| alumno_id | evaluacion_id | tipo | fecha | puntaje | tiempo_minutos |
| errores_vocabulario | errores_gramatica | errores_pronunciacion | 
| errores_comprension | comentarios |
```

**Tipos de evaluación:**
- Quiz semanal
- Examen parcial
- Proyecto
- Presentación oral
- Examen final

---

## 3. SCRIPTS DE ANÁLISIS (Python)

### 3.1 Análisis Semanal Automático

```python
# analisis_semanal.py
import pandas as pd
from datetime import datetime

def analizar_semana(grupo, semana, datos_path):
    """
    Genera reporte semanal automático para un grupo.
    """
    # Cargar datos
    df_clases = pd.read_csv(f"{datos_path}/clases_{grupo}.csv")
    df_alumnos = pd.read_csv(f"{datos_path}/alumnos_{grupo}.csv")
    
    # Filtrar semana actual
    df_semana = df_clases[df_clases['semana'] == semana]
    
    # Métricas
    asistencia_prom = df_semana['asistencia'].mean()
    participacion_prom = df_semana['participacion'].mean()
    comprension_prom = df_semana['comprension_tema'].mean()
    
    # Tendencia vs semana anterior
    df_anterior = df_clases[df_clases['semana'] == semana - 1]
    tendencia_part = participacion_prom - df_anterior['participacion'].mean()
    
    # Alumnos en riesgo
    df_alumnos_semana = df_alumnos[df_alumnos['semana'] == semana]
    en_riesgo = df_alumnos_semana[
        (df_alumnos_semana['participacion'] < 2) | 
        (df_alumnos_semana['tareas_entregadas'] < 1)
    ]['nombre'].tolist()
    
    # Dudas frecuentes (análisis de texto simple)
    dudas = df_semana['dudas_frecuentes'].str.cat(sep=' ')
    
    # Generar reporte
    reporte = f"""
    REPORTE SEMANAL - {grupo} - Semana {semana}
    Fecha: {datetime.now().strftime('%Y-%m-%d')}
    
    📊 MÉTRICAS:
    - Asistencia promedio: {asistencia_prom:.1%}
    - Participación: {participacion_prom:.1f}/5 ({'+' if tendencia_part > 0 else ''}{tendencia_part:.1f} vs semana anterior)
    - Comprensión: {comprension_prom:.1f}/5
    
    ⚠️ ALUMNOS EN RIESGO:
    {', '.join(en_riesgo) if en_riesgo else 'Ninguno'}
    
    💡 DUDAS FRECUENTES:
    {dudas[:500]}
    
    🎯 ACTIVIDAD MEJOR RECIBIDA:
    {df_semana['actividad_mejor_recibida'].mode()[0]}
    """
    
    return reporte

def generar_alertas(grupo, datos_path):
    """
    Genera alertas automáticas para alumnos que necesitan atención.
    """
    df = pd.read_csv(f"{datos_path}/alumnos_{grupo}.csv")
    
    alertas = []
    
    # Alerta: 2+ semanas sin entregar tareas
    for alumno in df['alumno_id'].unique():
        df_alumno = df[df['alumno_id'] == alumno].tail(2)
        if df_alumno['tareas_entregadas'].sum() == 0:
            nombre = df_alumno['nombre'].iloc[0]
            alertas.append(f"🔴 {nombre}: 2 semanas sin entregar tareas")
    
    # Alerta: Participación en declive
    for alumno in df['alumno_id'].unique():
        df_alumno = df[df['alumno_id'] == alumno].tail(3)
        if len(df_alumno) == 3:
            if df_alumno['participacion'].is_monotonic_decreasing:
                nombre = df_alumno['nombre'].iloc[0]
                alertas.append(f"🟡 {nombre}: Participación en declive")
    
    return alertas
```

### 3.2 Dashboard Simple (Google Sheets + Scripts)

**Fórmulas para Dashboard en Google Sheets:**

```
// Celda de Asistencia Promedio
=AVERAGE(FILTER(Datos!E:E, Datos!B:B=grupo_seleccionado, Datos!C:C=semana_seleccionada))

// Celda de Tendencia
=SPARKLINE(FILTER(Datos!F:F, Datos!B:B=grupo_seleccionado), {"charttype","line"})

// Conteo de Alumnos en Riesgo
=COUNTIFS(Alumnos!D:D, grupo, Alumnos!G:G, "<2")

// Predicción DELF (simple)
=IF(AVERAGE(Evaluaciones!E:E)>=70%, "Alta probabilidad", IF(AVERAGE(Evaluaciones!E:E)>=50%, "Probabilidad media", "Necesita refuerzo"))
```

---

## 4. FLUJO DE TRABAJO AUTOMATIZADO

### 4.1 Ciclo Semanal

```
VIERNES (después de última clase)
│
├── 17:00 - Profesor completa formulario post-clase
│
├── 18:00 - Script automático:
│           ├── Procesa datos de la semana
│           ├── Genera reporte semanal
│           ├── Identifica alumnos en riesgo
│           └── Envía resumen por email
│
├── SÁBADO - Coordinación revisa reportes
│           └── Contacta casos críticos
│
├── DOMINGO - GitHub Copilot genera:
│            ├── Borrador de presentaciones próxima semana
│            ├── Sugerencias de ajuste basadas en datos
│            └── Actividades alternativas para temas difíciles
│
└── LUNES - Profesor revisa y aprueba materiales
            └── Materiales listos para Martes
```

### 4.2 Ciclo Semestral

```
FIN DE SEMESTRE (última semana)
│
├── Análisis agregado de todos los grupos
│   ├── Temas más difíciles
│   ├── Actividades más efectivas
│   └── Patrones de aprendizaje
│
├── Actualización del PLAN BASE
│   ├── Reordenar temas si necesario
│   ├── Ajustar tiempo por tema
│   └── Agregar/quitar contenido
│
├── Generación de nuevos materiales
│   └── Presentaciones actualizadas para todo el semestre
│
└── Capacitación docente sobre cambios
```

---

## 5. INTEGRACIÓN DE HERRAMIENTAS EXTERNAS

### 5.1 Duolingo Classroom (Seguimiento)

**Datos a extraer:**
- Racha diaria por alumno
- Lecciones completadas
- Tiempo de práctica

**Cómo usar:**
1. Crear clase en Duolingo for Schools
2. Asignar tareas semanales
3. Revisar progreso cada viernes
4. Integrar datos en seguimiento general

### 5.2 Kahoot Reports

**Después de cada Kahoot:**
1. Descargar reporte de resultados
2. Identificar preguntas con más errores
3. Agregar a "temas para reforzar"

### 5.3 Google Classroom Analytics

**Métricas útiles:**
- Tiempo de entrega de tareas
- Quién entrega antes/después de fecha límite
- Interacciones con materiales

---

## 6. PROMPTS PARA COMUNICACIÓN CON PADRES

### 6.1 Generar Mensaje Semanal

```
Genera un mensaje de WhatsApp para padres de familia.

Contexto:
- Grupo: [nivel]
- Semana: [número]
- Tema vocabulario: [tema]
- Tema gramática: [estructura]
- Logro comunicativo: [qué pueden hacer ahora]
- Tarea: [descripción]
- Fecha entrega: [fecha]

Requisitos:
- Máximo 200 palabras
- Tono cálido y profesional
- En español con algunas palabras en francés
- Incluir 1 sugerencia de cómo apoyar en casa
- Usar emojis moderadamente
- Formato para WhatsApp (negritas con asteriscos)
```

### 6.2 Generar Mensaje de Seguimiento

```
Genera un mensaje para los padres de [nombre del alumno].

Situación:
[Describir: bajo rendimiento / ausencias / excelente progreso / etc.]

Datos:
- Asistencia: [X] de [Y] clases
- Tareas entregadas: [X] de [Y]
- Participación: [descripción]
- Fortalezas: [lista]
- Áreas de mejora: [lista]

Tono: [Preocupación empática / Felicitación / Neutral informativo]

Incluir:
- Reconocimiento de algo positivo (siempre)
- Descripción objetiva de la situación
- 2-3 sugerencias concretas
- Ofrecimiento de llamada si es necesario
```

---

## 7. MÉTRICAS DE ÉXITO DEL SISTEMA

### 7.1 KPIs del Programa

| Métrica | Meta | Fórmula |
|---------|------|---------|
| Asistencia promedio | >85% | Clases asistidas / Clases totales |
| Participación promedio | >3.5/5 | Promedio de escala de participación |
| Tareas entregadas | >80% | Tareas entregadas / Tareas asignadas |
| Aprobación DELF | >75% | Alumnos aprobados / Alumnos presentados |
| Satisfacción alumnos | >4/5 | Encuesta semestral |
| Satisfacción padres | >4/5 | Encuesta semestral |
| Retención | >90% | Alumnos que continúan / Alumnos inicio |

### 7.2 Evaluación del Sistema de IA

| Aspecto | Cómo Medir |
|---------|------------|
| Calidad de materiales generados | Revisión por coordinación (1-5) |
| Tiempo ahorrado por profesor | Encuesta + tracking |
| Precisión de predicciones | Comparar predicción vs resultado real |
| Efectividad de adaptaciones | Mejora en métricas post-ajuste |

---

*Documento creado: Febrero 2026*
*Para actualizar: cada semestre con nuevos aprendizajes*
