---
title: "Field Definitions: PM Submittals-65 Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-the-pm-submittals---6.5-form/field-definitions-pm-submittals-65-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-the-pm-submittals---6.5-form/field-definitions-pm-submittals-65-form"
---

# Field Definitions: PM Submittals-65 Form

The following is a list of field descriptions for the PM
 Submittals-65 form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Project

 Specify the project for which you are setting up this submittal.

## Submittal Type

Enter a document type or press F4 to select
 one from a list.
Submittal types are created and maintained
 using the [PM Document Types ](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form) form. Only document types associated
 with Submittals -
 6.5 selected in the Document Category field can be
 selected.

## Submittal

Create a new submittal
When creating a new submittal, you are
 creating a new submittal number for the type selected in the Submittal Type
 field.
There are several ways to create a new submittal using this field:

- Enter a '+' and press TAB. The system will create the submittal and
 assign it the next available number.

- Click the New Record icon () at the top
 of the form. Once you select a submittal type the system will populate this field with
 the next available number. Press TAB to move through this field and create the new
 submittal.

- Enter a number that has not already been used for the selected
 submittal type. The submittal number can be up to 10 characters long.

- The system will ignore alphanumeric numbers when determining the
 next number to assign.

- The system chooses the number in a slightly different way than
 other documents (RFIs, drawing logs, etc.). Numbers will be generated based on the
 Auto-Generate
 Submittal Numbers using option designated in PM Projects (Project or
 Project/Type). If the option is set to Project, the system will generate the next
 sequential number based on all submittals for the project. If the option is set to
 Project and Type, the system will generate the next sequential number based on all
 submittals having the same document type (e.g. all submittals for the project with a
 document type of ‘SPECS’). Select an
 existing submittal

Enter an existing submittal number or press F4 to select on from a list.

##  Revision

 Enter the revision number for this submittal (0-255).
 If a previous revision exists for this submittal, all header and item information (except tracking dates) will default from the previous revision.

## Description

Enter a description of the submittal. The description can be up to 60 characters long.

##  Phase

 Specify the phase (from PM Submittal Phase, PM
 Project Phases, or JC Phases) to which this submittal applies.
Note: Allows entry of phases that exist for the project
 (in PM Project Phases), but do not exist in JC Phases (e.g. phase is deleted from JC
 Phases after it has already been assigned to the submittal). Phase must meet ‘valid part
 of phase’ requirements.

## Status

Enter the status of this submittal or press F4 to select it from a list.
This field defaults to the status set up using
 the Default
 Beginning Status field on the Info tab of the [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form) form, or from the previous revision
 if one exists.

##  Sequence

 Optional.
 Enter a sequence (1-999999) for this submittal. You can use this number to identify the order in which you sent this submittal for approval or the order in which you logged the submittal. For example, your submittal number might indicate that it was the fifth one created, but assigning a sequence of ‘1’ indicates it was the first one you sent for approval.

##  Spec #

 Enter the specification number for this submittal, if applicable, up to 20 characters.
 If there is a previous revision, this field will default the value from the previous revision. Default may be overridden.

## Resp Person

Enter the person responsible for this submittal. Must be a valid contact defined for the 'Project Our Firm' in PM Projects or, if no ‘our firm’ specified for the project, the ‘Our Firm’ specified in PM Company Parameters.
If there is a previous revision, this field will default the value from the previous revision; otherwise, defaults as null.

##  Sub/Supplier Firm

 Enter the subcontractor/supplier firm who is submitting this item.
 If there is a previous revision, this field will default the value from the previous revision; otherwise, defaults as null.

##  Sub/Supplier Contact

 Enter the subcontractor/supplier contact for this submittal.
 If there is a previous revision, this field will default the value from the previous revision; otherwise, defaults as null.

## Architect/Engineer Firm

Enter the architect/engineer firm to whom this submittal will be sent.
If there is a previous revision, this field
 will default the value from the previous revision. If there is no previous revision
 (revision number is 0 or a new submittal), this field will the value defined for F3, or if
 none, will default the architect/engineer specified for the project (PM Projects). Defaults
 may be overridden.

## Architect/Engineer Contact

Enter the architect/engineer contact for this submittal.
If there is a previous revision, this field will default the value from the previous revision; otherwise, defaults as null.

## Date Due From

Specify the date this submittal is due from the subcontractor/supplier.

## Copies Required

Specify the number of copies (0-255) of the submittal required from the subcontractor/supplier.

## Date Received

Specify the date you received the submittal back from the subcontractor/supplier.

## Copies Received

Indicate the number of copies (0-255) of the submittal received from the subcontractor/supplier.

## Date Sent To

Specify the date this submittal was sent to the architect/engineer.

## Copies Sent

Indicate the number of copies (0-255) of this submittal sent to the architect/engineer.

## Date Due Back

