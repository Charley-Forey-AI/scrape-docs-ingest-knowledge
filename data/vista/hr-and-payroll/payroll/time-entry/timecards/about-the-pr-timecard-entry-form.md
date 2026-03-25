---
title: "About the PR Timecard Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form"
---

# About the PR Timecard Entry Form

Use this form to post, change, and delete timecard details to/from open payroll periods.
Each timecard entry includes specific information necessary to track an employee’s earnings, calculate required deductions and liabilities, and produce general ledger distributions. In addition, depending on the type of timecard you are entering, the system will generate appropriate job costs (job timecards), track equipment usage (job and mechanics' timecards), update mechanic’s labor costs to Equipment Management (mechanics' timecards) or technician's labor costs to SM work orders (SM work order timecards).
Note: Job and mechanic timecards can be entered manually in this form or created automatically using the PR Automatic Earnings or PR Auto Overtime posting forms.
Timecards may be posted to any open pay period, and may be edited here until the payroll period is closed. A closed payroll period may even be reopened if necessary to make additional edits. Posted entries can be edited even after checks have been printed.

## Field Tickets

Field tickets enable you to link labor, material, and equipment costs related to specific work activity on a job, and facilitate owner billing. When you enter a job timecard, you can assign the timecard to a field ticket associated with the contract for the specified job. You can assign multiple timecard entries to a single field ticket, as long as the ticket is still open (that is, has a status of O-Open in JC Field Ticket). Once the status is set to Closed, Approved, Rejected, or Billed, you can no longer post costs to that ticket.Note: Costs associated with approved field tickets only impact T&M billings; therefore, assigning field tickets to job timecards is only useful if the job's contract/contract item has a bill type of T&M or Both.Additionally, once you process payroll and run PR Ledger Update, entries associated with approved field tickets appear on the Cost Detail tab in JC Field Ticket for the specified field ticket.

 For more information about field tickets, see [JC Field Ticket](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

## Deleting Timecards

You can delete timecards from a batch in one of the following ways:

- You can manually delete a timecard by selecting the timecard line and clicking Delete.

- You can delete multiple timecards for an employee using the PR Delete Employee's Timecard form, which you can access from PR Timecard Entry by selecting File > Delete Employee's Entries. For more information, see [ PR Delete Employee's Timecard Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/pr-delete-employees-timecard-form).

- If you have not posted the batch, you can clear the batch in PR Batch Process (accessed from PR Timecard Entry by selecting File > Process Batch). For more information, see [PR Batch Process Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/pr-batch-process-form).

- For previously posted timecards pulled back into a batch, you must set the Action field to Delete and then post the batch.


Once you delete a timecard, the system adds an associated record for that
 timecard to the vPRTimeCardSafetyNet table in Vista. If you are an HR Management or
 Field Management Timecard Admin, you can only restore deleted timecards via the HR
 Management or Field Management web applications by navigating to Employee Tools > Safety Net; you cannot restore deleted timecards in Vista. For more information,
 see [Timecard Safety Net User
 Guide](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:HRV_000031:HRV:HRV).

Click the following links for more information on using this form.
[Posting Timecards](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/posting-timecards)
[Entering Job Timecards](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/enter-job-timecards)
[Entering Mechanics Timecards](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/enter-mechanics-timecards)
[Entering SM Work Order Timecards](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/entering-sm-work-order-timecards)
[Tracking Employee Start and Stop Times](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/tracking-employee-start-and-stop-times)
[Entering Start and Stop Time on Timecards](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/enter-start-and-stop-time-on-timecards)
[Initializing Crew Timecards](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/about-the-pr-initialize-crew-timecards-form)
[Adding Existing Timecards to a Batch](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-add-trans-to-timecard-batch-form)
[Customizing Timecard Entry](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-customizing-timecard-entry)
[Adding Attachments and Scanned Images to Timecards](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/add-attachments-and-scanned-images-to-timecards)

Related information

- [Show Employee Rate/Amount in Timecards - Video](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/show-employee-rateamount-in-timecards---video)

- [Batches](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/batches)

- [Totals](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/totals)

- [About the PR Initialize Crew Timecards Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/about-the-pr-initialize-crew-timecards-form)

- [Enter Mechanics Timecards](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/enter-mechanics-timecards)

- [Default to Job Type Entry](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/default-to-job-type-entry)

- [Add Attachments and Scanned Images to Timecards](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/add-attachments-and-scanned-images-to-timecards)

- [About Post by Day Number](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-post-by-day-number)

- [About Post by Job](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-post-by-job)

- [Posting Timecards](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/posting-timecards)

- [Default Post Sequence on Grid](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/default-post-sequence-on-grid)

- [PR Delete Employee's Timecard Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/pr-delete-employees-timecard-form)

- [Entering Equipment Usage with Service Timecards](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/entering-equipment-usage-with-service-timecards)

- [Enter Start and Stop Time on Timecards](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/enter-start-and-stop-time-on-timecards)

- [Pay Sequences](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/pay-sequences)

- [About the PR Add Trans to Timecard Batch Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-add-trans-to-timecard-batch-form)

- [Entering SM Work Order Timecards](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/entering-sm-work-order-timecards)

- [Enter Equipment Usage with Job Timecards](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/enter-equipment-usage-with-job-timecards)

- [About Post Equipment Usage](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-post-equipment-usage)

- [Equipment Class Override](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/equipment-class-override)

- [Enter Job Timecards](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/enter-job-timecards)

- [About Customizing Timecard Entry](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-customizing-timecard-entry)

- [About the PR Salary Distribution Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-the-pr-salary-distribution-form)

- [PR Automatic Earnings Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-automatic-earnings-form)

- [PR Auto Overtime Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/pr-auto-overtime-form)

- [About the PR My Timesheet Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/about-the-pr-my-timesheet-form)

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)

- [About Service Timecards](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-service-timecards)
