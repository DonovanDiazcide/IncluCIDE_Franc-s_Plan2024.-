#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para organizar la estructura de archivos del curso de francés IncluCIDE
Fecha: Febrero 2026
"""

import os
import shutil
from pathlib import Path

# Directorio base
BASE_DIR = Path(__file__).parent

# Definir la estructura de carpetas deseada
ESTRUCTURA = {
    '01_DOCUMENTACION': [
        'PROYECTO_SISTEMA_INTEGRAL.md',
        'README.md',
        'plan.md',
        'SISTEMA_VERIFICACION.md',
        'INVENTARIO_MAESTRO.md',
        'CONTROL_CALIDAD_PROGRESO.md',
        'VERIFICACION_B1.md',
        'REVISION_PEDAGOGICA.md',
        'INDICE_VISUAL_CAMBIOS.md',
        'RESUMEN_CAMBIOS.md',
        'REPORTE_EVIDENCIA_20260209.md',
        'plan2.md',
        'plan_backup.md'
    ],
    '02_GUIAS_PROFESOR': {
        'A1.1': [],
        'A1.2': [],
        'A2.1': [],
        'A2.2': [],
        'B1.1': [],
        'PLANTILLAS': ['GUIA_PROFESOR_PLANTILLA.md']
    },
    '03_PRESENTACIONES': {
        'A1.1': [],
        'A1.2': [],
        'A2.1': [],
        'A2.2': [],
        'B1.1': []
    },
    '04_EVALUACIONES': {
        'A1.1': ['EVALUACION_A1.1_Unidad1.md', 'EVALUACION_A1.1_Unidad2.md', 'EVALUACION_A1.1_Final.md'],
        'A1.2': ['EVALUACION_A1.2_Parcial.md', 'EVALUACION_A1.2_Final.md'],
        'A2.1': ['EVALUACION_A2.1_Parcial.md', 'EVALUACION_A2.1_Final.md'],
        'A2.2': ['EVALUACION_A2.2_Parcial.md', 'EVALUACION_A2.2_Final.md'],
        'B1.1': ['EVALUACION_B1.1_Final.md']
    },
    '05_RUBRICAS': [
        'RUBRICA_COMPRENSION_ESCRITA.md',
        'RUBRICA_COMPRENSION_ORAL.md',
        'RUBRICA_PRODUCCION_ESCRITA.md',
        'RUBRICA_PRODUCCION_ORAL.md',
        'RUBRICA_PARTICIPACION.md',
        'RUBRICA_OBSERVACION_DOCENTE.md'
    ],
    '06_CAPACITACION': [
        'MANUAL_CAPACITACION_DOCENTE.md',
        'MANUAL_PROGRAMA_INCLUCIDE.md',
        'GUIA_INDUCCION_RAPIDA.md',
        'TALLER_CAPACITACION_AGENDA.md',
        'CAPACITACION_MODULO1_ENSENANZA_ONLINE.md',
        'CAPACITACION_MODULO2_DIDACTICA_ADOLESCENTES.md',
        'CAPACITACION_MODULO3_SITUACIONES_DIFICILES.md',
        'CAPACITACION_MODULO4_HERRAMIENTAS_IA.md',
        'BANCO_ACTIVIDADES_CAPACITACION.md'
    ],
    '07_ACTIVIDADES_RECURSOS': [
        'ACTIVIDADES_INTERACTIVAS.md',
        'VIDEOS_APOYO_CURADOS.md'
    ],
    '08_DATOS_ANALISIS': [
        'FORMULARIOS_RECOLECCION.md',
        'scripts_analisis_datos.py',
        'DISENO_DASHBOARD.md',
        'SISTEMA_IA_DATOS.md'
    ],
    '09_IMAGENES': [
        'image.png',
        'image-1.png',
        'image-2.png'
    ]
}

def crear_carpetas():
    """Crea la estructura de carpetas"""
    print("📁 Creando estructura de carpetas...")
    
    for carpeta in ESTRUCTURA.keys():
        carpeta_path = BASE_DIR / carpeta
        carpeta_path.mkdir(exist_ok=True)
        print(f"   ✓ {carpeta}")
        
        # Crear subcarpetas si existen
        if isinstance(ESTRUCTURA[carpeta], dict):
            for subcarpeta in ESTRUCTURA[carpeta].keys():
                sub_path = carpeta_path / subcarpeta
                sub_path.mkdir(exist_ok=True)
                print(f"     ✓ {carpeta}/{subcarpeta}")

def mover_archivos_especificos():
    """Mueve archivos específicos según la estructura definida"""
    print("\n📦 Moviendo archivos específicos...")
    
    for carpeta, contenido in ESTRUCTURA.items():
        carpeta_path = BASE_DIR / carpeta
        
        if isinstance(contenido, list):
            # Es una lista simple de archivos
            for archivo in contenido:
                origen = BASE_DIR / archivo
                destino = carpeta_path / archivo
                
                if origen.exists() and origen.is_file():
                    try:
                        shutil.move(str(origen), str(destino))
                        print(f"   ✓ {archivo} → {carpeta}/")
                    except Exception as e:
                        print(f"   ✗ Error moviendo {archivo}: {e}")
        
        elif isinstance(contenido, dict):
            # Es un diccionario con subcarpetas
            for subcarpeta, archivos in contenido.items():
                sub_path = carpeta_path / subcarpeta
                
                for archivo in archivos:
                    origen = BASE_DIR / archivo
                    destino = sub_path / archivo
                    
                    if origen.exists() and origen.is_file():
                        try:
                            shutil.move(str(origen), str(destino))
                            print(f"   ✓ {archivo} → {carpeta}/{subcarpeta}/")
                        except Exception as e:
                            print(f"   ✗ Error moviendo {archivo}: {e}")

def mover_guias_profesor():
    """Mueve las guías de profesor a sus carpetas correspondientes"""
    print("\n📚 Organizando guías de profesor...")
    
    niveles = ['A1.1', 'A1.2', 'A2.1', 'A2.2', 'B1.1']
    base_guias = BASE_DIR / '02_GUIAS_PROFESOR'
    
    for nivel in niveles:
        patron = f"GUIA_PROFESOR_{nivel.replace('.', '_')}_"
        archivos = list(BASE_DIR.glob(f"{patron}*.md"))
        
        for archivo in archivos:
            destino = base_guias / nivel / archivo.name
            try:
                shutil.move(str(archivo), str(destino))
                print(f"   ✓ {archivo.name} → 02_GUIAS_PROFESOR/{nivel}/")
            except Exception as e:
                print(f"   ✗ Error moviendo {archivo.name}: {e}")

def mover_presentaciones():
    """Mueve las presentaciones a sus carpetas correspondientes"""
    print("\n🎬 Organizando presentaciones...")
    
    niveles = ['A1.1', 'A1.2', 'A2.1', 'A2.2', 'B1.1']
    base_presentaciones = BASE_DIR / '03_PRESENTACIONES'
    
    for nivel in niveles:
        patron = f"PRESENTACION_{nivel.replace('.', '_')}_"
        archivos = list(BASE_DIR.glob(f"{patron}*.md"))
        
        for archivo in archivos:
            destino = base_presentaciones / nivel / archivo.name
            try:
                shutil.move(str(archivo), str(destino))
                print(f"   ✓ {archivo.name} → 03_PRESENTACIONES/{nivel}/")
            except Exception as e:
                print(f"   ✗ Error moviendo {archivo.name}: {e}")

def crear_readme_carpetas():
    """Crea archivos README en cada carpeta principal"""
    print("\n📝 Creando archivos README...")
    
    readmes = {
        '01_DOCUMENTACION': """# Documentación Principal

