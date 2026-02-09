# Script para organizar archivos del curso de francés IncluCIDE
$baseDir = "C:\Users\donob\Documents\Notion_Planeacion_francés"
Set-Location $baseDir

Write-Host "🔧 Creando estructura de carpetas..." -ForegroundColor Cyan

# Crear estructura principal
$folders = @(
    "01_DOCUMENTACION",
    "02_PLAN_ESTUDIOS",
    "03_MATERIALES\Presentaciones\A1.1",
    "03_MATERIALES\Presentaciones\A1.2",
    "03_MATERIALES\Presentaciones\A2.1",
    "03_MATERIALES\Presentaciones\A2.2",
    "03_MATERIALES\Presentaciones\B1.1",
    "03_MATERIALES\Guias_Profesor\A1.1",
    "03_MATERIALES\Guias_Profesor\A1.2",
    "03_MATERIALES\Guias_Profesor\A2.1",
    "03_MATERIALES\Guias_Profesor\A2.2",
    "03_MATERIALES\Guias_Profesor\B1.1",
    "03_MATERIALES\Actividades_Recursos",
    "04_EVALUACION\Rubricas",
    "04_EVALUACION\Examenes",
    "05_CAPACITACION_DOCENTE\Modulos",
    "05_CAPACITACION_DOCENTE\Materiales_Apoyo",
    "06_SISTEMA_DATOS_IA",
    "07_COMUNICACION_PADRES"
)

foreach ($folder in $folders) {
    New-Item -ItemType Directory -Force -Path $folder | Out-Null
}

Write-Host "✅ Carpetas creadas" -ForegroundColor Green

# Mover archivos de documentación principal
Write-Host "`n📚 Organizando documentación principal..." -ForegroundColor Cyan
$docFiles = @(
    "PROYECTO_SISTEMA_INTEGRAL.md",
    "MANUAL_PROGRAMA_INCLUCIDE.md",
    "SISTEMA_VERIFICACION.md",
    "INVENTARIO_MAESTRO.md",
    "CONTROL_CALIDAD_PROGRESO.md",
    "VERIFICACION_B1.md",
    "REVISION_PEDAGOGICA.md",
    "RESUMEN_CAMBIOS.md",
    "REPORTE_EVIDENCIA_20260209.md",
    "INDICE_VISUAL_CAMBIOS.md"
)
foreach ($file in $docFiles) {
    if (Test-Path $file) {
        Move-Item $file "01_DOCUMENTACION\" -Force
        Write-Host "  ✓ $file" -ForegroundColor Gray
    }
}

# Mover plan de estudios
Write-Host "`n📖 Organizando plan de estudios..." -ForegroundColor Cyan
$planFiles = @("plan.md", "plan2.md", "plan_backup.md")
foreach ($file in $planFiles) {
    if (Test-Path $file) {
        Move-Item $file "02_PLAN_ESTUDIOS\" -Force
        Write-Host "  ✓ $file" -ForegroundColor Gray
    }
}

# Mover presentaciones por nivel
Write-Host "`n🎨 Organizando presentaciones..." -ForegroundColor Cyan
$nivelesPresent = @("A1.1", "A1.2", "A2.1", "A2.2", "B1.1")
foreach ($nivel in $nivelesPresent) {
    $files = Get-ChildItem "PRESENTACION_${nivel}_*.md" -ErrorAction SilentlyContinue
    foreach ($file in $files) {
        Move-Item $file.FullName "03_MATERIALES\Presentaciones\$nivel\" -Force
        Write-Host "  ✓ $($file.Name)" -ForegroundColor Gray
    }
}

# Mover guías de profesor por nivel
Write-Host "`n👨‍🏫 Organizando guías de profesor..." -ForegroundColor Cyan
$nivelesGuia = @("A1.1", "A1.2", "A2.1", "A2.2", "B1.1")
foreach ($nivel in $nivelesGuia) {
    $files = Get-ChildItem "GUIA_PROFESOR_${nivel}_*.md" -ErrorAction SilentlyContinue
    foreach ($file in $files) {
        Move-Item $file.FullName "03_MATERIALES\Guias_Profesor\$nivel\" -Force
        Write-Host "  ✓ $($file.Name)" -ForegroundColor Gray
    }
}

