#!/usr/bin/env bash

function change_cwd_to_server_port()
{
local port="$1"
local cwd_path='server'${port}
cd ${cwd_path}
}

function activate_python_venv()
{
local path_to_venv_activate=`ag -g "venv/bin/activate$"`
echo DBG ${path_to_venv_activate}
source ${path_to_venv_activate}
}

function run_flask_app()
{
local port="$1"
local main_file_path="$2"
export FLASK_APP=${main_file_path}
flask run -p ${port}
}

