RAND := $(shell awk 'BEGIN{srand();printf("%d", 65536*rand())}')

randomize:
	find user/src/bin -name "*.rs" | xargs sed -i 's/OK/OK$(RAND)/g'
	find check -name "*.py" | xargs sed -i 's/OK/OK$(RAND)/g'

test: randomize
	if [ $(CHAPTER) -ge 4 ]; \
	then cp overwrite/build-elf.rs ../os/build.rs; \
	else cp overwrite/build-bin.rs ../os/build.rs; \
	fi
	if [ $(CHAPTER) -le 2 ]; then \
		cp overwrite/Makefile-ch2 ../os/Makefile; \
	elif [ $(CHAPTER) -le 6 ]; then \
		cp overwrite/Makefile-ch3 ../os/Makefile; \
	else \
		cp overwrite/Makefile-ch7 ../os/Makefile; \
	fi
	if [ $(CHAPTER) -eq 7 ]; then \
		cp overwrite/easy-fs-fuse.rs ../easy-fs-fuse/src/main.rs; \
	fi
ifeq ($(CHAPTER), 3)
	make -C user all CHAPTER=3_0
	make -C ../os run | tee stdout-ch3_0
	python3 check/ch3_0.py < stdout-ch3_0

	make -C user all CHAPTER=3_1
	make -C ../os run | tee stdout-ch3_1
	python3 check/ch3_1.py < stdout-ch3_1

	make -C user all CHAPTER=3_2
	make -C ../os run | tee stdout-ch3_2
	python3 check/ch3_2.py < stdout-ch3_2
else
	make -C user all CHAPTER=$(CHAPTER)
	make -C ../os run | tee stdout-ch$(CHAPTER)
	python3 check/ch$(CHAPTER).py < stdout-ch$(CHAPTER)
endif

.PHONY: test randomize