# Mover plantilla y recursos
Write-Host "`n📋 Organizando plantillas y recursos..." -ForegroundColor Cyan
$recursosFiles = @(
    "GUIA_PROFESOR_PLANTILLA.md",
    "ACTIVIDADES_INTERACTIVAS.md",
    "VIDEOS_APOYO_CURADOS.md"
)
foreach ($file in $recursosFiles) {
    if (Test-Path $file) {
        Move-Item $file "03_MATERIALES\Actividades_Recursos\" -Force
        Write-Host "  ✓ $file" -ForegroundColor Gray
    }
}

# Mover rúbricas
Write-Host "`n📊 Organizando rúbricas..." -ForegroundColor Cyan
$rubricaFiles = Get-ChildItem "RUBRICA_*.md" -ErrorAction SilentlyContinue
foreach ($file in $rubricaFiles) {
    Move-Item $file.FullName "04_EVALUACION\Rubricas\" -Force
    Write-Host "  ✓ $($file.Name)" -ForegroundColor Gray
}

# Mover evaluaciones
Write-Host "`n✍️ Organizando evaluaciones..." -ForegroundColor Cyan
$evalFiles = Get-ChildItem "EVALUACION_*.md" -ErrorAction SilentlyContinue
foreach ($file in $evalFiles) {
    Move-Item $file.FullName "04_EVALUACION\Examenes\" -Force
    Write-Host "  ✓ $($file.Name)" -ForegroundColor Gray
}

# Mover módulos de capacitación
Write-Host "`n🎓 Organizando capacitación docente..." -ForegroundColor Cyan
$capacitacionModulos = Get-ChildItem "CAPACITACION_MODULO*.md" -ErrorAction SilentlyContinue
foreach ($file in $capacitacionModulos) {
    Move-Item $file.FullName "05_CAPACITACION_DOCENTE\Modulos\" -Force
    Write-Host "  ✓ $($file.Name)" -ForegroundColor Gray
}

$capacitacionOtros = @(
    "MANUAL_CAPACITACION_DOCENTE.md",
    "BANCO_ACTIVIDADES_CAPACITACION.md",
    "TALLER_CAPACITACION_AGENDA.md",
    "GUIA_INDUCCION_RAPIDA.md"
)
foreach ($file in $capacitacionOtros) {
    if (Test-Path $file) {
        Move-Item $file "05_CAPACITACION_DOCENTE\Materiales_Apoyo\" -Force
        Write-Host "  ✓ $file" -ForegroundColor Gray
    }
}

# Mover sistema de datos e IA
Write-Host "`n🤖 Organizando sistema de datos e IA..." -ForegroundColor Cyan
$datosIAFiles = @(
    "SISTEMA_IA_DATOS.md",
    "FORMULARIOS_RECOLECCION.md",
    "DISENO_DASHBOARD.md"
)
foreach ($file in $datosIAFiles) {
    if (Test-Path $file) {
        Move-Item $file "06_SISTEMA_DATOS_IA\" -Force
        Write-Host "  ✓ $file" -ForegroundColor Gray
    }
}

# Buscar script Python si existe
if (Test-Path "scripts_analisis_datos.py") {
    Move-Item "scripts_analisis_datos.py" "06_SISTEMA_DATOS_IA\" -Force
    Write-Host "  ✓ scripts_analisis_datos.py" -ForegroundColor Gray
}

Write-Host "`n✅ ¡Organización completada exitosamente!" -ForegroundColor Green
Write-Host "`n📂 Estructura final:" -ForegroundColor Cyan
tree /F /A | Select-Object -First 50

Write-Host "`n💡 Tip: Navega a cada carpeta para ver su contenido organizado" -ForegroundColor Yellow
