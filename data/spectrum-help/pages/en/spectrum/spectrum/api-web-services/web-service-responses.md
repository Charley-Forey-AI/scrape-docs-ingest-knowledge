---
title: "Web Service Responses | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/web-service-responses"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/web-service-responses"
---

# Web Service Responses

There are several types of errors returned from each web
 service identified by the existence of the `error_code`, `desc`,
 and `column` elements in the response message.

- error_code – This element can
 contain the following values:

- A = Abort error. This is typically when security is
 not authorized for the Request.

- I = Invalid value in an element.

- M = Missing information and must be supplied.

- S = Successful. Used for test connection service
 only.

- G = Good response with information being sent back
 from the service in the "desc" for the associated "column" element.

- W = Warning. Used for the 'Get' services.

- desc – This is the description corresponding to the
 error_code for the element identified in the column.

- column – This contains the
 name of the element in error.

Spectrum uses SQL database and ProIV programming logic together. The
 ProIV logic requires that specific elements exist within the SOAP Envelope and SOAP
 Response. The following examples are shown using SOAP and display the requirements needed
 by Spectrum.
