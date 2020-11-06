build:
	docker build -t python-election-2020 .

run:
	docker run --rm -it -v $(PWD):/code python-election-2020
