# Provision an EKS Cluster
Follow instructiosn found here to provision the EKS cluster: 
https://learn.hashicorp.com/tutorials/terraform/eks

**Stop after finishing "Configure kubectl" step. The rest of the instructions are for setting up a dashboard with metrics.**


# Create Dockerfile for the "flask-app" web application
In the 'app' directory, build local image:

` > docker build -t [dockerHub username]/flask-app:1.0 . `

Next, push this image to DockerHub:

` > docker push [dockerHub username]/flask-app:1.0 `

# Launch kubernetes deployment 

In the "k8s" directory, open "flask-app.yaml" and on line 17 change

` 17.          image: mperkhounkov/flask-app:1.0 `

to your username and save the file

` 17.          image: [dockerhub username]/flask-app:1.0 `

Next, run

` > kubectl apply -f flask-app.yaml `

# Verify functionality

First, check that deployment is up and running & gather IP information 

` > kubectl get pod -o wide `

For example:

```
NAME                         READY   STATUS    RESTARTS   AGE   IP           NODE                                       NOMINATED NODE   READINESS GATES

flask-app-5f567bf4c6-d4tcw   1/1     Running   0          8s    10.0.3.74    ip-10-0-3-29.us-east-2.compute.internal    <none>           <none>

flask-app-5f567bf4c6-k6qcf   1/1     Running   0          8s    10.0.2.251   ip-10-0-2-129.us-east-2.compute.internal   <none>           <none>

flask-app-5f567bf4c6-wzcfx   1/1     Running   0          8s    10.0.3.54    ip-10-0-3-29.us-east-2.compute.internal    <none>           <none>

flask-app-5f567bf4c6-zzpkq   1/1     Running   0          8s    10.0.1.46    ip-10-0-1-65.us-east-2.compute.internal    <none>           <none>
```


Next, pick any Pod and use kubectl to get a shell session

` > kubectl exec -it flask-app-b4cf5d4d9-cnck5 -- /bin/bash `

From here use curl to verify connectivity with other servers in the cluster & 
that the Flask app is serving correct info. 

` # curl 10.0.2.251:5000 `

Example output:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Oracle Voodoo Magic App</title>
</head>
<body>
    <h1>Your operating system is Linux #1 SMP Thu Apr 14 20:53:13 UTC 2022</h1>
    <div>
        <p1>The time is 2022-05-08 21:12:23.106735</p1>
    </div>
    <div>
        <p1> Your IP address is 10.0.2.251 </p1>
    </div>

</body>

```

# Limitations

Ran out of time to complete the following
1. Develop a test framework. Should be done in conjuction with building the app but not well enough versed to accomplish within the time constraints
2. No loadbalancer configured in Kubernetes
3. Disable external networking in Terraform. (ie. further customize the tutorial example)



