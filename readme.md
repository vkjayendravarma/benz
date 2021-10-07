# Mercedes Benz TechGig API

Based on flask

## Requrements 
docker 

## Steps to run the application

1. sudo docker build -t evpitstops .
2. sudo docker run -p 5000:5000 -it evpitstops

Here you will fet a local ip address. please open that ip address in browser to check if the api is accessable and working successfully.

Use postman to get results

url: http://<IP Address>:5000/getrouteplan
method: post 
content-type: application/json
body: { "vin": <vin>, "source": <source>, "destination": <destination> }