---
title: "About the DDFI Field Map Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/field-validation/about-the-ddfi-field-map-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/field-validation/about-the-ddfi-field-map-form"
---

# About the DDFI Field Map Form

You can use the DDFI Field Map form to map stored procedure parameters for custom
 validation to corresponding form fields or fixed values.
You can only access this form by entering a
 validation procedure on the System Overrides tab (Validation section) of the Field
 Properties (F3) form and then clicking the Link button (to the right of the procedure
 name).
To ensure that the correct parameters are passed to the stored procedure during validation, you will need to map each stored procedure parameter to a corresponding field on the form or a fixed value.

## Mapping Stored Procedure Parameters to Form Fields

Using the list boxes on the form, you can
 quickly and easily map each stored procedure parameter. The Stored Proc Parameters list
 box displays the parameters available for mapping based on information needed for the
 stored procedure. The Form Fields list box contains all fields that reside on the active
 form. The Stored Proc – Field Map list box displays the parameters that you have
 successfully mapped.
During the mapping process, the system
 automatically selects each parameter in its listed order and will not allow selection of
 another parameter until you have successfully mapped the selected parameter. This
 ensures that parameters are passed to the validation procedure in the correct order.
To map a parameter, select the field you
 are mapping to from the Form Fields list box (this should be a field that corresponds to
 the selected parameter). Then click the Map button (bottom of form). The system moves
 the parameter to the Stored Proc – Field Map list box, along with its field designation.
Once you have finished mapping the
 parameters, click OK to save the selections. The system returns you to the Field
 Properties form and displays the mapped values in the Parameters field.

## Assigning Fixed Values to Stored Procedure Parameters

To always pass a specific value to the
 stored procedure for a selected parameter, do not map the parameter to a form field.
 Instead, enter the value in the Fixed Value field and click the Map button. When you
 return to the Field Properties form, the fixed value displays in the Parameters field.
 Because this is a constant value, the system places it in single quotes.

## Remove Mapping for a Stored Procedure Parameter

The Remove button is used to remove the
 mapping for a selected parameter. Just select the parameter in the Stored Proc – Field
 Map list box and click the Remove button. This will clear the mapping and move the
 parameter back to the Stored Proc Parameters list box. You can either save the change or
 remap the parameter to a different form field.
