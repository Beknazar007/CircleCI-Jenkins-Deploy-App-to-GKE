FROM amazonlinux

RUN yum -y update
RUN yum -y install httpd

COPY ./index.html   /var/www/html/index.html
COPY ./script.js   /var/www/html/script.js
COPY ./_config.yml   /var/www/html/_config.yml
COPY ./style.css   /var/www/html/style.css

CMD ["/usr/sbin/httpd","-D", "FOREGROUND"]
EXPOSE 80