---
title: "Spectrum Data Exchange (SDX) | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/spectrum-data-exchange-sdx"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/tools/spectrum-data-exchange-sdx"
---

# Spectrum Data Exchange (SDX)

Spectrum Data Exchange (SDX) provides a quick, easy, and
 secure way to transfer data in and out of Spectrum without requiring duplicate data entry.
 SDX provides templates, tools, and a Microsoft Office Add-in to help you import data
 directly from Microsoft Excel.
There are several data exchange tools:
Batch File Uploads
One type of data exchange available in the SDX is a batch file upload that imports into Spectrum. The upload reads a file, validates the data, and processes it as if you had manually entered the data. If the data is correct, it is ready for you to process. If the data is incorrect then it is stored in an error correction screen where you can make the necessary corrections.

- [Vendor Invoice Import](https://trimble.deploy.heretto.com/v4/deployments/mVyHSMAo9PbkfqcxUBWF/object/9ad0ae20-8ea8-11ec-9179-02420ae60f1a?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2pvcnNlay5jb20vZXpkX29yZ2FuaXphdGlvbiI6InZpZXdwb2ludCIsImh0dHBzOi8vam9yc2VrLmNvbS9lemQvb2JqZWN0X3V1aWQiOiI5YWQwYWUyMC04ZWE4LTExZWMtOTE3OS0wMjQyMGFlNjBmMWEiLCJleHAiOjE3NzUzMjUyNTEsImp0aSI6IjViYjFjYjE1NTgxMTQ1MWI4N2JmYTUwMjcxYmY3ZDRlIiwiaHR0cHM6Ly9qb3JzZWsuY29tL2V6ZF9maWxlc2V0IjoiOE1GRmpJZEw3ZEZLQmJiVGwxTXMifQ.xJl-9YpkeHFuyBcOPE4k4EGwe7adXZNuGfln-WUDJ8Q&response-content-disposition=filename%3D%22Vendor_Invoice_Import_Manual_v1422.pdf%22) – automates the process of creating unposted or unapproved (based on settings) AP invoice transactions.

- [PO Receiving Import](https://trimble.deploy.heretto.com/v4/deployments/mVyHSMAo9PbkfqcxUBWF/object/9b4a9910-8ea8-11ec-9179-02420ae60f1a?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2pvcnNlay5jb20vZXpkX29yZ2FuaXphdGlvbiI6InZpZXdwb2ludCIsImh0dHBzOi8vam9yc2VrLmNvbS9lemQvb2JqZWN0X3V1aWQiOiI5YjRhOTkxMC04ZWE4LTExZWMtOTE3OS0wMjQyMGFlNjBmMWEiLCJleHAiOjE3NzUzMjUyNTEsImp0aSI6ImEzMDkwYWIzMDM4YTRhMjU5MzQ2OWJjMzhmNGM3YTRhIiwiaHR0cHM6Ly9qb3JzZWsuY29tL2V6ZF9maWxlc2V0IjoiOE1GRmpJZEw3ZEZLQmJiVGwxTXMifQ.weXmHsbkUu3i1I9BjP2W2IK3vlxS-50hSNwR9x36aRs&response-content-disposition=filename%3D%22PO_Receiving_Import_v1422.pdf%22) - automates the process of receiving PO line items and creating the AP invoices with PO using one step PO receiving.

Web Services (WSDL)
Web Services are another type of data exchange method available in the SDX module. A Web Service is a method of communication between electronic devices over the web that syncs data instead of importing it. Validation occurs during the sync, and any errors encountered display in red. The Data Exchange uses a SOAP-formatted XML envelope and their associated WSDL descriptions to send data via a secure path to connect with the Spectrum database.

- For the list of web services, see [List of Web Services](/en/spectrum/spectrum/api-web-services/list-of-web-services).

- Before you can use Web Services, you must create an [Authorization ID](https://trimble.deploy.heretto.com/v4/deployments/mVyHSMAo9PbkfqcxUBWF/object/9bd043d0-8ea8-11ec-9179-02420ae60f1a?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2pvcnNlay5jb20vZXpkX29yZ2FuaXphdGlvbiI6InZpZXdwb2ludCIsImh0dHBzOi8vam9yc2VrLmNvbS9lemQvb2JqZWN0X3V1aWQiOiI5YmQwNDNkMC04ZWE4LTExZWMtOTE3OS0wMjQyMGFlNjBmMWEiLCJleHAiOjE3NzUzMjUyNTEsImp0aSI6ImU2MzIyNTFmMzI5OTQwZjBhZDlmODM5NDczZWFmZjJjIiwiaHR0cHM6Ly9qb3JzZWsuY29tL2V6ZF9maWxlc2V0IjoiOE1GRmpJZEw3ZEZLQmJiVGwxTXMifQ.pbaoD_eowcEo3htmW6gCSC9HY0AZIytgZMjbZsdRDmc&response-content-disposition=filename%3D%22SDX-AUTHORIZATION-SETUP-2021R2.pdf%22) and establish security settings. The secure Authorization ID is created in the Data Exchange Installation screen and provides access to the individual Web services to send data to or from Spectrum. The Authorization ID can be set up for specific companies and Web services. The Data Exchange Installation screen provides access to the available report options.

- [The Office Add-in](https://trimble.deploy.heretto.com/v4/deployments/mVyHSMAo9PbkfqcxUBWF/object/9c1ae160-8ea8-11ec-9179-02420ae60f1a?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2pvcnNlay5jb20vZXpkX29yZ2FuaXphdGlvbiI6InZpZXdwb2ludCIsImh0dHBzOi8vam9yc2VrLmNvbS9lemQvb2JqZWN0X3V1aWQiOiI5YzFhZTE2MC04ZWE4LTExZWMtOTE3OS0wMjQyMGFlNjBmMWEiLCJleHAiOjE3NzUzMjUyNTEsImp0aSI6IjQ3ZmVjNTliZTJlZTQ1MWViZmY0ODY5YTU3OGU0MWU4IiwiaHR0cHM6Ly9qb3JzZWsuY29tL2V6ZF9maWxlc2V0IjoiOE1GRmpJZEw3ZEZLQmJiVGwxTXMifQ.veO5T-WcvzwlFnW8K_JcGug_Ad8QS0bFNny9HW1Zolw&response-content-disposition=filename%3D%22SDX-SPECTRUM-OFFICE-ADDIN-2021R2.pdf%22) uses a variety of Excel templates to bring data into Spectrum.

- Types:

- Put services – provides the ability to add or update information within Spectrum.

- Get services – provides the ability to request specific information from Spectrum.

Developer note regarding Cipher Suites
Data Exchange supports only TLS 1.2 (and newer) with the following Cipher Suites.
TLS_AES_256_GCM_SHA384
TLS_CHACHA20_POLY1305_SHA256
TLS_AES_128_GCM_SHA256
TLS_DHE_RSA_WITH_AES_256_GCM_SHA384
TLS_DHE_RSA_WITH_AES_128_GCM_SHA256
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
TLS_DHE_RSA_WITH_AES_256_CBC_SHA256
TLS_DHE_RSA_WITH_AES_128_CBC_SHA25
TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384
TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
Developer note regarding Java
RESTful services in Data Exchange require updating to Java 11.
Time Entry Workbook
The [Time Entry Workbook](https://trimble.deploy.heretto.com/v4/deployments/mVyHSMAo9PbkfqcxUBWF/object/9c7b77f0-8ea8-11ec-9179-02420ae60f1a?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2pvcnNlay5jb20vZXpkX29yZ2FuaXphdGlvbiI6InZpZXdwb2ludCIsImh0dHBzOi8vam9yc2VrLmNvbS9lemQvb2JqZWN0X3V1aWQiOiI5YzdiNzdmMC04ZWE4LTExZWMtOTE3OS0wMjQyMGFlNjBmMWEiLCJleHAiOjE3NzUzMjUyNTEsImp0aSI6ImY5NTIyYmQ5OTA2NDQwMzBhOGNkYWYyYjM0NjEyNzhlIiwiaHR0cHM6Ly9qb3JzZWsuY29tL2V6ZF9maWxlc2V0IjoiOE1GRmpJZEw3ZEZLQmJiVGwxTXMifQ.uaEgI3mpHZ1LoChRfH4t5c11eQcNPpkwq9AL1PsVXk0&response-content-disposition=filename%3D%22SDX-TIME_ENTRY_WORKBOOK.pdf%22) allows the user to record Payroll time using Microsoft Excel and Spectrum Data Exchange Web Services to send information between the spreadsheet and Spectrum. The Time Entry Workbook is a protected Excel Macro-Enabled workbook that provides lookup functionality on the Time Entry tab of the workbook.

- Direct job and equipment time entry is supported.

- You do not have to be connected to Internet to enter payroll time.

- Provides ability to show only the information needed (based on setup).
