#!/bin/sh -e
set -x

isort --recursive  --force-single-line-imports --apply src
autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place src --exclude=__init__.py
isort --recursive --apply src
black src
flake8 src
