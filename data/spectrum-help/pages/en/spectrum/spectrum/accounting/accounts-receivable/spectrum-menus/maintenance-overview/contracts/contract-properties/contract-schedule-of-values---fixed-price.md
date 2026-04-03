---
title: "Contract Schedule of Values - Fixed Price | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/contracts/contract-properties/contract-schedule-of-values---fixed-price"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/contracts/contract-properties/contract-schedule-of-values---fixed-price"
---

# Contract Schedule of Values - Fixed Price

Use this screen to enter and/or modify specific billing items for fixed price contracts. If the Use unit pricing? checkbox was selected on the Main screen, the [Contract Schedule of Values - Unit Price](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/contracts/contract-properties/contract-schedule-of-values---unit-price) will open instead.
Field
Description

Billing item
Enter the billing item code, or press F4 to select from a list of available codes. A billing item description may also be entered.
If a code was selected from Set Up Standard Fixed Billing Items, the item description will display. Otherwise, enter the item description.

Taxable
The software automatically selects this checkbox as a system default. Press Enter to accept the software default. The taxable flag in the detail portion of the screen defaults from the taxable flag in the upper portion of the screen.

Orig contract
The original contract amount will be calculated as the sum of the unit price multiplied by the quantity. Press Enter to accept this default, or enter the dollar amount contracted for this item.

Change orders
The change order amount for this item displays, if applicable. Otherwise, this field will be blank.

Rev contract
The revised contract amount will be calculated as the sum of the contract amount and the change order amount. Press Enter to accept this default, or enter the revised dollar amount for this item.

Proj revenue
Enter the projected revenue amount for this billing item.

Memo
Enter a note pertaining to this billing item. Any notes entered here will then will print on the A/R Draw Request (in the memo column) and on the Draw Request Billing Worksheet. Entry in this field is optional.

Cost center
If cost centers are set to Yes or Pending in the current company, enter a cost center for this billing item, if applicable. The cost center description displays to the right of this field.
Spectrum validates that you have permission to assign a cost center to the bill item, and if the cost center is not present in your assigned scheme the cost center cannot be assigned.

G/L account
Enter the General Ledger sales account number for this billing item. The account description will display to the right of this field.
 If the G/L status code you select has a status of Not used, you cannot proceed using this code. If the G/L status code you select has a status of Inactive, a warning will display.

Schedule totals
Totals for original, changes, revised contracts, and projected changes display in the upper right hand corner of this screen.
If the Original amount is not equal to the Original contract amount recorded on the Contract Main Properties screen, an out of balance warning message will appear on top of the grid and when you exit this screen. This will give you the option to set the original contract amount to distributed amount, or return to grid detail for editing.
