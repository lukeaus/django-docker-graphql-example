#!/bin/sh

set -o errexit
set -o nounset
set -o xtrace

rm -f './celerybeat.pid'
celery -A django_graphql_example.taskapp beat -l INFO
