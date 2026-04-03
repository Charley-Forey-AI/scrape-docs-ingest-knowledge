---
title: "Check Calculation | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/check-calculation"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/check-calculation"
---

# Check Calculation

The Check Calculation screen updates time card information
 onto employee paychecks.
It should only be executed after the Time Card Edit List has been
 printed and checked for errors. While the software will validate the 'direct cost' settings
 during Check Calculation, it is important to note that the user is responsible for proper
 setup of add-on codes, including 'calculation methods', 'paid to employee on paycheck'
 settings, and the associated G/L accounts.

- Check Calculation includes calculations based on the Payroll formula variables
 that are available in the Payroll > Formula File Maintenance screen. For convenience during the Check Calculation, FICA deductions
 for Social Security and Medicare are computed and stored for manual checks. The
 system calculates additional Medicare withholding when the employee year-to-date
 Medicare subject-to earnings exceed the mandated 'annual threshold'. If necessary,
 you can choose to override the computation. Other deductions and adjustments of the
 manual check require your input unless transferred from Layoff Check Entry or
 Replacement Check Entry.

- The Payroll tax tables allow an unlimited number of income tax filing statuses to be created in order to accommodate those who need the ability to set up more than four filing statuses for income tax withholding tables. In addition, the Payroll Manager can choose the name for these codes in order to match them with the filing statuses defined by the particular tax table code.

- If an employee has been assigned a permanent unemployment state in the
 Employee Tax Setup screen, Check Calculation computes the
 unemployment for that state instead of the resident state and work state for Regular
 and Manual checks.

- The Payroll Check Calculation will compute 'Subject to' amounts and 'Tax' based on 'Tax Effect' settings for add-ons not paid to the employee on the check. This significantly streamlines the process of recording certain taxable non-cash benefits, such as Life Insurance over $50,000 and Personal use of Company Vehicle.

- Check Calculation will apply limits to union add-ons and deductions based on setup in the [New/Edit Deduction/Add-on Code - Limits](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code/newedit-deductionadd-on-code---limits) tab.

- If the Limit basis
 specified in Worker's Compensation Code Maintenance is set to
 this state only the
 update will calculate unemployment based on the year-to-date subject to earnings and
 excess earnings for unemployment for the designated tax code only.

- The software will determine the applicable worker's compensation rate/$100 limit by summing subject-to earnings from Worker's Compensation History table and current pay cycle since the effective start date. If the Limit basis = All codes in this state, the software includes all records for the specified state between 'Start date' and 'Check date'.

- The portion of the Check Calculation that generates entries to allocate recurring add-on amounts by time card will conditionally assign the "Burden" phase and/or cost type from Job Payroll Setup for the Job code specified on the time card. If a "Burden" cost type is defined for the job, then this screen will assign that cost type. Otherwise, if the field is <blank> in Job Payroll Setup, the cost type from the time card line will be used. If the recurring add-on has been assigned the non-standard fringe calculation method, the add-on amount will be skipped.

- The Payroll Check Calculation also computes worker's compensation costs on recurring add-on amounts that are calculated 'by time card'. This calculation occurs when the particular add-on code is configured to 1) calculate by 'by time card', AND 2) flagged for 'Tax Effect' for worker's compensation in the particular jurisdiction in [Deduction / Add-on Code Maintenance](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance) 'Rate per hour' worker's compensation calculations are not applicable here because the 'Rate per hour' calculation only applies to lines with an hourly pay type.

- The Check Calculation and the Layoff Check Calculations will use exemptions on
 permanent work state, county and local tax codes specified on the Employee
 Tax Setup screen.

- If related tax codes have been set up for the employee code, the Check Calculation will
 calculate tax for each of the time card records.

Regarding Exempt and Foreign Employees: If the
 employee's federal tax status is set to 'Exempt', the Foreign employee checkbox must also be selected for the update to succeed.

 Check Calculation uses the Federal code specified for the employee. For Canadians
 specifically, the calculation of 'subject to' earnings for Employee and Employer State
 Disability Insurance uses the "Basic exemption" specified in the [New/Edit Tax Table - Other Taxes](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/tax-table-maintenance/newedit-income-tax-details---properties-tab/newedit-tax-table---other-taxes)
 tab.
For employees: after calculating the employee 'subject to' earnings for
 this check and before calculating the employee SDI tax, the Basic Exemption is applied, if
 any. 6
For employers: the same procedure detailed for employee SDI 'subject to'
 earnings the employer 'subject to' SDI earnings are adjusted using the Basic exemption'
 value.

Related information

- [Check Calculation Error Report](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/check-calculation/check-calculation-error-report)

- [Unemployment Hierarchy for Regular and Manual Checks](/en/spectrum/spectrum/accounting/payroll/default-hierarchies-overview/unemployment-hierarchy-for-regular-and-manual-checks)
