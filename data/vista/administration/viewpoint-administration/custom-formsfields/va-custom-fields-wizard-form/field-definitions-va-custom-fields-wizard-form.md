---
title: "Field Definitions: VA Custom Fields Wizard Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form/field-definitions-va-custom-fields-wizard-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form/field-definitions-va-custom-fields-wizard-form"
---

# Field Definitions: VA Custom Fields Wizard Form

The following is a list of field descriptions for the VA
 Custom Field Wizard form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Action

 Choose whether you want to add, change, or delete a custom field.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

## Combobox

 Select the type of combo box for the custom field. Combo box types defined in VA Custom Fields Combo Boxes display here.
 This field is available only if the
 Control to Use field is set to combo box.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

## Control to Use

 Use this field to select the type of control
 that you would like to use. This field is enabled when Text or Numeric is
 selected in the What is the general type of input? field on the previous step in the
 wizard. Once an option is selected, an example of the control will display in the lower
 portion of the form.

- Web – Select this option if the custom field will include a web address. Users can click a Web button and the page will open in the user's default browser.

- Notes – Select this option to add a scrollable notes field.

- Formatted Notes - Select this option if you would like to add a formatted notes field.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

- [Format a Notes Field](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/format-a-notes-field)

## Default Value

 Not required.
 Displays if

- Fixed Value
 is selected in the
 “How to Default”
 drop-down. Additionally displays, or

- Numeric
 is selected as the input and
 Variable Date
 is selected in the
 How to Default
 drop-down.

 Enter the default value for the field. If the
 selected input type is Text or Date, the Default Value must be %T, %L, or %F.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

## Enter a Comma-Separated List of Values for the Parameters

 Not required. Applicable only if the selected stored procedure has parameters.
 Enter a comma-separated list of values for the parameters.
Note: Use the “-2” parameter to indicate the new custom field being generated. This parameter is temporary and is replaced as soon as a sequence number for this field is generated. Use the “-1” parameter to indicate the currently active company.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

## Enter a mask that will be applied to the number

Note: This field displays when Numeric is
 selected in the What is the general type of input? drop-down and when the Use a pre-defined data
 type? option is not checked on the previous step.
 Enter a mask that applies to the custom field. The mask acts as a filter to include or exclude certain values.
Use the “0” and “#” characters to either display or suppress a leading zero when the number entered is smaller than the maximum value specified for the field; the number of “0” and “#” characters determines the size of the field.
For example, #,###,###,##0.00 indicates that the 3-numeric/decimal option was selected
 from the Select a
 numeric precision drop-down. Additionally, if a character is represented by
 a pound is a zero, then the zero does not display. So if the user enters a value of
 “12345.00,” the system displays it as “12,345.00.” The number fits within the established
 precision, but it does not reach the maximum value, so all of the zeros are removed.
