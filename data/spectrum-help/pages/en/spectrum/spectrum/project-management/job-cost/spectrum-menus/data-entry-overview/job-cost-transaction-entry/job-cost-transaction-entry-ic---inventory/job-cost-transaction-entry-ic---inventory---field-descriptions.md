---
title: "Job Cost Transaction Entry: IC - Inventory - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/job-cost-transaction-entry/job-cost-transaction-entry-ic---inventory/job-cost-transaction-entry-ic---inventory---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/job-cost-transaction-entry/job-cost-transaction-entry-ic---inventory/job-cost-transaction-entry-ic---inventory---field-descriptions"
---

# Job Cost Transaction Entry: IC - Inventory - Field Descriptions

Use the table below for reference when completing fields on this screen.
Fields
Descriptions

Item code
Description
For standard stock items, enter or search for an inventory item code. If the item status is set to 'Not used,' entry will be disallowed.
For stock items, the item code must have been previously defined in Inventory Item File Maintenance.
For non-stock items, enter an exclamation point (!) followed by a short item description.

Job
Enter or search for a job number, indicating the job to which the entered item should be charged.
The job number entered here should have been previously defined in Jobs; however, a new job may be entered.

Phase
Enter or search for a phase code for the job cost transaction. This job/phase combination should have been previously defined in Job Phases; however, it may be entered here.
Note: Entry is prevented when the phase status is set to
 Complete; a
 warning message displays if the phases' status is set to Inactive.
If this is a sub-job transaction set up on a master job, double-click on this field to search phases for the sub-job. This will allow you to easily select a phase set up on a master job, but not present on the sub-job. Spectrum will add a new phase to the sub job if the current job is a sub-job of a valid master job, the phase lengths of both jobs match, and the Phase + Cost type combination for the current job is valid and not 'Complete'.

Ct
Enter or search for a cost type for this line transaction. The phase description and cost type name will display under their respective codes.

Warehouse
For standard stock items, the warehouse defaults based on the previous line if a warehouse is specified. Otherwise, it defaults based on the Inventory Control Installation specifications for the Default warehouse field. Warehouse codes may be up to 10 characters long.
Non-stock items cannot be entered in this field.

Quantity
Enter the quantity of the inventory item used.

Total cost
For standard stock items, Spectrum multiplies the entered quantity by the price in the item file. Press Enter to accept the default, or enter the desired "total cost" for this line transaction.
If an override exists at the warehouse level, calculate the standard cost default using that value. If the standard cost is blank or zero, the standard cost from Item Main Properties will default instead.
For non-stock items, enter the total cost for this line transaction.

G/L debit
The debit account entered here must have the Job cost option selected in the Direct cost field of G/L Master File Maintenance.
Note: Entry is prevented if the account's status is set to
 Not
 used.

G/L credit
Enter or search for the General Ledger account to be credited. The credit account must have the No direct cost option selected in the Direct cost field of the G/L Master File Maintenance screen.
Note: Entry is prevented if the account's status is set to
 Not
 used.

Job name
Phase description
Warehouse name
The name of the job, phase description, and warehouse display.
