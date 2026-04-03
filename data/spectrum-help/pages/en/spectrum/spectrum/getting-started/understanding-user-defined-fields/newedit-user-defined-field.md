---
title: "New/Edit User-Defined Field | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/getting-started/understanding-user-defined-fields/newedit-user-defined-field"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/getting-started/understanding-user-defined-fields/newedit-user-defined-field"
---

# New/Edit User-Defined Field

Use this window to create new, or edit existing, user-defined fields for use throughout the current module.
Fields/Buttons
Descriptions

Type
From the drop-down list:

- Select Alpha if this will be a text field.

- Select Date if this field will contain numerical dates.

- Select Numeric if this field will contain dollar amounts or numeric figures.

Prompt
Enter the field label (for example, Due date).
Company
Select a company code to associate it with a user-defined field. This field is enabled when the Allow setup of company-specific fields checkbox is selected in the module's user-defined Installation screen.

Mask
 Enter the user-defined field's alignment mask (only applicable for Amount  fields).
When a report is initially created, the software suggests the display code, but the default may be overwritten. If the field length is changed after creating the report, the corresponding display code must also be changed.

Validated?
Select this checkbox if the selected user-defined field has validation codes; this checkbox is only available for Alpha type user-defined fields. If you select this checkbox, the User-Defined Fields Validation window displays when you click Close. The User-Defined Fields Validation window is available to add and edit valid field values and their descriptions. If an alpha user-defined field has validation codes, only specified values are allowed for that field; for example, a user-defined field may require a Yes or No entry. If an alpha user-defined field does not require a limited value (for example, an emergency contact's name), that field should not have validation codes.

Status
Assign a status to the user-defined field. The status assignment will be used to determine which fields display on the main User-Defined Fields screen. Users who are permitted to edit user-defined fields will see all fields, while other users will only see fields with an Active status.

Related information

- [UDF Values Input](/en/spectrum/spectrum/getting-started/understanding-user-defined-fields/udf-values-input)
