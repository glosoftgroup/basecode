#!/bin/bash
flake8 --exclude settings,*/migrations/*
exit $?
