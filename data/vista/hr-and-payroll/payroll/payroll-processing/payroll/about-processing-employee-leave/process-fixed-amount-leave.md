---
title: "Process Fixed Amount Leave | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-processing-employee-leave/process-fixed-amount-leave"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-processing-employee-leave/process-fixed-amount-leave"
---

# Process Fixed Amount Leave

Follow these instructions to process fixed amount leave codes.

The instructions below assume that you are following these procedures at the start of the reset date period (frequency) associated with either the limits or the fixed accrual.Note: Reset dates are associated with individual employees. The Last Date Reset fields in PR Employee Leave determine the start date for the limit frequency. For more information, see [PR Employee Leave Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-leave-form).

Note: If you have inactive leave codes at either the leave code level (in PR Leave Codes) or employee leave code level (in PR Employee Leave), the system skips accruals and usage for these codes during leave processing.

1. Reset accrual limits and/or leave balance limits, as necessary, using [PR Leave Code Reset](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-code-reset-form). If you have not set limits on your leave code, you do not need to perform this step.Note: You may need to reset each option at different times, depending on the specified frequency for each one. For example, if the reset frequency for Accrual Limit #1 is monthly, you would run the reset for that accumulator each month. At the same time, if you had an Available Balance reset frequency of yearly, you would only run the balance reset once a year.

1. Update fixed accruals using PR Auto Leave Accrual/Usage. This updates each associated employee with the accrual amount defined for the frequency. For more information, see [Update Fixed Amount Accruals](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/update-fixed-amount-accruals).

1. Post usage information either manually using PR Leave Entry automatically by PR group using PR Auto Leave Accrual/Usage. Typically, this is run once per pay period to ensure that you have accurate leave records.Note: You can use PR Leave Entry to modify entries created by PR Auto Leave Accrual/Usage. Additionally you can use PR Leave Entry to post the auto-created leave entries.

1. Repeat the previous steps at the start of the next frequency period (limit or fixed amount).