Esta carpeta contiene toda la documentación estratégica y de planificación del curso:
- Plan de estudios completo
- Sistema de verificación de calidad
- Documentación del proyecto integral
- Reportes de progreso y evidencia
""",
        '02_GUIAS_PROFESOR': """# Guías para Profesores

Guías detalladas clase por clase para cada nivel del curso.
Organizadas por nivel (A1.1, A1.2, A2.1, A2.2, B1.1).

Cada guía incluye:
- Objetivos de la sesión
- Desarrollo minuto a minuto
- Actividades detalladas
- Soluciones a problemas comunes
- Material de apoyo
""",
        '03_PRESENTACIONES': """# Presentaciones de Clase

Presentaciones organizadas por nivel para cada sesión del curso.
Formato Markdown compatible con reveal.js o Google Slides.

Estructura:
- Diapositivas de bienvenida
- Contenido léxico y gramatical
- Actividades interactivas
- Tareas y cierre
""",
        '04_EVALUACIONES': """# Evaluaciones

Evaluaciones parciales y finales para cada nivel del curso.

Tipos:
- Unidad (A1.1)
- Parcial (mitad de semestre)
- Final (fin de semestre)

Incluye:
- Comprensión oral y escrita
- Gramática y léxico
- Producción escrita y oral
""",
        '05_RUBRICAS': """# Rúbricas de Evaluación

