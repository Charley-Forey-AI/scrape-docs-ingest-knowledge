---
title: "Process a Batch | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/batch-processing/process-a-batch"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/batch-processing/process-a-batch"
---

# Process a Batch

Many of the posting forms within Vista use batches to create
 and post transactions. If you have added transactions to a batch, you must process the batch
 to enable updates to GL and applicable modules.
Enter and/or edit transactions as
 needed. You cannot process an empty batch.

Before you post a batch, you must validate the batch to
 ensure the data is valid. If no errors are found, the appropriate audit reports are
 created. Although not required, it is recommended that you print these reports. If
 errors are found, an error report is created so that you can review the errors and
 correct them. Once you have corrected the errors, re-validate the batch (at which time
 the audit reports will be created and can be printed).

1. From the posting or
 batch processing form, select File >
 Process Batch. The system displays the module Batch Process form (for example,
 AP Batch Process).

1. Review the information
 in the Info section of the form and click Validate. The system
 validates the batch and enables fields in the Audit Reports section.

1. Select the checkbox for
 each audit report that you wish to run. Click Preview to preview the reports onscreen. Click Print to print each report. To make the reports available to
 you after posting the batch, do one or both of the following:

- print the audit reports before posting a
 batch

- select the Attach
 Batch Reports to HQ Batch Control checkbox in the module's
 Company Parameters form. For example, in AP Company Parameters, this check
 box is located on the Audit Options tab.

- For more information, see [Attach Batch Reports to HQ Batch Control](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form/field-definitions-pr-company-parameters-form#ID-000059e7--en).
 For information about the audit reports available during batch processing,
 see the Audit Reports information in the form help for each module's Batch
 Process form.

1. Review the information
 in the Update section of the form.

1. In the Posting
 Date field, enter a date or accept the current date default.


1. Click Post.  The system posts the
 transaction and displays a success message.

1. Click Close.

You are returned to the main menu.
