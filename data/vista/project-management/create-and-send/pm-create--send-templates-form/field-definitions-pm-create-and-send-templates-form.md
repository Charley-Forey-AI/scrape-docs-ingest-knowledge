---
title: "Field Definitions: PM Create and Send Templates Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form/field-definitions-pm-create-and-send-templates-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form/field-definitions-pm-create-and-send-templates-form"
---

# Field Definitions: PM Create and Send Templates Form

The following is a list of field descriptions for the PM
 Create and Send Templates form.Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Template Name

Displays the name of the document template. This is the name that will be used to select the template when using the [Create and Send ](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature.
Note:You cannot change the template name of an existing template, so changing the value in this field will automatically create a new document template.

Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

## Location

This field defines where the system will look for the template. Changing the value in this field on an existing template does not change the location of the template; it just changes where the system looks for it. For example, if you change the value in this field but do not move the document template to that location, you will get an error message when you try to view the document template. If you want to change where a template is stored, use [PM Transfer ](/en/vista/vista/project-management/create-and-send/pm-transfer-form)
Document locations are created and maintained in [PM Create & Send Locations ](/en/vista/vista/project-management/create-and-send/pm-create--send-locations-form) to move the document template.

Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

## Automated Response

Check this box if the document template should
 generate an automated response PDF document when using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature. Checking this box will
 automatically set the Type of document to create drop down to
 PDF, and it will enable the Response Fields tab, which is used to add automated response
 fields to the document template.
For more information on setting up automated response forms, see [About Automated Response Forms](/en/vista/vista/costs-and-contracts/pre-construction/pc-create-and-send/about-automated-response-forms).
Note:This box only displays when you select an invitation to bid document template.

Related Information
Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

## Template File Name

This field displays the file name of the MS Word template associated with this template.
If this field is blank and you enter a value, the system will not create the MS Word template. This field is only used to associate a document template in the application with an existing MS Word document.
Changing the file name in this field does not change the name of the existing file; it just changes the name of the file that the system searches for when creating the document based on the template. For example, if you change the value in this field without changing the file name of the template, you will receive an error message stating that the file doesn't exist.
 The template selected in this field must have a ".dot" or ".dotx" extension.

Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

## Template Type

Use this field to select the document template type, for example RFI, RFQ, or PCO.
The template type determines which merge
 fields and table merge fields will populate on the template when you click the Initialize
 Fields button, and which document objects can be added to the template using
 the Merge Fields and Table Merge Fields tab.
If you created this template using [PM Copy Template](/en/vista/vista/project-management/projects-and-contracts/projects/pm-copy-template-form), the template will inherit the template type from the template that was copied.
RFQs
There are two options that relate to RFQs:

- REQQUOTE - Select this option if
 you are creating a template to use with the enhanced PM Request For Quote form that
 was created in the 6.7.0 release.

- RFQ - Select this option if you are
 creating a template to use with the legacy PM Request For Quote - 6.6 form.

Related Information
Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

## Type of Submittal

Enabled only when using the ‘Submit’ template type.
Specify the type of submittal document for this template. The submittal type determines if the document template is requesting submittal information, sending it for approval, or acknowledging the current status, and therefore controls what data to merge when creating documents using the Create with Template option (Tools menu or Create and Send button).

- Request – Indicates template is for a 'Request for Submittal' type document.

- Submitted – Indicates template is for a 'Submitted for Approval' type document.

- Transmittal – Indicates template is for a 'Transmittal of Submittal' type document.

Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

## Type of Document to Create

Select the type of document you would like to create when using the [Create and Send ](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature with this template.

- doc– Select this option to always create a Word document.

- docx - This option only applies to Pre-Construction module bid document templates. Use this output to increase performance of the Create & Send feature in the Pre-Construction module.

- pdf– Select this option to always create a PDF file.

Note:To generate PDFs, you must have Microsoft Office 2007 or later, and the “Microsoft Save as PDF or XPS” add-in (available from Microsoft’s website) installed. If you do not meet this criteria, a Word document will created regardless of the selected option.

Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

## Active Template

Check this box to activate a template.
Only active templates are available when
 creating documents using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature. For example only active templates
 will display in the Document drop down on the Documents tab of the PM Send Documents form.
Related Information
[](/en/vista/vista/project-management/create-and-send/about-creating-a-document-template)Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send
 Templates

## Edit Document in Create and Send

Check this box if by default you want to edit the generated project document.
When this box is checked, the Edit box on the
 PM Send Documents form (Document tab) is automatically checked when this document template
 in selected. This means by default you will be able to edit the generated project document
 before it is sent.
The selection in this box reduces data entry. If you do not check this box, users will still be able to edit documents generated using the document template.
Related Information
Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

## Word Item Table

This field is enabled when the template
 contains detail items that must be merged into a table in the associated MS Word template -
 for example, the PM Subcontract Item standard template contains detail line items that
 populate in a table on the MS Word template.
The selection in this field is not
 important!
The enhanced Create and Send feature
 introduced in version 6.6.X requires that every merge field in a detail table must be
 entered in the document template. When you generate a document, the merged data will
 populate in the merge fields entered on the document template, not in the table selected in
 the Word Item
 Table field.

Related Information
[About Creating a Document Template](/en/vista/vista/project-management/create-and-send/about-creating-a-document-template)
[About the Create and Send Feature](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)
[PM Create & Send Templates Form](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)

## Merge Fields: Document Object

If you created this template using Document Template Copy, the grid is automatically populated with all document objects defined for the source template. Document objects may be added or deleted as necessary.
If you created this template manually, use the Initialize Fields feature (below) to populate the grid with all document objects for the template type.
To add a document object manually, press F4
 and select a valid document object for the template type. If the document object does not
 already exist for the template, a message displays indicating that the document object has
 not had any columns selected yet and asking if you would like to select multiple columns
 from list. Click Yes to open the PM Column Selection form and select columns to add to the
 grid. Click No to manually add columns to the grid.
Note:Adding a document object and related column(s) here only adds the field(s) to the ‘Insert Merge Field’ list in the Word template. To include the field(s) in the document template, you must add them manually using the Edit Template function.

Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

## Merge Fields: Column Name

If you created this template using Document Template Copy, the grid is automatically populated with all columns defined for each document object on the source template. Columns may be added or deleted as necessary.
If you created this template manually, use the Initialize Fields function (below) to populate the grid with all document objects and related columns for the template type.
To add a column manually, press F4, select the
 desired column from the list, and click OK to add the column to the grid.

- If you added a document object (in the previous
 field) that did not already exist for the template, a message displays indicating
 that the document object has not had any columns selected yet and asking if you would
 like to select multiple columns from a list. Click Yes to
 open the PM Column Selection form and select columns to add to the grid. Click
 No to manually add columns to the grid.

- Adding a document object and related column(s) here only adds the field(s) to the ‘Insert Merge Field’ list in the Word template. To include the field(s) in the document template, you must add them manually using the Edit Template function.

Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

## Merge Fields: Merge Field Name

Defaults the merge field name of the selected column. This is the name that will display in the ‘Insert Merge Field’ list for the template.
You will generally not need to change this name. However, if you do change the merge field name, it must be unique for the template. Up to 30 characters are allowed, but the name can only consist of numbers (0-9) and/or letters (A-Z, upper or lower case), with no spaces.
If you need to change the 'merge field name' for a column that already exists on the Word template (not just in the Merge Fields list), it is suggested that you first remove the field from the Word template, and then change the 'merge field name' here. The new name will be updated to the ‘Insert Merge Field’ list, and can then be re-added to the Word template.

Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

##  Merge Fields: Merge Order

 Defaults the merge order defined for the template type. If you created this template using Document Template Copy, defaults the merge order defined for the source template.
 The merge order only determines the order in which the field appears in the document’s ‘Insert Merge Field’ menu; it does not affect the order in which the field displays in the document template.
Note: You will typically not need to change the merge order; however, if you do choose to change the order, it is suggested that you use the Reorder Merge Columns form, as it is a much easier method than manually changing the order here. If you do change the merge order here, be aware that entering a number already in use will cause all remaining fields to be renumbered accordingly.

Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

##  Table Merge Fields: Document Object

 Enabled only for document templates with one or more Word item tables.
 If you created this template using Document Template Copy, the grid is automatically populated with all document objects defined for the source template’s Word item table. Document objects may be added or deleted as necessary.
 If you created this template manually, use the Initialize Fields feature (below) to populate the grid with all document objects for the template’s Word item table.
 To add a document object manually, press F4 and select a valid document object for the template’s Word item table.

Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

##  Table Merge Fields: Column Name

 Enabled only for document templates with one or more Word item tables.
 If you created this template using Document Template Copy, the grid is automatically populated with all columns defined for each document object in the source template’s Word Item Table. Columns may be added or deleted as necessary.
 If you created this template manually, use the Initialize Fields feature (below) to populate the grid with all document objects and related columns for the template type.
 To add a column manually, press F4, select the desired column from the list, and click OK to add the column to the grid.

Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

## Table Merge Fields: Merge Field Name

 Enabled only for document templates with one or more Word item tables.
 Defaults the merge field name of the selected column. This is the name that will display in the ‘Insert Merge Field’ list for the template.
 You will typically not need to change this name. However, if you do change the merge field name, it must be unique for the template. Up to 30 characters are allowed, but name can only consist of numbers (0-9) and/or letters (A-Z, upper or lower case), with no spaces.
Important:If you need to change the 'merge field name' for a column that already exists on the Word template (not just in the Merge Fields list), it is suggested that you first remove the field from the Word template, and then change the 'merge field name' here. The new name will be updated to the ‘Insert Merge Field’ list, and can then be re-added to the Word template.

Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

## Table Merge Fields: Merge Order

The merge order defines the order in which the detail information will populate in the table on the document template. For example, the field with a merge order of 1 will populate in the first column of the table in the document, the field with merge order 2 will populate second. See the example below.
Table Merge Fields tab
Column Name
Merge Order

Item Number
1

Item Description
2

Item Cost
3

The Table on the Document Template
Item Number
Item Description
Item Cost

Merge Order #1
(item number)
Merge Order #2
(Item Description)
Merge Order #3
(Item Cost)

When setting merge order, make sure the merge order populates the table so that the information displays under the correct column heading. In the example below, the Item Description and Item Cost fields have incorrect merge orders so when the data populates in the document template, it displays incorrectly.
Table Merge Fields tab
Column Name
Merge Order

Item Number
1

Item Description
3

Item Cost
2

The Table on the Document Template
Item Number
Item Description
Item Cost

Merge Order #1
(Item Number)

Merge Order #2
(Item Cost)

Merge Order #3
(Item Description)

Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

## Table Merge Fields: Format

Enabled only for document templates with one or more Word item tables.
For numeric fields only, specify the format in which the data populating this column will displayed - for example ###0, ###,###.000 represents the format of a number . You only need to enter a value here if you do not want the value in this column displayed in the standard format defined for the field.

Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

## Bookmark

Use this field to create a hyperlink to a
 bookmark in the document. This will change the field label defined in the Caption field
 into a hyperlink, and clicking the hyperlink will take the user to the defined
 bookmark.
In order to use this feature, you must add the
 bookmark defined in this field to the document template (click the Edit Template
 button).
For more information on setting up automated response forms, see [About Automated Response Forms](/en/vista/vista/costs-and-contracts/pre-construction/pc-create-and-send/about-automated-response-forms).
Related Information
Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

## Caption

Enter the caption that will display on the automated response form. The value in this field can be up to 128 characters long.
For more information on setting up automated response forms, see [About Automated Response Forms](/en/vista/vista/costs-and-contracts/pre-construction/pc-create-and-send/about-automated-response-forms).

Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

## Column Name

Press F4 to select the field that you would like to
 add to the automated response form. Only fields that belong to the document object
 selected in the Document Object field will display in the list.
Changing the value in this field will probably break the automated response form.
For more information on setting up automated response forms, see [About Automated Response Forms](/en/vista/vista/costs-and-contracts/pre-construction/pc-create-and-send/about-automated-response-forms).

## Control Type

Select the type of field that you would like to add to the automated response form.

- If BidResponse is selected in the Column Name field, this field should be ComboBox.

- If Attending Walkthrough is selected in the Column Name field, this field should be CheckBox.

- If Notes is selected in the Column Name field, this field should be TextBox.
Changing the value in this field will probably break the automated response form.

For more information on setting up automated response forms, see [About Automated Response Forms](/en/vista/vista/costs-and-contracts/pre-construction/pc-create-and-send/about-automated-response-forms).
Related Information
Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

## Document Object

A document object is a grouping of fields. Use this field to select the grouping that contains the field that you would like to add to the automated response form. Press F4 to select a document object from a list.
Changing the value in this field will probably break the automated response form.
For more information on setting up automated response forms, see [About Automated Response Forms](/en/vista/vista/costs-and-contracts/pre-construction/pc-create-and-send/about-automated-response-forms).

Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

## Read Only

Check this box if the field should be read-only on the automated response form. By default this box is not checked.
For more information on setting up automated response forms, see [About Automated Response Forms](/en/vista/vista/costs-and-contracts/pre-construction/pc-create-and-send/about-automated-response-forms).

Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

## Response Field Name

Enter the name that you would like to display on the automated response form.
Changing the value in this field will probably break the automated response form.
For more information on setting up automated response forms, see [About Automated Response Forms](/en/vista/vista/costs-and-contracts/pre-construction/pc-create-and-send/about-automated-response-forms).

Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

## Response Order

Use this field to change the order that the automated response questions will display on the form.
Changing the value in this field will probably break the automated response form.
For more information on setting up automated response forms, see [About Automated Response Forms](/en/vista/vista/costs-and-contracts/pre-construction/pc-create-and-send/about-automated-response-forms).

Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

## Response Values

Press F5 in this field to open [PM Response Values](/en/vista/vista/project-management/create-and-send/pm-response-values-form). This form is used to maintain response value records.
Press F4 to select the response values that will display on the automated response form.

- When you select BidResponse in the Column
 Name field, press F4 and select ITBResponse from the list that
 appears.

- Leave this field blank if any other field is
 selected in the Column Name field.
Changing the value in this field will probably break the automated response form.

For more information on setting up automated response forms, see [About Automated Response Forms](/en/vista/vista/costs-and-contracts/pre-construction/pc-create-and-send/about-automated-response-forms).

## Sequence

This field will populate with the next available number when adding a new automated response field to the template.
For more information on setting up automated response forms, see [About Automated Response Forms](/en/vista/vista/costs-and-contracts/pre-construction/pc-create-and-send/about-automated-response-forms).

Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

## Visible

Check this box if the field should be visible on the automated response form. By default this box is checked.

Create a new document template
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create and Send Templates

## Notes

Enter any notes that apply to the document template.
If you want to spell check the text in this
 field, click the Spelling icon on the toolbar or select Tools > Spelling.
