#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SISTEMA DE ANÁLISIS DE DATOS - IncluCIDE Francés
Versión: 1.0
Autor: Equipo IncluCIDE con asistencia de GitHub Copilot

Este script procesa los datos recolectados de las clases de francés
y genera insights para mejorar la enseñanza.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json
import os

# ============================================================================
# CONFIGURACIÓN
# ============================================================================

CONFIG = {
    'ruta_datos': './datos/',
    'ruta_reportes': './reportes/',
    'umbral_asistencia_alerta': 0.70,
    'umbral_participacion_alerta': 2.0,
    'umbral_comprension_refuerzo': 3.0,
    'dias_sin_tarea_alerta': 14,
    'clases_ausencia_contactar': 2
}

# ============================================================================
# CLASE PRINCIPAL DE ANÁLISIS
# ============================================================================

class AnalizadorIncluCIDE:
    """Analizador principal para datos de clases de francés."""
    
    def __init__(self, config=None):
        self.config = config or CONFIG
        self.df_clases = None
        self.df_alumnos = None
        self.df_evaluaciones = None
        
    # ------------------------------------------------------------------------
    # CARGA DE DATOS
    # ------------------------------------------------------------------------
    
    def cargar_datos_clases(self, archivo_csv):
        """Carga datos de clases desde CSV."""
        columnas = [
            'fecha', 'grupo', 'semana', 'dia', 'tema', 
            'alumnos_presentes', 'total_inscritos', 'tasa_asistencia',
            'participacion', 'comprension', 'contenido_cubierto',
            'actividad_favorita', 'problemas_tecnicos', 'tiempo_ajuste',
            'dudas_frecuentes', 'notas'
        ]
        
        try:
            self.df_clases = pd.read_csv(archivo_csv, parse_dates=['fecha'])
            print(f"✓ Cargados {len(self.df_clases)} registros de clases")
            return True
        except Exception as e:
            print(f"✗ Error cargando clases: {e}")
            return False
    
    def cargar_datos_alumnos(self, archivo_csv):
        """Carga datos de seguimiento de alumnos desde CSV."""
        try:
            self.df_alumnos = pd.read_csv(archivo_csv)
            print(f"✓ Cargados {len(self.df_alumnos)} registros de alumnos")
            return True
        except Exception as e:
            print(f"✗ Error cargando alumnos: {e}")
            return False
    
    def cargar_datos_evaluaciones(self, archivo_csv):
        """Carga datos de evaluaciones desde CSV."""
        try:
            self.df_evaluaciones = pd.read_csv(archivo_csv, parse_dates=['fecha'])
            print(f"✓ Cargados {len(self.df_evaluaciones)} registros de evaluaciones")
            return True
        except Exception as e:
            print(f"✗ Error cargando evaluaciones: {e}")
            return False
    
    # ------------------------------------------------------------------------
    # ANÁLISIS DE CLASES
    # ------------------------------------------------------------------------
    
    def analizar_asistencia_grupo(self, grupo):
        """Analiza patrones de asistencia de un grupo."""
        df = self.df_clases[self.df_clases['grupo'] == grupo]
        
        return {
            'grupo': grupo,
            'clases_impartidas': len(df),
            'asistencia_promedio': df['tasa_asistencia'].mean(),
            'asistencia_minima': df['tasa_asistencia'].min(),
            'asistencia_maxima': df['tasa_asistencia'].max(),
            'tendencia': self._calcular_tendencia(df['tasa_asistencia']),
            'clases_bajo_umbral': len(df[df['tasa_asistencia'] < self.config['umbral_asistencia_alerta']])
        }
    
    def analizar_participacion_grupo(self, grupo):
        """Analiza niveles de participación de un grupo."""
        df = self.df_clases[self.df_clases['grupo'] == grupo]
        
        return {
            'grupo': grupo,
            'participacion_promedio': df['participacion'].mean(),
            'comprension_promedio': df['comprension'].mean(),
            'mejor_semana': df.loc[df['participacion'].idxmax(), 'semana'] if len(df) > 0 else None,
            'peor_semana': df.loc[df['participacion'].idxmin(), 'semana'] if len(df) > 0 else None,
            'tendencia_participacion': self._calcular_tendencia(df['participacion']),
            'tendencia_comprension': self._calcular_tendencia(df['comprension'])
        }
    
    def analizar_actividades_efectivas(self):
        """Identifica qué actividades son más efectivas."""
        if self.df_clases is None:
            return None
            
        actividades = self.df_clases.groupby('actividad_favorita').agg({
            'participacion': 'mean',
            'comprension': 'mean',
            'fecha': 'count'
        }).rename(columns={'fecha': 'frecuencia'})
        
        actividades['efectividad'] = (actividades['participacion'] + actividades['comprension']) / 2
        actividades = actividades.sort_values('efectividad', ascending=False)
        
        return actividades.to_dict('index')
    
    def identificar_temas_dificiles(self, umbral_comprension=3.0):
        """Identifica temas que consistentemente tienen baja comprensión."""
        if self.df_clases is None:
            return []
            
        temas_dificiles = self.df_clases[
            self.df_clases['comprension'] < umbral_comprension
        ].groupby('tema').agg({
            'comprension': 'mean',
            'fecha': 'count'
        }).rename(columns={'fecha': 'ocurrencias'})
        
        # Ordenar por menor comprensión
        temas_dificiles = temas_dificiles.sort_values('comprension')
        
        return [
            {'tema': tema, 'comprension_promedio': row['comprension'], 'veces_impartido': row['ocurrencias']}
            for tema, row in temas_dificiles.iterrows()
        ]
    
    def extraer_dudas_frecuentes(self):
        """Extrae y cuenta las dudas más frecuentes."""
        if self.df_clases is None or 'dudas_frecuentes' not in self.df_clases.columns:
            return {}
            
        # Juntar todas las dudas y contar frecuencia
        todas_dudas = []
        for dudas in self.df_clases['dudas_frecuentes'].dropna():
            # Separar por comas o punto y coma
            for duda in str(dudas).replace(';', ',').split(','):
                duda_limpia = duda.strip().lower()
                if duda_limpia:
                    todas_dudas.append(duda_limpia)
        
        # Contar frecuencias
        from collections import Counter
        return dict(Counter(todas_dudas).most_common(20))
    
    # ------------------------------------------------------------------------
    # ANÁLISIS DE ALUMNOS
    # ------------------------------------------------------------------------
    
    def identificar_alumnos_en_riesgo(self):
        """Identifica alumnos que necesitan intervención urgente."""
        if self.df_alumnos is None:
            return []
            
        # Última semana de datos por alumno
        ultimos_datos = self.df_alumnos.sort_values('semana').groupby('alumno_id').last()
        
        alumnos_riesgo = []
        for alumno_id, datos in ultimos_datos.iterrows():
            riesgos = []
            
            # Verificar tareas
            if datos['tareas_pct'] < 50:
                riesgos.append('tareas_bajas')
            
            # Verificar participación
            if datos['participacion'] <= 2:
                riesgos.append('participacion_baja')
            
            # Verificar calidad
            if datos['calidad_tareas'] <= 2:
                riesgos.append('calidad_baja')
            
            if riesgos:
                alumnos_riesgo.append({
                    'alumno_id': alumno_id,
                    'grupo': datos['grupo'],
                    'riesgos': riesgos,
                    'tareas_pct': datos['tareas_pct'],
                    'participacion': datos['participacion'],
                    'semana': datos['semana']
                })
        
        return sorted(alumnos_riesgo, key=lambda x: len(x['riesgos']), reverse=True)
    
    def identificar_alumnos_destacados(self):
        """Identifica alumnos con desempeño sobresaliente."""
        if self.df_alumnos is None:
            return []
            
        # Promedios por alumno
        promedios = self.df_alumnos.groupby(['alumno_id', 'grupo']).agg({
            'tareas_pct': 'mean',
            'calidad_tareas': 'mean',
            'participacion': 'mean'
        })
        
        # Puntaje compuesto
        promedios['puntaje'] = (
            promedios['tareas_pct'] / 100 * 0.3 +
            promedios['calidad_tareas'] / 5 * 0.35 +
            promedios['participacion'] / 5 * 0.35
        )
        
        # Top 10%
        umbral = promedios['puntaje'].quantile(0.9)
        destacados = promedios[promedios['puntaje'] >= umbral]
        
        return [
            {
                'alumno_id': idx[0],
                'grupo': idx[1],
                'puntaje': row['puntaje'],
                'tareas_pct': row['tareas_pct'],
                'calidad': row['calidad_tareas'],
                'participacion': row['participacion']
            }
            for idx, row in destacados.iterrows()
        ]
    
    def analizar_errores_comunes(self):
        """Analiza errores más comunes entre alumnos."""
        if self.df_alumnos is None or 'errores_frecuentes' not in self.df_alumnos.columns:
            return {}
            
        # Contar errores
        todos_errores = []
        for errores in self.df_alumnos['errores_frecuentes'].dropna():
            for error in str(errores).replace(';', ',').split(','):
                error_limpio = error.strip().lower()
                if error_limpio:
                    todos_errores.append(error_limpio)
        
        from collections import Counter
        return dict(Counter(todos_errores).most_common(10))
    
    # ------------------------------------------------------------------------
    # ANÁLISIS DE EVALUACIONES
    # ------------------------------------------------------------------------
    
    def analizar_rendimiento_evaluaciones(self, grupo=None):
        """Analiza rendimiento en evaluaciones por grupo."""
        if self.df_evaluaciones is None:
            return None
            
        df = self.df_evaluaciones
        if grupo:
            df = df[df['grupo'] == grupo]
        
        return {
            'puntaje_promedio': df['puntaje_total'].mean(),
            'desviacion_estandar': df['puntaje_total'].std(),
            'puntaje_minimo': df['puntaje_total'].min(),
            'puntaje_maximo': df['puntaje_total'].max(),
            'tasa_aprobacion': len(df[df['puntaje_total'] >= 60]) / len(df) if len(df) > 0 else 0,
            'areas_por_competencia': {
                'comprension_oral': df['comprension_oral'].mean() if 'comprension_oral' in df.columns else None,
                'comprension_escrita': df['comprension_escrita'].mean() if 'comprension_escrita' in df.columns else None,
                'gramatica': df['gramatica'].mean() if 'gramatica' in df.columns else None,
                'produccion_escrita': df['produccion_escrita'].mean() if 'produccion_escrita' in df.columns else None
            }
        }
    
    def predecir_exito_delf(self, grupo):
        """Predice probabilidad de éxito en DELF basado en datos actuales."""
        if self.df_evaluaciones is None or self.df_alumnos is None:
            return None
            
        # Combinar datos de evaluaciones y seguimiento
        eval_grupo = self.df_evaluaciones[self.df_evaluaciones['grupo'] == grupo]
        alumnos_grupo = self.df_alumnos[self.df_alumnos['grupo'] == grupo]
        
        if len(eval_grupo) == 0:
            return {'grupo': grupo, 'prediccion': None, 'mensaje': 'Sin datos de evaluaciones'}
        
        # Modelo simple: puntaje promedio + factor de tareas y participación
        puntaje_promedio = eval_grupo.groupby('alumno_id')['puntaje_total'].mean()
        
        # Ajustar por tareas y participación
        tareas_promedio = alumnos_grupo.groupby('alumno_id')['tareas_pct'].mean()
        participacion_promedio = alumnos_grupo.groupby('alumno_id')['participacion'].mean()
        
        # Fórmula: 60% evaluaciones, 20% tareas, 20% participación
        predicciones = []
        for alumno in puntaje_promedio.index:
            puntaje = puntaje_promedio.get(alumno, 50)
            tareas = tareas_promedio.get(alumno, 50)
            participacion = participacion_promedio.get(alumno, 3) * 20  # Normalizar a 0-100
            
            prediccion = puntaje * 0.6 + tareas * 0.2 + participacion * 0.2
            predicciones.append(prediccion >= 60)  # DELF requiere 50/100 pero ponemos 60 como umbral seguro
        
        tasa_prediccion = sum(predicciones) / len(predicciones) if predicciones else 0
        
        return {
            'grupo': grupo,
            'prediccion_aprobacion': tasa_prediccion,
            'alumnos_evaluados': len(predicciones),
            'alumnos_probables_aprobar': sum(predicciones),
            'confianza': 'Alta' if len(eval_grupo) >= 3 else 'Baja (pocos datos)'
        }
    
    # ------------------------------------------------------------------------
    # GENERACIÓN DE REPORTES
    # ------------------------------------------------------------------------
    
    def generar_reporte_semanal(self, semana, grupo=None):
        """Genera reporte semanal completo."""
        reporte = {
            'fecha_generacion': datetime.now().isoformat(),
            'semana': semana,
            'grupo': grupo or 'Todos',
            'metricas_clases': {},
            'alertas': [],
            'recomendaciones': []
        }
        
        # Filtrar datos de la semana
        df_semana = self.df_clases[self.df_clases['semana'] == semana]
        if grupo:
            df_semana = df_semana[df_semana['grupo'] == grupo]
        
        if len(df_semana) == 0:
            reporte['mensaje'] = 'No hay datos para esta semana'
            return reporte
        
        # Métricas de clases
        reporte['metricas_clases'] = {
            'clases_impartidas': len(df_semana),
            'asistencia_promedio': df_semana['tasa_asistencia'].mean(),
            'participacion_promedio': df_semana['participacion'].mean(),
            'comprension_promedio': df_semana['comprension'].mean(),
            'actividad_favorita': df_semana['actividad_favorita'].mode().iloc[0] if len(df_semana) > 0 else None
        }
        
        # Alertas
        if reporte['metricas_clases']['asistencia_promedio'] < self.config['umbral_asistencia_alerta']:
            reporte['alertas'].append({
                'tipo': 'ASISTENCIA_BAJA',
                'mensaje': f"Asistencia promedio ({reporte['metricas_clases']['asistencia_promedio']:.0%}) por debajo del umbral",
                'accion_sugerida': 'Contactar a alumnos ausentes y revisar horarios'
            })
        
        if reporte['metricas_clases']['participacion_promedio'] < self.config['umbral_participacion_alerta']:
            reporte['alertas'].append({
                'tipo': 'PARTICIPACION_BAJA',
                'mensaje': f"Participación promedio ({reporte['metricas_clases']['participacion_promedio']:.1f}/5) baja",
                'accion_sugerida': 'Incorporar más actividades interactivas'
            })
        
        if reporte['metricas_clases']['comprension_promedio'] < self.config['umbral_comprension_refuerzo']:
            reporte['alertas'].append({
                'tipo': 'COMPRENSION_BAJA',
                'mensaje': f"Comprensión promedio ({reporte['metricas_clases']['comprension_promedio']:.1f}/5) requiere refuerzo",
                'accion_sugerida': 'Dedicar tiempo de repaso en siguiente clase'
            })
        
        # Recomendaciones basadas en datos
        dudas = self.extraer_dudas_frecuentes()
        if dudas:
            top_duda = list(dudas.keys())[0]
            reporte['recomendaciones'].append({
                'tipo': 'REFUERZO_TEMA',
                'contenido': f"La duda más frecuente es '{top_duda}'. Considerar actividad de refuerzo."
            })
        
        return reporte
    
    def generar_reporte_mensual(self, mes, año):
        """Genera reporte mensual agregado."""
        # Filtrar por mes
        df_mes = self.df_clases[
            (self.df_clases['fecha'].dt.month == mes) & 
            (self.df_clases['fecha'].dt.year == año)
        ]
        
        reporte = {
            'periodo': f"{año}-{mes:02d}",
            'fecha_generacion': datetime.now().isoformat(),
            'resumen_general': {
                'clases_totales': len(df_mes),
                'grupos_activos': df_mes['grupo'].nunique(),
                'asistencia_promedio': df_mes['tasa_asistencia'].mean(),
                'participacion_promedio': df_mes['participacion'].mean(),
                'comprension_promedio': df_mes['comprension'].mean()
            },
            'por_grupo': {},
            'tendencias': {},
            'recomendaciones_sistema': []
        }
        
        # Análisis por grupo
        for grupo in df_mes['grupo'].unique():
            reporte['por_grupo'][grupo] = self.analizar_asistencia_grupo(grupo)
        
        # Tendencias
        reporte['tendencias']['temas_dificiles'] = self.identificar_temas_dificiles()[:5]
        reporte['tendencias']['actividades_efectivas'] = self.analizar_actividades_efectivas()
        reporte['tendencias']['errores_comunes'] = self.analizar_errores_comunes()
        
        return reporte
    
    def exportar_reporte_json(self, reporte, nombre_archivo):
        """Exporta reporte a JSON."""
        ruta = os.path.join(self.config['ruta_reportes'], nombre_archivo)
        
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(reporte, f, ensure_ascii=False, indent=2, default=str)
        
        print(f"✓ Reporte exportado: {ruta}")
    
    def exportar_reporte_markdown(self, reporte, nombre_archivo):
        """Exporta reporte a Markdown para fácil lectura."""
        ruta = os.path.join(self.config['ruta_reportes'], nombre_archivo)
        
        md = f"""# 📊 Reporte IncluCIDE Francés
**Generado:** {reporte.get('fecha_generacion', 'N/A')}

## Resumen

"""
        
        if 'metricas_clases' in reporte:
            metricas = reporte['metricas_clases']
            md += f"""### Métricas de la Semana {reporte.get('semana', '')}

| Métrica | Valor |
|---------|-------|
| Clases impartidas | {metricas.get('clases_impartidas', 'N/A')} |
| Asistencia promedio | {metricas.get('asistencia_promedio', 0):.0%} |
| Participación promedio | {metricas.get('participacion_promedio', 0):.1f}/5 |
| Comprensión promedio | {metricas.get('comprension_promedio', 0):.1f}/5 |
| Actividad favorita | {metricas.get('actividad_favorita', 'N/A')} |

"""
        
        if reporte.get('alertas'):
            md += "## ⚠️ Alertas\n\n"
            for alerta in reporte['alertas']:
                md += f"- **{alerta['tipo']}**: {alerta['mensaje']}\n"
                md += f"  - *Acción sugerida*: {alerta['accion_sugerida']}\n\n"
        
        if reporte.get('recomendaciones'):
            md += "## 💡 Recomendaciones\n\n"
            for rec in reporte['recomendaciones']:
                md += f"- **{rec['tipo']}**: {rec['contenido']}\n"
        
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(md)
        
        print(f"✓ Reporte Markdown exportado: {ruta}")
    
    # ------------------------------------------------------------------------
    # UTILIDADES
    # ------------------------------------------------------------------------
    
    def _calcular_tendencia(self, serie):
        """Calcula tendencia de una serie (subiendo, bajando, estable)."""
        if len(serie) < 2:
            return 'insuficientes_datos'
        
        # Regresión lineal simple
        x = np.arange(len(serie))
        y = serie.values
        
        # Pendiente
        pendiente = np.polyfit(x, y, 1)[0]
        
        if pendiente > 0.1:
            return 'subiendo'
        elif pendiente < -0.1:
            return 'bajando'
        else:
            return 'estable'


