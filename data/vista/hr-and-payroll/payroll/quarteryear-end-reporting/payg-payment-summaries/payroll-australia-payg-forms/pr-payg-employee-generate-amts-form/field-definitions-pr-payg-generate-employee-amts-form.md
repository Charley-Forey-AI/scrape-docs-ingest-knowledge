---
title: "Field Definitions: PR PAYG Generate Employee Amts Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/payroll-australia-payg-forms/pr-payg-employee-generate-amts-form/field-definitions-pr-payg-generate-employee-amts-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/payroll-australia-payg-forms/pr-payg-employee-generate-amts-form/field-definitions-pr-payg-generate-employee-amts-form"
---

# Field Definitions: PR PAYG Generate Employee Amts Form

The following is a list of field descriptions for the PR PAYG
 Generate Employee Amts form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Employee

Employee field on PR PAYG Employee Generate Amts form.
To generate amounts for one employee, enter
 the number for that employee or press F4 to select from a list of employees.
 You will typically only enter a single employee for part-year summaries.
To generate amounts for all employees, leave the field blank. When this field is left blank, the system assumes you are generating year-end summaries and automatically sets the Process Through Date to 30/6/YY (which cannot be changed).

Related information

- [Generate Employee PAYG Amounts for a Single Employee (Part-Year Summary)](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/about-part-year-payg-payment-summaries/generate-employee-payg-amounts-for-a-single-employee-part-year-summary)

- [PR PAYG Employee Generate Amts Form](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/payroll-australia-payg-forms/pr-payg-employee-generate-amts-form)

## Process Through Date

Process Through Date field on the PR PAYG Employee Generate Amts form.
This field is only enabled when you enter an
 employee in the Employee field.
For part-year summaries, enter the date through which to process summaries for the selected employee. If you entered a Period End Date for the employee's current reporting period (in PR Employees, PAYG Reporting Periods tab), enter that same date here.
 If you did not enter a Period End Date for the current reporting period, enter the period end date for the summary. The date entered here will be used as the Period End Date for the reporting period once the summary is generated.
For year-end summaries, this field is set to 30/6/YY for the selected Tax Year and disabled.
During the summary generation process (on-demand and year-end summaries), the system creates a single summary for each reporting period (in the Tax Year) up through the Process Through Date.
 If you have previously run summaries for the
 employee, the Startover: Overwrites All Existing Summaries in Tax Year checkbox
 determines which reporting periods are included in the summary generation. If you select
 this checkbox, the system deletes all existing summaries and regenerates summaries for all
 applicable reporting periods. If you do not select this checkbox, the system starts from
 the first reporting period that is not associated with a summary number.

Related information

- [Generate Employee PAYG Amounts for a Single Employee (Part-Year Summary)](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/about-part-year-payg-payment-summaries/generate-employee-payg-amounts-for-a-single-employee-part-year-summary)

- [PR PAYG Employee Generate Amts Form](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/payroll-australia-payg-forms/pr-payg-employee-generate-amts-form)

## Startover: Overwrites All Existing Summaries in Tax Year

Startover: Overwrites All Existing Summaries in Tax Year field on the PR PAYG Employee Generate Amts form.
Select this checkbox to replace existing summaries for the specified Tax Year. During the summary generation process, the system will delete all existing summaries for the tax year and replace them with new summaries.

- If you processed summaries at mid-year, you must select this checkbox when running year-end summaries to ensure that employees with multiple summaries get accurate values.

- The system will not overwrite manually entered summaries unless there is a matching period of reporting record (in PR Employees, Period of Reporting tab) for the employee.

If you do not select this checkbox, the system will leave existing summaries intact and begin summary generation from the first reporting period that is not associated with a summary number.

Related information

- [Generate Employee PAYG Amounts for a Single Employee (Part-Year Summary)](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/about-part-year-payg-payment-summaries/generate-employee-payg-amounts-for-a-single-employee-part-year-summary)

- [PR PAYG Employee Generate Amts Form](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/payroll-australia-payg-forms/pr-payg-employee-generate-amts-form)
