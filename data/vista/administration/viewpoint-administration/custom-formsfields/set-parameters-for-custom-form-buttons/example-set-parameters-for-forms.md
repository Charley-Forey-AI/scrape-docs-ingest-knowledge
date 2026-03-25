---
title: "Example: Set Parameters for Forms | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/custom-formsfields/set-parameters-for-custom-form-buttons/example-set-parameters-for-forms"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/custom-formsfields/set-parameters-for-custom-form-buttons/example-set-parameters-for-forms"
---

# Example: Set Parameters for Forms

This example discusses creating adds a button to the HR
 Resources form that launches the PR Employees form and opens the resource’s employee
 number.

1. On the Info tab in VA
 Custom Form Buttons, create the custom form button and select HR Resources in
 the Action field.

1. On the Parameters tab,
 in the Parameter ID field, enter a + to create a new entry and
 have the system automatically assign the next available ID number.

1. In the Name field, enter
 PR Employees

1. Select 3-Form Input
 value from the DefaultType
 dropdown.

1. In the DefaultValue field, press
 F4, select the
 field name that contains the value that the report will default in its parameter
 field, and select OK.
 In this example, select PREmp from the F4 lookup. 
 The system defaults the field’s sequence number in the DefaultValue field. In
 this example, the sequence is 10.

1. Save the record.

1. Open the HR Resources
 form and move the button to a new location, as necessary.

1. Click the custom form
 button. 

The PR Employees form
 displays and defaults to the PR employee number specified by the PR Empl # field in HR
 Resources.
