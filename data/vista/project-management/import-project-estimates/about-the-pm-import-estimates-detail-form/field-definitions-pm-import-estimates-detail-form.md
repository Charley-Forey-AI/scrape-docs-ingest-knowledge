---
title: "Field Definitions: PM Import Estimates Detail Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/import-project-estimates/about-the-pm-import-estimates-detail-form/field-definitions-pm-import-estimates-detail-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/import-project-estimates/about-the-pm-import-estimates-detail-form/field-definitions-pm-import-estimates-detail-form"
---

# Field Definitions: PM Import Estimates Detail Form

The following is a list of field descriptions for the PM
 Import Estimates Detail form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Template

 Enter the import template (set up in PM Import Estimate Template) for which to enter template detail.

## Contract Item

Check this box to import contract item records when this template is specified in PM Import Estimate Data. Then use the Identifier field to the right to indicate how to identify contract item records in the import data file.
Uncheck this box if not importing contract item records when using this template.

## Phase

Check this box to import phase records when this template is specified in PM Import Estimate Data. Then use the Identifier field to the right to indicate how to identify phase records in the import data file.
Uncheck this box if not importing phase records when using this template.

## Cost Type

Check this box to import cost type records when this template is specified in PM Import Estimate Data. Then use the Identifier field to the right to indicate how to identify cost type records in the import data file.
Uncheck this box if not importing cost type records when using this template.

## Subcontract Detail

Check this box to import subcontract detail records when this template is specified in PM Import Estimate Data. Then use the Identifier field to the right to indicate how to identify subcontract detail records in the import data file.
Uncheck this box if not importing subcontract detail records when using this template.

## Material Detail

Check this box to import material detail records when this template is specified in PM Import Estimate Data. Then use the Identifier field to the right to indicate how to identify material detail records in the import data file.
Uncheck this box if not importing material detail records when using this template.

## Estimate Info

Check this box to import project detail records when this template is specified in PM Import Estimate Data. Then use the Identifier field to the right to indicate how to identify project detail records in the import data file.
Uncheck this box if not importing project detail records when using this template.

##  Identifier

 For each of the record types included when importing data using this template, enter up to 10 numbers and/or characters that will identify each record type in the import data file. For example, if contract item records are identified by the number ‘1’ in the import file, enter ‘1’ here.
 Each record type initially defaults the standard identifier defined by Viewpoint.

##  Seq

 This field displays the system-assigned sequence number for each field in the record type. Cannot be overridden for existing sequences.
 If adding a custom field to this record type, enter a sequence number (1-999999999), or enter ‘N’, ‘New’, or ‘+’ to have the system assign the next sequential number available.

##  Column Name

 This field displays the column name for each field of this record type. Cannot be overridden for existing sequences.
 If adding a custom field to this record type, enter the column name of a valid custom field (one added to the related form via VA Custom Fields Wizard) or press F4 for a list of valid custom fields for the related form. For example, if adding a custom field to the Phase tab, the F4 will show only those custom fields added to the JC Job Phases form (via VA Custom Fields Wizard).

##  Column Desc

 This field displays the column description for each field of this record type. Cannot be overridden for existing sequences.
 If adding a custom field to this record type, this field defaults the description defined in VA Custom Fields Wizard. Default may be overridden. Up to 30 characters allowed.

## Rec Column

This field is enabled only for templates using a delimited format (defined on Info tab in PM Import Estimates Template).
For each field on the selected tab, specify the column in which the field is found in the import data file. You must enter a record column number for importing default values.
For example, let’s assume the following is a phase record in a delimited import data file. The phase (blue text) is located in Column 4; therefore, you would enter ‘4’ in this field for the Phase sequence on the Phase tab.
2,11000-,100,01003-,MOBILIZATION,Notes,Y,WC-GEN,10.00

## Beg/End Pos

This field is enabled only for templates using a fixed length format (defined on Info tab in PM Import Estimates Template).
For each field on the selected tab, specify the beginning and ending position of the field in the import data file. Base the ending position on the total allowable for the field. You must specify these positions for importing default values.
For example, let’s assume the following is a phase record in a fixed-width import data file (for space considerations, we will focus on the first part of the phase record). The phase (blue text) has a character allowance of 13. Based on the space allowance for the record type, project code, and contract item fields, the beginning position for the phase code is ‘22’. Since the character allowance for the phase code is 13, the ending position would be ‘34’.
2 11000-   100       01003-       MOBILIZATION

## Viewpoint Default

This checkbox works in conjunction with the
 Override checkbox to determine the value used for this field when importing
 data.

- If you check this box and the Override
 box, the Viewpoint Default Value (specified to the right of this field) will always
 be used, regardless of whether an import file value exists.

- If you check this box and uncheck the Override
 box, the import file will be used, unless null. In which case, the Viewpoint Default
 Value will be used. If the Viewpoint Default Value is null, the User Default Value
 will be used. If the User Default Value is null, the field will be set to null.

- If you uncheck this box and check the Override
 box, the User Default Value will always be used. If the User Default Value is null,
 the field will be set to null.

- If you uncheck both this box and the Override
 box, the import file value will always be used. If the import file value is null, the
 field will be set to null.

## Override

This checkbox works in conjunction with the Viewpoint Default checkbox to determine the value used for this field when importing data.

- If you check both this box and the Viewpoint
 Default box, the Viewpoint Default Value (specified to the right of
 this field) will always be used, regardless of whether an import file value exists.

- If you check this box and uncheck the Viewpoint
 Default box, the User Default Value will always be used, unless null.
 In which case, the field will be set to null.

- If you uncheck this box and check the Viewpoint
 Default box, the import file will be used, unless null. In which case,
 the Viewpoint Default Value will be used. If the Viewpoint Default Value is null, the
 User Default Value will be used. If the User Default Value is null, the field will be
 set to null

- If you uncheck both this box and the Viewpoint
 Default box, the import file value will always be used. If the import
 file value is null, the field will be set to null.

## User Default Value

Enter the default value to use for this field.
 The value in this field will only be used if the Viewpoint Default box is unchecked and
 the Overridebox is checked, or if the Viewpoint Default box is checked and the
 Override box is unchecked and no value exists in the import data file or
 the Viewpoint
 Default Value field.

- You will typically only enter a value here when a specific value is required for all records of this type. For example, if you want all imported phases to default a 10% minimum projection percent, you would enter 10.00 in this field for the Projection Minimum Percent field on the Phase tab.

- When entering a user default value, you must also
 specify a record column in the Rec Column field or a value in the
 Beg
 Pos and End Pos field in the case of a
 fixed-length format.

- Although the character allowance for this field is unlimited (to accommodate the various field lengths), you should restrict entry to the number of characters allowed for the selected field. For example, if entering a default value for contract item and the contract item format allows 16 characters, the value should be no longer than 16 characters.
