FROM python:latest
#FROM nginx:latest

USER root

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python python-pip

#COPY /orderForm /orderForm
ADD /orderForm/ssl/vectronic-wildlife.com_ssl_certificate_06_18.cer /usr/share/ca-certificates/vectronic-wildlife.com_ssl_certificate.cer
ADD /orderForm/ssl/_.vectronic-wildlife.com_private_key_06_18.key /usr/share/ca-certificates/_.vectronic-wildlife.com_private_key.key
ADD /orderForm/ssl/-.vectronic-wildlife.com_ssl_certificate_INTERMEDIATE_06_18.cer /usr/share/ca-certificates/-.vectronic-wildlife.com_ssl_certificate_INTERMEDIATE.cer
COPY /orderForm/requirements.txt /orderForm/requirements.txt


RUN pip3 install -r /orderForm/requirements.txt
RUN pip3 install gunicorn
#RUN chmod +x /orderForm/unicorn.sh

CMD ["orderForm/unicorn.sh"]

#CMD ["python", "/orderForm/manage.py", "runserver", "0.0.0.0:8000"]

#CMD ["gunicorn", "--threads 3", "-w 3", "-b 0.0.0.0:8000", "orderForm.wsgi:application"]

