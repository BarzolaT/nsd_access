.PHONY: install_coco

install_coco:
	mkdir -p vendor
	git clone https://github.com/cocodataset/cocoapi.git vendor/cocoapi
	rm -rf vendor/cocoapi/.git
	$(MAKE) -C vendor/cocoapi/PythonAPI/ install
