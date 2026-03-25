---
title: "Field Definitions: PM Daily Logs Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form/field-definitions-pm-daily-logs-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form/field-definitions-pm-daily-logs-form"
---

# Field Definitions: PM Daily Logs Form

The following is a list of field descriptions for the PM
 Daily Logs form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Project

 Enter the project for which you are setting up this daily log.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

## Log Date

 Enter the date of this daily project log. The corresponding day of the week displays to the right.
Shortcuts
T or t
Set the date to the current date.

MMDD
Four digit month and day
Enter a four digit month and date (MMDD) and the system will automatically add the current year.

+
The system will automatically set the date to tomorrow.

+5
The system will automatically set the date to 5 days in the future.
You can actually enter any value after the +, for
 example you can enter +7 to set the date to next week.

-
The system will automatically set the date to the previous day.

-5
The system will automatically set the date to 5 days in the past.
Just like with +, you can enter any value after the
 -, for example you can enter -7 to set the date to the
 previous week.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

## Daily Log

This field represents a specific log entry on
 the date entered in the Log Date field. For example, if this is
 the first entry of the day, enter a 1.
The value in this field can be up to five characters long and between -32,767 and 32,767.
Create a new daily log
The daily log number must be unique for each log date because it represents a specific entry on a specific log date.
There are a few ways to create a new daily log using this field:

- Click the New Record icon () and select a date in the
 Log
 Date field. The system will populate the Daily Log
 field with the next available number. TAB through the field to create a new daily
 log.

- Enter a '+' in this field and then press TAB to exit the field. The system will automatically create a new daily log and assign it the next available number.

- Enter a daily log number that doesn't already exist and then press TAB to exit the field. The system will automatically create a new daily log. You can also press F4 to see a list of daily log numbers that have already been created.
Select an existing daily log

Enter an existing daily log number or press F4 to select one from a list.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Description

 Enter a description of the daily log. The description can be up to 255 characters long.
The text entered here will print on the Daily Project Log report under the Log Date.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Document Type

 Use this field to categorize the daily log
 that you are creating. Press F4to select a document type from a
 list.
Document types are created and maintained
 using the [PM Document Types ](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form) form. Click [here](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form) for more information on document types.
Required when using 'Send with Transmittal'
If you select  >  Send with
 transmittal, a document type must be selected in this field.
Click [here](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) for an overview of the Create & Send feature.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Logs

## Weather

Enter the weather conditions for the day, up to 60 characters available (e.g. sunny, warm, rain, cloudy, etc.).
Note:If you have Internet access, clicking the Weather button will take you directly to the Google weather site.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Wind

 Enter the wind speed and direction (e.g. NNW, 10 mph), up to 30 characters.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Temperature: High

 Enter the high temperature for the day.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Temperature: Low

 Enter the low temperature for the day.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Include In Document

 For each option listed, check the box to include the corresponding information on the PM Daily Project Log report.

 Employees
 Conversations

 Crews
 Deliveries

 Subcontractors
 Accidents

 Equipment
 Visitors

 Activity

 Leave the box unchecked for information you want excluded from the Daily Project Log report.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Employees: Sequence

 Enter the sequence number (1-9999) or enter ‘+’ to auto-generate the next sequential number available.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Employees: Employee

 Specify the employee (from PM Firm Contacts or PR Employees) to which this daily log entry applies. Press F4 for a list of firm contacts or PR employees. You can also enter the first few characters of the sort name and the system will locate and display the first closest match.

- You can only enter an employee (from PR Employees) if in PM Company Parameters you have checked the PR in Use box and assigned a PR company.

- If you specify an employee that does not exist as an ‘our firm’ contact, that employee will be automatically added to PM Firm Contacts, with the Exclude from Lookups flag checked, once you save the record. (Note: The Exclude from Lookups flag is ignored when using the F4 lookup from this field; all ‘our firm’ contacts will display when using the ‘Firm Contacts’ lookup option, regardless of how you set the Exclude from Lookups flag. However, all other Firm Contact lookups in PM will exclude contacts with this flag checked.)

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Employees: Start Time

 Specify the time at which this employee began working on the project, in 24-hour format.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Employees: End Time

 Specify the time at which this employee stopped working for the day on this project, in 24-hour (for example, 17:00 for 5:00 p.m.). Typically, the end time comes after the start time; however, in cases where the end time falls on the next day, it will come before the start time. In this case, the system gives you a warning that the end time comes before the start time; however, the entry will be saved. When you print the PM Daily Project Log report, the times will accurately show the a.m./p.m. designation.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Employees: Phase

 Specify the phase (from PM Project Phases or
 PM Phases) on which this employee worked.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Employees: Worked

 Check this box if this employee worked today.
 Leave this box unchecked if this employee did not work today.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Employees: Location

 Specify the project location (from PM Project Locations) a which this employee worked.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Employees: Remarks

 Use this field to enter any remarks or notes about this employee. For additional space in which to write more detailed notes, double-click on this field. The Grid Notes window will display, allowing you virtually unlimited space for your notes and information. There is however, a maximum allowance of 8k.
