# My Portfolio web

## This is the code that I use for my portfolio website

Decided to make if public git... well why not :) 

## Develop

1. Clone the repo
2. Run postgresdb for dev/test using run_dev.sh
    ```shell
    $ bash run_dev.sh
    ```
    This will start docker postgres container for dev DB
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