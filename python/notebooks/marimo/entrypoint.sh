#!/bin/sh
echo "Running marimo with notebook: ${NOTEBOOK_NAME}"
exec marimo run notebooks/${NOTEBOOK_NAME}.py --host 0.0.0.0 -p 8080