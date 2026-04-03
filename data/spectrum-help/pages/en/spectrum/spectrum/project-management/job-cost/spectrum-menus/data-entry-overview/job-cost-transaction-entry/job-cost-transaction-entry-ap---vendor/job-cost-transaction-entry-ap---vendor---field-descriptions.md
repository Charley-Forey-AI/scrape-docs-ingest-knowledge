---
title: "Job Cost Transaction Entry: AP - Vendor - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/job-cost-transaction-entry/job-cost-transaction-entry-ap---vendor/job-cost-transaction-entry-ap---vendor---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/job-cost-transaction-entry/job-cost-transaction-entry-ap---vendor/job-cost-transaction-entry-ap---vendor---field-descriptions"
---

# Job Cost Transaction Entry: AP - Vendor - Field Descriptions

Use the table below for reference when completing fields on this screen.
Fields
Descriptions

Vendor Vendor name
Enter or search for a vendor code in this required field. The vendor name also displays.
The vendor code entered here must have been previously defined in
 Vendor File Maintenance.

Job
Enter or search for a job number, indicating the job to which this adjustment should be charged.
The job number entered here should have been previously defined in Jobs; however, a new job may be added.

Phase
Enter or search for a phase code for the job/invoice being entered. The job/phase combination entered here should have been previously defined in Job Phases.
Note: Entry is prevented if the phase's status is set
 to Complete.

If this is a sub-job transaction set up on a master job, double-click on this field to search phases for the sub-job. This will allow you to easily select a phase set up on a master job, but not present on the sub-job. Spectrum will add a new phase to the sub job if the current job is a sub-job of a valid master job, the phase lengths of both jobs match, and the Phase + Cost type combination for the current job is valid and not 'Complete'.

Ct
Enter or search for a cost type for this line transaction. The phase description and cost type name will display under their respective codes.

Amount Invoice date
Enter the dollar amount and invoice date for this line transaction.
The invoice date specified in the heading of the screen defaults. It will display on the Job Cost History Report.

Invoice # P.O.
The invoice number and purchase order number will display on the Job Cost History Report.

Check #
Enter the check number if this invoice has been paid.

G/L debit
The debit account entered here must have the Job cost option selected
 in the Direct cost
 field of G/L Master File Maintenance.
Note: Entry is prevented if the account's status is set to
 Not
 used.

G/L credit
Enter or search for the General Ledger account to be credited. The credit
 account must have the No
 direct cost option selected in the Direct cost field of the
 G/L Master File Maintenance screen.
Note: Entry is prevented if the account's status is set to
 Not
 used.

Job name Phase description
The name of the job and phase description display.
