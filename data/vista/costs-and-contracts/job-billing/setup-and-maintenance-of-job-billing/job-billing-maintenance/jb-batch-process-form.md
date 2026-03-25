---
title: "JB Batch Process Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/job-billing-maintenance/jb-batch-process-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/job-billing-maintenance/jb-batch-process-form"
---

# JB Batch Process Form

Use this program to process batches created by JB Interface.
 After you specify the month and batch to process, the Info section displays information about the batch (specifically, batch creator, creation date, batch source, and status).
The next step is to validate the information in the
 batch (by clicking Validate). The validation process runs through all the data in the
 batch and creates Audit Reports to preview and/or print before posting the batch. It is
 recommended that you print the audit lists before posting the batch. Once you post the
 batch, the audit reports are no longer available. For a list of audit reports available
 for this module, see [Audit Reports](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/job-billing-maintenance/jb-batch-process-form/field-definitions-jb-batch-process-form#ID-000148b9--en).
Once the batch is ready for processing, enter the posting date and click Post. The system clears the entries and closes the batch.

## About Clearing the Batch

You can clear a batch if needed by
 selecting File > Clear Batch. The data in the batch is not updated online; therefore, you can
 delete it completely without affecting any modules, including Job Billing. The
 system will clear/delete all data from the batch. If the batch contains previously
 posted transactions, they are only cleared from the batch—they are not deleted.
Note: The system creates an audit record each time you
 clear a batch. For information about cleared batches (i.e. user who cleared batch,
 as well as the date and time the batch was cleared), use the VA 'Other Events'
 Statistics report.
You cannot clear a batch if posting is in progress (that is, the
 batch has a status of 4-Posting in Progress. This is to prevent partially updated
 batches from being deleted should the update process be interrupted (i.e. power
 outage, system failure, etc.). When a batch update is interrupted, only a portion of
 the intended updates may occur. If a user later clears the batch, there is no way to
 determine the updated data.