Spelling Check
 Click the Spelling icon on the toolbar or select Tools >  Spelling  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Crews: Sequence

 Enter the sequence number (1-9999) or enter ‘+’ to auto-generate the next sequential number available.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Crews: Crew

 Enter the crew code (from PR Crews) for this daily log entry.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Crews: Start Time

 Indicate the time at which this crew began working on the project. Enter in 24-hour format.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Crews: End Time

 Specify the time at which this crew stopped working for the day on this project. Enter in 24-hour format (for example, 17:00 for 5:00 p.m.).
Typically, the end time comes after the start time; however, in cases where the end time falls on the next day, it will come before the start time. In this case, the system gives you a warning that the end time comes before the start time; however, the entry will be saved. When you print the PM Daily Project Log report, the times will accurately show the a.m./p.m. designation.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Crews: Supervisor

 Specify who the supervisor for this crew is, up to 30 characters.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Crews: Foremen

 Specify the number of foremen (0-255) in this crew.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Crews: Journeymen

 Specify the number of journeymen (0-255) in this crew.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Crews: Apprentices

 Specify the number of apprentices (0-255) in this crew.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Crews: Location

 Specify at which location of the project (PM Project Locations) this crew worked.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Crews: Remarks

 Use this field to enter any remarks or notes about this crew. For additional space in which to write more detailed notes, double-click on this field. The Grid Notes window will display, allowing you virtually unlimited space for your notes and information. There is however, a maximum allowance of 8k.
Spelling Check
 Click the Spelling icon on the toolbar or select Tools >  Spelling  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Subcontractors: Sequence

 Enter the sequence number (1-9999) or enter ‘+’ to auto-generate the next sequential number available.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

## Subcontractors: Firm

Enter the subcontractor or press F4 to select it
 from a list.
Tip:The sort name can be used instead of the firm number
 when selecting firms in PM module forms. Generally the sort name is the first several
 letters of the firm name.  For example when creating a subcontract in the [PM Subcontracts](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form) form for 'Bryan Electrical', you can
 enter the sort name 'bryan' in the Vendorfield instead of the firm number
 '10042'. The sort name of a firm is set up using the Sort Name
 field on the [PM Firms](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firms-form) form.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Subcontractors: Start Time

 Specify the time at which this subcontractor began working on the project, in 24-hour format.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Subcontractors: End Time

 Specify the time at which this subcontractor stopped working for the day on this project, in 24-hour format.
Typically, the end time comes after the start time; however, in cases where the end time falls on the next day, it will come before the start time. In this case, the system gives you a warning that the end time comes before the start time; however, the entry will be saved. When you print the PM Daily Project Log report, the times will accurately show the a.m./p.m. designation.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Subcontractors: Supervisor

 Specify the supervisor for this subcontractor, up to 30 characters.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Subcontractors: Foremen

 Specify the number of foremen (0-255) working for this subcontractor on this project.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Subcontractors: Journeymen

 Specify the number of journeymen (0-255) working for this subcontractor on this project.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Subcontractors: Apprentices

 Specify the number of apprentices (0-255) working for this subcontractor on this project.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Subcontractors: Location

 Specify at which location of the project (PM Project Locations) this subcontractor worked.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Subcontractors: Remarks

 Use this field to enter any remarks or notes
 about this subcontractor. For additional space in which to write more detailed notes,
 double-click on this field. The Grid Notes window will display, allowing you virtually
 unlimited space for your notes and information. There is however, a maximum allowance of
 8k.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools >  Spelling
  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Equipment: Sequence

 Enter the sequence number (1-9999) or enter ‘+’ to auto-generate the next sequential number available.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Equipment: EMCo

 Specify the EM company for the equipment to which this daily log entry applies.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Equipment: Equipment

 Specify the equipment to which this daily log
 entry applies. May be a valid piece of equipment from EM Equipment; otherwise any equipment
 code, up to 10 characters, may be entered.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Equipment: Description

 If you specified a valid piece of equipment
 from EM, this field will default the description defined for the equipment in EM Equipment.
 If you entered an non-valid piece of equipment (not set up in EM Equipment), enter the
 equipment description.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Equipment: Firm

 Specify the firm that owns or is renting this piece of equipment. If you do not know the firm number, enter the first few characters of the sort name and the system will locate and display the first closest match.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Equipment: Quantity

 Specify the quantity of this equipment being used at this location for this project.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Equipment: UM

 Specify the unit of measure that applies to this equipment.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Equipment: Location

 Specify at which location of the project (PM Project Locations) this equipment is being used.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Activity: Sequence

 Enter the sequence number (1-9999) or enter ‘+’ to auto-generate the next sequential number available.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Activity: Description

 Enter a description of the activity that occurred. For additional space in which to write more detailed notes, double-click on this field. The Grid Notes window will display, allowing you virtually unlimited space for your notes and information. There is however, a maximum allowance of 8k.
