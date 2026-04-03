---
title: "Job Cost Transaction Entry: PR - Employee - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/job-cost-transaction-entry/job-cost-transaction-entry-pr---employee/job-cost-transaction-entry-pr---employee---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/job-cost-transaction-entry/job-cost-transaction-entry-pr---employee/job-cost-transaction-entry-pr---employee---field-descriptions"
---

# Job Cost Transaction Entry: PR - Employee - Field Descriptions

Use the table below for reference when completing fields on this screen.
Fields
Descriptions

Employee
Name
The employee code entered here must have been previously defined in the Employee Maintenance screen. The full employee name will display once a code has been entered.

Job
Enter or search for a job number, indicating the job to which payroll hours for this employee should be charged.
The job number entered here should have been previously defined in Jobs; however, a new job may be entered here, if desired.

Phase
Enter or search for a phase code for the job cost transaction. This job/phase combination should have been previously defined in Job Phases; however, it may be entered here.
Note: Entry is prevented if the phase's status is set to
 Complete.
If this is a sub-job transaction set up on a master job, double-click on this field to search phases for the sub-job. This will allow you to easily select a phase set up on a master job, but not present on the sub-job. Spectrum will add a new phase to the sub job if the current job is a sub-job of a valid master job, the phase lengths of both jobs match, and the Phase + Cost type combination for the current job is valid and not 'Complete'.

Ct
Enter or search for a cost type for this line transaction. The phase description and cost type name will display under their respective codes.

Total hours
Enter the total hours that will be distributed to this job, phase, and cost type.

Rate

- Rate: Enter the rate per hour (including burden) for this employee.

- Bill rate: Enter the billing rate per hour for this employee. This field displays if entry is for a Time + Material job and the employee has a billing code set up in Employee Maintenance-Rates. When this entry is posted it will be updated to T + M transaction files.

Total gross
Enter the total amount for this payroll check (hours multiplied by rate).

Check #
Enter the check number of the payroll check. This information will be posted to the job history file and will print on the Job Cost History Report.

Billing rate
Enter the billing rate per hour for this employee. This field only displays if entry is for a T + M job and the employee has a billing code set up in Employee Maintenance-Rates. When this entry is posted, it will be updated to T + M transaction files.

- If the Bill rate of the transaction is zero, then the markup is calculated on the cost.

- If the Bill rate of the transaction is non-zero, then the markup is calculated using that bill rate.

If this is a sub-job billed from a master job, the software will read for job-specific setup rates for the master job, and if none are found use standard settings. If this is a sub-job billed at the sub-job level, the software will read for job-specific setup rates for the sub-job first, and if billing rates are not found then the master job, and if none are found there use standard settings.

Message
Enter a brief message describing the transaction.

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
The name of the job and Phase description display.
