apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    run: my-fast-api
  name: my-fast-api
spec:
  replicas: 2
  selector:
    matchLabels:
      run: my-fast-api
  template:
    metadata:
      labels:
        run: my-fast-api
    spec:
      containers:
      - image: gcr.io/article-ci-cd/my-fast-api:latest 
        name: my-fast-api
        ports:
        - containerPort: 8080

---

kind: Service
apiVersion: v1
metadata:
  name: my-fast-api
spec:
  selector:
     run: my-fast-api
  ports:
  - protocol: TCP
    port: 8090
    targetPort: 8080
  type: LoadBalancer