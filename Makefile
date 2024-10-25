build: 
	docker build -t app app 

up: ## Start the project
	docker-compose up --build

run: 
	docker run app 
	
