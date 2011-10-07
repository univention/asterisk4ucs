#!/bin/bash

set -e
set -u

cd "`dirname $0`"

. settings.sh

echo "Installing UMC module..."
install -m664 frontend/asterisk/* "$UNI_UDM_PATH/handlers/asterisk/"
echo -e "\t\t\t\t\t\t\tdone."

echo "Restarting apache2..."
invoke-rc.d apache2 restart
echo -e "\t\t\t\t\t\t\tdone."

echo "Installation successful."
