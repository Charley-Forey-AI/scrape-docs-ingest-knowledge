---
title: "Time Card Entry by Job | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/time-card-entry/time-card-entry-by-job"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/time-card-entry/time-card-entry-by-job"
---

# Time Card Entry by Job

The Time Card Entry screens are used to enter detailed time
 cards for all employees.
During Time Card Entry, hours may be distributed to various unions, departments, jobs, and
 worker's compensation classifications. Time Card Entry can be performed by employee, job,
 or quantity. Quantities other than payroll hours may also be entered at this time.

- Entry methods: A
 variety of entry methods may be used within a pay cycle. For example, entry may be
 done by job for most information, then by employee for additional time, salaried
 employees and void checks. After all time has been entered, the Time Card Edit List
 should be reviewed for accuracy, and then the payroll may be calculated.

- Pay rates: Any
 pre-scheduled pay rate adjustments and union contract changes defined in Employees,
 Union File Maintenance, or Wage Code File Maintenance will default as they are
 scheduled. Time Card Entry will automatically refigure pay rates when any field that
 affects the default rate is changed.

Once the header information is completed, click New to open the Time Card Entry window and enter new time card lines. If you are adding a pre-time card or regular time card entry and add an employee, job, or phase on the fly, make sure the time card line is fully completed in order to save the newly-added record.

## Hierarchy for Charge Rates

If applicable, this rate information will default the amount set up in the Job-Specific
 Equipment Charge Rates screen. If no job-specific record is found (or rate is blank),
 the system will determine if this job is a sub job of a master job and use the
 job-specific rate from the master job. If there is no job-specific rate for the job or
 master job, the system will read for the standard job rate of the equipment code.

## Note regarding Time Card Approval Workflow

If the 'Allow override operator to modify approved time cards' option was selected in
 the Time Card Approval Workflow, approved time cards can be edited or deleted if the
 current user is an override operator.

## Note regarding Related Taxes

If related tax codes have been set up for the employee code, the related tax codes will
 automatically be created on entry by job.
