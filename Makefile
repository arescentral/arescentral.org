# Makefile for Sphinx documentation

# You can set these variables from the command line.
SPHINXBUILD     = sphinx-build
SPHINXOPTS      =
RSYNC           = rsync
RSYNCOPTS       = -rtvz --delay-updates --delete
BUILDDIR        = _build
PYTHON 			= python
DEPLOY          = florence.sfiera.net:/srv/www/arescentral.org/htdocs
STAGE           = florence.sfiera.net:/srv/www/staging.arescentral.org/htdocs

# Internal variables.
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(SPHINXOPTS) .

.PHONY: help clean html changes linkcheck stage deploy

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make HTML files"
	@echo "  changes    to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck  to check all external links for integrity"
	@echo "  serve      to serve the site at localhost:8000"
	@echo "  stage      to push to staging.arescentral.org"
	@echo "  deploy     to push to arescentral.org"

clean:
	-rm -rf $(BUILDDIR)/*

html:
	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/html
	cp -f htaccess $(BUILDDIR)/html/.htaccess
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

changes:
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $(BUILDDIR)/changes
	@echo
	@echo "The overview file is in $(BUILDDIR)/changes."

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

serve: html
	cd $(BUILDDIR)/html/ && $(PYTHON) -m SimpleHTTPServer 8000

stage: html
	$(RSYNC) $(RSYNCOPTS) $(BUILDDIR)/html/ $(STAGE)

deploy: html
	$(RSYNC) $(RSYNCOPTS) $(BUILDDIR)/html/ $(DEPLOY)
