#!/bin/bash - 
#===============================================================================
#
#          FILE: run.sh
# 
#         USAGE: ./run.sh 
# 
#   DESCRIPTION: starts up the dev tracker server
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: Diaa Kasem (me@diaa.me), 
#  ORGANIZATION: 
#       CREATED: 02/26/15 09:43
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error
python app/server.py

