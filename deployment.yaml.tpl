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
              value: x-memcached
            - name: MEMCACHE_PORT
              value: 11211
            - name: DB_URL
              value: postgres:5432/postgres
            - name: DB_USER
              value: postgres
            - name: DB_PASS
              valueFrom:
                secretKeyRef:
                  name: my-db-secret
                  key: postgres-password

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