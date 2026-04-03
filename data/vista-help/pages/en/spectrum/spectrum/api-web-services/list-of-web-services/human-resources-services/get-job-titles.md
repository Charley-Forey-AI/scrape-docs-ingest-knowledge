---
title: "Get Job Titles | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/human-resources-services/get-job-titles"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/human-resources-services/get-job-titles"
---

# Get Job Titles

Use this service to import Job Titles information.
WSDL: GetJobTitles.jws
Method: GetJobTitles

## Parameter Fields

Use the table below for reference when using this service.
Element Name
Description
Req?
Type
Max
Field Information

Authorization_ID
Authorization ID to access the server
YES
Text
20
Data Exchange Installation Screen

GUID
Unique reference number created by programming
Text
36
** See GUID definition

pCompany_Code
Company Code
YES
Text
3
Valid Company in Spectrum. Defaults from Authorization ID if not populated.

## Return Fields

Use the table below for reference when using this service.
Element Name
Description
Type
Max
Field Information

Company_Code
Company Code
Text
3
Valid Spectrum company

Job_Title
Job Title
Text
50
Job Title File Maintenance
