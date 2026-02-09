# 🔒 SISTEMA DE VERIFICACIÓN Y CONTROL DE CALIDAD
## Protocolo de Auto-Auditoría para Generación de Contenido

---

## 1. FILOSOFÍA DEL SISTEMA

### Problema a resolver
Cuando se generan grandes cantidades de contenido educativo:
- Se pierden detalles por acumulación de contexto
- Se pueden inventar datos sin fuente verificable
- La coherencia entre archivos se degrada
- Los errores se propagan sin detección

### Solución: Sistema de 4 Capas con Evidencia

```
┌─────────────────────────────────────────────────────────────────┐
│                    PIPELINE DE VERIFICACIÓN                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐     │
│  │  CAPA 1  │──▶│  CAPA 2  │──▶│  CAPA 3  │──▶│  CAPA 4  │     │
│  │ Inventario│   │  Roles   │   │ Fuentes  │   │ Evidencia│     │
│  │ Completo │   │ Expertos │   │Verificables│  │ Auditable│     │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘     │
│       │              │              │              │            │
│       ▼              ▼              ▼              ▼            │
│  [Checklist]    [3 Perspectivas] [Referencias]  [Log público]  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. CAPA 1: INVENTARIO COMPLETO

### Propósito
Mantener una lista exhaustiva de TODO lo que debe existir, verificar contra lo que existe, identificar gaps.

### Formato de Inventario

```markdown
## INVENTARIO MAESTRO - [Fecha]

### Archivos Requeridos
| ID | Archivo | Estado | Verificado | Notas |
|----|---------|--------|------------|-------|
| P001 | PRESENTACION_A1.1_S1_Martes.md | ✅ Existe | ✅ 3 capas | OK |
| P002 | PRESENTACION_A1.1_S1_Jueves.md | ✅ Existe | ⏳ Pendiente | - |
| G001 | GUIA_PROFESOR_A1.1_S1_Martes.md | ✅ Existe | ✅ 3 capas | OK |
| G002 | GUIA_PROFESOR_A1.1_S1_Jueves.md | ❌ Falta | - | CREAR |
```

### Regla de Oro
**Nunca asumir que algo existe. Siempre verificar con `view` o `glob` antes de marcar como completado.**

---

## 3. CAPA 2: ROLES DE VERIFICACIÓN

### Roles Obligatorios para Contenido Educativo

#### 🎓 ROL: ESTUDIANTE (12-15 años, principiante)
**Pregunta central:** "¿Entiendo esto sin ayuda externa?"

| Criterio | Pregunta de Verificación | Pasa/Falla |
|----------|--------------------------|------------|
| Claridad | ¿Las instrucciones son claras? | □ |
| Carga cognitiva | ¿Hay máximo 10-12 palabras nuevas? | □ |
| Engagement | ¿Hay algo divertido/interesante? | □ |
| Progresión | ¿Esto conecta con lo anterior? | □ |
| Ejemplos | ¿Hay suficientes ejemplos antes de practicar? | □ |

#### 👨‍🏫 ROL: PROFESOR (ejecutor del material)
**Pregunta central:** "¿Puedo dar esta clase sin prepararme más?"

| Criterio | Pregunta de Verificación | Pasa/Falla |
|----------|--------------------------|------------|
| Timing | ¿50 minutos es realista? | □ |
| Notas | ¿Las notas del presentador son suficientes? | □ |
| Materiales | ¿Tengo todo lo necesario? | □ |
| Backup | ¿Hay plan B si algo falla? | □ |
| Errores | ¿Sé cómo manejar errores comunes? | □ |

#### 🎯 ROL: EXPERTO EN FRANCÉS (lingüista/DELF examiner)
**Pregunta central:** "¿Esto es correcto y apropiado para el nivel?"

| Criterio | Pregunta de Verificación | Pasa/Falla |
|----------|--------------------------|------------|
| Gramática | ¿Las explicaciones son correctas? | □ |
| Pronunciación | ¿El IPA es preciso? | □ |
| Nivel CECR | ¿Corresponde al nivel indicado? | □ |
| Progresión | ¿Sigue estándares didácticos? | □ |
| Excepciones | ¿Las irregularidades están bien manejadas? | □ |

### Roles Adicionales (según tipo de contenido)

| Tipo de Contenido | Rol Adicional | Pregunta Central |
|-------------------|---------------|------------------|
| Scripts Python | Desarrollador Senior | ¿El código funciona y es mantenible? |
| Formularios | UX Designer | ¿Es fácil de completar? |
| Dashboards | Data Analyst | ¿Las métricas son útiles y correctas? |
| Comunicación padres | Padre de familia | ¿Entiendo qué hacer? |

---

## 4. CAPA 3: FUENTES VERIFICABLES

### Principio de Honestidad
**Si no tengo una fuente verificable, debo declararlo explícitamente.**

### Categorías de Afirmaciones

#### ✅ VERIFICABLE (usar sin restricción)
- Conjugaciones verbales (Bescherelle)
- Pronunciación IPA (Le Petit Robert, Wiktionary)
- Niveles CECR (documentos oficiales del Consejo de Europa)
- Vocabulario por nivel (listas DELF oficiales)

**Formato de citación:**
```
[FUENTE: Bescherelle, La conjugaison pour tous, p.XX]
[FUENTE: CECR, Common European Framework, Appendix A]
```

#### ⚠️ INFERENCIA RAZONABLE (declarar como tal)
- "Basándome en el patrón de los niveles anteriores..."
- "Por analogía con otros métodos FLE..."
- "Siguiendo la progresión típica DELF..."

**Formato:**
```
[INFERENCIA: Basado en progresión típica de métodos FLE como Alter Ego]
```

#### ❌ INVENCIÓN (prohibido sin declarar)
- Estadísticas de aprendizaje inventadas
- Citas de autores sin verificar
- Datos de investigación no confirmados

**Si no tengo fuente, debo escribir:**
```
[SIN FUENTE VERIFICABLE - Requiere validación del usuario]
```

### Fuentes Autorizadas para este Proyecto

| Categoría | Fuentes Primarias | Cómo Verificar |
|-----------|-------------------|----------------|
| Conjugación | Bescherelle, Le Conjugueur (web) | Cruzar 2 fuentes |
| Pronunciación | IPA oficial, Forvo, Wiktionary FR | Notación estándar IPA |
| Niveles CECR | Consejo de Europa, CIEP | Descriptores oficiales |
| Vocabulario | Listas DELF A1-B1, Français Facile | Frecuencia de uso |
| Didáctica | Alter Ego, Édito, plan UPIICSA original | Secuenciación probada |

---

## 5. CAPA 4: EVIDENCIA AUDITABLE

### Log de Verificación

Cada archivo generado debe tener un bloque de verificación al final:

```markdown
---
## 📋 REGISTRO DE VERIFICACIÓN

