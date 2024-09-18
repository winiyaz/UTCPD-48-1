# Selenium Cloud 

Running selenium in cloud testing

# Steps to run in cloud 

1. Make a `Dockerfile`
2. make a `docker-compose.yml`
3. then check it if is running `docker-compose ps`
4. Then execute your command 'docker-compose exec selenium python /workspace/p1w.py' - outside of the container  
   - This will work if you se the path correctly inside the `docker-compose.yml` file
   - ```docker
         volumes:
      - .:/workspace
     ```
    - Thisis he poitn where the workspace is defined
  4. Observe the config file in this folder 

# Starting up the container 

```docker 
docker-compose up -d 
```
- starts it in detached mode , so you can execute the python script below

# Executing the python script 

1. Ensure tht it is in this folder 

```docker 
docker-compose exec selenium python /workspace/p1w.py
```