

# deploy 至 aws lambda
chalice deploy
# 本機測試 Serving on http://127.0.0.1:8000
chalice local


# 本機資料庫連線
# 連結RDS需要到 aws 加本地 ip 到 RDS VPC inbound rule (TCP) 

### stripe user 範本
{
  "data": [
    {
      "address": null,
      "balance": 0,
      "created": 1631775324,
      "currency": null,
      "default_source": null,
      "delinquent": false,
      "description": "My First Test Customer (created for API docs)",
      "discount": null,
      "email": "henry@gmail.com",
      "id": "cus_KEhvN9Rn024wCH",
      "invoice_prefix": "558A43AE",
      "invoice_settings": {
        "custom_fields": null,
        "default_payment_method": null,
        "footer": null
      },
      "livemode": false,
      "metadata": {},
      "name": null,
      "next_invoice_sequence": 1,
      "object": "customer",
      "phone": null,
      "preferred_locales": [],
      "shipping": null,
      "tax_exempt": "none"
    }
  ],
  "has_more": true,
  "object": "list",
  "url": "/v1/customers"
}
###