# Send SQL query as CSV by mail

This simple docker image runs a Query against a MySQL server and send its output
as CSV by email.

To accomplish this, some variables must be set.

## Configuration variables:

Every configuration is done via environment variables. There are variables to:

* Personalize the report send by email
* Configure MySQL server connection
* Configure SMTP server connection

### Report configuration

* **`REPORT_NAME`:** name of attachment send by email. If not defined, defaults to **report**.
* **`MAIL_SUBJECT`:** subject of email. Defaults to _Mail query_.
* **`MAIL_BODY`:** body of email. Defaults to _Results are attached, have a nice day!_.

## MySQL variables

Mysql variables are self explanatory:

* **`DB_HOST`**
* **`DB_USER`**
* **`DB_PASSWORD`**
* **`DB_NAME`**
* **`QUERY`:** this variable is an SQL query. For example: `select * from
  products`.

## SMTP variables

This variables are also self explanatory:

* **`MAIL_FROM`**
* **`MAIL_TO`**
* **`SMTP_HOST`**
* **`SMTP_USERNAME`**
* **`SMTP_PASSWORD`**
* **`SMTP_PORT:`** defaults to 25

> SMTP username and password can be ignored and they will not be used.

> SMTP tls/ssl connections are not implemented. It's not complicated to add
> those configurations, but in our environment is not needed because of a relay
> server.


# Example

```bash
docker run --rm \
  -e DB_HOST=127.0.0.1 \
  -e DB_USER=root \
  -e DB_PASSWORD=root \
  -e DB_NAME=dbname \
  -e QUERY="select * from products" \
  -e MAIL_FROM=user@example.com \
  -e MAIL_TO=other@example.com \
  -e SMTP_HOST=smtp.example.com  \
  --network host \
  mikroways/sql2csv-by-mail
```

