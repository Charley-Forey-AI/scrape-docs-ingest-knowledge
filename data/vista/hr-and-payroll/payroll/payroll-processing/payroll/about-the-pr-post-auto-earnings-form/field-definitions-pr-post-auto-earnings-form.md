---
title: "Field Definitions: PR Post Auto Earnings Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-the-pr-post-auto-earnings-form/field-definitions-pr-post-auto-earnings-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-the-pr-post-auto-earnings-form/field-definitions-pr-post-auto-earnings-form"
---

# Field Definitions: PR Post Auto Earnings Form

The following is a list of field descriptions for the PR Post
 Auto Earnings form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Restrict by Employee

 Check this box if you want to process a single employee’s automatic earnings.
 Do not check this box if you want all employees within the specified PR group to be processed.

##  Employee

 Available when Restrict by Employee checkbox is selected.
 Enter an active employee who is assigned to the batch’s PR Group and who has been assigned automatic earnings codes in PR Automatic Earnings.

##  Restrict Posting to a Single Payment Seq #

 Check this box if you want to restrict posting of automatic earnings to a single payment sequence number.
 Do not check this box if you want all payment sequences within the specified PR group to be processed.

##  Payment Seq#

 If restricting posting to a single payment sequence, enter a valid sequence number that has been set up for the pay period. Automatic earnings set up without a Pay Seq# post to the one entered here. Automatic earnings set up with a Pay Seq# post to their assigned sequence.

##  Timecard Date

 Enter the date to use as the actual posting date for each new timecard. A warning displays if this date is outside the date range of the pay period.

## Delete & Replace if Timecards for Empl, Pay Seq...

Check this box if you want to replace previously posted Automatic Earnings. Existing timecards posted to an Employee, Pay Seq#, and Earnings Code combination that match an active Automatic Earnings are pulled into the batch and flagged for deletion. New entries generate based on the current values in PR Automatic Earnings and then are added to the batch.
If unchecked, the system skips active Automatic Earnings if a timecard already exists for the Employee, Pay Seq#, and Earnings Code.
Only Automatic Earnings assigned an active Frequency Code for the pay period are processed.
Employee Payment Sequences that have already been paid do not change (e.g., no existing timecards will be “pulled,” or new entries created).
