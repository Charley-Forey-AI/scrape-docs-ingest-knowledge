---
title: "Field Definitions: CM Clear Entries Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/cash-management/processing/reconciliation/about-the-cm-clear-entries-form/field-definitions-cm-clear-entries-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/cash-management/processing/reconciliation/about-the-cm-clear-entries-form/field-definitions-cm-clear-entries-form"
---

# Field Definitions: CM Clear Entries Form

The following is a list of field descriptions for the CM Clear Entries form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## CM Account

CM Account field on the CM Clear Entries form
Enter a valid CM Account number from which to clear entries. There must be an open statement for the CM account. The current statement date (as set up in CM Statement Control) displays in the Statement Date field below.

Related information

- [Fix Cleared Amount Discrepancies](/en/vista/vista/accounting/cash-management/processing/reconciliation/fix-cleared-amount-discrepancies)

- [Display Outstanding or Cleared Items](/en/vista/vista/accounting/cash-management/processing/reconciliation/display-outstanding-or-cleared-items)

- [About the CM Clear Entries Form](/en/vista/vista/accounting/cash-management/processing/reconciliation/about-the-cm-clear-entries-form)

## Display Through Date

Display Through Date field on the CM Clear Entries form
Specify the date through which to display transactions for this CM account. Initially defaults to the current statement date. All transactions (checks, EFTs, deposits, adjustments, and/or transfers) posted on or before this date will display in the grid below.
Note: Transactions displayed will depend on the items you selected for display in the ‘Check Items to Display’ selection box to the right of the grid.

Related information

- [Fix Cleared Amount Discrepancies](/en/vista/vista/accounting/cash-management/processing/reconciliation/fix-cleared-amount-discrepancies)

- [Display Outstanding or Cleared Items](/en/vista/vista/accounting/cash-management/processing/reconciliation/display-outstanding-or-cleared-items)

- [About the CM Clear Entries Form](/en/vista/vista/accounting/cash-management/processing/reconciliation/about-the-cm-clear-entries-form)

## Check Items to Display

Check Items to Display section on the CM Clear Entries form
Select the checkbox for each of the items you want displayed in the grid. You must select at least one transaction type and one entry type, regardless of whether you are selecting items to display in the grid or whether you will be using the Initialize feature.
Transaction Types:

- Checks/Electronic Payments

- Deposits

- Adjustments

- Transfers

Entry Types:

- Outstanding Entries

- Cleared Entries

Related information

- [Display Outstanding or Cleared Items](/en/vista/vista/accounting/cash-management/processing/reconciliation/display-outstanding-or-cleared-items)

- [About the CM Clear Entries Form](/en/vista/vista/accounting/cash-management/processing/reconciliation/about-the-cm-clear-entries-form)

## Default Date Cleared

Default Date Cleared field on the CM Clear Entries form
Enter the date cleared for all transactions being reconciled. This will default to the statement date that is normally used if clearing all items on a statement. However, if clearing items daily, this may be the actual date cleared.

Related information

- [Display Outstanding or Cleared Items](/en/vista/vista/accounting/cash-management/processing/reconciliation/display-outstanding-or-cleared-items)

- [About the CM Clear Entries Form](/en/vista/vista/accounting/cash-management/processing/reconciliation/about-the-cm-clear-entries-form)

## Cleared

Cleared checkbox on the CM Clear Entries form
The system will automatically select this checkbox for all entries cleared through Initialization. If clearing entries manually, select this checkbox to indicate this entry was cleared.
Do not select this checkbox if this entry is outstanding (was not cleared). If you need to reset all cleared entries to “outstanding”, you can use the Undo button (bottom right of form) to reset all entries at once.

Related information

- [Display Outstanding or Cleared Items](/en/vista/vista/accounting/cash-management/processing/reconciliation/display-outstanding-or-cleared-items)

- [About the CM Clear Entries Form](/en/vista/vista/accounting/cash-management/processing/reconciliation/about-the-cm-clear-entries-form)

## Date Cleared

Date Cleared field on the CM Clear Entries form
If entries were cleared through initialization, this field defaults the Statement Date. If entries are cleared manually, this field defaults the Default Date Cleared specified above. Date may be overridden.
This field is used as the date cleared for entries in the grid. If you clear entries monthly (when you receive your statement), this will most likely be the same as the statement date, and all entries will show the one date as the date cleared. However, if you receive information more frequently from the bank of items cleared, such as daily, then this may be the actual date cleared.

Related information

- [Display Outstanding or Cleared Items](/en/vista/vista/accounting/cash-management/processing/reconciliation/display-outstanding-or-cleared-items)

- [About the CM Clear Entries Form](/en/vista/vista/accounting/cash-management/processing/reconciliation/about-the-cm-clear-entries-form)

## Cleared Amt

Cleared Amt field on the CM Clear Entries form
This field automatically defaults the total Amount of the transaction. If the actual amount cleared by the bank differs from the default, enter the cleared amount. The line’s color will change to Yellow to indicate that there is a discrepancy between the transaction’s amount and the cleared amount. These discrepancies can be reviewed by printing the CM Differences report.
Note: If you clear a voided check (those with Void column set to Y), the cleared amount will default to 0.00 since no true amount is being cleared.

Related information

- [Display Outstanding or Cleared Items](/en/vista/vista/accounting/cash-management/processing/reconciliation/display-outstanding-or-cleared-items)

- [Fix Cleared Amount Discrepancies](/en/vista/vista/accounting/cash-management/processing/reconciliation/fix-cleared-amount-discrepancies)

- [About the CM Clear Entries Form](/en/vista/vista/accounting/cash-management/processing/reconciliation/about-the-cm-clear-entries-form)
