#!/usr/bin/env bash

set -e

if [[ "$TRAVIS_PULL_REQUEST" == "false" ]]; then
    echo "Well not a PR so i can try to push";
    if [[ -n "$TRAVIS_TAG" ]]; then
        echo "Found tag: $TRAVIS_TAG pushing to docker hub a tagged image";
        docker push "$DOCKER_USERNAME"/wordofthedaytelegrambot:"$TRAVIS_TAG";
    else
        echo "Commit not tagged, will not push the image to docker hub";
    fi;
fi;