---
title: "Value Added Tax Code Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/value-added-tax-code-maintenance/value-added-tax-code-maintenance---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/value-added-tax-code-maintenance/value-added-tax-code-maintenance---field-descriptions"
---

# Value Added Tax Code Maintenance - Field Descriptions

Refer to the table below when completing the fields in the
 New or Edit Value Added Tax Code window.
Fields
Descriptions

Value added tax code
Enter a unique tax code.

Description
(Optional) Enter a description of the tax code. Text entered here will display
 on the main screen and in the Search Value Added Tax Codes window.

Tax percent
Enter the tax percent value, up to 99.9999.

Invoice text
(Optional) Enter the text that will display on A/R invoice forms and other billing forms. For example, you might want to enter the "Registrant Number" or other required information.

G/L accounts

Customer current tax payable
Customer retention tax
 payable
Vendor current input tax
 credit
Vendor retention input tax
 credit

- Select a non-direct cost G/L account code for each of these fields.

- A warning displays if you select an Inactive account, but you will be allowed to continue.

- The G/L account description displays after an account is selected.

- When Enterprise Installation option for Cost centers is set to Yes or Pending in this
 company, then when adding or changing a tax code, the system will
 allow entry of a G/L account code only if the operator entering the
 G/L account has permission to assign that code. The system compares
 the G/L account's list of shared cost centers with cost centers in
 the operator's assigned scheme, and if there are no common cost
 centers, then that G/L account cannot be assigned.

- Once a G/L account code has been assigned to a tax code (by an authorized operator), then that G/L account will be used by all operators for processing involving that tax code.

View example of completed window:
