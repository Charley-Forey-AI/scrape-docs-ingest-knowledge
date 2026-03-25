---
title: "Set Up Smart Payroll | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/time-entry/trimble-smart-payroll/set-up-smart-payroll"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/time-entry/trimble-smart-payroll/set-up-smart-payroll"
---

# Set Up Smart Payroll

You can use Smart Payroll to enhance your operational efficiency, help you stay compliant, and support you in making informed decisions about your payroll.
Smart Payroll works by identifying timecard discrepancies based on employee history and/or compliance rules (depending on enabled rules and compliance settings), and then allowing you to accept the discrepancies or correct them before posting the timecards.In order to use the Smart Payroll feature, there are specific setups you must do before payroll validation can occur.

1. [Set Up State Compliance Information](/en/vista/vista/administration/headquarters/company-setup/set-up-state-compliance-information). Using the HQ State Compliance form, configure the applicable compliance settings (such as the Department of Labor and Department of Revenue requirements) for each country, state, and effective date combination.

1. In PR Company Parameters, select the Enable Timecard Compliance checkbox (Info tab). You must select this checkbox before you can set up timecard validation rules. If you do not select this checkbox, you will be unable to access the PR Timecard Validation Rules form.

1. In PR Employees (Add'l Info tab), select the FLSA Exempt checkbox for each employee that is exempt under the Fair Labor Standards Act (FLSA). The system checks this flag during the timecard validation process to determine whether certain compliance rules apply to the employee.

1. [Configure Timecard Validation Rules](/en/vista/vista/hr-and-payroll/payroll/time-entry/trimble-smart-payroll/configure-timecard-validation-rules). Using the PR Timecard Validation Rules form, select which validation rules to enable, set their severity levels, and then configure their parameters.

You are now set up for Smart Payroll. When you select to process a timecard batch (in PR Timecard Entry), the system checks for discrepancies based on employee history and/or compliance rules (depending on enabled rules and compliance settings) and provides a list of violated rules. For more information, see [PR TimeCard Compliance Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/trimble-smart-payroll/smart-payroll-forms/pr-timecard-compliance-form).
