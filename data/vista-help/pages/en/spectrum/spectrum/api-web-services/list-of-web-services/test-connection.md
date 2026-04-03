---
title: "Test Connection | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/test-connection"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/test-connection"
---

# Test Connection

Use this version to test the Data Exchange connection.
WSDL: WSTestConnection.jws
Method: WSTestConnection
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Field Descriptions

Use the table below for reference when using this service.
Element Name
Description
Req
Type
Max
Format
Validation

Authorization_ID
Authorization ID to access the server
YES
Text
20
Data Exchange Installation Screen

Version
Version of programming
YES
Text
36
Enter whole numbers for each segment of version. Do not send multiple zero's in format. They will be stripped out. Format =3.3 and anything after that will be ignored. Examples to send =1.12 or 2.
Validates against current version defined in ProIV file
