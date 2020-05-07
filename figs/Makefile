SUBDIRS = svg matplotlib tikz

.PHONY: clean subdirs $(SUBDIRS)

subdirs: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@

clean:
	$(MAKE) clean -C $(SUBDIRS)