Spelling Check
 Click the Spelling icon on the toolbar or select Tools >  Spelling  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Activity: Location

 Specify at which location of the project (PM Project Locations) this activity occurred.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Conversations: Sequence

 Enter the sequence number (1-9999) or enter ‘+’ to auto-generate the next sequential number available.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Conversations: Firm

 Specify the firm involved in this conversation. If you do not know the firm number, enter the first few characters of the sort name and the system will locate and display the first closest match.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Conversations: Contact

 Specify the contact (from the specified firm) with whom the conversation took place.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Conversations: Description

 Enter a description of the conversation. For additional space in which to write more detailed notes, double-click on this field. The Grid Notes window will display, allowing you virtually unlimited space for your notes and information. There is however, a maximum allowance of 8k.
Spelling Check
 Click the Spelling icon on the toolbar or select Tools >  Spelling  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Deliveries: Sequence

 Enter the sequence number (1-9999) or enter ‘+’ to auto-generate the next sequential number available.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Deliveries: Firm

 Specify the firm from which the material being delivered was purchased. If you do not know the firm number, enter the first few characters of the sort name and the system will locate and display the first closest match.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

## Deliveries: PO #

Enter the purchase order number that applies to the delivery or press F4 to select a PO from a list.
If you select a PO that has not yet been set up in [PO Purchase Order Entry ](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form), you will need to create it now - the system does not automatically create a PO when you enter a new PO number. Press F5 while in this field to open PO Purchase Order Entry and create a new PO.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Deliveries: Material

 Enter the material (HQ Materials) that was delivered.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Deliveries: Time

 Specify the time that this material was delivered, in 24-hour format.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Deliveries: Location

 Specify the project location (PM Project Locations) to which the material was delivered.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Deliveries: Delivery Ticket

 Enter the delivery ticket number, if applicable, up to 10 characters.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Accidents: Sequence

 Enter the sequence number (1-9999) or enter ‘+’ to auto-generate the next sequential number available.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

## Accidents: Firm

Specify the firm (from PM Firms) involved in the accident. If you do not know the firm number, enter the first few characters of the sort name and the system will locate and display the first closest match.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Accidents: Employee

 Specify the employee (from the specified firm) who was involved in the accident. If you do not know the employee number, enter the first few characters of the sort name and the system will locate and display the first closest match.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

## Accidents: Description

Use this tab to enter any notes about this item. The space allowance is virtually unlimited.
Spelling Check
 Click the Spelling icon on the toolbar or select Tools >  Spelling  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Accidents: Time

 Enter the time that this accident occurred, in 24-hour format.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Accidents: Location

 Specify the project location (from PM Project Locations) where the accident occurred.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Visitors: Visitor

 Enter the name of the person visiting, up to 60 characters.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Visitors: Activity

 Use this tab to enter any miscellaneous notes about this item. The space allowance is virtually unlimited.
Spelling Check
 Click the Spelling icon on the toolbar or select Tools >  Spelling  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Visitors: Arrived

 Enter the arrival time of this visitor, in 24-hour format.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Visitors: Departed

 Enter the departure time of this visitor, in 24-hour format.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

##  Visitors: Location

 Specify which project location (defined in PM Project Locations) this person visited.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log

## Sent To Firm

Enter the firm that should receive the
 document(s) generated using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature or press F4 to select a
 firm from a list.
