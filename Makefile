build:
	docker build -t python-election-2020 .

run:
	docker run --rm -v $(PWD):/code python-election-2020
