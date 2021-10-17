imagename=lineapy
build:
	docker-compose build \
	${args} \
	${imagename}

test:
	docker-compose run --rm ${imagename} pytest

lint:
	docker run --rm -v "${PWD}":/apps alpine/flake8:latest --verbose .

blackfix:
	docker run --rm -v "${PWD}":/data cytopia/black .