# ============================================================================
# GENERADOR DE INSIGHTS CON IA
# ============================================================================

class GeneradorInsightsIA:
    """Genera prompts para obtener insights adicionales con ChatGPT/Copilot."""
    
    @staticmethod
    def generar_prompt_mejora_clase(datos_clase):
        """Genera prompt para mejorar una clase específica."""
        return f"""
Analiza los siguientes datos de una clase de francés nivel {datos_clase.get('nivel', 'A1')} 
y sugiere mejoras específicas:

DATOS DE LA CLASE:
- Tema: {datos_clase.get('tema', 'No especificado')}
- Participación: {datos_clase.get('participacion', 'N/A')}/5
- Comprensión: {datos_clase.get('comprension', 'N/A')}/5
- Dudas frecuentes: {datos_clase.get('dudas', 'Ninguna registrada')}
- Actividad favorita: {datos_clase.get('actividad_favorita', 'No especificada')}
- Problemas: {datos_clase.get('problemas', 'Ninguno')}

CONTEXTO:
- Alumnos: Adolescentes mexicanos 12-15 años
- Modalidad: Online (50 minutos)
- Siguiente clase: {datos_clase.get('siguiente_tema', 'No especificado')}

SOLICITUD:
1. ¿Cómo reforzar el tema que tuvo baja comprensión?
2. ¿Qué actividad alternativa propones para aumentar participación?
3. ¿Cómo abordar las dudas frecuentes de manera efectiva?
4. Sugiere una actividad de "warm-up" para la siguiente clase que conecte con lo aprendido.
"""
    
    @staticmethod
    def generar_prompt_alumno_riesgo(datos_alumno):
        """Genera prompt para estrategia de intervención con alumno en riesgo."""
        return f"""
Un alumno de francés nivel {datos_alumno.get('nivel', 'A1')} presenta las siguientes 
dificultades y necesita intervención:

DATOS DEL ALUMNO:
- Grupo: {datos_alumno.get('grupo', 'No especificado')}
- Semana actual: {datos_alumno.get('semana', 'N/A')}
- Tareas entregadas: {datos_alumno.get('tareas_pct', 0)}%
- Participación: {datos_alumno.get('participacion', 'N/A')}/5
- Errores frecuentes: {datos_alumno.get('errores', 'No especificados')}
- Fortalezas: {datos_alumno.get('fortalezas', 'No identificadas')}
- Riesgos identificados: {', '.join(datos_alumno.get('riesgos', []))}

CONTEXTO:
- Edad: 12-15 años
- Modalidad: Online
- Ya se contactó a padres: {datos_alumno.get('contacto_padres', 'No')}

SOLICITUD:
1. Estrategia de intervención personalizada (5 acciones concretas)
2. Mensaje sugerido para padres (en español, tono empático)
3. Actividades de refuerzo específicas para sus errores frecuentes
4. Cómo aprovechar sus fortalezas para motivarle
"""
    
    @staticmethod
    def generar_prompt_analisis_semestral(datos_semestre):
        """Genera prompt para análisis profundo del semestre."""
        return f"""
Realiza un análisis pedagógico profundo del siguiente semestre de francés:

DATOS DEL SEMESTRE:
- Nivel: {datos_semestre.get('nivel', 'A1.1')}
- Grupos: {datos_semestre.get('num_grupos', 1)}
- Alumnos totales: {datos_semestre.get('total_alumnos', 'N/A')}
- Clases impartidas: {datos_semestre.get('clases_totales', 'N/A')}

MÉTRICAS PROMEDIO:
- Asistencia: {datos_semestre.get('asistencia_promedio', 0):.0%}
- Participación: {datos_semestre.get('participacion_promedio', 0):.1f}/5
- Comprensión: {datos_semestre.get('comprension_promedio', 0):.1f}/5
- Aprobación evaluaciones: {datos_semestre.get('tasa_aprobacion', 0):.0%}

TEMAS MÁS DIFÍCILES:
{datos_semestre.get('temas_dificiles', 'No identificados')}

ERRORES MÁS COMUNES:
{datos_semestre.get('errores_comunes', 'No identificados')}

ACTIVIDADES MÁS EFECTIVAS:
{datos_semestre.get('actividades_efectivas', 'No identificadas')}

SOLICITUD:
1. Análisis de fortalezas y debilidades del programa
2. Recomendaciones para ajustar el plan de estudios
3. Estrategias para mejorar los temas difíciles identificados
4. Cambios sugeridos en la metodología para el próximo semestre
5. Predicción de resultados DELF basada en los datos
"""


