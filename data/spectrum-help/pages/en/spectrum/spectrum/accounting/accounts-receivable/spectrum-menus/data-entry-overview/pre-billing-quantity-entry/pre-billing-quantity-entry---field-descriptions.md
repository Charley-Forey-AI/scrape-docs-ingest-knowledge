---
title: "Pre-Billing Quantity Entry - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/pre-billing-quantity-entry/pre-billing-quantity-entry---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/pre-billing-quantity-entry/pre-billing-quantity-entry---field-descriptions"
---

# Pre-Billing Quantity Entry - Field Descriptions

Use this table for reference when completing the fields on this screen.
Field
Description

Job
Enter a valid job number.

Customer
Enter a valid customer code for this job. There must be a contract already set up for the job and customer specified. If the customer code's status is set to Not used, then to entry is allowed.

Batch code
Enter the batch code. The batch code window shows all outstanding batches with the batch code, job customer, and number of transactions.

Detail

Group
Enter the unit price billing group.

Bill item
Enter the billing item code. If a new billing item code is entered, the record is added to the billing file.
 If you enter a billing item that is not set up for this contract, a window opens to set up billing item details for the contract.

Description
The description field displays the description previously recorded in Contracts.

Um
The unit of measure field displays the unit of measure previously recorded in the Contracts.

Date
Enter a date for this quantity entry or press Enter to accept the default of the current A/R processing date. This transaction file allows multiple entries for the same billing item by recording different dates.

Type
Enter E for
 engineering or A
 for actual. The software defaults to Actual or Engineering based on the
 default entry type selected on the Accounts Receivable Installation > Draw Request tab.

- If Actual is selected, enter the Actual period quantity.

- If Engineering is selected, enter the Engineering period quantity and amount.

Actual period qty
Enter the actual period quantity:

- If Job-to-date
 method was specified on the Accounts Receivable Installation > Draw Request tab, the software defaults to the last chronological
 quantity entered for a job-to-date total.

- If This period
 method was specified on the Accounts Receivable Installation > Draw Request tab, the software adds all entries with the same
 billing item and batch code.

Engineering period qty
Enter the engineering period quantity:

- If This period
 method was specified on the Accounts Receivable Installation > Draw Request tab, the software adds all entries with the same
 billing item and batch code.

- If Job-to-date
 method was specified on the Accounts Receivable Installation > Draw Request tab, the software defaults to the last chronological
 quantity entered for a job-to-date total.

Bid quantity
The bid quantity will default from the contract quantity specified for the billing item.

Bid $ amount
The bid amount is the sum of the actual period quantity entered and the bid quantity.
