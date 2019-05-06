FROM tensorflow/tensorflow:latest-py3

RUN apt-get update && \
    apt-get upgrade -y && \ 	
    apt-get install -y \
	git \
	python3 \
	python3-dev \
	python3-setuptools \
	python3-pip \
	nginx \
	supervisor \
	sqlite3 && \
	pip3 install -U pip setuptools && \
   rm -rf /var/lib/apt/lists/*

RUN pip3 install uwsgi && pip3 install django

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY nginx-app.conf /etc/nginx/sites-available/default
COPY supervisor-app.conf /etc/supervisor/conf.d/



COPY . /home/docker/code/

# install django, normally you would remove this step because your project would already
# be installed in the code/app/ directory
# RUN django-admin.py startproject website /home/docker/code/app/

EXPOSE 8000
#CMD ["supervisord", "-n"]