Specify the date this submittal is due back from the architect/engineer. Initially defaults a due date based on the Date Sent To and the Default Standard Days Due specified in PM Projects.
Note: Changing the Date Sent To will automatically recalculate this date, even if you overrode the original default date.

## Date Received Back

Specify the date you received the submittal back from the architect/engineer.

## Copies Received Back

Indicate the number of copies (0-255) of the submittal received back from the architect/engineer.

## Date Ret'd To (Date Returned To)

Specify the date this submittal was returned to the subcontractor/supplier.

## Copies Ret'd (Copies Returned)

Indicate the number of copies (0-255) of the submittal sent back to the subcontractor/supplier.

## Activity Date

Enter the date that the activity on the submittal is scheduled to begin.
You can also enter an activity date on submittal items using the Submittal Items tab.

##  Submittal Items: Item

 Enter the submittal item number (1-32,767) or enter ‘N’, ‘New’, or ‘+’ to have the system auto-assign the next sequential item number.
Note: Items copied from an existing submittal will default a number as defined during the copy process, which cannot be changed.

##  Submittal Items: Description

 Enter a description of this submittal item, up to 60 characters. Initially defaults the description from the submittal header. Items copied from an existing submittal will default the description as previously defined.
TIP: Using the Down Arrow in this field will save the current description and advance you to the next line. This can be useful for quick modification of item descriptions when adding revisions to a submittal.

## Submittal Items: Status

Specify the status (from PM Status IDs) of this submittal item. Initially defaults the status from the submittal header.
Note: Items copied from an existing submittal will default the status from the current submittal header rather than the source submittal.

## Submittal Items: Spec #

Enter the specification number for this submittal, up to 20 characters. Initially defaults the specification number specified in the submittal header.

##  Submittal Items: Send

 Check this box if this submittal item is ready to be sent to the subcontractor/supplier or architect/engineer. This box must be checked in order for this item to be included when generating the submittal document using the ‘Create with Template’ feature. Who the submittal document is sent to is determined by the 'tracking dates' in the submittal header.
 Leave this box unchecked if this submittal item is not ready to be sent to the subcontractor/supplier or architect/engineer. Item will be excluded when generating the submittal document using the ‘Create with Template’ feature.
Note: Items copied from an existing submittal will default this flag from the source submittal item. May be overridden.

##  Submittal Items: Date Due

 Specify the date this submittal item is due back from the subcontractor. Defaults the ‘Date Due From’ (for subcontractor/supplier) as specified in the header of the current submittal, regardless of whether item was copied from an existing submittal item.

##  Submittal Items: Req'd

 Specify the number of copies (0-255) of this submittal item requested from the subcontractor/supplier. Defaults the ‘Copies Required’ (for subcontractor/supplier) as specified in the header of the current submittal, regardless of whether item was copied from an existing submittal item.

##  Submittal Items: Date Rec'd

 Specify the date you actually received this submittal item back from the subcontractor. Defaults the ‘Date Received’ (for the subcontractor/supplier) as specified in the header of the current submittal, regardless of whether item was copied from an existing submittal item.

##  Submittal Items: Rec'd

 Indicate the number of copies (0-255) received of this submittal item from the subcontractor/supplier. Defaults the ‘Copies Received’ (for the subcontractor/supplier) as specified in the header of the current submittal, regardless of whether item was copied from an existing submittal item.

##  Submittal Items: To Arch/Eng

 Specify the date this submittal item was sent to the architect/engineer. Defaults the ‘Date Sent To’ (for the architect/engineer) as specified in the header of the current submittal, regardless of whether item was copied from an existing submittal item.

##  Submittal Items: Sent Arch

 Indicate the number of copies (0-255) of this submittal item you sent to the architect/engineer. Defaults the ‘Copies Sent’ (for the architect/engineer) as specified in the header of the current submittal, regardless of whether item was copied from an existing submittal item.

## Submittal Items: Date Due Back

Enter the date this submittal item is due back from the architect/engineer.
This field defaults the ‘Date Due Back’ (for
 the architect/engineer) as specified in the header of the current submittal, regardless of
 whether item was copied from an existing submittal item. If that date is not present, the
 field defaults from the PM Projects (Default Standard Days Due field, PM
 Info).

##  Submittal Items: Date Rec'd Back

 Specify the date you received the submittal item back from the architect/engineer. Defaults the ‘Date Rec’d Back’ (for the architect/engineer) as specified in the header of the current submittal, regardless of whether item was copied from an existing submittal item.

##  Submittal Items: Rec'd Arch

 Indicate the number of copies (0-255) of this submittal item received back from the architect/engineer. Defaults the ‘Copies Rec’d Back’ (for the architect/engineer) as specified in the header of the current submittal, regardless of whether item was copied from an existing submittal item.

