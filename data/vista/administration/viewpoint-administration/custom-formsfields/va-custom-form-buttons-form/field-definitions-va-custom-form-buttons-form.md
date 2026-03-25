---
title: "Field Definitions: VA Custom Form Buttons Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-form-buttons-form/field-definitions-va-custom-form-buttons-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-form-buttons-form/field-definitions-va-custom-form-buttons-form"
---

# Field Definitions: VA Custom Form Buttons Form

The following is a list of field descriptions for the VA
 Custom Form Buttons form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Action Type

Action Type field on the VA Custom Form Buttons form, Info
 tab.
 Select the type of action that this button should initiate.

- Form – to open a specific form.

- Report – to run a specific report.

- Stored Procedure – to initiate a stored procedure.

- External Application – to run an external application. When selecting this option, the Browse button appears next to the Action field.

- Stored Procedure to File – to initiate a stored procedure and
 write the contents to a file on your system.

Related information

- [Create Custom Form Buttons](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/create-custom-form-buttons)

- [VA Custom Form Buttons Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-form-buttons-form)

## Button ID

Button ID field on the VA Custom Form Buttons form
Use this field to uniquely identify each custom button on a form.
Enter ‘New’, ‘N’, or ‘+’ in this field and the system will automatically assign the new button the next available number.

Related information

- [Create Custom Form Buttons](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/create-custom-form-buttons)

- [VA Custom Form Buttons Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-form-buttons-form)

## Action

Action field on the VA Custom Form Buttons form, Info tab.
 Depending on the option that you selected in
 the Action
 Type field, you will enter different values in this field.

- If you selected Form from the Action
 Type dropdown, enter the form you want the button to open in this
 field. Press F4 to see a list of available forms.

- If you selected Report from the Action
 Type dropdown, enter the report that you want the button to run. Press
 F4 to see a list of available reports.

- If you selected Stored Procedure from the
 Action
 Type dropdown, enter the stored procedure that you want the button to
 initiate. Press F4 to see a list of available
 stored procedures.

- If you selected External Application from the
 Action
 Type dropdown, enter the network location of the executable that you
 want the button to run. Select the Browse button to open a browse
 window to locate the executable on your system.

- If you selected Stored Procedure to
 File from the Action Type dropdown, enter the
 stored procedure that you want the button to initiate. Press F4 to see
 a list of available stored procedures. After this stored procedure runs, the contents
 will write to a file on your system.

Related information

- [Create Custom Form Buttons](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/create-custom-form-buttons)

- [VA Custom Form Buttons Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-form-buttons-form)

## Button Refresh

The Button Refresh field on the VA Custom Form Buttons form, Info tab.
Select how the data will refresh when you
 select the custom button.

- No Refresh - Select this option if
 no data should be refreshed.

- Refresh Record - Select this option
 if only the current record should be refreshed.

- Refresh Data Set - Select this
 option if all of the data should be reloaded.

## Default Type

DefaultType field on the VA Custom Form Buttons form, Parameters tab.
 If you want to restrict the parameter to a
 current system setting, select the default parameter type from the drop-down. Choose from
 the following options:

- 0-Fixed Value

- 1-Current Date (+/-)

- 2-Current Month (+/-)

- 3- Form Input Value

- 4-Active Company

- 5-Active Project

- 6- Active Job

- 7-Active Contract

- 8-Active PR Group

- 9-Active PR End Date

- 10-Active JB Prog Bill Mth

- 11-Active JB Prog Bill#

- 12-Active JB TM Bill Mth

- 13-Active JBTM Bill#

- 16-Current User

- 17-Current Record ID

If you select either 0-Fixed
 Value or 3-Form Input Value, the system enables the
 [Default Value](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-form-buttons-form/field-definitions-va-custom-form-buttons-form#ID-0004870b--en) field. Otherwise, the system passes the correct
 value and DefaultValue is display only.

Related information

- [Create Custom Form Buttons](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/create-custom-form-buttons)

- [VA Custom Form Buttons Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-form-buttons-form)

## Default Value

DefaultValue field on the VA Custom Form Buttons form, Parameters tab.
The system enables this field when you select
 either 0-Fixed Value or
 3-Form Input Value in the
 [Default Type](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-form-buttons-form/field-definitions-va-custom-form-buttons-form#ID-000486f6--en) field. Otherwise, the system
 passes the correct value.
Depending on the option you select in the
 DefaultType field, you will enter different values in this field.

- If you selected 0-Fixed
 Value, enter the value that you want the parameter to pass.

- If you selected 3-Form Input
 Value, enter the sequence number of the field that contains the value
 that you want the parameter to pass through. Press F4 to see a
 list of fields associated with the form you specified in the
 Form field.

Related information

- [Create Custom Form Buttons](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/create-custom-form-buttons)

- [VA Custom Form Buttons Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-form-buttons-form)

## Form

Form field on the VA Custom Form Buttons form
 Press F4 to select from a list of Vista forms.

Related information

- [Create Custom Form Buttons](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/create-custom-form-buttons)

- [VA Custom Form Buttons Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-form-buttons-form)

## Name

Name field on the VA Custom Form Buttons form, Parameters tab
 Depending on the option that you selected in the Action Type field, you will enter different values in this field.

- If you selected Form from the Action Type
 drop-down, enter a name for this parameter. This field is optional; however, it is a
 good idea to enter a name that helps describe the parameter.

- If you selected Report from the Action Type
 drop-down, enter a report parameter or press F4 to select from a list of parameters
 associated with the report that you specified in the Action field.

- If you selected Stored Procedure from the Action
 Type drop-down, enter a name for this parameter. This field is optional; however, it
 is a good idea to enter a name that helps describe the parameter.

- If you selected External Application from the
 Action Type drop-down, enter the parameter name from the third-party application.

Related information

- [Create Custom Form Buttons](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/create-custom-form-buttons)

- [VA Custom Form Buttons Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-form-buttons-form)

## ParameterID

Parameter ID field on the VA Custom Form Buttons form, Parameters tab
 Enter an identification number for this parameter or enter ‘New’, ‘N’, or ‘+’ for the system to use the next available number. This number uniquely identifies this button from other parameters associated with this button.

Related information

- [Create Custom Form Buttons](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/create-custom-form-buttons)

- [VA Custom Form Buttons Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-form-buttons-form)

## Text

Text field on the VA Custom Form Buttons form
Enter the text that will display on the custom button.

Related information

- [Create Custom Form Buttons](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/create-custom-form-buttons)

- [VA Custom Form Buttons Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-form-buttons-form)
