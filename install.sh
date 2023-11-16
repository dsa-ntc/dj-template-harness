#!/bin/bash

# FILEPATH: /workspaces/dj-template-harness/install.sh

if [ ! -d ".venv" ]; then
    python -m venv .venv
fi

source .venv/bin/activate
pip install .
django-admin migrate
