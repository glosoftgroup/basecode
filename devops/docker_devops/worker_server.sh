#!/usr/bin/env bash

celery -A configuration.settings.celeryapp flower --port=5555