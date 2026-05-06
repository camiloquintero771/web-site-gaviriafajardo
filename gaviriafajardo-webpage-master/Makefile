init:
	test -n "$(name)"
	rm -rf ./.git
	find ./ -type f -exec perl -pi -e 's/gaviriafajardo/$(name)/g' *.* {} \;
	mv ./gaviriafajardo ./$(name)

npm-install:
	docker exec -it gaviriafajardo npm install

webpack-dev:
	docker exec -it gaviriafajardo npm run dev

webpack-dev-server:
	docker exec -it gaviriafajardo npm run dev-server

webpack-build:
	docker exec -it gaviriafajardo npm run build
up:
	docker-compose up
superuser:
	docker exec -it gaviriafajardo ./manage.py createsuperuser

bash:
	docker exec -it gaviriafajardo bash

shell:
	docker exec -it gaviriafajardo ./manage.py shell

makemigrations:
	docker exec -it gaviriafajardo ./manage.py makemigrations $(extra)

migrate:
	docker exec -it gaviriafajardo ./manage.py migrate

fullmigrate:
	docker exec -it gaviriafajardo ./manage.py makemigrations $(extra)
	docker exec -it gaviriafajardo ./manage.py migrate

initialfixture:
	docker exec -it gaviriafajardo ./manage.py loaddata initial

testfixture:
	docker exec -it gaviriafajardo ./manage.py loaddata test

test:
	docker exec -it gaviriafajardo ./manage.py test

statics:
	docker exec -it gaviriafajardo ./manage.py collectstatic --noinput

makemessages:
	docker exec -it gaviriafajardo django-admin makemessages

compilemessages:
	docker exec -it gaviriafajardo django-admin compilemessages

startapp:
	docker exec -it gaviriafajardo ./manage.py startapp $(name)
	sudo chmod 777 -R ./$(name)
