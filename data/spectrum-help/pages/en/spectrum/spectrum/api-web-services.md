---
title: "API Web Services | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services"
---

# API Web Services

The Data Exchange Web Services provides
 a secure, quick, and easy way to transfer data into your Spectrum application.
These three components streamline time-consuming data entry processes via a
 secure web connection:

- Web Services

- Authorization ID with optional settings

- Spectrum Office Add-in tool

## Web Services

A Web Service is a method of communication between electronic devices over the web. Within Spectrum we have created a group of [Web Services](/en/spectrum/spectrum/api-web-services/list-of-web-services), and each one has predefined layouts with specific requirements and validation rules for the field names. The Web Services can be accessed using our Spectrum Office Add-In tool, which links data via Microsoft® Excel®, or by connecting with a third-party website.
The structure and functionality for each Web Services (API) is unique for each service and is subject to change. The functionality of the Web Services will not exactly match the existing entry points within Spectrum. See the individual Web Service documentation under Web Service's Layouts for more information.

## Authorization ID

The secure Authorization ID is created in the Data Exchange Installation screen and provides access to the individual Web Services to send data to Spectrum. The Authorization ID can be set up for specific companies and Web Services. You can define specific options such as default options for field names, mapping user-defined fields, or creating counter overrides.
To learn more about Authorization ID, refer to the [Authorization Setup manual](https://trimble.deploy.heretto.com/v4/deployments/mVyHSMAo9PbkfqcxUBWF/object/9bd043d0-8ea8-11ec-9179-02420ae60f1a?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2pvcnNlay5jb20vZXpkX29yZ2FuaXphdGlvbiI6InZpZXdwb2ludCIsImh0dHBzOi8vam9yc2VrLmNvbS9lemQvb2JqZWN0X3V1aWQiOiI5YmQwNDNkMC04ZWE4LTExZWMtOTE3OS0wMjQyMGFlNjBmMWEiLCJleHAiOjE3NzUzMjUxODYsImp0aSI6ImRiNWQ2ZWU5NWI4MjRmMDJiYzE2OWUyZjg5ODE2MGJhIiwiaHR0cHM6Ly9qb3JzZWsuY29tL2V6ZF9maWxlc2V0IjoiOE1GRmpJZEw3ZEZLQmJiVGwxTXMifQ.H3piQRxcVGRis1fv6_Mabd4XIsDswQVaFI6de5OzRvU&response-content-disposition=filename%3D%22SDX-AUTHORIZATION-SETUP-2021R2.pdf%22) for information on
 setting up and using an Authorization ID.

## Office Add-in

The Spectrum Office Add-in allows you to use Excel to create the necessary files to import into Spectrum via our Web Services within the Data Exchange module. The Spectrum Office Add-in needs to be updated (for example, downloaded and installed) after each new release of Spectrum is installed. Each Web Service has its own template that can be used to bring data into Spectrum. Each Web Service is defined below with specific requirements and validation rules for field names.
To learn more about the Office Add-in tool, refer to the [Spectrum Office Add-in manual](https://trimble.deploy.heretto.com/v4/deployments/mVyHSMAo9PbkfqcxUBWF/object/9c1ae160-8ea8-11ec-9179-02420ae60f1a?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2pvcnNlay5jb20vZXpkX29yZ2FuaXphdGlvbiI6InZpZXdwb2ludCIsImh0dHBzOi8vam9yc2VrLmNvbS9lemQvb2JqZWN0X3V1aWQiOiI5YzFhZTE2MC04ZWE4LTExZWMtOTE3OS0wMjQyMGFlNjBmMWEiLCJleHAiOjE3NzUzMjUxODYsImp0aSI6ImQ0OTY3OTUyY2VhNTQ2Mjc5NTQyNjRlNDFlOGIzOTI4IiwiaHR0cHM6Ly9qb3JzZWsuY29tL2V6ZF9maWxlc2V0IjoiOE1GRmpJZEw3ZEZLQmJiVGwxTXMifQ.Trdiccm7o1UELHak8ZyT4kq0d3vaUm5Sq9NlazETjXU&response-content-disposition=filename%3D%22SDX-SPECTRUM-OFFICE-ADDIN-2021R2.pdf%22) for information on
 installation, usage and sync status codes.
The Data Exchange Web Services has a predefined operator (for example, *WS) that is defined during installation. The Operator ID displays anywhere an Operator ID is needed when a Web Service is used to import data into Spectrum.
The Data Exchange Web Service contains a validation hierarchy. Each Web Service follows the same logic and provides error reporting at each level. The logic is as follows:

- Authorization and required fields.

- Numeric, date, and generic validation (such as lengths, field type, field mask, defaults, and user-defined fields mapping).

- Validation that applies to the specific Web Service.
