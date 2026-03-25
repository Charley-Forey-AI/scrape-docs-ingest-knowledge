---
title: "Field Definitions: UD User Table Form Setup Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/user-database/custom-tables-and-forms/about-the-ud-user-table-and-form-setup-form/field-definitions-ud-user-table-form-setup-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/user-database/custom-tables-and-forms/about-the-ud-user-table-and-form-setup-form/field-definitions-ud-user-table-form-setup-form"
---

# Field Definitions: UD User Table Form Setup Form

The following is a list of field descriptions for the UD User
 Table Form Setup form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Table Name

 Enter a name for the table, up to 18 characters. The name cannot contain any spaces. For example, you can enter “CompanyVehicles”, but not “Company Vehicles”.
After you tab off this field, the system automatically assigns a two-character prefix to the table name (“ud”), identifying it as a user-created table (for example,“udCompanyVehicles”).

##  Description

 Enter a description of the table, up to 30 characters. Spaces may be used. This description is used as the title of the form, displaying in the UD Programs folder, as well as at the top of the form when it is open.

##  Form Name

 This field initially defaults from the Table Name entered above, but may be overridden. If overriding the default, make sure to enter the name without any spaces. Up to 28 characters are allowed. As with the Table Name, the system automatically adds the “ud” prefix.

## Company Based

 Select this checkbox if the data maintained by this form is company-specific. If checked, each company maintains its own set of records. The system automatically generates an invisible Company column that populates with the currently active company when the form is accessed.
Note: If you will be implementing data level security for any fields on this form, select this box. Data level security cannot be implemented without the Company relation. For more information, see Related Topics below.
 If this box is not selected, one set of records will be maintained and used by all companies.
 Once the table/form is created, this checkbox is disabled and cannot be changed.

Related information

- [Set Data Level Security when Creating a New Custom Form](/en/vista/vista/administration/user-database/custom-tables-and-forms/data-level-security-for-custom-tables-and-forms/set-data-level-security-when-creating-a-new-custom-form)

##  Use Notes Options

Use this drop-down field to add a Notes column to the database table for the user-defined form you are creating. The drop-down also determines what kind of notes will be included. If you select either
 Standard Notes
 or
 Formatted Notes
 , a Notes field displays on the Info tab of the user-defined form. If you select
 No Notes
 , no Notes field will display on the user-defined form.
Important: If you save your user-defined form with Formatted Notes selected, you cannot later switch to Standard Notes for that user-defined form. However, you can switch from Standard Notes to Formatted Notes.
Important: If you save your user-defined form with either Formatted Notes or Standard Notes selected, and then later you select No Notes, the Notes column will be deleted from the table, the Notes tab will disappear from the user-defined form, and any existing notes will be lost.
When you select
 Formatted Notes
 , a formatting toolbar displays above the Notes field on the Info tab.
 You can use the toolbar to apply text formatting (font face, font size, etc), list formatting, and paragraph formatting to your notes.

## Auditing

Check this box when you want to monitor the additions, modifications, and deletions for this custom form/table. When you check this box, you can view the audit log for this form using the VA Audit Log Viewer form.

## Enable for Field Capture

Enable for Field Capture checkbox on the UD User Table and Form Setup form
Check this box to allow this form to be available for use within Field View.

## Column Name

Use this field to enter the name of each column (field) in your table, up to 30 characters. Enter the name without any spaces; for example, “VehicleType.” This name represents the column throughout Vista™.
Important: Although you can have your column names begin with a number or a SQL-reserved word (e.g., ADD, ASC, CHECK, DESC, GROUP, USER, etc.), it is not recommended. Although columns beginning with numbers or SQL-reserved words will work fine within Vista™, they may cause problems when accessing the data in some third-party tools (e.g., Crystal, Access, Query Analyzer, etc.). In addition, DO NOT add a “Company” column to your table. The system automatically generates an invisible Company column that populates with the currently active company when the form is accessed.
If the column is associated with a ‘group-related’ data type, add a column that indicates the “group.” Make sure to assign “bGroup” as the datatype. As noted above, consider beginning the column name with something other than “GROUP.”
For example:
Column Name
Description
Datatype

