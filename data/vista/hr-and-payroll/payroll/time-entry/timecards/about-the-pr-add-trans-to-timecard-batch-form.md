---
title: "About the PR Add Trans to Timecard Batch Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-add-trans-to-timecard-batch-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-add-trans-to-timecard-batch-form"
---

# About the PR Add Trans to Timecard Batch Form

Use this form to add existing timecards to the current batch.
Access this form by selecting File > Add
 Timecard from PR Timecard Entry. Different filtering criteria is available,
 depending upon the timecard option selected in the Options section of PR Add Trans to
 Timecard Batch. Options for adding timecards are discussed in the sections below.

## Adding Timecards from the Current Payroll Into Your Batch

This option allows you to add timecards that have already
 been posted for the specified employee in the current pay period. Typically, this is used when you need to
 make corrections to some or all of the employee's timecards for the pay period. You can
 restrict which timecards are added using the filtering criteria in the Restrictions
 section of the form. To filter, enter a value into each relevant field; if all fields
 are blank, all timecards for the current payroll are batched. Only timecards meeting all
 restrictions are added to the batch; a message displays when one or more timecards are
 already in the batch. You also have the option to flag all timecards that are added to
 the batch for deletion. Additionally, you can exclude timecards if the employee or pay
 sequence have been paid.

## About Initialize Reversing Timecards from Another Payroll

This option allows you to add timecards to a current pay
 period that were posted in a previous pay period. When selected, this option restricts which
 timecards are added using the filtering criteria in the Restrictions section of the
 form. To filter, enter a value into each relevant field; if all fields are blank, all
 timecards for the current payroll are batched. The system locates all timecards meeting
 the criteria and adds them to the batch with negative values.
Note: The Pay Seq must be valid for the reversing pay
 period and the Post To Pay Seq must be valid for the current pay period.
Using this option, you can 'back out' an
 employee's posted job earnings and costs, as well as correct entries, for the specified
 batch. For example, if an employee's time was posted to the wrong job, you can pull in
 the posted timecards to 'back out' the earnings and job costs. Then, in the same batch,
 manually add the earnings and costs to the correct job with new timecard lines.
If you are posting timecards for the
 employee for the current pay period, and do not want the reversing entries to reduce the
 employee's earnings, post the reversing entries to a different pay sequence. After
 posting the batch, post a 'dummy' check to account for the negative earnings. This step
 is not necessary if you post a correcting entry in the same batch or if you post the
 reversing entries to the same pay sequence to reduce the earnings by the reversing
 amount.

## Timecards Posted to SM Work Orders

Changes made to the timecard will update
 Payroll accordingly; however, the system will also update the work completed labor lines
 for the work order as follows:

- If the work order has not been invoiced, the system will update the cost
 and price information for each applicable work completed labor entry (in SM Work
 Orders).

- If the work order has been invoiced, the system will update cost
 information only; the price information will remain intact.

If you mark the timecards for deletion (i.e.,
 check the Mark
 added timecards as "Delete" box), work completed entries will be handled
 as follows:

- If the work order has not been invoiced, the associated work completed
 labor entries will be deleted from the work order.

- If the work order has been invoiced, the associated work completed labor
 entries will not be deleted; however, the system will set the costs to 0.00 and
 leave the price information intact.

Related information

- [About the PR Timecard Entry Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form)

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)

- [SM Work Completed Labor Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-labor-form)
