---
title: "Build Projected Cost Transaction File - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/build-projected-cost-transaction-file/build-projected-cost-transaction-file---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/build-projected-cost-transaction-file/build-projected-cost-transaction-file---field-descriptions"
---

# Build Projected Cost Transaction File - Field Descriptions

Use the table below for reference when completing fields on this screen.
Fields
Descriptions

Calculations
Click to open the [Projected Cost Calculations window](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/projected-cost-calculations-window) window.

Selections

Batch code
Enter the batch code, or double-click in this field to select from a list of valid batch codes. The operator code displays as the default batch.
When the Clear file for
 batch checkbox is selected, all selected jobs will be cleared
 when the build is run.

Job
Enter the number of the job to include in this build. The update will select jobs that are not yet built. Jobs already built will not be assigned the above batch code.
Note: The default job number that displays is the last job number
 entered in this field during the current session. If you are accessing this
 page for the first time during a session, this field will default to blank.
 A job number must be specified before you can proceed with the
 worksheet.

Phase
Cost type
Division
Superintendent
Estimator
Project manager
Enter the phase number, cost type, job division, superintendent, estimators, and project managers to include in this build.

Transaction date
The estimate and actual costs for the selected period display. Projections include transactions through the current Job Cost processing date.
The Build Projected Cost Transaction File page checks the
 current batch for any projected cost history records that come after the
 date in this field. If any dates are found, the following message displays:
 "Projections have already been posted for a subsequent date."

Fiscal year
The fiscal year for this entry displays.

Period
The period for this entry displays.

Set projected = estimate?
Select the checkbox to set projected cost figures to the current estimated cost figures. This is typically done the first time this job is built.
When the transaction file is built for the first time, the software will set the projected amount for each phase and cost type equal to the estimated amount if the actual cost is zero. If there is an actual cost, even if the projection is zero, the build does not set the projection equal to the estimate.
In subsequent months, the checkbox defaults to clear since the project manager provides ongoing projection information and it is not recommended to reset the projected costs to equal the estimates.

Include open commitments?
Select the checkbox to include open commitments in the transaction file.
Including open commitments allows you to consider committed costs as if they have been incurred.
By selecting this checkbox, the actual cost-to-date will include invoices that have been received, as well as open purchase orders, remaining subcontract amounts, and open job cost requisitions. The open commitment calculation will include use tax recorded on purchase orders and job requisitions.
If you select this checkbox, reports and inquiries display JTD + Open. If you do not
 include open commitments, JTD or Actual
 displays.

Include Payroll in progress?
Select this checkbox to include pre-time card entries and time card entries in cycle in Projected Cost Processing. Enter the pre-time card batch number.

Include A/P invoices in progress?
Select this checkbox to include unapproved and unposted Accounts Payable invoices in Projected Cost Processing; otherwise, leave this checkbox clear. This feature allows you to review job-related amounts including invoices that have been received but not yet approved and posted to Job Cost History.

Group summary

Major group only
Through minor group
Phase summary
Phase/Cost type
This option group defaults from information specified in the Job
 Cost Installation screen for Group summary.
Select the Major group
 only or Through
 minor groupoption to display the Projected Cost
 Entry (by Group) screen, showing one line for each group. If a
 percent complete, cost-to-complete, or final projection is entered for the
 group, Spectrum allocates this percent to all detail phases in the
 group.
Select the Phase
 summary option to display the Projected Cost Entry
 (by Phase) screen and summarize by phase.
Select the Phase/Cost
 type option to display the Projected Cost Entry (by
 Phase) screen. If a phase category has been designated in the
 Job screen, then Spectrum uses the category-specific
 group description. If no phase category has been designated, the
 company-wide description displays. This group is not available if projected
 cost processing is already in progress for this batch.

Through minor group

Period type

Week-to-date
Month-to-date
Year-to-date
The period type defaults based on settings on the Job Cost Installation > Reports tab.
The option you select in this section affects the information displayed in the
 Projected Cost Entry page's Last Period column.
The selection made here does not affect the projections — it is an
 informational setting that determines which column displays for actual costs
 along with the job-to-date actual costs.
This feature provides companies with flexibility when reviewing their projections. For example, if unusual delays occurred last week, you could look at the week prior and use this as an indication of what productivity will be for the remainder of the project.

Week-to-date begin
Week-to-date end
These fields are applicable if Week-to-date is selected as the Period type option.
The week-to-date beginning and end dates default based on the current Job Cost processing date (less six days for Week-to-date begin).

Description
The description defaults based on your Period type selection. It
 will appear as the Last
 period column header on the Projected Cost Entry
 page.
Press Enter to
 accept this default or enter a different description.

Job status

- Active?

- Inactive?

- Complete?

Select at least one job status to include in the build.

Phase status

- Active?

- Inactive?

- Complete?

Select at least one phase status to include in the build.
If inactive or completed phases should not be changed during projected cost
 processing, select only active phases and use security restrictions to
 prevent unauthorized users from building projected costs. This is because
 the Projected Cost Entry pages allow changes to
 complete phases when the transaction line already exists but prevents the
 operator from adding a new transaction line when the phase is complete.
