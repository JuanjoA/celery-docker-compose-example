===============================
Celery + docker-compose example
===============================

This is a simple example, with only one task, and two test to launch the task and see Celery working.
You can use it as a template (flower is not protected).


Install
-------

``$ git clone --depth 1 https://github.com/JuanjoA/celery-docker-compose-example.git``

``$ cd celery-docker-compose-example``

``$ touch environment.secret``

Use
---

Launch:

    ``$ docker-compose up --build``

or to detached mode:

    ``$ docker-compose up --build -d``

With this, you need to launch other command to see logs:

    ``$ docker-compose logs -f``

Flower URL: http://localhost:5555      (If you use virtualbox or other machine, set the correct ip)


Tests
-----

Launch test1:

    ``./test1.sh``  or maybe  ``chmod +x test1.sh;./test1.sh``  or ``bash test1.sh``  or . . . :-)


Launch test2:

    ``./test2.sh``  or maybe  ``chmod +x test2.sh;./test2.sh``  or ``bash test2.sh``  or . . . :-)

    You can see now logs and flower changes.


Clean data
----------

Finally remove containers and volumes:

    ``$ docker-compose down -v``

    Or

    ``$ docker-compose rm -v``

And rm directory.