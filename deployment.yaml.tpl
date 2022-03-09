apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: SERVICE
spec:
  template:
    spec:
      containers:
      - image: gcr.io/my-john-project-7313/my-fast-api:latest
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