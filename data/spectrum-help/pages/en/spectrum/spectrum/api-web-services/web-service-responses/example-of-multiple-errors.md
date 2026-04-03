---
title: "Example of Multiple Errors | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/web-service-responses/example-of-multiple-errors"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/web-service-responses/example-of-multiple-errors"
---

# Example of Multiple Errors

```
`<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<SOAP-ENV:Header/>
<SOAP-ENV:Body>
<nis:AddGLAccountResponse xmlns:nis="http://www.northgate-is.com/proiv/webservices/types">
<returnArray>
<returnData>
<response>
<error_code>I</error_code>
<desc>Account_Type_Code is invalid, value does not match specified field mask</desc>
<column>Account_Type_Code</column>
</response>
<response>
<error_code>I</error_code>
<desc>Status is invalid, value does not match specified field mask</desc>
<column>Status</column>
</response>
</returnData>
</returnArray>
</nis:AddGLAccountResponse>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>`
```
