# Python on aws lambda with chalice 
### DB: RDS MYSQL
### Crypto keys by KMS

### 本地需 pip3 install requirements.txt 裡面的 module 才能 local test

### deploy 至 aws lambda

chalice deploy

### 本地測試 Serving on http://127.0.0.1:8000

chalice local

### 本機資料庫連線

### 連結 RDS 需要到 aws 加本地 ip 到 RDS VPC inbound rule (TCP)