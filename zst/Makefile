# zst: zeta spectral triples on FLINT/arb. Needs FLINT >= 3.0 (apt: libflint-dev), gmp, mpfr.
# Rules of the house (see README.md): red-green TDD (a failing test precedes every change), mutation
# testing (`make mutate`), fuzzing (`make fuzz`, `make fuzz-plain`), and every formula in src/ cites
# its ground-truth source (local copy under refs/src/ or the mpmath prototype) by file and line.
CC      ?= gcc
CFLAGS  ?= -O2 -std=c11 -Wall -Wextra -Wno-unused-parameter -Iinclude
LDLIBS  ?= -lflint -lmpfr -lgmp -lm
CLANG   ?= clang

SRC   := $(wildcard src/*.c)
OBJ   := $(SRC:src/%.c=build/%.o)
TESTS := $(patsubst tests/%.c,build/%,$(wildcard tests/*.c))

.PHONY: all check clean fuzz fuzz-plain mutate

all: build/libzst.a build/zst

build/%.o: src/%.c include/zst.h | build
	$(CC) $(CFLAGS) -c $< -o $@

build/libzst.a: $(OBJ)
	ar rcs $@ $^

build/zst: tools/zst.c build/libzst.a
	$(CC) $(CFLAGS) $< build/libzst.a $(LDLIBS) -o $@

build/test_%: tests/test_%.c build/libzst.a
	$(CC) $(CFLAGS) $< build/libzst.a $(LDLIBS) -o $@

build:
	mkdir -p build

check: $(TESTS)
	@for t in $(TESTS); do ./$$t || exit 1; done

# libFuzzer harnesses (clang with the compiler-rt fuzzer + asan runtime); FUZZ_TIME seconds each.
FUZZ_TIME ?= 30
fuzz: build/libzst.a
	$(CLANG) -O1 -g -fsanitize=fuzzer,address -Iinclude fuzz/fuzz_secular.c build/libzst.a $(LDLIBS) -o build/fuzz_secular
	$(CLANG) -O1 -g -fsanitize=fuzzer,address -Iinclude fuzz/fuzz_ab.c build/libzst.a $(LDLIBS) -o build/fuzz_ab
	mkdir -p build/corpus_secular build/corpus_ab
	ASAN_OPTIONS=detect_leaks=0 ./build/fuzz_secular -max_total_time=$(FUZZ_TIME) -max_len=64 build/corpus_secular
	ASAN_OPTIONS=detect_leaks=0 ./build/fuzz_ab -max_total_time=$(FUZZ_TIME) -max_len=8 build/corpus_ab

# the same harnesses driven by a seeded PRNG, no clang needed
fuzz-plain: build/libzst.a
	$(CC) $(CFLAGS) -DZST_PLAIN_FUZZ fuzz/fuzz_secular.c build/libzst.a $(LDLIBS) -o build/fuzz_secular_plain
	$(CC) $(CFLAGS) -DZST_PLAIN_FUZZ fuzz/fuzz_ab.c build/libzst.a $(LDLIBS) -o build/fuzz_ab_plain
	./build/fuzz_secular_plain 2000 1
	./build/fuzz_ab_plain 300 1

mutate:
	python3 tools/mutate.py --max $(or $(MUTANTS),40)

clean:
	rm -rf build

# RTP round 1, lane A1 driver (not part of the certified pipeline; reuses libzst unchanged)
build/rtp1_a1: tools/rtp1_a1.c build/libzst.a
	$(CC) $(CFLAGS) $< build/libzst.a $(LDLIBS) -o $@

# RTP round 2, lane D (standalone experiment; not part of all)
build/rtp2_dirichlet: tools/rtp2_dirichlet.c ../notes/rtp-round-2/dirichlet/checks/reference.c build/libzst.a
	$(CC) $(CFLAGS) $< build/libzst.a $(LDLIBS) -o $@

# RTP round 2, lane E (standalone weight-two experiment; not part of all)
build/rtp2_ellcurve: tools/rtp2_ellcurve.c ../notes/rtp-round-2/ellcurve/checks/spectra.c build/libzst.a
	$(CC) $(CFLAGS) $< build/libzst.a $(LDLIBS) -o $@

# RTP round 2, lane S (driver-only OpenMP; not part of all)
build/rtp2_scale: tools/rtp2_scale.c build/libzst.a
	$(CC) $(CFLAGS) -fopenmp $< build/libzst.a $(LDLIBS) -o $@
