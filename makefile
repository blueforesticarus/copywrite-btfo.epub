BOOK=books/cuentas_y_leyendas
BUILD=$(abspath ./build)
test:
	mkdir -p $(BUILD)
	rm -f $(BUILD)/test.epub
	cd $(BOOK); zip -X0   $(BUILD)/test.epub mimetype
	cd $(BOOK); zip -9 -r $(BUILD)/test.epub *

validate: test
	epubcheck build/test.epub
