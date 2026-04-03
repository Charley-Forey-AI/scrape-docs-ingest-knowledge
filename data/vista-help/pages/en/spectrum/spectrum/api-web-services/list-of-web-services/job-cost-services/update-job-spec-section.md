---
title: "Update Job Spec Section | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/update-job-spec-section"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/job-cost-services/update-job-spec-section"
---

# Update Job Spec Section

Use this service to update existing Project Management Job
 Spec Section information for the defined fields only.
 WSDL: UpdateJobSpecSection.jws
 Method: UpdateJobSpecSection
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Job Spec Section information, the following file maintenance screens must be completed:

- System Administration > Installation > Project Management

- System Administration > Installation > Project Management > Job Spec Sections

## Assumptions and Dependencies

- The Project Management module must be set up.

- The Job must exist in the defined Company code.

- The Job Spec Section Web Service updates existing Project Management Job Spec Section information for the defined fields only.

- The Spec_Section must exist in order to change the Description information.

- Any field that is left blank will not be updated in Spectrum. The service does not delete values that exist in Spectrum; it only changes data defined in the layout.

## Field Descriptions

Use the table below for reference when using this service.
The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.Excel
Element NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen
GUIDUnique reference number created by programmingText36** See GUID definition
B
Company_CodeCompany CodeText3Valid Company in Spectrum. Defaults from the Authorization ID if not populated.
C
Job_NumberJob NumberYESText10
D
Spec_SectionSectionText30
E
Spec_Section_DescSection DescriptionText50

NOTE = Invalid data will be ignored based on the layout requirements.
