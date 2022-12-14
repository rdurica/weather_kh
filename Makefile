#!/bin/bash
repository = weather-kh
tag = 0.6.2
platform = linux/amd64,linux/arm64

build:
	poetry export --without-hashes --output requirements.txt
	docker build -t $(repository) .

publish:
	poetry export --without-hashes --output requirements.txt
	docker buildx build --platform $(platform) --push -t rdurica/$(repository):$(tag) .