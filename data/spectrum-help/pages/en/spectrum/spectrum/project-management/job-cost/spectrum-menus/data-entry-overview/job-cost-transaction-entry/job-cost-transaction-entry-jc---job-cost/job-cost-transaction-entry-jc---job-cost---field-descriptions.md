---
title: "Job Cost Transaction Entry: JC - Job Cost - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/job-cost-transaction-entry/job-cost-transaction-entry-jc---job-cost/job-cost-transaction-entry-jc---job-cost---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/job-cost-transaction-entry/job-cost-transaction-entry-jc---job-cost/job-cost-transaction-entry-jc---job-cost---field-descriptions"
---

# Job Cost Transaction Entry: JC - Job Cost - Field Descriptions

Use the table below for reference when completing fields on this screen.
Fields
Descriptions

Reference
Enter a reference code for this job cost adjustment. The reference code should be something that identifies this adjustment (for example, the entry date or source document number).

Description
Enter a description of this job cost adjustment. This description will post to the job history file and will print on the Job Cost History Report.

Job
Enter or search for a job number, indicating the job to which this adjustment should be charged.
The job number entered here should have been previously defined in Jobs; however, a new job may be added.

Phase
Enter or search for a phase code for the job cost transaction. This job/phase combination should have been previously defined in Job Phases and will default here but may be overwritten.
Entry is prevented when the phase status is set to Complete; a warning message displays if the phase status is set to Inactive.
If this is a sub-job transaction set up on a master job, double-click on this field to search phases for the sub-job. This will allow you to easily select a phase set up on a master job, but not present on the sub-job. Spectrum will add a new phase to the sub job if the current job is a sub-job of a valid master job, the phase lengths of both jobs match, and the Phase + Cost type combination for the current job is valid and not 'Complete'.

Ct
Enter or search for a cost type for this line transaction. The phase description and cost type name will display under their respective codes.

Hours
Enter the adjusted hours for this job cost adjustment. Either positive or negative hours may be entered.

Amount
Enter the adjustment dollar amount for this job cost adjustment. Either positive or negative dollar amounts may be entered.

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

Job name Phase description
The name of the job and phase description display.
