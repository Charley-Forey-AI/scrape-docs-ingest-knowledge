---
title: "About Setting up Automatic Overtime | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-up-automatic-overtime"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-up-automatic-overtime"
---

# About Setting up Automatic Overtime

The Automatic Overtime controls in PR Company Parameters help you customize whether overtime is automatically calculated or manually posted.
If you are using automatic overtime, timecards can be processed and overtime entries generated with the PR Automatic Overtime Posting form. The PR Timecard Entry form will not display warnings if an Employee exceeds the standard number of hours per day, or 40 hours per week. If you are not using automatic overtime, then the Automatic Overtime form cannot be run and warnings will be displayed when entering timecards if the standard number of daily or weekly hours is exceeded.
You can have the system determine automatic overtime in three different ways: by timecard entry, craft/class, or by whichever rate is highest (this includes the employee rate from PR Employees).

- [Set Automatic Overtime to Use the Timecard Rate](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-up-automatic-overtime/set-automatic-overtime-to-use-the-timecard-rate#task-6759--en__task-6759)

- [Set Automatic Overtime to Use the Craft/Class Rate](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-up-automatic-overtime/set-automatic-overtime-to-use-the-craftclass-rate#task-2173--en__task-2173)

- [Set Automatic Overtime to Use the Highest Available Rate](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-up-automatic-overtime/set-automatic-overtime-to-use-the-highest-available-rate#task-1430--en__task-1430)

For all options above, the system determines the earnings code using the overtime schedule associated with the employee (OT Schedule field, PR Employees). The exception is weekly overtime calculations which use the earnings code you entered in the Overtime Earnings Code field.
Note: If you post timecards for an employee in a way that differs from the employee's assigned overtime type (Overtime field, PR Employees), weekly overtime rules apply. For example, if you selected J-Job from the Overtime field for an employee, but the employee's timecards were not posted to any jobs, the system will use weekly overtime rules to determine overtime hours. The overtime rate is then determined by the posted rate of the last timecard entered, multiplied by the factor defined for the overtime earnings code assigned in PR Company Parameters (Overtime Earnings Code field).

If you are using weighted average overtime rates, the methods specified here for determining overtime rates do not apply. For more information, see [Weighted Average Overtime Rates](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-up-automatic-overtime/weighted-average-overtime-rates).

Related information

- [Set Pay Stub Attachment Options](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-payment-report-information/set-pay-stub-attachment-options)

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)
