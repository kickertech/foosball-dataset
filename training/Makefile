
DIR = $(shell pwd)
# this is used in obj.data
export EXPORTPATH=${DIR}/../export

build-image:
	docker build -t darknet .

prepare:
	python ${DIR}/split_train.py -data_dir $(EXPORTPATH)
	cp ${DIR}/../class_list.txt $(EXPORTPATH)/obj.names
	cp ${DIR}/obj.* $(EXPORTPATH)/

run-shell: build-image prepare
	docker run --gpus all -u $(shell id -u):$(shell id -g) \
		-v $(DIR)/../:/repo \
		-w /repo/ --rm -it \
		--entrypoint=/bin/bash \
		darknet

train-docker: build-image prepare
	docker run --gpus all -u $(shell id -u):$(shell id -g) \
		-v $(DIR)/../:/repo \
		-w /repo/ --rm -it \
		--entrypoint=/bin/bash \
		darknet \
		-c "make train"

train: prepare
	cd $(EXPORTPATH) && darknet detector train obj.data obj.cfg obj.weights -dont_show
