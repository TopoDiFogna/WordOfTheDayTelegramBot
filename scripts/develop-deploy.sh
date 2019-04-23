#!/usr/bin/env bash

set -e

if [[ "$TRAVIS_PULL_REQUEST" == "false" ]]; then
    echo "Well not a PR so i can try to push";
    docker push "$DOCKER_USERNAME"/wordofthedaytelegrambot;
fi;