---
title: "Edit Custom Fields | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/custom-formsfields/edit-custom-fields"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/custom-formsfields/edit-custom-fields"
---

# Edit Custom Fields

You can use VA Custom Fields Wizard to edit existing custom fields.
Editing capabilities are somewhat flexible, but due to variety of ways to create a field, there are some changes that you cannot make.
The following list outlines the majority of limitations/restrictions:

- Description – You can change the description for any custom field. The description is the 'label' that displays on the form to identify the field. The only restriction to this type of change is that you are limited to 30-characters.

- Datatype – If you previously assigned a datatype to the custom field, you cannot change the assignment. This prevents fields from changing to a new datatype that may not be compatible with the previous datatype. For example, changing a text field to a date field would not work due to the inability to convert alphanumeric values to date values.

- Input Mask – You can define input masks only for numeric fields, so you can edit the input mask for these types of fields only. However, if you assign the field a datatype, the system disables the input mask field.  You can increase the 'before and after decimal' allowance, but only the decimal precision ('after decimal' allowance) can be decreased. Decreasing the decimal precision causes existing data to be rounded based on the new decimal precision. For example, if you have a format of ###,##0.00000, with existing data of 2,450.06582, changing the format to ###,##0.000 would convert the existing data to 2,450.066.

- Input Length – You cannot change the input length for fields assigned a datatype, nor can you decrease an input's length, since decreasing the length would cause existing data to be truncated. However, you can increase the length either manually or by assigning a datatype with a larger input allowance. For example, if the field is a text field with an input length of 20, assigning a 'bDesc' datatype increases the input length to 30 characters.  There is one exception to the restriction on decreasing the input length, and that is if you are decreasing the decimal precision for an input mask (i.e. the number of characters after the decimal point), which would require having to also change the input length. However, this type of change is allowed and existing data is rounded accordingly.

Note: When editing custom fields, there are situations where multiple forms exist that share a table. For example, if you add a field to JC Jobs, you also have the option to add the field to PM Projects. When editing a field that exists on multiple forms, the system updates all instances of the field.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

- [Delete Custom Fields](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/delete-custom-fields)

- [Set Data Level Security for Custom Fields](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/set-data-level-security-for-custom-fields)
