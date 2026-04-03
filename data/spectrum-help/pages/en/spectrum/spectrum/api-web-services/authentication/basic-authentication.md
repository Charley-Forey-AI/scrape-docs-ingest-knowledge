---
title: "Basic Authentication | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/authentication/basic-authentication"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/authentication/basic-authentication"
---

# Basic Authentication

The Basic Authentication method is used for REST services.
Username: Company_Code

Password: Authorization_Id

Note: Basic Authentication is not required on SOAP/XML services.

Example:
```
`curl --request POST \
--url {url_to_endpoint} \
--header 'Authorization: Basic Q29tcGFueV9Db2RlOkF1dGhvcml6YXRpb25fSWQ=' \
--header 'Content-Type: application/json' \
--data '{payload}'`
```
