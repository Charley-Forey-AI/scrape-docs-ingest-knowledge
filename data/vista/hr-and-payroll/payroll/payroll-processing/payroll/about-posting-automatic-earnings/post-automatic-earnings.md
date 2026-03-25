---
title: "Post Automatic Earnings | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-posting-automatic-earnings/post-automatic-earnings"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-posting-automatic-earnings/post-automatic-earnings"
---

# Post Automatic Earnings

You will use PR Post Auto Earnings to automatically post predefined employee earnings (in PR Automatic Earnings).
The following instructions detail how to post automatic earnings.
Note: Before posting automatic earnings with this form, make sure to post manually entered timecards (in PR Timecard Entry). Any automatic earnings that are based on other earnings must have the other earnings posted first.

1. Double-click the PR Post Auto Earnings icon in the PR Programs folder on the Main Menu.The Batch Selection form displays.

1. Make sure that the information in the Batch Month, PR Group, PR End Date, and Pay Seq fields is accurate and click OK.The PR Post Auto Earnings form displays.

1. If you want to restrict automatic earnings posting by a specific employee, select the Restrict by Employee checkbox and enter the employee number in the Employee field. Press F4 from the Employee field to see a list of valid employees.

1. If you want to restrict automatic earnings posting to a single payment sequence, select the Restrict posting to a single Payment Seq# checkbox and enter the sequence in the Payment Seq# field. Note: If you do not choose to restrict automatic earnings posting by specifying an employee or a payment sequence, the system will bring in all employees and sequences for the pay period.

1. In the Timecard Date field, enter the date to use as the actual posting date for each new timecard. Note: A warning displays if this date is outside the date range of the pay period.

1. Select the Delete and replace if timecards... checkbox if you want to delete existing timecards with the same employee, pay sequence, and earnings code. Note: You would check this box if you have already processed automatic earnings and you need to make a change or delete any existing entries.

1. Click Process.The system displays a confirmation message.

1. Click Close.The employees matching the criteria display in the grid.

1. Select File  Process Batch.The PR Batch Process form displays.

1. [Process the batch](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/pr-batch-process-form). The system then calculates earnings for each of the earnings codes specified for the employee.
Tip: To see how the system posted automatic earnings, view the Batch List report from the PR Batch Process form after you validate the batch.
Note: Negative earnings (e.g., 401(k), Section 125, etc.) and other non-taxable earnings (earnings that do not have the True earnings for Payroll Reports box checked in PR Earnings Codes) are automatically distributed across all tax states that the employee worked in. This ensures that the tax benefits of these "earnings" are applied to the state(s) where taxes are paid.
Note: For example, if an automatic earnings entry for 401(k) is set up as –10% of gross for an employee, and he earns $500 in Oregon and $600 in Washington state within the pay period/sequence, the form generates two 401(k) timecard entries during processing. The first timecard entry would be $–50 with an OR tax state and the second entry would be $–60 with a Washington tax state.

You can now [process your pay period](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/processing-payroll/processing-a-payroll-period).

Related information

- [About the PR Post Auto Earnings Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-the-pr-post-auto-earnings-form)
