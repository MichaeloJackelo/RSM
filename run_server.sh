#!/usr/bin/env bash

source common_functions.sh

function change_cwd_to_server_port()
{
local port="$1"
local cwd_path='server'${port}
cd ${cwd_path}
}


PORT="$1"
export PI_NUMBER="$2"
cwd=`pwd`


activate_python_venv
change_cwd_to_server_port ${PORT}
run_flask_app ${PORT} ${cwd}"/server.py"
