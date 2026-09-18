# ihz: the CCM construction for the Ihara zeta of a regular graph, on FLINT/arb (>= 3.0).
CC      ?= gcc
CFLAGS  ?= -O2 -std=c11 -Wall -Wextra -Wno-unused-parameter -Iinclude
LDLIBS  ?= -lflint -lmpfr -lgmp -lm

SRC   := $(wildcard src/*.c)
OBJ   := $(SRC:src/%.c=build/%.o)
TESTS := $(patsubst tests/%.c,build/%,$(wildcard tests/*.c))

.PHONY: all check clean

all: build/libihz.a build/ihz

build/%.o: src/%.c include/ihz.h | build
	$(CC) $(CFLAGS) -c $< -o $@

build/libihz.a: $(OBJ)
	ar rcs $@ $^

build/ihz: tools/ihz.c build/libihz.a
	$(CC) $(CFLAGS) $< build/libihz.a $(LDLIBS) -o $@

build/test_%: tests/test_%.c build/libihz.a
	$(CC) $(CFLAGS) $< build/libihz.a $(LDLIBS) -o $@

build:
	mkdir -p build

check: $(TESTS)
	@for t in $(TESTS); do ./$$t || exit 1; done

clean:
	rm -rf build