Rúbricas estandarizadas para evaluar diferentes competencias:
- Producción oral
- Producción escrita
- Comprensión oral
- Comprensión escrita
- Participación en clase
- Observación docente
""",
        '06_CAPACITACION': """# Capacitación Docente

Materiales para la capacitación de profesores del programa.

Módulos:
1. Fundamentos de enseñanza online (2h)
2. Didáctica del francés para adolescentes (3h)
3. Manejo de situaciones difíciles (2h)
4. Uso de herramientas de IA (2h)

Incluye banco de actividades y guías rápidas.
""",
        '07_ACTIVIDADES_RECURSOS': """# Actividades y Recursos

Recursos complementarios para las clases:
- Banco de actividades interactivas (Kahoot, Quizizz)
- Videos curados por nivel
- Material audiovisual
""",
        '08_DATOS_ANALISIS': """# Sistema de Datos y Análisis

Herramientas para recolección y análisis de datos del curso:
- Formularios de recolección
- Scripts de análisis (Python)
- Diseño de dashboards
- Sistema de IA para insights
""",
        '09_IMAGENES': """# Imágenes y Recursos Visuales

Recursos visuales utilizados en la documentación y presentaciones.
"""
    }
    
    for carpeta, contenido in readmes.items():
        readme_path = BASE_DIR / carpeta / 'README.md'
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(contenido)
        print(f"   ✓ README.md en {carpeta}/")

def crear_indice_principal():
    """Crea un índice principal en el README.md de la raíz"""
    print("\n📋 Creando índice principal...")
    
    indice = """# 🇫🇷 IncluCIDE Francés - Plan 2024

Sistema Integral de Enseñanza de Francés para adolescentes mexicanos de 12-15 años en modalidad online.

## 📁 Estructura del Proyecto

### 01_DOCUMENTACION
Documentación estratégica, plan de estudios, sistema de verificación y reportes.

### 02_GUIAS_PROFESOR
Guías detalladas clase por clase organizadas por nivel:
- **A1.1**: 24 guías (12 semanas)
- **A1.2**: 14 guías (7 semanas)
- **A2.1**: 20 guías (10 semanas)
- **A2.2**: 24 guías (12 semanas)
- **B1.1**: 18 guías (9 semanas)

### 03_PRESENTACIONES
Presentaciones de clase en formato Markdown:
- **100 presentaciones** totales
- Organizadas por nivel y sesión
- Compatibles con reveal.js/Google Slides

### 04_EVALUACIONES
Evaluaciones por nivel:
- **10 evaluaciones** totales
- Parciales y finales
- Incluye criterios de evaluación

### 05_RUBRICAS
6 rúbricas estandarizadas:
- Producción oral y escrita
- Comprensión oral y escrita
- Participación y observación docente

