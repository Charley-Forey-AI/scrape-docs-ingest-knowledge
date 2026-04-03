---
title: "Job Cost Transaction Entry: EQ - Equipment - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/job-cost-transaction-entry/job-cost-transaction-entry-eq---equipment/job-cost-transaction-entry-eq---equipment---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/job-cost-transaction-entry/job-cost-transaction-entry-eq---equipment/job-cost-transaction-entry-eq---equipment---field-descriptions"
---

# Job Cost Transaction Entry: EQ - Equipment - Field Descriptions

Use the table below for reference when completing fields on this screen.
Fields
Descriptions

Equipment
Description
Enter or search for an equipment code, indicating the piece of equipment to be charged to the job for this line transaction. Entry is prevented if the equipment's status is set to Retired.
The equipment code entered here must be for a piece of equipment previously set up in Equipment File Maintenance.

Job
Enter or search for a job number, indicating the job to which the entered equipment should be charged.
The job number entered here should have been previously defined in Jobs; however, a new job may be entered.

Phase
Enter or search for a phase code for the job cost transaction. This job/phase combination should have been previously defined in Job Phases; however, it may be entered here.
Note: Entry is prevented if the phase's status is set to
 Complete.
If this is a sub-job transaction set up on a master job, double-click on this field to search phases for the sub-job. This will allow you to easily select a phase set up on a master job, but not present on the sub-job. Spectrum will add a new phase to the sub job if the current job is a sub-job of a valid master job, the phase lengths of both jobs match, and the Phase + Cost type combination for the current job is valid and not 'Complete'.

Ct
Enter or search for a cost type for this line transaction. The phase description and cost type name will display under their respective codes.

Total hours
Enter the total number of hours this equipment was used.

Rate
Press Enter to accept the default rate for this piece of equipment.
Hierarchy for charge rates
If applicable, this rate information will default the amount set up in the Job-Specific Equipment Charge Rates screen. If no job-specific record is found (or rate is blank), the system will determine if this job is a sub job of a master job and use the job-specific rate from the master job. If there is no job-specific rate for the job or master job, the system will read for the standard job rate of the equipment code.

Total cost
Spectrum multiplies the total hours by the rate. Press Enter to accept this calculation, or enter the desired total gross for this line transaction. Note that if the calculated total gross is overridden, the rate will be adjusted accordingly.

Billing rate
Billing rates are only applicable to Time + Materials jobs and T+M phases of other jobs. The billing rate defaults based on the equipment billing code stored in the equipment file.
If this is a sub-job billed from a master job, the software will read for job-specific setup rates for the master job, and if none are found use standard settings. If this is a sub-job billed at the sub-job level, the software will read for job-specific setup rates for the sub-job first, and if billing rates are not found then the master job, and if none are found there use standard settings.

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
The name of the job and phase description display.
