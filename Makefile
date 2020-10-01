.PHONY: book

book:
	jupyter-book build iris_book/

myst:
	bookflow create myst iris_book/$(NAME)

config:
	bookflow create config project_config.yaml