Numeric masks that do not include decimals could indicate any of the "int" options. For more information on these options, see [Select a Numeric Precision](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form/field-definitions-va-custom-fields-wizard-form#ID-00048377--en).

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

## Error Message

 Not required.
 Enter the message that displays when the regular expression fails to validate user entries.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

## Form Label

 Enter the display name for the field. The system will automatically add a colon (:) after the text that you enter in this field.
An example of how the field will display on the form is at the bottom of the form.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

## Form Tab where the control will reside

 Select the tab where the custom field should appear. Each available tab displays in the combo box.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

## FYI, these Fields are Already on the Form

 This field populates when a form is selected in the “What Form will the Custom Field Go On” field; displays all fields currently on the selected form.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

## Grid Column Heading Text

 Specify the display name for the custom field’s grid column. This field automatically populates with the name entered in the Form Label field; it is recommended that the names match each other, but it is not required.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

## Hint Help Text that Appears in the Status Bar

 Not required.
 Enter help text that explains the field’s function to the user. This text displays at the bottom of the software screen on the display bar.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

## How Many Characters Do You Plan to Store?

Displays when “Text” is selected in the “What is the general type of input?” drop-down and when the “Use a pre-defined data type?” option is not checked.
Enter the number of characters that the text field displays; limit of 8,000 characters. If more characters are needed, use the bNotes pre-defined datatype.
Note: The system defaults to a maximum display length of 30 characters. If you specify a field length that exceeds 30 characters, you can resize the field to allow displaying additional characters using the [Move Custom Fields](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/create-custom-fields) option on the destination form.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

## How to Default

 Not required.
 Specify how the field defaults. There are four options available:

- Standard – defaults blank.

- Previous Value – defaults to the last entered value.

- Fixed Value – defaults to the value specified in the Default Value field to the right.

- Variable Date – defaults to the variable date value specified in the Default Value field to the right.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

## Is the Field Required?

 Not required.
 Specify whether or not the user is required to enter information in the field.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

## Maximum Value

 Not required.
 Set the maximum value for the custom field. For example, if a numeric field has been set up to allow two characters and you want the characters between 10 and 20, you would specify 20 here.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

## Minimum Value

 Not required.
 Set the minimum value for the custom field. For example, if a numeric field has been set up to allow two characters and you want the characters between 10 and 20, you would specify 10 here.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

## Name the Custom Field

 Enter the name of the custom field. The name must begin with “ud” which defines it as a custom field. For example, when adding a field called “Begin Service,” you might enter the table id as “udBegSvc.”
 Do not delete “ud” from the name.
 When changing or deleting a custom field, this field displays as “Select the Custom Field.” When changing, specify the custom field to change. When deleting, specify the custom field to delete.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

## Optionally Enter a Description for the Custom Field

 Enter a description for the custom field.
 When changing or deleting a custom field, this field displays as “Description.” After selecting the custom field from the “Select the Custom Field” option, the description appears. The description can be changed.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

## Use a Pre-defined Data Type / Pre-Defined Data Type

 Check the Use a pre-defined data
 type box, and then enter a data type in this field or press F4 to select
 one from a list.
Note: Datatypes cannot be modified when changing a custom field.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

- [Format a Notes Field](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/format-a-notes-field)

## Regular Expression

 Not required. Most users will not use this option.
 Enter a regular expression to validate entries. Regular expressions act as a template for a text string. If you are unfamiliar with regular expressions, the following web sites may provide help:

- [www.msdn.microsoft.com](http://www.msdn.microsoft.com/)

- [http://www.codeproject.com/Articles/9099/The-30-Minute-Regex-Tutorial](http://www.codeproject.com/Articles/9099/The-30-Minute-Regex-Tutorial)

- [http://www.regular-expressions.info/reference.html](http://www.regular-expressions.info/reference.html)

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

## Select a Numeric Precision

 Displays when Numeric is
 selected in the What is the general type of input? drop-down and when the Use a pre-defined data
 type? option is not checked.
 Specify a numeric precision:

- 0-Tinyint – Input can be up to three digits, for a range of 0-255.

- 1-Smallint – Input can be up to 5 digits, for a range of -32,768 to 32,767.

- 2-Int – Input can be up to 10 digits, for a range of -2,147,483,648 to 2,147,483,647.

- 3-Numeric/Decimal – Input can be up to 38 digits, as well as a decimal point in the mask.

- 4-BigInt – Input cab be up to 19 digits, for a range of -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

## Stored Procedure

Not required.
Specify a stored procedure for use with the custom field. The drop-down automatically populates with stored procedures that you created in UD User Validation.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

## Validation Options

 Not required.
 Select a validation option for the custom field. There are four options available:

- Invalid value OK, no warning – users can enter a value that does not match the input type for the field.

- Invalid value OK, but display warning – users can enter a value that does not match the input type, but warning displays.

- Valid value required, but focus can be moved – users cannot enter a value that does not match the input type, but can move to another field before saving form.

- Valid value required, focus stays on input – users cannot enter a value that does not match the input type and must enter a correct value before moving on from the field.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

## What Form will the Custom Field Go On?

Specify the form for the custom field.
When changing or deleting a custom field, this field displays as “What form is the custom field on?” When changing the custom field, specify the form that contains the custom field to change. When deleting a custom field, specify the form that contains the custom field to delete.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

## What is the General Type of Input?

Select the custom field input type.
The selection in this field determines what configuration options will display in the wizard.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

- [Format a Notes Field](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/format-a-notes-field)
