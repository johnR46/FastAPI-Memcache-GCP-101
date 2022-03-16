apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    run: my-fast-api
  name: my-fast-api
  namespace: fast-backend
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
              value: cache-memcached-service
            - name: MEMCACHE_PORT
              value: '11211'
            - name: DB_URL
              value: postgres://postgres-service:5432/postgres
            - name: DB_PASS
              valueFrom:
                secretKeyRef:
                  name: postgres-secret
                  key: POSTGRES_PASSWORD

---

apiVersion: v1
kind: Service
metadata:
  name: my-fast-api-service
  namespace: fast-backend
spec:
  selector:
     run: my-fast-api
  ports:
  - protocol: TCP
    port: 8090
    targetPort: 8080
  type: LoadBalancer