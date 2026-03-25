---
title: "Apply Custom Validation to a Field | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/field-validation/apply-custom-validation-to-a-field"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/field-validation/apply-custom-validation-to-a-field"
---

# Apply Custom Validation to a
 Field

You can apply customer validation to system fields.
Before assigning custom validation to a form field,
 you must have created a custom validation procedure using the UD User Validation form or
 another appropriate application. You cannot assign standard validation procedures (those
 created by Viewpoint Construction Software) to standard or custom fields; however, you
 can copy a standard validation procedure, rename it, modify it as necessary, and then
 assign it here.
If you are applying custom validation to a Viewpoint field with standard validation, the custom validation will be considered ‘secondary validation’ and will be triggered only after the standard validation procedure is completed successfully.
Note: When adding secondary validation to a key field, the system only validates the data when the form is in Add mode, or, if using the grid, the grid is in Add mode.

1. Place focus in the field to which you are assigning custom validation.

1. Press the F3 to
 access the Field Properties form.

1. Open the System Overrides
 tab.

1. In the Level
 field, use the drop-down menu to select the validation level to use.Note: If you are assigning secondary validation to
 the field, keep in mind that the system will use the more restrictive validation
 level for both the primary and secondary validation.

1. In the Procedure
 field, enter the name of the custom SQL stored procedure to use for validation of
 this field. The procedure name entered here must match a procedure in the Vista
 database.Note: You can use the F4 lookup to select the
 procedure name; however, the lookup will show only custom validation procedures
 created using the UD User Validation form.

1. To auto-map stored procedure
 parameters to form fields, click the Link button to the right of the
 procedure name. The Validation Field Linking form displays.Note: The Stored Proc Parameters list box in the
 Validation Field Linking form displays all parameters associated with the custom
 stored procedure. The system automatically selects each parameter in its listed
 order and will not allow selection of another parameter until you have
 successfully mapped the selected parameter.

1. To map to a field, use the
 Form Fields
 list box to select the form field that corresponds to the selected parameter. To assign a fixed value to the parameter, enter the value in the
 Fixed Value
 field.

1. Click the
 Map
 button. The system moves the selected parameter to the Stored Proc – Field Map list box, along with the field designation (field’s sequence number and field name) or the fixed value. Note: Fixed values are enclosed in single quotes.

1. Repeat Step 7-8 for each parameter in the Stored Proc Parameters list box.

1. Click OK.
 System saves the settings and returns you to the Field Properties form. Mapped values
 are displayed in the Parameters field. Tip: You can manually enter parameters in the
 Parameters field. See the F1 help for more information.)