### Metadatos
- **Archivo:** [nombre]
- **Generado:** [fecha]
- **Última verificación:** [fecha]

### Verificación por Roles
| Rol | Verificador | Fecha | Resultado | Notas |
|-----|-------------|-------|-----------|-------|
| Estudiante | Claude (auto) | 2026-02-09 | ✅ PASA | Claridad OK |
| Profesor | Claude (auto) | 2026-02-09 | ✅ PASA | Timing realista |
| Experto FR | Claude (auto) | 2026-02-09 | ✅ PASA | IPA correcto |

### Fuentes Utilizadas
1. [FUENTE] Bescherelle - conjugación ÊTRE p.84
2. [FUENTE] CECR A1 - Can-do statements
3. [INFERENCIA] Progresión basada en Alter Ego 1

### Limitaciones Declaradas
- [ ] Contiene inferencias sin fuente primaria
- [ ] Requiere validación de nativo
- [x] Auto-verificado, pendiente revisión humana

### Checklist Final
- [x] Inventario actualizado
- [x] 3 roles verificados
- [x] Fuentes declaradas
- [x] Evidencia registrada
---
```

---

## 6. PROTOCOLO DE EJECUCIÓN

### Antes de generar cualquier contenido:

```
1. INVENTARIO
   □ ¿Qué archivos deben existir?
   □ ¿Cuáles existen ya? (verificar con glob/view)
   □ ¿Cuáles faltan?

2. PRIORIZACIÓN
   □ Ordenar por dependencias (primero lo que otros necesitan)
   □ Agrupar por tipo (eficiencia)

