# Webhooks

Subscribe an HTTPS endpoint and Larkspur will POST events to it.

Every delivery carries `X-Larkspur-Signature: t=<unix>,v1=<hmac>` where the MAC
is `HMAC-SHA256(SECRET_KEY, "<t>." + body)`. Verify it before trusting a
payload, and reject timestamps older than five minutes.

Deliveries are retried up to five times with exponential backoff.