##  Submittal Items: Date Ret'd

 Specify the date this submittal item was returned to the subcontractor. Defaults the ‘Date Ret’d’ as specified in the header of the current submittal, regardless of whether item was copied from an existing submittal item.

##  Submittal Items: Copies Ret'd

 Indicate the number of copies (0-255) of the submittal item that were returned to the subcontractor/supplier. Defaults the ‘Copies Ret’d’ as specified in the header of the current submittal, regardless of whether item was copied from an existing submittal item.

##  Submittal Items: Activity Date

 Specify the date that the activity defined on this submittal is scheduled to begin. Defaults the ‘Activity Date’ specified in the header of the current submittal, regardless of whether item was copied from an existing submittal item.

## Notes

Enter any notes that apply to the submittal item.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.
Spelling Check
 Click the Spelling icon on the toolbar or select Tools >  Spelling  to spell check the text in this field.

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
Tip: The sort name can be used instead of the firm number
 when selecting firms in PM module forms. Generally the sort name is the first several
 letters of the firm name.  For example when creating a subcontract in the [PM Subcontracts](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form) form for 'Bryan Electrical', you can enter the sort name 'bryan'
 in the Vendor field instead of the firm number '10042'. The sort name of a firm is
 set up using the Sort Name field on the [PM Firms](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firms-form) form.

[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
PM Submittals - Overview
[](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-the-pm-submittal-package-form)PM Submittal Package

## Sent To Contact

Enter the contact that should receive the
 document(s) generated using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature, or press F4 to select
 one from a list. Only contacts associated with the firm selected in the Sent To Firm
 field can be selected.
Contacts are associated with firms using [PM Firm Contacts ](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firm-contacts-form).
Distribution defaults
When creating a new record, the Distribution
 tab will automatically populate with any PM firm contact set up as a distribution
 default.
For example, if a contact at an architecture firm should receive a copy of all drawing logs of document type 'ARCH', you can use the distribution default feature to set up that contact as a default for 'ARCH' documents. When drawing logs of that type are created, that contact will automatically populate on the Distribution tab.
Click [here](/en/vista/vista/project-management/create-and-send/pm-assign-distribution-defaults-form) for more information on distribution defaults.

Create and Send - Overview
PM Submittals - Overview
[](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-the-pm-submittal-package-form)PM Submittal Package

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

[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
PM Submittals - Overview
[](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-the-pm-submittal-package-form)PM Submittal Package

## Preferred Method

Use this field to select which type of communication should be sent to the contact when using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature. This field defaults based on the preferred method set up using [PM Firm Contacts](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firm-contacts-form).

- M - Print — Print a hard copy of the generated PDF document(s).
 When this option is selected, the contact will not receive a copy of the email body
 text.

- E - Email — Send the generated PDF document(s) using email. The
 email address of the contact is pulled from the Email field on the Info tab of the PM
 Firm Contacts form. F -Fax — Send the generated PDF document(s) suing fax. The system
 will use the fax number set up on the PM Firm Contacts form. Note: This option requires that you have a fax server set up in the
 Fax Server
 Name field on the Info tab of [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form).

Create and Send - Overview
PM Submittals - Overview
[](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-the-pm-submittal-package-form)PM Submittal Package

## Send Type

Select how the contact should be added to the
 communication generated from the Create and Send feature: To, Cc, Bcc.
When a communication is created using the Create and Send feature (), the contact will automatically be added using the selection in this field.
Click [here](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) for an overview of the Create and Send feature.
If a communication has already been sent
If an email generated using the Create and Send feature has already been sent to the contact, this field will display how the contact was included on the last communication.
For example if the contact was added to an
 email in the To field on the PM Send Documents form, To will display
 in this field. When a new email is created using the Create and Send form, the contact will
 automatically populate in the To field.

Create and Send - Overview
PM Submittals - Overview
[](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-the-pm-submittal-package-form)PM Submittal Package

## Date Sent

Enter the date the submittal was sent to this firm/contact.
This field initially populates a date based on the following:

- The current date

- Or the date is entered in the Date Sent To field on the Info tab if one is entered.

## Date Signed

Enter the date the contact signed the document.
Date field shortcuts
T
 or tSet the date
 to the current date.
MMDDFour digit month and
 day
Enter a four
 digit month and date (MMDD) and the system will automatically add the current
 year.
+The system
 will automatically set the date to tomorrow.
+5The system
 will automatically set the date to 5 days in the future. You can actually enter any
 value after the +, for example you can enter +7 to set the date to next
 week.

-The system
 will automatically set the date to the previous day.
-5The system
 will automatically set the date to 5 days in the past.Just like with +, you can enter
 any value after the -, for example you can enter -7 to set the date to the previous week.

[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
PM Submittals - Overview
[](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-the-pm-submittal-package-form)PM Submittal Package

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

Create and Send - Overview
PM Submittals - Overview
[](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-the-pm-submittal-package-form)PM Submittal Package
