#!/bin/bash

if [[ -d "migrations" ]]
then
	until flask db upgrade
	do
		echo "Waiting for Database connection..."
		sleep 2
	done
	echo "flask db upgrade executed"
fi

flask run --host 0.0.0.0 --port 5000

