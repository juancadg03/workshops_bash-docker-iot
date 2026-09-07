#!/bin/bash

echo "Monitor iniciado"

while true
do
    echo "$(date) - Monitor ejecutándose" >> /logs/monitor.log
    sleep 10
done