### 06_CAPACITACION
Materiales para capacitación docente:
- 4 módulos de capacitación
- Manual completo
- Banco de actividades
- Guía de inducción rápida

### 07_ACTIVIDADES_RECURSOS
Recursos complementarios:
- Actividades interactivas
- Videos curados por nivel

### 08_DATOS_ANALISIS
Sistema de análisis y mejora continua:
- Formularios de recolección de datos
- Scripts de análisis con Python
- Diseño de dashboards
- Sistema de IA para insights

### 09_IMAGENES
Recursos visuales del proyecto.

---

## 🚀 Inicio Rápido

1. **Para profesores nuevos**: Leer `06_CAPACITACION/GUIA_INDUCCION_RAPIDA.md`
2. **Para planificación**: Consultar `01_DOCUMENTACION/plan.md`
3. **Para preparar una clase**: Revisar guía en `02_GUIAS_PROFESOR/[NIVEL]/`
4. **Para materiales visuales**: Usar presentación en `03_PRESENTACIONES/[NIVEL]/`

## 📊 Estado del Proyecto

- ✅ **Fase 1-4**: Completadas (Documentación, Materiales, Datos, Capacitación)
- ⏳ **Fase 5**: Piloto (Pendiente)
- ⏳ **Fase 6**: Escalamiento (Pendiente)

---

## 📖 Documentación Principal

Para información detallada del proyecto, consultar:
- `01_DOCUMENTACION/PROYECTO_SISTEMA_INTEGRAL.md` - Documento maestro del proyecto
- `01_DOCUMENTACION/plan.md` - Plan de estudios completo A1.1 a B1.1

---

*Última actualización: Febrero 2026*
*Autores: Donovan Byron Díaz Moreno, con asistencia de GitHub Copilot CLI*
"""
    
    readme_principal = BASE_DIR / 'README.md'
    
    # Respaldar README existente si existe
    if readme_principal.exists():
        backup = BASE_DIR / 'README_backup.md'
        shutil.copy(str(readme_principal), str(backup))
        print(f"   ℹ️  README existente respaldado como README_backup.md")
    
    with open(readme_principal, 'w', encoding='utf-8') as f:
        f.write(indice)
    
    print(f"   ✓ README.md principal actualizado")

def generar_reporte():
    """Genera un reporte de la organización realizada"""
    print("\n" + "="*60)
    print("✅ ORGANIZACIÓN COMPLETADA")
    print("="*60)
    
    # Contar archivos por carpeta
    print("\n📊 Resumen de archivos organizados:\n")
    
    for carpeta in sorted(ESTRUCTURA.keys()):
        carpeta_path = BASE_DIR / carpeta
        if carpeta_path.exists():
            archivos = list(carpeta_path.rglob('*.md'))
            scripts = list(carpeta_path.rglob('*.py'))
            imagenes = list(carpeta_path.rglob('*.png'))
            total = len(archivos) + len(scripts) + len(imagenes)
            print(f"   {carpeta}: {total} archivos")
    
    print("\n" + "="*60)
    print("🎉 Todos los archivos han sido organizados correctamente")
    print("="*60)

def main():
    """Función principal"""
    print("="*60)
    print("🚀 INICIANDO ORGANIZACIÓN DE ARCHIVOS")
    print("="*60)
    print(f"\n📂 Directorio base: {BASE_DIR}\n")
    
    try:
        # 1. Crear estructura de carpetas
        crear_carpetas()
        
        # 2. Mover archivos específicos
        mover_archivos_especificos()
        
        # 3. Mover guías de profesor
        mover_guias_profesor()
        
        # 4. Mover presentaciones
        mover_presentaciones()
        
        # 5. Crear READMEs en cada carpeta
        crear_readme_carpetas()
        
        # 6. Crear índice principal
        crear_indice_principal()
        
        # 7. Generar reporte
        generar_reporte()
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
