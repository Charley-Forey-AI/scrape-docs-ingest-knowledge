---
title: "Example: Set Parameters for Stored Procedures | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/custom-formsfields/set-parameters-for-custom-form-buttons/example-set-parameters-for-stored-procedures"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/custom-formsfields/set-parameters-for-custom-form-buttons/example-set-parameters-for-stored-procedures"
---

# Example: Set Parameters for Stored Procedures

This example discusses placing a button on the PR Employees
 form that, when clicked, will pass the current employee’s sort name to an associated stored
 procedure.

1. On the Info tab in VA
 Custom Form Buttons, create the custom form button. Make sure to specify PR Employees as the form you are placing the form on,
 and the stored procedure in the Action field.

1. On the Parameters tab,
 in the Parameter ID field, enter a + to create a new entry and
 have the system automatically assign the next available ID number.

1. Enter a name for the
 parameter in the Name field.

1. Select 3-Form
 Input value from the DefaultType drop-down.

1. In the
 DefaultValue field, press F4,
 select the field name that contains the value to pass to the stored procedure,
 and click OK. In this example, select
 SortName from the F4 lookup. The system defaults the
 field’s sequence number in the DefaultValue field. In this example, the sequence
 is 20.

1. Save the record.

1. Open PR Employees and
 move the button to a new location, as necessary.

1. Click the custom form
 button to initiate the stored procedure.
