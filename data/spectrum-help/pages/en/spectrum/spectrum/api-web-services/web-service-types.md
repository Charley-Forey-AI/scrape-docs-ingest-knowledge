---
title: "Web Service Types | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/web-service-types"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/web-service-types"
---

# Web Service Types

A Web Service is a method of communication between electronic devices over the web. This communication can be used to add data to, update data in, or retrieve data from the database.
The Data Exchange Web Services provide the following types of services:

- A 'Put' Web Service provides the user the ability to add or update information within Spectrum.

- A 'Get' Web Service provide the user the ability to define a specific set of parameters which then returns the defined data for the user to use.

The Authorization ID associated with a 'Get' Web Service requires a Spectrum operator to provide access based on the operator's job based security and cost center logic. The Parameter fields are the available selection criteria used to collect the data. The Return fields are the results provided back from the web service.
Each 'Get web service contains three fields at the end of each return layout that is used to provide information regarding any errors that may occur. The fields are defined as:

- Error_Code – displays the web service sync status code. The same codes are used with the Spectrum Office Add-in in the Sync_Status column.

- Error_Description – displays the associated description that applies to the error that is occurring.

- Error_Column – displays the parameter field name that is causing the error.

An example would be as follows:

- Error_Code = E

- Error_Description = The web service is not Authorized

- Error_Column = Authorization_ID
