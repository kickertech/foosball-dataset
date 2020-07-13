include check.mk
TABLE=leonhart
KIND=black-green
DS=01

DATA_DIR=${PWD}/data
PICTURES_DIR=$(DATA_DIR)/$(TABLE)/$(KIND)/$(DS)/pictures
OUT_DIR=$(DATA_DIR)/$(TABLE)/$(KIND)/$(DS)/out
CLASS_LIST=${PWD}/class_list.txt
EXPORT_DIR=${PWD}/export

label:
	python \
		./OpenLabeling/main/main.py \
		-i $(PICTURES_DIR) \
		-o $(OUT_DIR) \
		-c $(CLASS_LIST)

split:
	@:$(call check_defined, INPUT, path to video file which should be split)
	@echo "writing frames from ($(INPUT)) to ($(PICTURES_DIR))"
	mkdir -p ${PWD}/$(TABLE)/$(KIND)/$(DS)/{pictures,out}
	python ${PWD}/tools/split.py \
		-input $(INPUT) \
		-output_dir $(PICTURES_DIR)

.PHONY: export
export:
	mkdir -p $(EXPORT_DIR)
	python ${PWD}/tools/export.py \
		-data_dir $(DATA_DIR) \
		-output_dir $(EXPORT_DIR)

train:
	@echo TODO. not implemented