# ============================================================================
# FUNCIÓN PRINCIPAL DE EJECUCIÓN
# ============================================================================

def main():
    """Función principal para ejecutar análisis."""
    print("=" * 60)
    print("SISTEMA DE ANÁLISIS - IncluCIDE Francés")
    print("=" * 60)
    
    # Inicializar analizador
    analizador = AnalizadorIncluCIDE()
    
    # Ejemplo de uso (descomentar cuando haya datos reales)
    """
    # Cargar datos
    analizador.cargar_datos_clases('datos/clases_2026.csv')
    analizador.cargar_datos_alumnos('datos/alumnos_2026.csv')
    analizador.cargar_datos_evaluaciones('datos/evaluaciones_2026.csv')
    
    # Generar reporte semanal
    reporte = analizador.generar_reporte_semanal(semana=3, grupo='A1.1-2026A')
    analizador.exportar_reporte_markdown(reporte, 'reporte_semana3.md')
    
    # Identificar alumnos en riesgo
    riesgo = analizador.identificar_alumnos_en_riesgo()
    print(f"\nAlumnos en riesgo: {len(riesgo)}")
    for alumno in riesgo[:5]:
        print(f"  - {alumno['alumno_id']}: {alumno['riesgos']}")
    
    # Generar prompt para IA
    generador = GeneradorInsightsIA()
    prompt = generador.generar_prompt_mejora_clase({
        'tema': 'Passé Composé',
        'participacion': 3,
        'comprension': 2,
        'dudas': 'Auxiliar être vs avoir',
        'nivel': 'A2.1'
    })
    print("\nPrompt para IA:")
    print(prompt)
    """
    
    print("\n✓ Sistema inicializado correctamente")
    print("  Usa las funciones del analizador con tus datos reales")
    print("  Ejemplo: analizador.cargar_datos_clases('archivo.csv')")


if __name__ == "__main__":
    main()
