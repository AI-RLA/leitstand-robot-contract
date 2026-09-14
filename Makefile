BUF ?= buf
# Pin matches buf.lock; bump both together.
PROTOVALIDATE_REF = buf.build/bufbuild/protovalidate:50325440f8f24053b047484a6bf60b76

.PHONY: gen lint format format-check build breaking check sync

gen:
	$(BUF) generate
	$(BUF) generate $(PROTOVALIDATE_REF)

lint:
	$(BUF) lint

format:
	$(BUF) format -w

format-check:
	$(BUF) format -d --exit-code

build:
	$(BUF) build -o /dev/null

# Compares with the last tag. On 0.x a reported break is allowed when it is documented.
breaking:
	$(BUF) breaking --against '.git#tag=$(shell git describe --tags --abbrev=0)'

check: lint format-check build

# CI freshness guard: committed stubs must match the protos.
sync: gen
	git diff --exit-code gen/
