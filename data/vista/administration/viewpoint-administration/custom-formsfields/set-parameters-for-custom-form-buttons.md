---
title: "Set Parameters for Custom Form Buttons | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/custom-formsfields/set-parameters-for-custom-form-buttons"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/custom-formsfields/set-parameters-for-custom-form-buttons"
---

# Set Parameters for Custom Form
 Buttons

When you create a custom form button using VA Custom Form Buttons, you can set parameters for each action type.
Parameters determine how the program (form, report, stored
 procedure, or external application) associated with the action type displays data or
 defaults. Parameters are passed in the format of `Name=Value`,
 where `Name` is what you defined in the Name
 field and `Value` is from the
 DefaultValue field.
The parameter configuration options
 depend on the type of program the custom button is accessing.

- If the button opens a form, you may want to add parameters that will
 pass values to the form when it opens.

- If the button opens a report, you may want to populate the report’s
 parameters with data from the form you are working on.

- If the button opens an external application, you want to pass
 parameters to the application and should understand the types of parameters
 that the application will accept. The way in which you configure parameters
 depends on the application that you are passing information to. The external
 application must have some way of receiving and processing parameters.

- If the button initiates a stored procedure, you may want to define
 parameters that will return specific values from the stored procedure after
 it runs.

- If the button initiates a stored procedure that will write the results to
 a file, you may want to define parameters that return specific
 values from the stored procedure and specify the name of the file for the
 results to write to.

Note: When you set
 parameters, the system automatically inserts a parameter for the current
 company, although this parameter does not display on the Parameters tab. Do not
 add a parameter for the current company or the custom form button may not work
 properly.

1. From the Vista main menu, go to Viewpoint Administration > Programs > VA Custom Form Buttons.

1. If you already created a custom button, find it in the grid and open the
 record. If you need to create a new button, follow the steps outlined in [Create Custom Form Buttons](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/create-custom-form-buttons).

1. On the Parameters tab,
 in the Parameter ID field, enter a + to create
 a new entry and have the system automatically assign the next available ID
 number.

1. In the Name field, enter a name the parameter.

1. Select a Default
 Type from the dropdown.For details about each of these options, see [Default
 Type](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-form-buttons-form/field-definitions-va-custom-form-buttons-form#ID-000486f6--en).

1. If you chose a
 Default Type of either 0-Fixed Value or 3-Form Input Value, enter a
 Default Value. Press F4 and select the field name
 that contains the value that the accessed form will default in its key field. For details about each of these options, see [Default Value](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-form-buttons-form/field-definitions-va-custom-form-buttons-form#ID-0004870b--en).

1. Save the record.

If you set parameters for a stored procedure, you may also
 want to [Create a Stored Procedure Success Message](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/set-parameters-for-custom-form-buttons/create-a-stored-procedure-success-message).If you'd like to see
 examples for setting parameters in a variety of different situations, see the
 following articles:

- [Example: Set Parameters for Forms](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/set-parameters-for-custom-form-buttons/example-set-parameters-for-forms)

- [Example: Set Parameters for Reports](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/set-parameters-for-custom-form-buttons/example-set-parameters-for-reports)

- [Example: Set Parameters for External Applications](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/set-parameters-for-custom-form-buttons/example-set-parameters-for-external-applications)

- [Example: Set Parameters for Stored Procedures](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/set-parameters-for-custom-form-buttons/example-set-parameters-for-stored-procedures)
