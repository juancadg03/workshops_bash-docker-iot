#!/bin/bash

if [ $# -lt 1 ]; then
    echo "Error: No se especifico ningun archivo."
    echo "Uso correcto: $0 <archivo1> [archivo2 ...]"
    exit 1
fi

 ($@)
for ARCHIVO in "$@"; do
    echo "==============================================="
    echo "       INFORMACION DE ARCHIVO: $ARCHIVO"
    echo "==============================================="

  
    if [ ! -f "$ARCHIVO" ]; then
        echo "Error: El archivo '$ARCHIVO' no existe."
        echo "==============================================="
        echo ""
        continue
    fi


    echo "Archivo: $ARCHIVO"

    LINEAS=$(wc -l < "$ARCHIVO")
    echo "- Cantidad de lineas: $LINEAS"

    PALABRAS=$(wc -w < "$ARCHIVO")
    echo "- Cantidad de palabras: $PALABRAS"

    CARACTERES=$(wc -m < "$ARCHIVO")
    echo "- Cantidad de caracteres: $CARACTERES"

    ERRORES=$(grep -c "ERROR" "$ARCHIVO" 2>/dev/null)
    echo "- Lineas con ERROR: $ERRORES"

    ADVERTENCIAS=$(grep -c "WARN" "$ARCHIVO" 2>/dev/null)
    echo "- Lineas con WARN: $ADVERTENCIAS"

    echo "==============================================="
    echo ""
done
