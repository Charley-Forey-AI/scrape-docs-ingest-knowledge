---
title: "Add Project Log Recipient | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/project-management-services/add-project-log-recipient"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/project-management-services/add-project-log-recipient"
---

# Add Project Log Recipient

Use this service to import Project Log Recipient
 information.
 WSDL: AddPJRecipient.jws Method:
 AddPJRecipient
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Project Log Recipient information, the following file maintenance screens must be completed:

- System Administration > Installation > Job Cost

- System Administration > Installation > Project Management > Project Log

- System Administration > Installation > Project Management > Category Maintenance

- System Administration > Installation > Job Cost > Job Contacts

- System Administration > Installation > Systems Administration > Contacts

## Assumptions and Dependencies

- The Project Log must exist in order to add the Project Log Recipients.

- The Project Log Recipients web service will create a new Recipient entry.

- If Company_Code field is blank then use the Authorization ID default value.

- To update the Project Log Recipients on a specific Project Log the TransactionId must be defined OR the Job_Number, Category and Reference_Num must be defined. Once it is a validated then the Project Log Recipients will be added.

- Contact_ID field

- The Contact_ID is an internally created Id number that does not appear on a screen in Spectrum but controls the Contact Name shown on the Project Log Recipients List.

- The following hierarchy logic will be used to define the correct Recipients based on the fields define in the Web Service. If the information is not valid then each component will be processed to find the correct Recipient. If the Recipient is not found then it will provided an error.

- If a Contact_ID is provided then it will be used to define the Recipient information.

- If the Contact_ID is blank then the Recipient_Email is required and will be used to define the Recipient information.

- If the Recipient_Email doesn't exist then the Last_Name and First_Name fields will be used to define the Recipient information.

- The first created Contact ID found in Spectrum with and ACTIVE status will be used to populate the Recipient information if the Recipient_Email or the combination of the Last_Name and First_Name fields is used.

- If duplicate records exist, then they will all be added as they are processed.

- Any field that is left blank will not be updated in Spectrum.

## Field Descriptions

Use the table below for reference when using this service.
The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.Excel
Element NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen
GUIDUnique reference number created by programmingText36** See GUID definition
B
Company_CodeCompany CodeText3Valid Company in Spectrum. Defaults from the Authorization ID if not populated.
C
Job_NumberJob NumberYESText10Valid Job
D
TransactionIdInternally created Project Log IDText36Not found in Spectrum. Leave blank if using Template.Valid Project Log ID. *See Assumptions and Dependencies in manual
E
CategoryCategoryText30*See Assumptions and Dependencies in manual
F
Reference_NumNumberText10If TransactionId is blank then Category and Reference_Num must be defined.*See Assumptions and Dependencies in manual
G
Recipient_TypeTypeText1T=To ; F=From ; C=Courtesy copy or B=Blind copy
H
Contact_IDInternally created Contact IDText10Not found in Spectrum. Leave blank if using Template.Valid Contact. *See Assumptions and Dependencies in manual.
I
Recipient_EmailRecipient EmailText80If Contact_ID not defined then Recipient_Email is required. Format = name@domain.com.*See Assumptions and Dependencies in manual
J
Last_NameRecipient Last NameText30If Recipient_Email is not defined then the Last_Name and First_Name are required.*See Assumptions and Dependencies in manual
K
First_NameRecipient First NameText20If Recipient_Email is not defined then the Last_Name and First_Name are required.*See Assumptions and Dependencies in manual
