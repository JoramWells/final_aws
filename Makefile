build-dev:
	cd server && $(MAKE) build-dev

run-dev:
	docker-compose -f docker-compose.yaml up


### REMOTE

SSH_STRING:=ubuntu@172-31-25-216

ssh:
	ssh $(SSH_STRING)


# apt install make

copy-files:
	scp -r ./* $(SSH_STRING):/root/