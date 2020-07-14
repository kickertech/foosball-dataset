
DIR = $(shell pwd)
# this is used in obj.data
export EXPORTPATH=${DIR}/../export

build-image:
	docker build -t darknet .

run-shell: build-image prepare
	docker run --gpus all -u $(shell id -u):$(shell id -g) \
		-v $(EXPORTPATH):/data \
		-w /data/ --rm -it \
		--entrypoint=/bin/bash \
		darknet

prepare:
	python ${DIR}/split_train.py -data_dir $(EXPORTPATH)
	cp ${DIR}/../class_list.txt $(EXPORTPATH)/obj.names
	cp ${DIR}/obj.* $(EXPORTPATH)/

train-docker: build-image prepare
	docker run --gpus all -u $(shell id -u):$(shell id -g) \
		-v $(EXPORTPATH):/data \
		-w /data/ --rm -it \
		darknet detector train obj.data obj.cfg obj.weights

train: build-image prepare
	cd $(EXPORTPATH) && darknet detector train obj.data obj.cfg obj.weights
