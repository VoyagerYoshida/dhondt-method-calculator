PWD := $(shell pwd)
NETWORK_NAME:=selenium_network
REMOTE_CONTAINER_NAME:=remote.selenium
HOST_IMAGE_NAME:=voyagerwy130/selenium
HOST_CONTAINER_NAME:=host.selenium
HOST_WORKING_DIR:=/workspace/


.PHONY: setup/network
setup/network:
	@docker network create $(NETWORK_NAME)


.PHONY: remote/up
remote/up:
	@docker run -d \
		-p 4444:4444 \
		-v /dev/shm:/dev/shm \
		--net $(NETWORK_NAME) \
		--name $(REMOTE_CONTAINER_NAME) \
		selenium/standalone-chrome

.PHONY: remote/down
remote/down:
	@docker stop $(REMOTE_CONTAINER_NAME)


.PHONY: host/build 
host/build:
	@docker build . -t $(HOST_IMAGE_NAME)

.PHONY: host/run
host/run:
	@docker run --rm -it \
		-p 2222:8888 \
		-v $(PWD)/workspace/:$(HOST_WORKING_DIR) \
        --net $(NETWORK_NAME) \
		--name $(HOST_CONTAINER_NAME) \
		$(HOST_IMAGE_NAME) /bin/bash
