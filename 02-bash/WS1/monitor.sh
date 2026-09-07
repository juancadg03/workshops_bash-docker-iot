#!/bin/bash

echo "==============================================="
echo "        MONITOR BÁSICO DEL CONTENEDOR"
echo "==============================================="

echo "1. Hostname: $(hostname)"
echo "2. Usuario actual: $(whoami)"
echo "3. Fecha y hora: $(date)"
echo "4. Directorio actual: $(pwd)"

echo "5. Espacio en disco:"
df -h
echo ""

echo -n "6. Cantidad aproximada de procesos activos: "
ps -e | wc -l

echo "===== FIN DEL REPORTE ====="
