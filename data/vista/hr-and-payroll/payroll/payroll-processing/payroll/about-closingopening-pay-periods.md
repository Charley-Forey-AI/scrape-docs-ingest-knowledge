---
title: "About Closing/Opening Pay Periods | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-closingopening-pay-periods"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-closingopening-pay-periods"
---

# About Closing/Opening Pay Periods

The status of a pay period controls what actions and updates may be made with entries posted to this pay period.

There are two status values available: open and closed.
An open period allows you to [enter timecards](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/posting-timecards),
 [post automatic
 earnings](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-posting-automatic-earnings/post-automatic-earnings), [process payroll
 periods](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/processing-payroll/processing-a-payroll-period), [review processed payroll and post any necessary overrides](/en/vista/vista/hr-and-payroll/payroll/payments/about-reviewing-processed-payrolls), [print
 checks](/en/vista/vista/hr-and-payroll/payroll/payments/print-payroll-checks), [process EFTs](/en/vista/vista/hr-and-payroll/payroll/payments/process-payroll-eft-payments) , and
 perform ledger and AP updates. The system assigns this status to all newly created pay
 periods, and each payroll group may have multiple open pay periods; however, it is
 recommended that you keep this to a minimum of one or two.
The most common reason to have more than one pay period open at a time is to process layoff checks for one week, when the prior week has not been fully completed. However, a reason for caution is to prevent inaccuracies due to exceeding limits. As long at the employee's pay periods have been processed in consecutive order, there will not be a problem, even if accumulations have not updated for the pay period prior to the one you are currently working in.
The following table gives an example:
Pay Period
Pay Period Processed?
Accumulations Updated?

Through Prior Month
Y
Y

Open Week 1
Y
Y

Open Week 2
Y

Open Week 3
Y

In this example, if you made a correction to Week 2 and reprocessed the pay period, the system would recalculate and check limits through Week 2, but would not look at the calculations in Week 3. It would then be necessary to reprocess the employee for Week 3. This would then recalculate and check limits through Week 3.
A pay period cannot be closed unless it is fully processed; that is, all time posted, deductions and liabilities calculated, accumulations updated, and checks printed. Once closed, you cannot enter or change any timecard entries, reprocess a payroll, or print checks. You may, however, print any of the Payroll reports (e.g., PR Timecard Entry List, PR Payroll Register, PR Employee Accumulations, etc.).
When a pay period is closed, you can run the final ledger and AP updates. If JC, EM, or GL has already been updated, only the difference between what was previously interfaced and what is now processed will be interfaced. Closed pay periods may be purged after the final interfaces and updates have been run using PR Purge.
You can reopen a closed pay period, but you will need to rerun final updates, even if you have not made changes. The most common reason to reopen a pay period is to void and re-issue a check. After making the change, you should close the period again and rerun the AP update to flag the period as having a complete final update, even if there are no change to any of the other ledgers.
Note: The only restriction to reopening a pay period is that the month (or months) of the pay period be open in the subledgers. You can then make changes, but caution should be used to make sure limits are not exceeded because of changing amounts which have been processed in later pay periods. If limits are involved, you should remember to re-process all subsequent pay periods for the employee so that they will also be corrected
For more information about using this form, click the links below.
[Close a Pay Period](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-closingopening-pay-periods/close-a-pay-period)
[Reopen a Pay Period](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-closingopening-pay-periods/reopen-a-pay-period)

Related information

- [Common Problems When Closing Pay Periods](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-closingopening-pay-periods/close-a-pay-period/common-problems-when-closing-pay-periods)

- [PR Pay Period Control Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/pr-pay-period-control-form)

- [Processing Payroll](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/processing-payroll)
