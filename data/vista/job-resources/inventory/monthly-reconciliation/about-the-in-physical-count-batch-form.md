---
title: "About the IN Physical Count Batch Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/monthly-reconciliation/about-the-in-physical-count-batch-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/monthly-reconciliation/about-the-in-physical-count-batch-form"
---

# About the IN Physical Count Batch Form

Use this form to add entries from the physical count worksheet to an adjustment batch.

1. Enter the physical
 counts using the [IN Physical Count Worksheet ](/en/vista/vista/job-resources/inventory/monthly-reconciliation/in-physical-count-worksheet-form) form.

1. Optional: It is also
 recommended that you print the Physical Count Report (also accessed from the
 File menu of the IN Physical Count Worksheet form) and review the data to ensure
 it is correct.

1. Check the Ready box next to each entry that should be included in the
 adjustment batch.Note: You can also select File > Set Ready Flag to set the Ready box on all of the
 entries in the worksheet. This option only works if the entries have a
 physical count, count date, and system count.

1. Select File > IN Physical Count
 Batch from the menu at the top of the form. This will open the IN
 Physical Count Batch form.

1. Enter the month of the
 adjustment batch in the Month field.The month entered in this field
 must be greater than the last month that was closed(All Other Sub Ledgers),
 and less than or equal to the last month that was closed plus the maximum
 number of open months. You can view the last month that was closed using the
 All Other Sub Ledgers field on the Info tab of the [GL Company Parameters ](/en/vista/vista/accounting/general-ledger/gl-setup-and-maintenance/about-the-gl-company-parameters-form) form, and you can
 set the maximum number of open months using the Max # of
 Open Months field on that same form and tab.

1. Click the Update button when complete. As entries are added to the batch,
 they are deleted from the worksheet. This will open the IN Batch Process
 form.Note: Adjustment batches are user-specific;
 therefore, only those materials existing on the current user’s worksheet(s)
 will be added to the adjustment batch. Materials marked as “ready” on
 worksheets created by other users will be bypassed.

1. Use the IN Batch Process
 form to process the adjustments batch. Adjustments to Inventory and the GL
 update are made when the batch is posted.

Related information

- [IN Physical Count Worksheet Form](/en/vista/vista/job-resources/inventory/monthly-reconciliation/in-physical-count-worksheet-form)
