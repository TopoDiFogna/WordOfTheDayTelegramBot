#!/usr/bin/env bash

set -e

if [[ "$TRAVIS_PULL_REQUEST" == "false" ]]; then
    TAG ="$(git describe --tags --exact-match)"
    docker push "$DOCKER_USERNAME"/wordofthedaytelegrambot:"$TAG";
fi;