Click [here](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) for an overview of the Create and Send feature.
Drag and Drop
 To drag and drop firms/contacts to the distribution grid, double-click the Distribution tab (label) or select View  >  Project Firms List. This displays the Project Firm Contacts list. You can then select a firm/contact and drag it to the grid.
Note:If you manually add a firm/contact to the grid that
 is not set up for the project, upon saving the record, the system displays a message
 indicating the firm/contact does not exist in PM Firms and gives you the option to add
 the firm/contact. Select Yes to add the firm/contact to the
 distribution list and to PM Firms. Select No to add the firm/contact to the
 distribution grid only.
Distribution defaults

When creating a new record, the Distribution
 tab will automatically populate with any PM firm contact set up as a distribution default.
For example, if a contact at an architecture firm should receive a copy of all drawing logs of document type 'ARCH', you can use the distribution default feature to set up that contact as a default for 'ARCH' documents. When drawing logs of that type are created, that contact will automatically populate on the Distribution tab.
Click [here](/en/vista/vista/project-management/create-and-send/pm-assign-distribution-defaults-form) for more information on distribution defaults.
Using the sort name
Tip:The sort name can be used instead of the firm number
 when selecting firms in PM module forms. Generally the sort name is the first several
 letters of the firm name.  For example when creating a subcontract in the [PM Subcontracts](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form) form for 'Bryan Electrical', you can
 enter the sort name 'bryan' in the Vendorfield instead of the firm number
 '10042'. The sort name of a firm is set up using the Sort Name
 field on the [PM Firms](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firms-form) form.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview

## Sent To Contact

Enter the contact that should receive the
 document(s) generated using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature, or press F4to select one
 from a list. Only contacts associated with the firm selected in the Sent To Firm
 field can be selected.
Contacts are associated with firms using [PM Firm Contacts ](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firm-contacts-form).
Distribution defaults
When creating a new record, the Distribution
 tab will automatically populate with any PM firm contact set up as a distribution default.
For example, if a contact at an architecture firm should receive a copy of all drawing logs of document type 'ARCH', you can use the distribution default feature to set up that contact as a default for 'ARCH' documents. When drawing logs of that type are created, that contact will automatically populate on the Distribution tab.
Click [here](/en/vista/vista/project-management/create-and-send/pm-assign-distribution-defaults-form) for more information on distribution defaults.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview

## Send

Check this box if the contact should receive communications generated using the [Create and Send ](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature.
When this box is not checked, the contact can
 be manually added to a Create and Send email but they will not automatically populate in
 the To,
 Cc,
 or Bcc
 fields on the Message tab of the PM Send Documents form.
Click [here](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) for an overview of the Create and Send feature.
If a communication has already been sent
If this contact was added to an email generated using the Create and Send feature, this box will be checked.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview

## Preferred Method

Use this field to select which type of communication should be sent to the contact when using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature. This field defaults based on the preferred method set up using [PM Firm Contacts](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firm-contacts-form).

- M -Print — Print a hard copy of the generated PDF document(s). When this option is selected, the contact will not receive a copy of the email body text.

- E -Email — Send the generated PDF document(s) using email. The email address of the contact is pulled from the Email field on the Info tab of the PM Firm Contacts form. F -Fax — Send the generated PDF document(s) suing fax. The system will use the fax number set up on the PM Firm Contacts form.
Note:This option requires that you have a fax server set up in the Fax Server Name field on the Info tab of [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form).

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview

## Send Type

Select how the contact should be added to the communication generated from the Create and Send feature: To, Cc, Bcc.
When a communication is created using the Create and Send feature (), the contact will automatically be added using the selection in this field.
Click [here](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) for an overview of the Create and Send feature.
If a communication has already been sent
If an email generated using the Create and Send feature has already been sent to the contact, this field will display how the contact was included on the last communication.
For example if the contact was added to an
 email in the Tofield on the PM Send Documents form, To will display in this field. When a new
 email is created using the Create and Send form, the contact will automatically populate in
 the Tofield.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview

## Date Sent

This field displays the date a communication was sent to the contact using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature.
If several communications have been sent, the most recent date will display.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview

## Notes

Enter any notes that relate to this contact. You can double click in the field if you need more space to enter information.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.
Spelling Check
 Click the Spelling icon on the toolbar or select Tools >  Spelling  to spell check the text in this field.

[](/en/vista/vista/project-management/logs-lists-and-meeting-minutes/logs-and-lists/pm-daily-logs-form)PM Daily Log
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
