---
title: "Field Definitions: UD User Defined Lookups Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/user-database/lookups/about-the-ud-user-defined-lookups-form/field-definitions-ud-user-defined-lookups-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/user-database/lookups/about-the-ud-user-defined-lookups-form/field-definitions-ud-user-defined-lookups-form"
---

# Field Definitions: UD User Defined Lookups Form

The following is a list of field descriptions for the UD User
 Defined Lookups form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Lookup

 Enter the name of your lookup, up to 28 characters. This name must be entered without any spaces (for example, “CompanyVehicles”). After tabbing off this field, the system automatically assigns a prefix to the lookup name (“ud”), identifying it as a user-created lookup (for example, udCompanyVehicles).

##  Title

 Enter a title for your lookup, up to 30 characters. Spaces may be used. This is the description/title that displays when accessing this lookup.

## From Clause

A From Clause is used to specify the table that contains the records for the lookup.
Use this field to specify which table is used
 for this lookup. Press F4 for a list of valid tables. Select the
 User Defined Table Name radio button to view custom tables. If manually entering tables,
 user-created tables must be entered with the “ud” prefix.
If multiple tables are involved, specify the main lookup table here. Use the [Join Clause](/en/vista/vista/administration/user-database/lookups/about-the-ud-user-defined-lookups-form/field-definitions-ud-user-defined-lookups-form#ID-00047552--en) field to identify any other tables required to pull information for the lookup.
For example, in the JCPC Lookup (Phase Cost Types), there are two tables used to pull the lookup information: JCPC and JCCT. In this case, specify JCPC in the From Clause. The join clause identifies the second table (JCCT) with the statement: Join JCCT on JCPC.PhaseGroup=JCCT.PhaseGroup and JCPC.CostType=JCCT.CostType.
Using the Lookup function (F4, toolbar, or menu) to add additional tables to the 'From Clause' of an existing lookup with a single table will trigger a wizard that will walk you through the steps to convert your 'From Clause' to the new SQL-92 syntax (i.e. ANSI standard).

## Where Clause

A Where Clause is used to limit rows of data displayed by the lookup.
For example, the JCPC (Phase Cost Types) table holds all of the phase and cost type values set up on your system. A lookup used to display cost types for a specific phase group and phase would need the following 'where' clause:
JCPC.PhaseGroup=? and JCPC.Phase=?
Only those rows with a matching Phase Group and Phase code will be returned and displayed by the lookup. Without a 'where clause', all rows from the table are returned.
Note: The question marks are replaced by the parameters established in the F3 (Form Properties) window when the lookup is accessed.

## Join Clause

A Join Clause is only applicable if you are using more than one table in your lookup. It determines how the tables associate records with each other by specifying a unique set of values that exist in both tables. Typically, a join clause is used when the information displayed in the lookup comes from more than one table.
 For example, in the JCPC (Phase Cost Types) Lookup, the desired result is a list of valid cost types for the specified phase and their descriptions. However, the JCPC table does not contain a description of the cost type, so the “join” is created to pull the cost type description from JCCT (JC Cost Types).
JCPC.PhaseGroup=JCCT.PhaseGroup and JCPC.CostType=JCCT.CostType
The join specifies that both the Phase Group and Phase must be the same in the JCPC and JCCT tables. Based on these conditions, the system pulls the appropriate description for the cost type from JCCT, and displays it in the F4 window.

##  GroupBy Clause

 A GroupBy Clause is used to group the lookup records by one or more columns.
 For example, in the HQBCMths (Batch Months by Company) lookup, the Mth field is specified in the GroupBy Clause field. This ensures that all records returned to the lookup are grouped by month.

## Order by Column

 Specify the sequence number of the column (from the grid below) by which to sort records in the lookup. For example, using the setup shown below, if you want the lookup to sort by Cost Type, you would set the Order by Column to '0'.

Seq#
Column Name

 0
CostType

 1
 Description

Note: This field defaults to zero, as Vista™’s standard lookup sequence begins with zero.
The order of the column display is controlled by assigned sequence numbers. The value of the Order by Column controls which column is pre-sorted when accessing the F4 (Lookup) window. Standard F4 functionality allows other columns to be sorted manually by clicking on the column header.

## Sort Descending

Unchecked by default.
By default, columns display in a lookup in ascending order, from lowest to highest sequence number. However, using this checkbox, you can set the columns to display in descending order.
Note: Sequence numbers are set in the [Seq#](/en/vista/vista/administration/user-database/lookups/about-the-ud-user-defined-lookups-form/field-definitions-ud-user-defined-lookups-form#ID-00047587--en) field on the Details tab.

##  Notes

 Use this field to enter any additional notes regarding this lookup.

## Enable for Field Capture

Enable for Field Capture checkbox on the UD User Defined Lookups form

Click this box to enable this lookup to be used in Field View.

## Seq#

 Enter a number (0-255) to identify the sequence of this column. This is the order in which this column appears in the lookup. Sequence numbers cannot be changed once added.
Note:Vistasoftware's standard lookup sequence begin with zero. However, any number sequence can be used when creating custom lookups.
To change the sequence number, first delete the line and then re-add it with the new sequence number.
Note: The [Sort Descending](/en/vista/vista/administration/user-database/lookups/about-the-ud-user-defined-lookups-form/field-definitions-ud-user-defined-lookups-form#ID-0004757a--en) checkbox on the Info tab enables you to reverse the default order from ascending order to descending order.
Note: The [Order by column](/en/vista/vista/administration/user-database/lookups/about-the-ud-user-defined-lookups-form/field-definitions-ud-user-defined-lookups-form#ID-00047552--en) field on the Info tab enables you to specify the order in which the lookup sorts its records. This is done by specifying the sequence number of the column you want to sort by.

## Column Name

Enter the name of the column that will appear in the custom lookup. It must be a valid column from the table(s) specified in the [From Clause](/en/vista/vista/administration/user-database/lookups/about-the-ud-user-defined-lookups-form/field-definitions-ud-user-defined-lookups-form#ID-0004752f--en) or [Join Clause](/en/vista/vista/administration/user-database/lookups/about-the-ud-user-defined-lookups-form/field-definitions-ud-user-defined-lookups-form#ID-00047544--en). Press F4 for a list of columns valid for the specified table(s).

##  Column Heading

 This is the heading that displays for this column in the F4 Lookup. If it is a custom (user-defined) column, this is the description assigned to the column in “UD User Table and Form Setup”. The description may be overridden, up to 30 characters allowed.

## Hidden

Select this checkbox to not have the column display in the lookup. This is useful when the lookup uses this column as a sort or is used to filter data, but it doesn’t need to be viewed in the lookup. An example of this might be the Vendor SortName field.

##  Datatype

 Defaults the Vista software datatype assigned to the column, if defined when the column was set up. This value may be overridden; however it is not recommended. Typically, this value should be the same in the lookup as it is in the associated table. Using a Vista™ datatype controls the Input Type, Input Mask, Input Length, and Precision, and results in matching the format to standard fields.
