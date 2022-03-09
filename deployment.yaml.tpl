apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    run: my-fast-api
  name: my-fast-api
  namespace: fastapi-memcache-dev
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
      - image: gcr.io/my-john-project-7313/my-fast-api:latest
        name: my-fast-api
        ports:
        - containerPort: 8080
        env:
        - name: MEMCACHE_SERVER
        valueFrom:
          configMapKeyRef:
            name: memcache-config
        key: mem_ip
        - name: MEMCACHE_PORT
        valueFrom:
          configMapKeyRef:
            name: memcache-config
        key: mem_port

---

kind: Service
apiVersion: v1
metadata:
  name: my-fast-api
  namespace: fastapi-memcache-dev
spec:
  selector:
     run: my-fast-api
  ports:
  - protocol: TCP
    port: 8090
    targetPort: 8080
  type: LoadBalancer