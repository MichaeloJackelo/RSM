#!/usr/bin/env bash

source common_functions.sh

PORT="$1"
cwd=`pwd`


activate_python_venv
change_cwd_to_server_port ${PORT}
run_flask_app ${PORT} cwd"/server.py"
