---
title: "Update Fixed Amount Accruals | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/update-fixed-amount-accruals"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/update-fixed-amount-accruals"
---

# Update Fixed Amount Accruals

How often you need to update accruals for fixed-amount leave codes depends on the frequency specified in PR Leave Codes.
If you will be updating a leave code with limits (either accrual limits or available balance limits) you must first reset the accrual accumulators or leave balance settings. For more information, refer to [About Processing Employee Leave](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-processing-employee-leave).
If employees accrue a fixed amount of leave per year, you will update the accrual amount yearly. Fixed amount accruals are reset using PR Auto Leave Accrual/Usage.
The following instructions describe how to update accruals for fixed-amount leave codes using PR Auto Leave Accrual/Usage.

1. In the PR Leave Entry form, select File > Leave Accrual Usage Init. The PR Auto Leave Accrual/Usage form displays.

1. Select the Update Fixed Accruals checkbox.The system enables the other fields in the Fixed Accruals section of the form.

1. In the Accrual Date field, enter the posting date for accruals.

1. Determine which leave codes are updated by selecting the appropriate radio button in the Leave Code section:

- All

- Selected

1. If you chose to include a selected leave code, use the Leave Code field to enter the leave code (must be active) or press F4 for a list of valid active leave codes.Note: The system does not allow entry of an inactive leave code. However, if you enter an active leave code, but the leave code is inactive for the employee (in PR Employee Leave), that leave code is skipped during initialization.

1. Determine which frequency this applies to by selecting the appropriate radio button in the Frequency section:

- All

- Selected

1. If you chose to include a selected frequency code, use the Frequency field to enter the specific frequency or press F4 for a list of valid frequencies.

1. (Optional) In the Description field, enter a description for this fixed accrual.

1. If you want the system to delete existing accrual entries for the specified date, select the Delete Any Existing Accruals checkbox.The system replaces all previously posted fixed accruals and adjusts balances accordingly.
Note: Use this option if you need to rerun a fixed accrual update because of an error.

1. Click Update.The system displays a confirmation message; click Close. You are returned to the PR Leave Entry form, where you can review the leave entries.Note: The update process includes only active employees and leave codes; if inactive employees and leave codes are found, they are skipped.

1. Select File > Process Batch. The PR Batch Process form displays.

1. [Process the batch](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/pr-batch-process-form).

Related information

- [PR Auto Leave Accrual/Usage Form](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-auto-leave-accrualusage-form)

- [PR Leave Codes Form](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-codes-form)

- [PR Leave Entry Form](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-entry-form)
