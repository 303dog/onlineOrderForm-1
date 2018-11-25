#!/usr/bin/env bash
docker run -t -i -h OrderFormular --restart=always --name OrderFormular -d -p 443:443 -v /DockerRepository/OrderForm/orderForm:/orderForm orderform
#docker run -t -i -h OrderFormular --restart=always --name OrderFormular -d -p 9002:8000 -v /home/felixeisenmenger/OrderForm/orderForm:/orderForm orderform
#docker run -t -i -h OrderFormular --restart=always --name OrderFormular -d -p 9002:8000 -v /DockerRepository/OrderForm/orderForm:/orderForm orderform