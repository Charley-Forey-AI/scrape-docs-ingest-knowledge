---
title: "Field Definitions: DDFI Field Map Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/user-interface-guide/system-forms/field-validation/about-the-ddfi-field-map-form/field-definitions-ddfi-field-map-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/user-interface-guide/system-forms/field-validation/about-the-ddfi-field-map-form/field-definitions-ddfi-field-map-form"
---

# Field Definitions: DDFI Field Map Form

The following is a list of field descriptions for the DDFI
 Field Map form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Fixed Value

Enter the fixed value to pass to the validation procedure for the selected stored procedure parameter. Then click the Map button. This moves the selected parameter to the Stored Proc – Field Map list box, along with this value.
Once you complete the mapping process, click OK to update mapped values to the Parameters field in the Field Properties (F3) form.
Note: Fixed values are enclosed in single quotes once updated to the Parameters field.

## Form Fields

This box displays all fields on the active form. If mapping a parameter to a form field, select the field from this list and click the Map button. This moves the parameter and field designation to the Stored Proc – Field Map list box.
Note: To pass the active company to the stored procedure during validation, map the selected parameter to the ‘(Company)’ field in the Form Fields list. Active company designations show as ‘-1’ in the Parameters field (F3 window).
Once you complete the mapping process, click OK to update mapped values to the Parameters field in the Field Properties (F3) form.
Note: When mapping fields, only the field sequence number (shown to the left of the field in the Form Fields list) is updated to the Parameters field.

## Stored Proc - Field Map

This box displays mapped parameters. Parameters are moved to this box once you specify the field or fixed value to map to and click the Map button.
To remove the mapping for a parameter, select the parameter and click the Remove button.
Once you complete the mapping process, click OK to update mapped values to the Parameters field in the Field Properties (F3) form.

## Stored Proc Parameters

This box displays the parameters from the validation stored procedure, listed in the order they are referenced by the stored procedure. The values for these parameters must be passed to the stored procedure in the order of reference and therefore mapped in that same order. The system automatically selects each parameter in the listed order and will not allow selection of another parameter until you have successfully mapped the selected parameter.
To map a parameter to a field, select the corresponding field from the Form Fields list box and click the Map button. This moves the parameter and field designation to the Stored Proc – Field Map list box.
To map a parameter to a fixed value, enter the value in the Fixed Value field and click the Map button. This moves the parameter and fixed value designation to the Stored Proc – Field Map list box.
Once you complete the mapping process, click OK to update mapped values to the Parameters field in the Field Properties (F3) form.