3. GENERACIÓN
   □ Crear archivo
   □ Aplicar verificación de 3 roles
   □ Declarar fuentes
   □ Agregar bloque de evidencia

4. POST-GENERACIÓN
   □ Actualizar inventario
   □ Verificar coherencia con archivos relacionados
   □ Documentar en log maestro
```

### Durante generación larga (anti-olvido):

```
Cada 5 archivos generados:
  □ Re-leer inventario maestro
  □ Verificar que no hay drift de estilo
  □ Confirmar coherencia de nomenclatura
  □ Actualizar progreso visible

Cada 10 archivos generados:
  □ Revisión cruzada de muestra aleatoria
  □ Verificar que fuentes siguen siendo consistentes
  □ Buscar contradicciones entre archivos
```

---

## 7. PRUEBAS DE CALIDAD (DISEÑADAS PARA AUTO-APLICAR)

### Prueba 1: Coherencia de Conjugación
```
Seleccionar 3 archivos aleatorios
Buscar: conjugación de ÊTRE, AVOIR, verbos -ER
Verificar: ¿Son idénticas en todos los archivos?
Resultado: □ Pasa □ Falla (documentar discrepancia)
```

### Prueba 2: Progresión Lógica
```
Leer: Semana 3 Jueves de cualquier nivel
Pregunta: ¿Tiene sentido sin haber visto Semana 3 Martes?
Pregunta: ¿Repasa algo de Semana 2?
Resultado: □ Pasa □ Falla
```

### Prueba 3: IPA Consistente
```
Buscar: todas las instancias de "bonjour"
Verificar: ¿Todas dicen /bɔ̃.ʒuʁ/?
Resultado: □ Pasa □ Falla
```

### Prueba 4: Carga Cognitiva
```
Contar: palabras nuevas en cualquier presentación
Verificar: ¿Máximo 10-12?
Resultado: □ Pasa □ Falla
```

### Prueba 5: Timing Realista
```
Sumar: tiempos de cada sección en guía de profesor
Verificar: ¿Total = 48-52 minutos?
Resultado: □ Pasa □ Falla
```

---

## 8. FORMATO DE REPORTE DE EVIDENCIA

### Resumen Ejecutivo (para el usuario)

```markdown
# 📊 REPORTE DE VERIFICACIÓN - [Fecha]

## Estado General
- Archivos generados: X/Y
- Verificación completa: X/Y
- Alertas: Z

## Verificación por Capas
| Capa | Estado | Detalles |
|------|--------|----------|
| 1. Inventario | ✅ 100% | Todos los archivos listados |
| 2. Roles | ✅ 100% | 3 roles aplicados |
| 3. Fuentes | ⚠️ 95% | 5 inferencias sin fuente primaria |
| 4. Evidencia | ✅ 100% | Todos con bloque de verificación |

## Pruebas de Calidad
| Prueba | Resultado | Muestra |
|--------|-----------|---------|
| Coherencia conjugación | ✅ Pasa | 3/3 archivos |
| Progresión lógica | ✅ Pasa | 5/5 semanas |
| IPA consistente | ✅ Pasa | grep "bonjour" |
| Carga cognitiva | ✅ Pasa | 10 archivos random |
| Timing realista | ⚠️ 90% | 1 archivo con 55 min |

## Limitaciones Conocidas
1. IPA no verificado por nativo francés
2. Timing basado en estimación, no en ejecución real
3. [otras limitaciones]

## Próximos Pasos
1. [acción]
2. [acción]
```

---

## 9. APLICACIÓN INMEDIATA

### Para esta sesión, aplicaré:

1. **Crear inventario completo** de archivos requeridos vs existentes
2. **Identificar gaps** (qué falta)
3. **Generar faltantes** con verificación de 3 roles
4. **Documentar fuentes** explícitamente
5. **Producir reporte de evidencia** al final

### Compromiso de Honestidad

Cuando no tenga certeza:
- Diré "No tengo fuente verificable para esto"
- Marcaré como [INFERENCIA] o [REQUIERE VALIDACIÓN]
- No inventaré datos, estadísticas o citas

---

*Sistema diseñado: 2026-02-09*
*Propósito: Garantizar calidad y trazabilidad del contenido generado*
*Autor: Claude con supervisión de Donovan*
