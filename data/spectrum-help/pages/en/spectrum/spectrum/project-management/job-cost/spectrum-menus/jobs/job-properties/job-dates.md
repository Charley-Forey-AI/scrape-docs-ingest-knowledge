---
title: "Job Dates | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-dates"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-dates"
---

# Job Dates

Use the Job Dates screen to enter the actual and estimated dates pertaining to the job schedule.
If you're accessing this screen from Projected Cost Entry, it is view-only and the Edit button doesn't display.
When editing the job dates, you can enter date shortcuts in fields with drop-down arrows. Entry in these fields is optional.

FieldsDescriptions
Job forecast dates
Estimated start date Estimated completeEdit the estimated start and completion dates for this project.
Estimated durationSpectrum calculates the project's estimated duration based on the dates entered in the Estimated start and complete date fields. If the duration length is less than zero, it displays as 0.
Projected completion dateEnter the projected date of completion.
Project durationSpectrum calculates the project's duration based on the dates entered in the Actual start date and Projected complete date fields. If the duration length is less than zero, it displays as 0.
Job milestones
Job create dateThis date determines when the job first appears on the Contract Status Report.
Actual start dateThis date is used in document tracking. If the date is blank, Spectrum is unable to create the next recurring document in 'AP Document Tracking'. For example, if you have set a subcontract to create a monthly Certified Report requirement, it will not generate the recurring Yes/No document. With the date properly set, each month it will create a new Certified Report tracking item.
Actual complete dateThe [Contract Status Report](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/contract-status-report) can print completed jobs based on the completion date entered here. The reports look at the current status setting plus the complete date to determine where to include the job on the report (for example, among Active and Inactive, or Complete jobs). Therefore, when a job is set to Complete and the Contract Status Report is reprinted for an earlier date, the job appears within Active jobs even though it has been completed.
This date also displays under the Status section on the [Job Main Properties](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-main-properties) screen.
If you purge a job, you must record an actual complete date first.

Actual durationIf you entered the Actual complete date, then Spectrum calculates the actual duration of the project in days.
Job history dates
Last projected dateThe most recent projected date displays.
Certified dateThis field is used on the Certified Payroll Report to calculate the payroll number on the report heading.The certified date is automatically set during the Payroll Update equal to the earliest work date, provided that this field is blank or the date entered is later than the first work date in the pay cycle.
Last payroll date The last work date from the time card lines for this job displays.
During the Payroll Update, this information is also updated here and is helpful in protecting your lien rights.

Last cost dateThis is the latest date that a cost was incurred on this job.
The default date is based on the latest date stored in the job cost transaction history file, based on the current processing date.

Last billing dateThis is the latest date a billing was issued for this job. This information comes from Accounts Receivable.Note: If the Rebuild Balance Files from History error recovery update is run, this date will be written from the Contract file.

Phase dates
Phase datesThese dates come from the [Job Phases](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-phases) screen. If you have security authorization to that screen, you can edit the dates there.
