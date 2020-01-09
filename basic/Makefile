

.PHONY: help
help:
	@echo "build - build the app"
	@echo "clean - remove build artifacts"
	@echo "veryclean - remove build artifacts and virtualenv"

env:
	virtualenv --python=python3.7 $@
	./$@/bin/pip install "transcrypt<3.8"


.PHONY: build
build: env
	./env/bin/transcrypt -b -m app.py

clean:
	rm -rf __target__

veryclean: clean
	rm -rf env

