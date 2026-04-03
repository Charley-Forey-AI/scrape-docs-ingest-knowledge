---
title: "Detail Billing Selection - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/time--material/spectrum-menus/data-entry-overview/detail-billing-selection/detail-billing-selection---field-descriptions"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/time--material/spectrum-menus/data-entry-overview/detail-billing-selection/detail-billing-selection---field-descriptions"
---

# Detail Billing Selection - Field Descriptions

A reference for completing the fields on this screen.

## Header and Grid

Field/ButtonDescription
Selections Opens a Selections window. See field descriptions in the table below.
SwitchOpens a different job.
JobEnter the job number for which you are selecting or deselecting billing transactions.
CustomerThe customer name from the Job Cost > Job Main Properties screen.
Billing #Enter the billing number. You can enter existing unposted billing or the next new one. Leave this field blank to view unselected transactions for the specified job. If the billing number exceeds 999, the billing number will automatically be converted to the alpha equivalent (Example: A00 = 1000).
Select
Select All
Deselect
Deselect All
Delete
Use these buttons as needed to select the records you want.
If you have security authorization, you can delete transactions that should never be billed.

Selected for billing (right-hand side)
Transaction countThe number of transactions completed for the corresponding billing number. Unselected or deleted rows are not included.
Total transaction amountThe total amount for all of the transactions listed currently selected.
Status button
Choose whether to display Selected, Unselected, or both transactions in the grid.

The status is Selected when:

- The Billing # had been associated with this transaction when the list box was compiled.

- Highlight this row and click the Select button.

The status is Unselected when:

- There is no Billing # associated with this transaction when the grid was compiled.

- Highlight this row and click the Deselect button.Note: When the grid was compiled, any billing transactions that were already selected for another Billing # in progress have been excluded from this list.

DescriptionThe name for the transaction line.
Hours/qtyThe number of hours or quantity for the transaction line.
Pay typeThe pay type for the transaction line: Regular, Overtime, or Double.
Billing rateThe Billing rate for the transaction line.
ExtensionThe billing extension (total bill less Markup).
MarkupThe Markup and total bill amount.
Bill amountThe dollar total for each line (Extension plus Markup).
Taxable?Yes or No depending whether or not the item is taxable.
MessageAny messages entered for the billing transaction.
Code
Reference
P.O.#
The item's code, reference number, and purchase order number.
Work dateNote: This field is only used by Payroll Time + Material transactions.
The correct work date is calculated from the period end date in the Payroll module.
The work date field is populated when T+M Payroll entries are made in Payroll. If you enter Payroll transactions in Time + Material > Transaction Entry, you can use the Modify T+M Billing > Transaction Detail tab to enter a work date.

Inv/check date
Billing code
The check date and billing code.

## Selections window

This window opens when you click the Selections button.
This tool makes it easier to manage the billing process by limiting which bills appear in the grid, based on your selections.
FieldDescription
PhaseThe Phase code and description to be included on the billing. The code can be up to 20 characters.
Cost typeThe Cost type for the transaction line.
From/to transaction dateThe transaction date range you want to narrow results to.
From/to work dateThe date range of when the work was performed. See the definition for Work date in the table above.
Transaction typesThe transaction type, if you want to limit results to less than all types.
