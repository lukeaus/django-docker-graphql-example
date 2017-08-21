#!/bin/sh

set -o errexit
set -o nounset
set -o xtrace

celery -A django_graphql_example.taskapp worker -l INFO
