---
title: "Equipment Work Order Notes | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/preventive-maintenance-services/equipment-work-order-notes"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/preventive-maintenance-services/equipment-work-order-notes"
---

# Equipment Work Order Notes

Use this service to import Preventive Maintenance Equipment
 Work Order Notes information.
 WSDL: EquipWONotes.jws Method: EquipWONotes
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Preventive Maintenance Equipment Work Order Notes information, the following file maintenance areas must be completed:

- System Administration > Installation > Preventive Maintenance

- System Administration > Installation > Equipment Control

- System Administration > Installation > Preventive Maintenance > Equipment Work Order Maintenance

- System Administration > Installation > Preventive Maintenance > Work Order Note Topics Maintenance

- System Administration > Installation > Equipment Control > Equipment Maintenance

## Assumptions and Dependencies

- If Company_Code is blank then use the Authorization ID default value.

- The Site_ID, Contract_Number and Notes_Topic must exist in order to add the notes.

- Notes can be added to any Service Contract regardless of the status.

- The Service Contract Notes web service has an option to append to the current Note Topic.

- If not defined then the Notes will be replaced.

- The formatting options available within the Notes are not supported.

- The Notes_Text can hold up to 1000 characters total in the table therefore if appending the notes and the value of the current notes plus the web service notes exceeds the limit, the web service notes will be truncated.

- If duplicate records exist to be updated, then they will all be updated as they are processed.

## Field Descriptions

Use the table below for reference when using this service.
The Authorization_ID and GUID elements are not shown on the Spectrum Excel Office Add-in templates for data entry points.Excel
Element NameDescriptionReqTypeMaxFormatValidation
Authorization_IDAuthorization ID to access the serverYESText20Data Exchange Installation Screen
GUIDUnique reference number created by programmingText36** See GUID definition
B
Company_CodeCompany CodeText3Valid Company in Spectrum. Defaults from the Authorization ID if not populated.
C
Maintenance_WO_NumberEquipment Work order numberYESText10Valid Equipment Work Order
D
Notes_TopicNotes TopicYESText20Equipment Work Order Note Topics Maintenance
E
Notes_TextNotesText1000
F
Append_NoteAppend Notes?Text1(Y) to append. Blank = Replace all notes
