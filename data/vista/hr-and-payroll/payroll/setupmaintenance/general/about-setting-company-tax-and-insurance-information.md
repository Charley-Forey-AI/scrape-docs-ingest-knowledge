---
title: "About Setting Company Tax and Insurance Information | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information"
---

# About Setting Company Tax and Insurance Information

You can use the State/Local tab of PR Company Parameters to
 set up the tax, unemployment, and insurance defaults for each company in the system.
The settings on this tab determine if tax, unemployment, and insurance information defaults from the job that an employee works on, or if the information defaults from the employee record in PR Employees. If you set the information to default based on the job, this setting affects all employees in the system; however you can override this setting in PR Employees as necessary.

- Defaulting Tax and Insurance Information from Jobs - If you
 want to use tax, unemployment, or insurance information from a job when entering
 timecards, check the appropriate boxes on the State/Local tab. For example, if
 you want to use the tax state that is specified on the job, check the Use Job, SM
 Work Order or Office State for Tax State box. In this case, when
 you enter timecards for an employee, the system will use the state specified for
 the job in JC Jobs (PR State field). For
 employees who do not work on jobs (e.g., office clerical workers), the system
 defaults information from PR Employees. In the case where you have non-job
 employees who live in a different state or city/county from where your office is
 located, enter the applicable state in the Office State field, or the
 appropriate local code in the Office Local field, for your
 office location. This allows the system to use the correct information for the
 non-job employees on your payroll.Note: If you
 do not enter a state or local code in the Office
 State or Office Local fields, the
 system uses the information from the Work Office Tax State or
 the Work Office Local Code fields in PR Employees. If those
 fields are blank, the system uses the Resident Tax State or the
 Resident Local Code fields in PR Employees.

- Defaulting Tax and Insurance Information from SM Work Orders
 - If you want to use tax, unemployment, or insurance information from SM work
 orders when entering timecards, check the appropriate boxes on the State/Local
 tab of PR Company Parameters. For example, if you want to use the tax state that
 is specified on the work order, check the Use Job, SM Work Order or Office State
 for Tax State box. In this case, when entering SM Work Order
 timecards for an employee, the system will use the state specified on the work
 order in SM Work Orders (PR State field).Note: If you do not enter a PR State on the work
 order or if you always use the employee's resident/work office information
 (Always use Employee's Work/Resident checkboxes are selected
 in PR Employees), the system defaults information from PR Employees.


- Defaulting Tax and Insurance Information from Employee
 Records - If you are not using jobs or work orders to determine the tax,
 unemployment, and insurance information defaults for timecard entries, set up
 the information for each employee in PR Employees. In the event that an office
 worker lives in a different state from where your office is located , you can
 enter your office state or local code in the Office
 State or Office Local fields on PR
 Company Parameters. This allows the system to determine if there is a reciprocal
 agreement between the two states. In this case, the system defaults the state
 specified in PR Employees when you are entering timecard information in PR
 Timecard Entry. See [Setting Employee Tax and Insurance Information ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information)
 for more information.

Related information

- [Secure EFT Data Files](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-payment-report-information/secure-eft-data-files)

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

- [JC Jobs Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)

- [About the PR Timecard Entry Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form)
