#!/usr/bin/env bash

source common_functions.sh

PORT="$1"
cwd=`pwd`


activate_python_venv
cd "loadbalancer"
run_flask_app ${PORT} ${cwd}"/load_balancer.py"