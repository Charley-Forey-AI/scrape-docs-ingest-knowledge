---
title: "Summary Billing Selection - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/time--material/spectrum-menus/data-entry-overview/summary-billing-selection/summary-billing-selection---field-descriptions"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/time--material/spectrum-menus/data-entry-overview/summary-billing-selection/summary-billing-selection---field-descriptions"
---

# Summary Billing Selection - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields
Descriptions

Activity type

Activity type
Click Select to display transactions that are currently selected, but have not yet been updated. Click Deselect to display transactions that are pending deselection, but have not yet been updated.
The selection made here determines the data that displays the
 Current Selections section of the screen
 (including the associated Billings-in-Progress
 Summary drill-down window.)

Processing status

Jobs currently selected
The total number of jobs included in the current selection displays.
Click the adjacent arrow to display the [Billings-in-Progress Summary window](/en/spectrum/spectrum/accounting/time--material/spectrum-menus/data-entry-overview/summary-billing-selection/billings-in-progress-summary-window) window to review and deselect transactions on a billing selection before it is processed.

Transaction count
The total number of transactions for the current selection displays.

Total transaction amount
The total amount for all of the transactions listed currently selected displays.

Selections

Job
This field defaults to <blank> and must be completed before continuing.
If you select a specific job number, both the number and description will be
 displayed; an Enter bill # field will be added. If
 you select ALL, advance directly from the Job field to the
 Division field.

Billing #
This field becomes available when you enter a specific job code above. If the billing number exceeds 999, the billing number will automatically be converted to the alpha equivalent (Example: A00 = 1000).

Division
Enter a job division.
Note: The SuperSelect options are conditional based on the
 Validate job division with G/L department checkbox selection on the Job Cost Installation > Properties tab.

Phase Cost type
Enter the Phase code. and Cost type you want to include.

From/through transaction date
Enter the dates from which transactions should be selected, or press Enter to leave these fields blank and the system will use the earliest available Time + Materials processing date as the earliest transaction date and through date.

From PR work date
Enter a date here if you want to only include payroll transactions. Job Cost, Accounts Payable, and other transaction types will not be included. If left blank, the system will use the earliest available T + M processing date as the earliest work date.
 The work date field is populated when T+M Payroll entries are made in
 Payroll. If you enter Payroll transactions in Time + Material > Transaction Entry, you can use the Modify Billing screen
 to enter a work date.

Through PR work date
Enter the work date through which transactions should be selected, or press
 F4 or double-click on this field to select a date
 from the Date Change window. Press
 Enter to accept the current Time + Materials
 processing date as the through work date.
This field is only used by Payroll Time + Material transactions. The work date
 field is populated when T+M Payroll entries are made in Payroll. If you
 enter Payroll transactions in Time + Material > Transaction Entry, you can use the Modify Billing screen
 to enter a work date. The Billing Selection is correct when you select
 Payroll transactions and a 'From work date' is entered.

Create billing for jobs with no activity?
Select this checkbox if you want the system to automatically generate a single billing record for jobs with no activity. The billing record will be assigned to the first phase of the job.

Default invoice dates

Invoice date G/L date
Enter the Invoice date and the G/L date for the invoice, or press
 Enter to accept the current Time + Materials
 processing dates.
In Accounts Receivable Installation, if the Invoice date must be in G/L
 period checkbox is selected, any date within the T+M minimum
 /maximum date range can be entered. However, the G/L date field entry must
 be in the same period.

Transaction types

Transaction types
Select which transaction type(s) to include on the report:

- Accounts Payable

- Equipment

- General Ledger

- Inventory

- Job Cost

- Payroll

The selection made here determines the data that displays in the
 Processing status section (including the
 associated Billings-in-Progress Summary drill-down
 window.)
