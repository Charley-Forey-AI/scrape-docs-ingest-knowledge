---
title: "New/Edit Contract - Unit Price Contract Detail | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/newedit-contract---unit-price-contract-detail"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/newedit-contract---unit-price-contract-detail"
---

# New/Edit Contract - Unit Price Contract Detail

Use this tab to enter and/or modify specific billing items.
 If the contract for this job does specify the use of unit pricing (in the Properties window of
 Contracts), then the Contract Detail window displays fields specifically for unit priced
 billing items.
For fixed price contracts, the [New/Edit Contract - Fixed Price Contract Detail](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/newedit-contract---fixed-price-contract-detail) tab will open
 instead.
When adding new billing items for unit price jobs, the pricing logic defaults the special price first by customer/job, then customer only (if the job field is left blank) as the second priority, and finally the standard company pricing (if the customer field is left blank) as the last resort. This pricing default is used only when setting up new billing items to be billed. The billing item lookup windows also reflect this customer/job option.
After a job has been set up, it is recommended that billing items be entered in the Contracts screen before phases are set up in the Phases screen.
Important: If no information appears in the detail lines after the initial fields have been completed, do not change the job contract amount in the Jobs screen which will not be reset. If there are detail lines, the software will automatically set the original contract to the sum of the detail.
Field
Description

Billing group/item
Billing Group/item serve two purposes; they are used for draw requests and for the Billing Item Analysis Report.
Enter a code for this billing item. The cursor will move down one line. If a code was selected from Set Up Standard Unit Billing Items, the item description will display. Otherwise, enter the item description. When adding a new code, click the drill-down button to view the bill groups already established for the draw request.
Double-click on the Description field or press F4 to enter an additional description. The expanded description will print on the draw request, draw request worksheet and on the Contract File Listing report. For contracts that require additional room for billing item numbers, enter the expanded billing item number in the Description field and then press F4 to enter the description.

G/L account
Enter the General Ledger sales account number for this billing item. If the G/L status code you select has a status of Not used, you cannot proceed using this code. If the G/L status code you select has a status of Inactive, a warning will display.

Tx
Select this checkbox if the item is taxable.

Um
Select the unit of measure for the selected item.

Unit price
This field will be skipped if the unit of measure is Lump Sum (LS). Otherwise, the unit price for this specific item displays. Press Enter to accept the unit price default. Defaults for this field are set up during Accounts Receivable Installation.
Double-click on this field or press F4 to open the Display Mask window. Use this window to override the default display mask settings.

Contract quantity
Enter the contract quantity for this item, or press Enter to accept the software default.
Double-click on this field or press F4 to open the Display Mask window. Use this window to override the default display mask settings.

C.o.
The change order quantity for this billing item displays.

Rev.
The revised quantity for this billing item displays.

Contract amount
The original contract amount will be calculated as the product of the two previous fields; that is, the unit price multiplied by the quantity. Press Enter to accept this default, or enter the dollar amount contracted for this item.

Projected/job-to-date Quantity
Initially, the "original quantity" will default. Enter the projected quantity for this item.

Projected/job-to-date Amount
Enter the contract amount for this billing item.

Memo
Enter a note pertaining to this billing item. Any notes entered here will then will print on the A/R Draw Request (in the memo column) and on the Draw Request Billing Worksheet. Entry in this field is optional.

Jtd
The job to date quantity displays.

Related information

- [Example: Setting Up Bill Groups](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/example-setting-up-bill-groups)
