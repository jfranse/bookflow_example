.PHONY: book

# some custom shortcuts
# the myst and config recipes utilize the bookflow utilities CLI

book:
	jupyter-book build iris_book/

myst:
	bookflow create myst iris_book/$(NAME)

config:
	bookflow create config project_config.yaml