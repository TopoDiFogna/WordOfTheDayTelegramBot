#!/usr/bin/env bash

set -e

if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
    docker push "$DOCKER_USERNAME"/wordofthedaytelegrambot;
fi;