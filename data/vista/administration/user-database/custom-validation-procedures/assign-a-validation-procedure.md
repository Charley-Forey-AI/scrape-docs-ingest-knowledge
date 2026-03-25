---
title: "Assign a Validation Procedure | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/user-database/custom-validation-procedures/assign-a-validation-procedure"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/user-database/custom-validation-procedures/assign-a-validation-procedure"
---

# Assign a Validation Procedure

Validation procedures are assigned to a field using the
 Validation section of the Form Properties (F3) window, System Overrides tab.
This topic gives a general overview of assigning
 validation procedures. For more information on the F3 window, refer to F3 (Field
 Properties) in Related Topics below. To
 assign a validation procedure in the F3 window:

1. Select the
 Value is required
 checkbox if the field requires input.

1. Select the appropriate
 validation level from the Level drop-down. For additional information on
 available level options, refer to [F1 help](/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-field-properties-form/field-definitions-field-properties-form#ID-0004cb11--en) for the Level field.

1. Enter the custom
 validation procedure in the Procedure field. Press
 F4

 for a list of available custom procedures.

1. Specify the parameter(s)
 in the Parameters field if the validation procedure is searching for a specific
 column. Typically, this is the field’s sequence number (indicated in the Field
 Seq# field). This is matching the form’s input sequence to the parameter
 specified in the validation.

1. Click
 Apply
 . The validation procedure is now set for the field.

1. Click
 Cancel
 to close the F3 window. Note: If you want to have the validation
 description to display when you are viewing the field from the Grid tab,
 select the Show In Grid checkbox on the System Overrides tab. Then, from the
 Description in Grid drop-down, select 1-Show Above Grid Only. The system
 will display the description field above the active Grid tab. You can only
 select to have the description field display above the grid; you cannot set
 it to display from within the grid.
