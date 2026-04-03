---
title: "New User-Defined Field window | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/job-user-defined-fields-maintenance/new-user-defined-field-window"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/job-user-defined-fields-maintenance/new-user-defined-field-window"
---

# New User-Defined Field window

Use this window to add new Job Cost user-defined fields.
FieldDescription
TypeUse the drop-down menu to select the field type (Alpha, Date, or Numeric). Select Alpha if this will be a text field. Select Date if this field will contain numerical dates. Select Numeric if this field will contain dollar amounts or numeric figures.
PromptEnter the field title (for example, DUE DATE).
CompanyEnter the code for the company that will use this user-defined field, or press F4 or double-click on this field to select from a list of available company codes.
MaskEnter the user-defined field's alignment mask using either numbers or a string of letter z, for example 999999 or ZZZZZZ (only applicable for Amount fields).
When a report is initially created, the system suggests the display code, but the default may be overwritten. If the field length is changed after creating the report, the corresponding display code must also be changed.

Validated?Select this checkbox if the selected user-defined field has validation codes. If this user-defined field does not have validation codes, leave this checkbox clear. This checkbox is only available for Alpha user-defined fields.
If you select this checkbox, the [User-Defined Fields Validation window](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/job-user-defined-fields-maintenance/user-defined-fields-validation-window) window displays when you click OK. Use this window to add or edit valid field values and their descriptions. Validation is available only alpha user-defined fields that have validation codes.
If an alpha user-defined field has validation codes, only specified values are allowed for that field; for example, a user-defined field may require a Yes,No, or blank value. If an alpha user-defined field does not require a limited value (for example, an emergency contact's name), that field should not have validation codes.[User-Defined Fields Validation window](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/job-user-defined-fields-maintenance/user-defined-fields-validation-window)

StatusSelect the user-defined field's status: Active or Not used.