Vendor
Vendor
bVendor

VendGrp
Vendor Group
bGroup

PhaseCode
Phase
bPhase

PhaseGrp
Phase Group
bGroup

The following table displays group-related datatypes (and their associated columns). For more information regarding group-related datatypes, refer to HQ Company Setup and HQ Groups in Related Topics below.
Inputs
Datatype

(AR) Customer
bCustomer

(AP) Vendor
bVendor

(PM) Firm
bFirm

(HQ) Material
bMatl

(HQ) Tax Code
bTaxCode

(JC) Phase
bPhase

(JC) Cost Type
bJCCType

(EM) Cost Code
bCostCode

(EM) Revenue Code
bRevCode

(EM) Cost Type
bEMCType

Related information

- [HQ Company Setup Form](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)

- [HQ Groups Form](/en/vista/vista/administration/headquarters/company-setup/hq-groups-form)

##  Description

 Enter a description of the column (field), up to 30 characters. This description is used as the label for the input field (text box, checkbox) on the form.

## Key Seq

This field is for “key” fields only.
Enter the sequence number, 0-255. The sequence number determines the order in which each key field is loaded into the form.
Key fields uniquely identify data records. For
 example, when setting up a contract (in JC Contracts), “Contract” is the key field. In most
 standard forms, the “key” fields are generally those fields first accessed in the form and
 are usually not included on tabs or grids.
On occasion, a key field will be located
 elsewhere on the form such as in JC Phases Maintenance. On this form, “Phase” is the first
 key field and is located at the top of the form. However, “Cost Type” is also a key field
 and it is located as the first field in the Cost Types grid of the form.
Note: Once the form has been saved (Update Table button), key sequences cannot be changed and new ones cannot be added.

## Auto Seq. Type

This field is activated when the column has been designated as a “key” field.
Use this drop-down list to determine how a key field defaults.

- 0-Not used - Use this option to indicate that the field does not auto-increment. In other words, the field is required, but the system does not insert a value of any kind. This option is the same as leaving this drop-down blank.

- 1-Auto value only - Use this option to have the field automatically default to the next value in the sequence. For example, if the last record entered was “1000,” the next record would default to “1001.” This option does not allow the user to change the value of the key field.

- 2-Auto value, but allow entry - Use this option to have the field automatically default to the next value in the sequence. However, this option also allows the user to enter a different value, if necessary.

Note: Auto-sequencing can only be applied to the last key field for the table/form you are creating. Auto-sequenced key fields depend on all the other key fields to be filled in, as it bases it's sequencing on changed values in at least one of the other key fields.

##  Control Type

 Use this field to determine the type of control the field uses. Available control types include:

- Textbox:the field displays as a text box.

- Checkbox:the field displays as a checkbox.

- Combobox:the field displays as a drop-down selection box.

- Date:the field displays the current date; can be changed by user.

- Month:the field displays the current month; can be changed by user.

- Web:the field displays a web address; by clicking the associated Web button, the default browser displays the web site.

- Notes:the field displays as a scrollable notes field.

## Combo Type

This field is activated when “Combobox” is selected as the Control Type.
Use this field to select the type of combo box to use. The field displays all custom-created combo boxes. Before creating a form with a combo box, make sure to create the combo box type using VA Custom Field Combo Boxes.

Related information

- [VA Custom Field Combo Boxes Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-field-combo-boxes-form)

## Datatype

Enter a Vista datatype for this field (column), or press
 F4
 to select one from a list.
