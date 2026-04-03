---
title: "Equipment Notes | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/equipment-control-services/equipment-notes"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/equipment-control-services/equipment-notes"
---

# Equipment Notes

Use this service to import Equipment Notes
 information.
 WSDL: EquipmentNotes.jws Method:
 EquipmentNotes
[Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)

## Underlying File Maintenance

Prior to importing Equipment Notes information, the following file maintenance areas must be completed:

- System Administration > Installation > Equipment Control

- System Administration > Installation > Equipment Control > Equipment Maintenance

- System Administration > Installation > Equipment Control > Equipment Note Topics Maintenance

## Assumptions and Dependencies

- If Company_Code is blank then use the Authorization ID default value.

- The Equipment_Code and Notes_Topic must exist in order to add the notes.

- The Equipment Notes web service has an option to append to the current Note Topic.

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
Company_CodeCompany CodeYESText3Valid Company in Spectrum. Defaults from the Authorization ID if not populated.
C
Equipment_CodeEquipment CodeYESText10Valid Equipment code and must exist for the defined Company Code.
D
Notes_TopicNotes TopicYESText20Equipment Note Topics Maintenance
E
Notes_TextNotesText1000
F
Append_NoteAppend Notes?Text1 (Y) to append. Blank = Replace all notes
