---
title: "Field Definitions: PM Create and Send Settings Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/create-and-send/pm-create--send-settings-form/field-definitions-pm-create-and-send-settings-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/create-and-send/pm-create--send-settings-form/field-definitions-pm-create-and-send-settings-form"
---

# Field Definitions: PM Create and Send Settings Form

The following is a list of field descriptions for the PM
 Create and Send Settings form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Document Category

Enter the document category for which to
 define overrides. Press F4 for a list of valid categories or use
 the navigation buttons in the toolbar to locate the desired category.
RFQs
There are two options that relate to RFQs:

- REQQUOTE - Select this option if
 you want to set up the document category used by the PM Request For Quote form that
 was created in the 6.7.0 release.

- RFQ - Select this option if you
 want to set up the document category that is used by the legacy PM Request For Quote
 - 6.6 form.

Related Information
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-settings-form)PM Create and Send Settings

## Attach Document to Parent Record after Send

Check this box if a document generated using
 the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature should by default be attached to
 the parent form. When documents of this category are generated, by default the Attach Document to parent
 form box will be checked.
Related Information
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-settings-form)PM Create and Send Settings

## Deactivate Document Create and Send Feature

Check this box to disable the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature on this document category. This will remove the Create and Send icon from the toolbar at the top of the form.
For example if you check this box on the
 CCO
 document category, the Create and Send () icon will not display on the [PM Contract Change Orders](/en/vista/vista/project-management/change-orders/pm-contract-change-orders-form) form for all users.
Related Information
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-settings-form)PM Create and Send Settings

## Use Viewpoint Standard Subject Line

Check this box to use the standard Viewpoint subject line format (document type, document number, and description) for all documents generated for this document category.
Uncheck this box to customize the format of
 the subject line for documents generated for this document category. Use the Subject Line
 text box below to define the subject line format.
Related Information
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-settings-form)PM Create and Send Settings

## Subject Line

Use this field to set up the default subject line of the selected document category. This allows you to automatically add document information to the subject line. For example when setting up the default subject line of the RFI document category you can configure it to automatically include the project and RFI number.
This field is only enabled when the
 Use Viewpoint Standard Subject Line
 box is not checked.
Using the Email Fields button

1. Enter any standard text that should be included in the subject. For example
 if you include your company name in all emails, enter it into the Subject
 Line field.

1.  Click on the Email Fields button to add a field
 that the system will automatically populate when the communication is generated. For
 example, the project number associated with the document.

1.  The PM Document Category form will display all of the fields related to the
 selected document category.

1.  Select a table in the drop down at the top of the form.
 The drop down menu at the top of
 the form allows you to select a different table. For example when setting up
 the RFI document category, you can select the JCJM table, which contains
 general information about the project/job (job description, job address, etc.),
 or the PMRI table, which contains general information about the RFI (RFI
 number, RFI date, etc.).

1.  To add a field to the subject line, drag and drop a field from the PM
 Document Category List View form to the Subject Line field on the PM Create
 & Send Settings form.

1.  Click the Close button when complete to close
 the PM Document Category List View form.
 Using the Test Subject Line
 button
Click the Test Subject
 Line button to see a sample of the subject line format. The Test
 Results window displays, showing you how generated subject lines will
 appear.
Related Information
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-settings-form)PM
 Create and Send Settings

## Document File Naming Convention

Use the Document File Naming Convention
 section in the lower portion of the Info tab to define the file name format of the document
 generated by the Create and Send feature. This is the file or files that are included in
 the email to the project contact. For example if you collate several project documents,
 reports, and attachments into a single document, the setting in this section determines the
 name of that file.
Follow the steps below to use fields from the
 application to determine the file name of the generated document.

1. Make sure the Use Viewpoint Standard File Naming
 Convention box is not checked.

1. Click the File Name Fields button. The PM
 Document Category List form will display.

1. Use the PM Document Category List form to select the fields that
 you want to include in the file name of the generated documents. For example if you
 are using the firm name and contact name fields, you should also include the system
 date (via manual entry) to ensure that the file name is unique:
 [SysDateNum]_[PMFM.FirmName]_[PMPM.LastName][PMPM.FirstName]
When a document is generated, the file
 name will look something like this: 20141023_ABCConstruction_FranklinBob.doc

1.  On the PM Document Category List form, select the table that contains the field
 you would like to add to the file name.

1.  Find the file in the list and then drag and drop it into the File Name field on the PM Create and Send
 Settings form.

1.  Close the PM Document Category List form.

1.  Click the Test File Name button to
 view a sample file name. The Test Results window displays, showing you how generated
 file names will appear.
 Related Information
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-settings-form)PM Create and Send Settings

## Use Viewpoint Standard CC List

Check this box to use the standard Viewpoint CC list format (contact name, firm name, phone number, fax number) for all documents generated for this document category.
Uncheck this box to customize the format of
 the CC list for documents generated for this document category. Use the CC List text
 box below to define the CC list format.
Related Information
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-settings-form)PM Create and Send Settings

## CC List

This field is enabled only when the Use Viewpoint Standard CC
 List box is unchecked.
Using the PMFM - Firm Master and PMPM - Firm
 Contact list boxes below, drag and drop the columns you want included when displaying CC
 list information on documents for this document category.
Note:The columns selected here only control the information shown for each contact flagged for CC in the distribution list of the originating form. It does not control the contacts included in the CC list of the generated Word document, or the Cc line of the resulting email/fax.
Test CC List

Click this button to see a sample of the CC list format. The Test Results window displays, showing you how the values will appear in the CC section of the document.
Related Information
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-settings-form)PM Create and Send Settings

## Notes

Use this field to enter notes on the Create and Send settings. The notes entered in this field will not display anywhere in the generated emails.
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
Related Information
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-settings-form)PM Create and Send Settings

## Table

Press the F4 button, and from the list, select the table containing the column you want to add for display to the Project Firm Contacts window for this document category.
Note: The Project Firm Contacts window displays when you double-click the Distribution grid on any form with Document Tool functionality.

[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-settings-form)PM Create and Send Settings

## Column

Press the F4 button, and from the list, select the column from the specified table to display in the Project Firm Contacts window for this document category.
Note: The Project Firm Contacts window displays when you double-click the Distribution grid on any form with Document Tool functionality.

[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-settings-form)PM Create and Send Settings

## Column Heading

Initially defaults the pre-defined heading for this column. You may leave the default intact or enter a new column heading, up to 50 characters.
Note:Changing the heading description will affect only the heading displayed in the  Project Firm Contact window for this document category; it does not affect the heading for any other document category, nor does it affect any other heading in the system where the selected column may be in use.

[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-settings-form)PM Create and Send Settings

## Visible

Check this box to show this column when the Project Firm Contacts is displayed (by double-clicking the Distribution tab of related form for this document category). Initially defaults as checked for all columns.
Uncheck this box to hide this column when the Project Firm Contacts is displayed for this document category.

[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-settings-form)PM Create and Send Settings