Note: Viewpoint does not recommend the use of the bTime datatype for time because this datatype also includes the date.
Datatypes allow a custom field to have the same format as a standard field. For example, if the custom field is a date field, then the bDate datatype can be assigned as the datatype, and the field is automatically formatted as MMDDYY. If F4 Lookup and F5 Setup assignments exist, the custom field uses the F4 and F5 assigned to the datatype; these assignments may be overridden in the F3 properties window. Copied formatting also includes the input type, length, mask (if one exists), and precision (if numeric) parameters.
Note: Parameters cannot be changed unless the datatype assignment is removed from the custom column/field.
If a datatype is specified, the cursor automatically skips the remaining fields and moves to the Column Name input for the next custom column/field. If a datatype is not specified, enter the input type, mask, length, and precision of the field as applicable.
Note: If the field is a checkbox, use the standard “bY/N” datatype. checkbox fields cannot be created without referencing this datatype.
When implementing data level security, assign a securable datatype to the applicable field. For example, if an “Employee” field has been added and you want the field to be securable, assign the “bEmployee” datatype. Additionally, the [Company Based](/en/vista/vista/administration/user-database/custom-tables-and-forms/about-the-ud-user-table-and-form-setup-form/field-definitions-ud-user-table-form-setup-form#ID-00047137--en) checkbox should be selected. For a list of securable datatypes, see Related Topics below.

Related information

- [Set Data Level Security when Creating a New Custom Form](/en/vista/vista/administration/user-database/custom-tables-and-forms/data-level-security-for-custom-tables-and-forms/set-data-level-security-when-creating-a-new-custom-form)

## Input Type

This field is required if a datatype has not been specified.
Use this field to indicate which type of input to assign to the custom field.

- 0-Text: Use this input type for all “text” (alpha/numeric) type inputs (e.g. Description, Location, Sort Name, etc.)

- 1-Numeric: Use this input type for all inputs that are strictly numeric (e.g. Company number, account number, employee number, etc.)

- 2-Date:Use this input type for date fields.

- 3-Month:Use this input type to default to current month.

- 5-Multi-Part:Use this type if the input is a multi-part value (for example, 12-34532-12). Most often, this option is used in conjunction with a datatype (e.g., bPhase, bJob, etc.)

## Input Mask

Use this field only if a datatype is not specified. Typically, input masks are used for numeric fields, but they can be used for text fields to indicate a specific text justification.
Text Fields
If the
 Input Type
 is set to
 0-Text
 , available options are:

- R- Right Justified

- L- Left Justified

- F- Fixed Length

- LUCASE- Left Justified Upper Case

- FUCASE- Fixed Upper Case

If an input mask is not specified, text automatically defaults as left justified.
For more information, see [Input Type](/en/vista/vista/administration/user-database/custom-tables-and-forms/about-the-ud-user-table-and-form-setup-form/field-definitions-ud-user-table-form-setup-form#ID-00047246--en).
Numeric Fields
If the
 Input Type
 is set to
 1-Numeric
 , enter the input mask for this field; include commas and decimals if applicable.
In the
 Precision
 field, if you select
 0-tinyint
 ,
 1-smallint
 , or
 2-int
 , an input mask is not required. However, if you want the input to contain commas (such as for smallint or int precisions where the character allowance is larger), enter an input mask to indicate where the commas should go.
If you want the input to contain decimals, in the
 Precision
 field, select a precision of
 3-numeric/decimal
 , then base the input mask on the input length specified. For example, if an input length of 16 is specified, you would enter #,###,###,##0.00. For decimals requiring greater precision (such as units), you can specify up to 5 decimal places (e.g. #,###,##0.00000).
Use the “#” symbol when entering a mask to indicate that the position will be filled with a digit (0-9) or a blank space. For example:
If the input is a whole number and the input mask is #####
Input
Will appear as

1234
1234

0
[blank]

If the input is a decimal and the input mask is ##,###.##
Input
Will appear as

1234
1,234.

.12
.12

0
[blank]

If zero values should be printed instead of blank, use zeros in the mask.
For example, if the input mask is ##,##0.00
Input
Will appear as

1234
1,234.00

.12
0.12

0
0.00

When using zeros with masks for whole numbers (i.e. ###0), then a zero only prints when a zero is entered.
For example, if the input mask is ####0
Input
Will appear as

1234
1234

12340
12340

0
0

If the numeric should appear with a dollar sign ($), place that symbol in front of the input mask. For example:$##,##0.00.
Input
Will appear as

1234
$1,234.00

.12
$0.12

Note: When using decimals, edits to the input mask are somewhat limited. Due to SQL limitations, the number of characters before the decimal on an input mask can only be increased—decreasing them will cause the following error:
Note: “Number of characters to the left of the decimal must be at least XX”
“XX” represents the number of characters before the decimal on the previously defined mask (i.e., the mask being changed). For example, if changing a mask of ##,###.00, the new mask needs to contain at least 6 characters before the decimal (including commas).
Note: If the field requires a multi-part code, use one of the pre-defined datatypes provided with Vista™ (e.g., bContract, bPhase, or bJob).

## Input Length

 This field is required if a datatype is not specified.
 Enter the input length for this field. The input length defines the maximum number of characters allowed for entry in the field (including commas and decimals, if applicable).

-  If the field’s [Input Type](/en/vista/vista/administration/user-database/custom-tables-and-forms/about-the-ud-user-table-and-form-setup-form/field-definitions-ud-user-table-form-setup-form#ID-00047246--en) is 1-Numeric, the input length is controlled by the [Precision](/en/vista/vista/administration/user-database/custom-tables-and-forms/about-the-ud-user-table-and-form-setup-form/field-definitions-ud-user-table-form-setup-form#ID-00047343--en). For example, if the precision is 1 (smallint), input is limited
 to entry of numbers between -32,768 and 32,767. Therefore, the input length should
 not exceed 6 characters (including commas).

-  If the field’s [Input Type](/en/vista/vista/administration/user-database/custom-tables-and-forms/about-the-ud-user-table-and-form-setup-form/field-definitions-ud-user-table-form-setup-form#ID-00047246--en) is 0-Text,
 the character allowance is a maximum of 8,000 characters. However, because field
 display is limited, inputs with a larger character allowance may require the user to
 scroll through the text in order to see all data. On some forms, the display length
 of the field may be expanded by resizing the form itself.

- If you are editing the input length for an existing field, the input length cannot be changed to less than the longest value already in the existing table.

##  Precision

 This field is required if a datatype is not
 selected and [Input Type](/en/vista/vista/administration/user-database/custom-tables-and-forms/about-the-ud-user-table-and-form-setup-form/field-definitions-ud-user-table-form-setup-form#ID-00047246--en) is set to 1-Numeric. Available options include:

- 0-tinyint – Input can be up to three digits, for a range of 0-255.

- 1-smallint – Input can be up to 5 digits, for a range of -32,768 to 32,767.

- 2-int – Input can be up to 10 digits, for a range of -2,147,483,648 to 2,147,483,647.

- 3-numeric/decimal – Input can be up to 38 digits, as well as a decimal point in the mask. This option allows up to 38 digits, but characters before and after the decimal are determined by the [input mask](/en/vista/vista/administration/user-database/custom-tables-and-forms/about-the-ud-user-table-and-form-setup-form/field-definitions-ud-user-table-form-setup-form#ID-0004725c--en).

- 4-bigint – Input can be up to 19 digits, for a range
 of -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807.

Note: Due to SQL limitations, the number of characters before the decimal on an input mask can only be decreased—decreasing them causes the following error: “Number of characters to the left of the decimal must be at least XX.”
 “XX” represents the number of characters before the decimal on the previously defined mask (including commas). For example, if the previous mask was ##,###.00, the new mask needs to contain at least 6 characters before the decimal (e.g. ###,###.00).
 The Precision of a numeric should be in sync with the input mask and [input length](/en/vista/vista/administration/user-database/custom-tables-and-forms/about-the-ud-user-table-and-form-setup-form/field-definitions-ud-user-table-form-setup-form#ID-00047332--en) of the field. For example, if the input mask is #####, and the input length is “5,” the precision should be either 1-smallint or 2-int. A 1-smallint precision would allow entry of a number up to 32,767, while a 2-int precision would allow for a number up to 99999.
