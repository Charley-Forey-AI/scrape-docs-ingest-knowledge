---
title: "Create Custom Form Buttons | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/custom-formsfields/create-custom-form-buttons"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/custom-formsfields/create-custom-form-buttons"
---

# Create Custom Form Buttons

You can set up custom buttons to open a form, report, or external application, or initiate a stored procedure.

1. From the Vista main menu, go to Viewpoint Administration > Programs > VA Custom Form Buttons. For more information, see [VA Custom Form Buttons Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-form-buttons-form).

1. Select the new record () icon in the toolbar at the top of the form.

1. In the Form field, press F4 and select the form you want to add the button to.

1. In the Button ID field, enter a + to have the system automatically assign the next available ID number. Note: The number distinguishes this button from all other custom buttons on the specified form.

1. On the Info tab, enter the text that will display on the button in the Text field.

1. In the Action Type dropdown, select what you want to button to do. Choose between:

- Form

- Report

- Stored Procedure

- External Application

- Stored Procedure to File

For details about each of these options, see [Action Type](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-form-buttons-form/field-definitions-va-custom-form-buttons-form#ID-00048685--en).

1. In the Action field, enter an action that corresponds with the Action Type you entered previously. The action is what will happen once someone selects the button. See [Action](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-form-buttons-form/field-definitions-va-custom-form-buttons-form#ID-000486a2--en) for guidance on what to enter based on the Action Type you selected.
Note: If you selected an Action Type of External Application, a Browse button displays. Select this to choose the network location of the executable that you want the button to run.

1. Select a refresh option in the Button Refresh field. Choose between:

- No Refresh

- Refresh Record

- Refresh Dataset

For details about each of these options, see [Button Refresh](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-form-buttons-form/field-definitions-va-custom-form-buttons-form#ID-0005de29--en).

1. On the Parameters tab, specify any parameter settings that you want to pass to the program (form, report, external application, or stored procedure) associated with the button. For guidance, see [Set Parameters for Custom Form
 Buttons](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/set-parameters-for-custom-form-buttons).

1. Save the record.

1. Open the form where you added the button.

1. Select Tools > Move Custom Buttons to move and resize the button.

1. When you finish positioning the button, select Accept.Note: If you reposition a button outside of the normal tab control area, the button will not be included in the input / tabbing order.
