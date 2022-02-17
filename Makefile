ENVFILE:=.env
include $(ENVFILE)


.PHONY: setup/network
setup/network:
	@docker network create $(NETWORK_NAME)


.PHONY: remote/up
remote/up:
	@docker run --rm -d \
		-p $(REMOTE_PORT):$(REMOTE_PORT) \
		-v /dev/shm:/dev/shm \
		--net $(NETWORK_NAME) \
		--name $(REMOTE_CONTAINER_NAME) \
		$(REMOTE_IMAGE_NAME)

.PHONY: remote/down
remote/down:
	@docker stop $(REMOTE_CONTAINER_NAME)


.PHONY: host/build 
host/build:
	@docker build . -t $(HOST_IMAGE_NAME)

.PHONY: host/run
host/run:
	@docker run --rm -it \
		-v $(shell pwd)/workspace:/workspace \
		--net $(NETWORK_NAME) \
		--env-file $(ENVFILE) \
		--name $(HOST_CONTAINER_NAME) \
		$(HOST_IMAGE_NAME) /bin/bash
