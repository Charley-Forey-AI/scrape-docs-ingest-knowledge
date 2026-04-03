---
title: "Developer Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/developer-information"
fetched_at: "2026-04-03T20:47:07.463050+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/developer-information"
---

# Developer Information

Some of the web services available here are RESTful web services intended for systems analysts and programmers who are familiar with Web service programming standards, such as SOAP and WSDL. Web services and their standards are supported by a variety of development tools on a variety of platforms.
The Spectrum Data Exchange module consists of a set of WSDL's which can
 contain one or multiple web methods for sending information into the Spectrum Accounting
 System. The Endpoint for each WSDL is a unique URL (referenced by 'myserver.com'- change
 this to match your server's URL name) and Port for each Spectrum installation. The URL and
 Port for each installation is displayed within Spectrum on the Data Exchange Excel Download
 screen located in the System Administration > Utilities > Data Exchange Download menu.

- Endpoint: https://myserver.com:8482

- WSDL: https://myserver.com:8482/wsdls/AddJob.jws

Each web method requires the following to be passed:

- Authorization_ID – This is a mandatory value (up to 20 characters)
 created by a user within the Spectrum Data Exchange module. The Authorization ID
 grants access to the specific web service methods, the specific companies and must
 have an active status in order for the web services to work.

- GUID – This is a mandatory value (up to 36 characters) that is a
 unique reference number used as a session identifier. This unique reference number is
 auto-generated within the web service programming, or can be defined within the
 individual web service. Recommendation: Let the
 programming auto-generate the GUID.

- Each individual web service method requires the GUID to be defined however it
 can be unique for each record or be used repeatedly based on the web service
 method.Note: We recommend that if you are sending
 multiple records for a web service then use the same GUID for that group of
 records.

- When used repeatedly, it is assumed that the same web service method, Authorization_ID, and GUID combination is part of the same grouping of records.

- The GUID has expiration logic and will need to be replaced after a certain time of inactivity (by default within 24 hour period) especially if the same GUID is going to be used repeatedly.

- If the Web service method / Authorization_ID / GUID combination was used once and then was not used again within a 24 hour period the web service will send an expiration message – "Time out has occurred". At this point a new GUID will need to be used.

- The same GUID can be used with different Web service methods and the same Authorization ID but it cannot be used with the same web service method with a different Authorization ID.

- Elements – Each Web service method has a specific set of elements
 defining the data being sent to Spectrum. The data is in the XML format (that is, Raw
 data is being sent) using web requests. The ProIV programming requires the data to be
 sent in the following format: <element name> DATA<element name> Please
 refer to the individual web service layouts for the list of elements needed.
