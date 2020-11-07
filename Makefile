build:
	docker build -t python-election-2020 .

run:
	docker run --rm -v $(PWD):/code python-election-2020 && git add election_data_SG_GA.csv graph.png && git commit -m "Update $(shell date +"%F %T")" && git push

graph:
	docker run --rm -v $(PWD):/code python-election-2020 python graph.py
