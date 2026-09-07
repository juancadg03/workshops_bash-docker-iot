#!/bin/bash

echo "Analizando logs..."

if [ -f /logs/monitor.log ]
then
    echo "Número de líneas:"
    wc -l /logs/monitor.log

    echo "Últimas líneas:"
    tail /logs/monitor.log
else
    echo "No existe el archivo monitor.log"
fi
