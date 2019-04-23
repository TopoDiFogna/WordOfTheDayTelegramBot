#!/usr/bin/env bash

set -e

if [[ "$TRAVIS_PULL_REQUEST" == "false" ]]; then
    if [[ -z "$TRAVIS_TAG" ]]; then
        docker push "$DOCKER_USERNAME"/wordofthedaytelegrambot:"$TRAVIS_TAG";
    fi;
fi;