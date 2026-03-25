---
title: "About the PM Import Estimates Detail Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/import-project-estimates/about-the-pm-import-estimates-detail-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/import-project-estimates/about-the-pm-import-estimates-detail-form"
---

# About the PM Import Estimates Detail Form

Use this form (accessed by clicking the Detail button in PM Import Estimates Template) to format import detail by record type.
The Info tab is used to indicate which record types will be included in the import file. Record types identify the types of data that you will be importing for the specified template (e.g. contract items, phases, cost types, subcontract detail, material detail, and estimate information). For each record type, you must specify how to identify that record type in the text file.
The remaining tabs are used to define the specifics for importing the data for each record type. For each field, you must indicate where the field is found in the text file, whether the field is required, and define any applicable defaults. On these tabs, you cannot delete standard records; however, you can delete any custom records that you have added.
Note: You will only need to set up specifications for those
 record types that are included in the import data file and for which you defined an
 identifier on the Info tab.

- Column Name/Column Desc –
 Identifies each field in the import data file. You will note that each tab
 includes a Record Type field. The
 Record Type identifies each type of record in the import file (i.e. Items,
 Phases, Cost Types, Subcontract Detail, Material Detail, and Estimate Info).
 For this field, you will only need to specify the location of the record
 type in the data file (i.e. the Rec Column or Beg/End Pos).

- Rec Column – This field is
 enabled for delimited import templates only (i.e. data fields in the import
 file are separated by a delimiter, such as a comma). You will use this field
 to identify where in the import data file the specified field is located.
 You must enter a record column number for importing default values. Each
 record column is separate by a comma. For example, let’s assume the
 following record is a phase record:

2,11000-,100,01003-,MOBILIZATION,Notes,Y,WC-GEN,10.00
In this example, the record columns for each of the fields would be as follows:
Column Name
Rec Column

Record Type
1

Project Code
2

Item
3

Phase
4

Description
5

Notes
6

Active
7

Insurance Code
8

Project Minimum Percent
9

- Viewpoint Default – This field is used to indicate
 whether you will use the Viewpoint Default for the field. It is used in
 conjunction with the Override checkbox to
 determine if, and when, the Viewpoint Default Value is used. See Viewpoint
 Default Value below for specifics.

- Viewpoint Default Value – Display-only, the
 Viewpoint default value for this field, if applicable. This value will always be
 used if both the Viewpoint Default and
 Override boxes are checked, regardless of whether an import
 file value exists. If you check the Viewpoint Default box, but uncheck the
 Override box, this value will only be used when import file value is null.

- Override – This option indicates whether to override
 the import file value for the field. It is used in conjunction with the
 Viewpoint Default checkbox to determine whether to use the
 Viewpoint Default Value, the User Default Value, or the import file value as
 follows:

- If you check both the Viewpoint Default and Override boxes, the Viewpoint Default Value will always
 be used, regardless of whether an import file value exists.

- If you check the Viewpoint Default box and uncheck the Override box, the system will use the import file
 value. If the import file value is null, the Viewpoint Default Value is
 used. If the Viewpoint Default Value is null, the User Default Value is
 used. If the User Default Value is null, the field value is set to null.

- If you uncheck the Viewpoint Default box and check the Override box, the User Default Value is always used,
 regardless of whether an import file value exists.

- If you uncheck both the Viewpoint Default and Override boxes, the import file value will always be
 used.

- User Default Value – This field is used to enter a user-defined default value. You will typically only use this when a specific value is required for all records. For example, if the Projection Minimum Percent for phase records should always be 10%, you would enter 10.00 in this field for the Projection Minimum Percent field on the Phase tab. The value in this field will only be used if the Viewpoint Default box is unchecked and the Override box is checked, or if the Viewpoint Default box is checked and the Override box is unchecked and no value exists in the import data file or the Viewpoint Default Value field.
