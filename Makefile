VENV?=.venv
PY?=$(VENV)/bin/python
CGP?=$(VENV)/bin/ssot-cgp
COURSE=ssot-input/course.json
OUT=dist

.PHONY: venv install validate build clean

venv:
	python -m venv $(VENV)

install: venv
	$(VENV)/bin/pip install -e "./ssot[dev]"

validate:
	$(CGP) validate $(COURSE)

build:
	$(CGP) build $(COURSE) --out $(OUT)

clean:
	rm -rf $(OUT)
