---
title: "Add an Accounts Receivable User-Defined Field | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/customer-user-defined-fields-maintenance/add-an-accounts-receivable-user-defined-field"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/customer-user-defined-fields-maintenance/add-an-accounts-receivable-user-defined-field"
---

# Add an Accounts Receivable User-Defined Field

Use this table for reference when adding an Accounts Receivable user-defined field.
Field
Description

Company
Enter a company code for the selected user-defined field, or press Enter to accept the current company code.
When editing an existing user-defined field, the Company field will appear below the Mask field.

Type
Use the drop-down menu to select the field type (Alpha, Date or Numeric).
Select Alpha if this will be a text field. Select Date if this field will contain numerical dates. Select Numeric if this field will contain dollar amounts or numeric figures.

Prompt
Add or edit the title for this field (for example, DUE DATE).

Validated?
Select this checkbox if the selected user-defined field has validation codes. If this user-defined field does not have validation codes, leave this checkbox clear. This checkbox is only available for Alpha user-defined fields.
If you select this checkbox, the User-Defined Fields Validation window displays when you click OK. Use this window to add or edit valid field values and their descriptions. Validation is available only alpha user-defined fields that have validation codes. If an alpha user-defined field has validation codes, only specified values are allowed for that field; for example, a user-defined field may require a Yes, No, or blank value. If an alpha user-defined field does not require a limited value (for example, an emergency contact's name), that field should not have validation codes.

Mask
The user-defined field mask displays. A mask must be entered for numeric user-defined fields. When a report is initially created, the software suggests the display code, which can be overwritten. If the field length is changed after creating the report, the corresponding display code must also be changed. See the table below for appropriate codes.

Status
Select the status for this user-defined field: Active or Not used.
