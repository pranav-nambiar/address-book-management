# Address Book Management

I've explored implementing APIs with and without Django REST Framework(DRF). Uses MySQL as backend.

Building APIs manually without DRF is tedious since one has to manually serialize the model object to pythonic data type, and vice versa.

## Steps common to both projects:

1. Set up a virtual environment.
    ```
    python3 -m venv env
    ```
2. Activate the virtual environment.
    ```
    source env/bin/activate
    ```
3. Install dependencies.
    ```
    cd WithRestFramework
    ```
    OR
    ```
    cd WithoutRestFramework
    ```
    then,
    ```
    pip install -r requirements.txt
    ```
4. Ensure MySQL is installed and running. [If not, here's how.](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)
5. Enter MySQL shell and create a database and user. Grant the user all privileges on the database.
    ```
    $ mysql -u root -p
    ```
    ```
    mysql> CREATE DATABASE addressbook;
    mysql> CREATE USER 'djangouser'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
    mysql> GRANT ALL ON addressbook.* TO 'djangouser'@'localhost';
    mysql> FLUSH PRIVILEGES;
    ```
6. Create an OPTIONS file so that Django can access this created database.
    ```
    gedit ~/.my.cnf
    ```
   - Copy the following into the editor, make changes where required.
        ```
        [client]
        database = addressbook
        user = djangouser
        password = your_actual_password
        default-character-set = utf8
        ```
7. Edit settings.py file in the root project directory, and set 'read_default_file' to the OPTIONS file you created.
    ```
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS':  {
            'read_default_file': '~/.my.cnf',
        }
      }
   }
   ````
8. Migrate and run server.
    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```
