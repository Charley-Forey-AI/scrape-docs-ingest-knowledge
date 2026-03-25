---
title: "Set Holiday Week Overtime | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/set-holiday-week-overtime"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/set-holiday-week-overtime"
---

# Set Holiday Week Overtime

The following instructions detail how to set up holiday week overtime.
Click [here](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/set-holiday-week-overtime-canada) for information on setting up holiday week overtime for Canada.
If you need to compute automatic overtime pay for holiday weeks during weekly or bi-weekly pay periods, you can use the Maximum Regular Hours in Week 1 and the Maximum Regular Hours in Week 2 fields in PR Pay Period Control to set regular time hours. These fields default to 40.00. If the maximum regular hours are less than 40.00 (e.g., a holiday falls during the week), set the fields appropriately. If employees work beyond that initial setting for the holiday week, they are paid at an overtime rate for the additional hours (based on the Automatic Overtime settings in PR Company Parameters).
Note: This function is using a weekly overtime calculation, so if an employees only work on the holiday, and do not have any other hours that week, they do not receive the holiday pay rate.
Note: This functionality does not apply to employees associated with a salaried earnings code.

1. Make sure that the correct employees are set up for holiday week overtime. In PR Employees, the Overtime field (Add'l Info tab) should be set to W-Weekly.

1. When creating a weekly pay period (in PR Pay Period Control), enter the maximum regular hours that employees can work for this pay period in the Maximum Regular Hours in Week 1 field.

1. When creating a bi-weekly pay period, enter the maximum regular hours that employees can work for the first week in the pay period in the Maximum Regular Hours in Week 1 field, and enter the maximum number for the second week in the Maximum Regular Hours in Week 2 field.

1. [Set up a holiday for the pay period](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-setting-holidays-for-pay-periods).

1. Save the pay period record as normal. These settings may be overridden for craft. See [Holiday Week Overtime by Craft](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-holiday-week-overtime-by-craft) for more information.

Related information

- [PR Pay Period Control Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/pr-pay-period-control-form)

- [Set Up Single-Month Pay Periods](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/set-up-single-month-pay-periods)

- [Set Up Split-Month Pay Periods](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/set-up-split-month-pay-periods)

- [PR Automatic Earnings Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-automatic-earnings-form)

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)
