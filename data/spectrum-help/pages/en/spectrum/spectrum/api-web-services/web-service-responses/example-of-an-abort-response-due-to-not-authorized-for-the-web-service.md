---
title: "Example of an Abort Response due to Not Authorized for the Web Service | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/web-service-responses/example-of-an-abort-response-due-to-not-authorized-for-the-web-service"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/web-service-responses/example-of-an-abort-response-due-to-not-authorized-for-the-web-service"
---

# Example of an Abort Response due to Not Authorized for the Web Service

 "Error_code" is A.

```
`<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<SOAP-ENV:Header/>
<SOAP-ENV:Body>
<nis:AddGLAccountResponse xmlns:nis="http://www.northgate-is.com/proiv/webservices/types">
<returnArray>
<returnData>
<response>
<error_code>A</error_code>
<desc>The Web Service is not authorized. Authorization ID is not setup in the system.</desc>
<column>Authorization_ID</column>
</response>
</returnData>
</returnArray>
</nis:AddGLAccountResponse>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>`
```
