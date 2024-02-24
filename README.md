# My Portfolio

## This is the code that I use for my portfolio website

Decided to make if public git... well why not :) 

## Develop

1. Clone the repo
2. Run postgresdb for dev/test using docker compose
   ```shell
   $ docker compose up
   ```
3. Run migration if you run for first time:
    ```shell
    $ pyhton manage.py migrate
    ```
4. Create superuser:
    ```shell
    $ python manage.py createsuperuser
    ```
5. Start server
    ```shell
    $ python manage.py runserver
    ```
6. Enjoy :)


## Run tests

``` shell
pytest
```
