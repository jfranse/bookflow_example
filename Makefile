.PHONY: book

book:
	jupyter-book build lorem_book/

myst:
	bookflow create myst lorem_book/$(NAME)

config:
	bookflow create config project_config.yaml