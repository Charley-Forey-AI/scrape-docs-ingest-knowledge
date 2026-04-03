---
title: "Example of Response Identifying an Invalid field | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/web-service-responses/example-of-response-identifying-an-invalid-field"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/web-service-responses/example-of-response-identifying-an-invalid-field"
---

# Example of Response Identifying an Invalid field

 "Error_code" is I.

```
`<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<SOAP-ENV:Header/>
<SOAP-ENV:Body>
<nis:AddGLAccountResponse xmlns:nis="http://www.northgate-is.com/proiv/webservices/types">
<returnArray>
<returnData>
<response>
<error_code>I</error_code>
<desc>GL Account does not match GL Mask</desc>
<column>GL_Account</column>
</response>
</returnData>
</returnArray>
</nis:AddGLAccountResponse>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>`
```
