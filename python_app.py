apiVersion: apps/v1
kind: Deployment
metadata:
  namespace: default
  name: user-service-app-deployment
  labels:
    app: user-service-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: user-service-app
  template:
    metadata:
      labels:
        app: user-service-app
    spec:
      #restartPolicy: Never
      containers:
        - name: user-service-container
          image: 221694501242.dkr.ecr.us-east-1.amazonaws.com/employee:v1
          imagePullPolicy: Always
          # command: ["/bin/sh"]
          # args: ["-c", "while true; do echo hello; sleep 10;done"]
          ports:
            - containerPort: 5000
        #   env:
        #     - name: DB_HOST
        #       value: "mysql-service"
        #     - name: DB_USER
        #       value: "root"
        #     - name: DB_PASS
        #       value: "password"
---
apiVersion: v1
kind: Service
metadata:
  name: user-service-app-nodeport-service
  labels:
    app: user-service-app
  annotations:
    alb.ingress.kubernetes.io/healthcheck-path: /app1/health
spec:
  type: NodePort
  selector:
    app: user-service-app
  ports:
    - port: 80
      targetPort: 5000
