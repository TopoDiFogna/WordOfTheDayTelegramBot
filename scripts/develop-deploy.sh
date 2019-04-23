#!/usr/bin/env bash

set -e

echo "Pushing a nightly version from develop branch"
docker push "$DOCKER_USERNAME"/wordofthedaytelegrambot
