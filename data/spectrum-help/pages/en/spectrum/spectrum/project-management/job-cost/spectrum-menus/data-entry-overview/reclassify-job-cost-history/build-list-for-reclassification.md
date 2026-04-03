---
title: "Build List for Reclassification | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/reclassify-job-cost-history/build-list-for-reclassification"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/reclassify-job-cost-history/build-list-for-reclassification"
---

# Build List for Reclassification

Use this window to define information that will display in the [Reclassify Job Cost History](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/reclassify-job-cost-history) screen.
Fields
Descriptions

Selections

Transaction type
Select from one of the following transaction types:
Note: A transaction type will not display if you do not have the corresponding module.

Job
Phase
Cost type
Enter a job number, phase number, and cost type.
Validation occurs each time a phase code is added; however, validation is not performed on pre-existing Job Cost entries . Entry is prevented when the phase status is set to Complete; a warning message displays if the phases' status is set to Inactive.

Reference #
You can accept the default of all or enter a specific transaction reference:
AP = Vendor code
PR = Employee code
IC = Item code
EQ = Equipment code

Reference #2
AP = Invoice number
PR = Check
IC= Warehouse

From date To date
Enter the first date and last dates to select, or press Enter to accept the defaults of the minimum and current Job Cost processing dates.

Custom group
If cost centers are set to 'Yes' in the current company, specify a custom cost group in this field, or press Enter to include ALL.

Reset debit cost center to current default?
If this option is selected, the utility will automatically flag all selected history transactions where the 'history' cost center is different than the current default cost center assigned to the job or phase.

Defaults

New batch code
Enter or search for a batch code. This batch code will be assigned to
 transactions that will be created in [Job Cost Transaction Entry](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/job-cost-transaction-entry).

Debit G/L account
Enter the G/L code to use as a default if the cost type G/L is blank. Entry is prevented if the account's status is set to Not used.
Note: This must be a direct job cost code.

Credit G/L account
Enter the credit G/L code to use as a default. Entry is prevented if the account's status is set to Not used.
Note: This cannot be a direct job cost code.

Credit custom cc
If cost centers are set to 'Yes' in the current company, specify a custom cost center to use as a default.

Related information

- [Job Cost Transaction Entry: JC - Job Cost](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/job-cost-transaction-entry/job-cost-transaction-entry-jc---job-cost)

- [Reclassify Job Cost History: Transaction Type AP - Vendor](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/reclassify-job-cost-history/reclassify-job-cost-history-transaction-type-ap---vendor)

- [Job Cost Transaction Entry: EQ - Equipment](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/job-cost-transaction-entry/job-cost-transaction-entry-eq---equipment)

- [Job Cost Transaction Entry: IC - Inventory](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/job-cost-transaction-entry/job-cost-transaction-entry-ic---inventory)

- [Reclassify Job Cost History: Transaction Type PO - Accrual](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/reclassify-job-cost-history/reclassify-job-cost-history-transaction-type-po---accrual)

- [Job Cost Transaction Entry: PR - Employee](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/job-cost-transaction-entry/job-cost-transaction-entry-pr---employee)
