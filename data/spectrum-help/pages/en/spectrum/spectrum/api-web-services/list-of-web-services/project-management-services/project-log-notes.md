---
title: "Project Log Notes | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/project-management-services/project-log-notes"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/project-management-services/project-log-notes"
---

# Project Log Notes

Use this service to import Project Log Notes
 information.
 WSDL: ProjectLogNotes.jws Method:
 ProjectLogNotes
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Assumptions and Dependencies

- If Company_Code and Category field names are blank then use the Authorization ID default value. Both fields are required in order to process the web service.

- The Project Log entry must exist in order to add the notes.

- Either the TransactionId or the Reference_Num field must be defined to add the notes to the Project Log entry.

- If the TransactionId is defined and valid then it will update the pre-existing record with the defined notes.

- If the Reference_Num is defined along with the Company_Code, Job_Number, and Category and the unique combination of those fields is valid then it will update the pre-existing record with the defined notes.

- The following hierarchy will be used if the TransactionId, Category and Reference_Num are all populated in this order:

- TransactionId

- Category and Reference_Num

- The Project Log Notes Web Service has an option to append to the current Note Topic. If not defined then the Notes will be replaced. The formatting options available within the Notes on the Project Log are not supported.

- The Notes_Text can hold up to 1000 characters total in the table therefore if appending the notes and the value of the current notes plus the web service notes exceeds the limit, the web service notes will be truncated.

- If duplicate records exist to be updated, then they will all be updated as they are processed.

## Field Descriptions

Use the table below for reference when using this service.
The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.Excel
Element NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen
GUIDUnique reference number created by programmingText36** See GUID definition
B
Company_CodeCompany CodeYESText3 Can default from Authorization IdValid Company in Spectrum. Defaults from the Authorization ID if not populated.
C
Job_NumberJob codeYESText10Valid Job in Spectrum
D
TransactionIdProject Log IDText36TransactionId is created within Spectrum when the project log is added. If defined then the record will be added.Validates to the Project Log entry.
E
CategoryCategoryText30Validates to the Project Management Category Maintenance
F
Reference_NumReference numberText10Reference_Num is created within Spectrum when the project log is added. ** If defined and the Company_Code, Job_Number and Category is unique the record will be updated.Validates to the Project Log entry.
G
Notes_TopicProject Note TopicText20Validates to the Project Note Topics Maintenance
H
Notes_TextNotesText1000
I
Append_NoteAppend Notes?Text1(Y) to append. Blank = Replace all notes

NOTE = Invalid data will be ignored based on the layout requirements.
