# Python on aws lambda with chalice

### DB: RDS MYSQL

### Crypto keys by KMS

# Requirement

### 本地需在 aws cli 有 IAM user 的 credential

### 本地需 pip3 install requirements.txt 裡面的 module 才能 local test

## deploy 至 aws lambda

```
chalice deploy
```

## 本地測試 Serving on http://127.0.0.1:8000

```
chalice local
```

### 本機資料庫連線

### 連結 RDS 需要到 aws 加本地 ip 到 RDS VPC inbound rule (TCP)

### 要加正式環境請參考下面連結

https://aws.github.io/chalice/topics/stages.html

設置好 prod.json & config 後, 多加 --stage {環境名稱} 即可.

```
chalice deploy --stage dev
chalice deploy --stage prod
```
