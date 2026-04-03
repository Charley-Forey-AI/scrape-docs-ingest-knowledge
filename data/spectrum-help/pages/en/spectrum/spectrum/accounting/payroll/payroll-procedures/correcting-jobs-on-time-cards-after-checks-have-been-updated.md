---
title: "Correcting Jobs on Time Cards After Checks Have Been Updated | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/payroll-procedures/correcting-jobs-on-time-cards-after-checks-have-been-updated"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/payroll-procedures/correcting-jobs-on-time-cards-after-checks-have-been-updated"
---

# Correcting Jobs on Time Cards After Checks Have Been Updated

You can correct jobs on time cards even after you have updated checks.
When time cards have been incorrectly coded to the wrong job, the checks have been updated, and the month is NOT closed, first determine if the check was auto deposit. If it was, it's necessary to follow the [Void an Auto Deposit](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/checks--auto-deposit-procedures/void-an-auto-deposit) instructions when performing the first step.

1. Set up a new Payroll cycle with the same dates as the original cycle and void the original check. Update.

1. Set a second Payroll cycle with the same dates as the original and re-enter the time as a (M)anual check to the correct job.Note: Manual checks do not calculate FIT, SIT, and other taxes – they only
 calculate FICA. It's necessary to use Check Adjustment to enter the exact tax
 dollars as the original check.

1. The void and reissue may create a problem with unemployment excess. Review the Payroll Wage and Tax History Report for the unemployment figures on all 3 checks. If they are different figures, it will be necessary to run the PR Error Recovery function #3, Unemployment Tax Amount Update.

If the month IS closed or you have issued financial statements and cannot reopen the dates:

1. Use the positive/negative time card lines in the same Payroll cycle.

1. Burden adjustments need to be handled manually-- either with a journal entry or Job Cost Transaction Entry.

1. If either of these jobs are certified, navigate to Payroll > Period End > Employee Certified
 History. Call up the employee code and check number. Select the Time Card button and correct
 the work date and/or certified flag as necessary.
