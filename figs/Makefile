SUBDIRS = svg

.PHONY: clean subdirs $(SUBDIRS)

subdirs: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@

clean:
	$(MAKE) clean -C $(SUBDIRS)
