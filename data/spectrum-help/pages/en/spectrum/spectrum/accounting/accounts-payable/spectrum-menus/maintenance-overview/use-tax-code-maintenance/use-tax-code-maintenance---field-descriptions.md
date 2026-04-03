---
title: "Use Tax Code Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/use-tax-code-maintenance/use-tax-code-maintenance---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/use-tax-code-maintenance/use-tax-code-maintenance---field-descriptions"
---

# Use Tax Code Maintenance - Field Descriptions

This table describes the fields found on the Use Tax Code windows accessed when the New, Edit, or View buttons are clicked.
Fields/Buttons
Descriptions

Use tax code
Enter the use tax code (up to 15 alpha-numeric characters), or use the drop-down list to select a code. If you are editing the details of a record, no changes can be made to this field.

Description
This field will automatically default to the selected use tax code description if the use tax code was entered first. Otherwise, enter an alternate description.

Current tax rate
This fields defaults to the corresponding percentage if the use tax code was entered first; otherwise, enter a percentage.

G/L account code
 Enter the General Ledger account number or use the drop-down list to select a code.
Note: G/L codes with a status of Not used may not be selected. In
 addition, the G/L code selected must be a non-direct cost code.

Tax type

- A sales tax code will add the sales tax amount to the vendor invoice; this amount will be posted to the invoice total amount.

- A use tax code will accrue use tax to a separate G/L liability account and will not add the tax amount to the vendor invoice.

In both cases, if the line item is charged to a job, the tax amount will post to the same job, phase, and cost type. [About Vendors](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors) prompts for the vendor's default tax code.

Next tax rate
The next scheduled tax percent displays from the [Rate History window](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/use-tax-code-maintenance/rate-history-window) window.

Effective as of
The date that the next scheduled tax percent will take effect displays from the [Rate History window](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/use-tax-code-maintenance/rate-history-window) window.

Comments
Up to one line of information about the next scheduled tax percent displays from the [Rate History window](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/use-tax-code-maintenance/rate-history-window) window.

Rates button
Click this button to open the Rate History window.
