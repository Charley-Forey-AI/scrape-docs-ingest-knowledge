---
title: "PR W2 FLSA Qualified Overtime Premium | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/payroll-reports/payroll-reports-united-states-specific-reports/pr-w2-flsa-qualified-overtime-premium"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/payroll-reports/payroll-reports-united-states-specific-reports/pr-w2-flsa-qualified-overtime-premium"
---

# PR W2 FLSA Qualified Overtime Premium

You can use the US-specific PR W2 FLSA Qualified Overtime
 report to verify compliance with the new federal income tax deduction for qualified overtime
 compensation (QOC), introduced in the One Big Beautiful Bill Act. For the tax year that you
 specify, this report prints a week-by-week calculation of the FLSA QOC premium amount for
 the employee, as well as the employee's year-to-date sum total of QOC. To run the report, go
 to Payroll > Reports > PR W2 FLSA Qualified Overtime
 Premium.
Report ID: 1340
Report Calculation Process:
For each payroll group, the first workweek is defined by finding the earliest
 beginning date among all regular pay periods whose Limit Month values fall within
 the tax year (even if that date is in the prior year). This date is set as the
 official first day of the first workweek, and all seven-day workweeks for the year
 are established from that point forward.
To make the Premium Calculation, for each employee, the report
 aggregates hours and pay from hourly timecards paid within the tax year across these
 workweeks.

- Premium
 Hours: These are all hours worked *over 40 hours* in a given
 workweek.

- Premium
 Rate: This rate is *one-half (0.5x)* the *weighted
 average straight-time hourly rate* for the employee for that
 week.

- Weekly
 Premium Amount = Premium Hours ×
 Premium
 Rate

The YTD total, the sum of all weekly premium amounts for the year,
 is the final reportable FLSA QOC
 premium amount for the employee's W-2 form.
Note:Premium Hours (hours over 40)
 are calculated independently of standard payroll Overtime Hours (hours paid
 using a factor >1.0), meaning the two values for any given week are not
 necessarily the same.

FLSA QOC Reporting:
In 2026, an employee's FLSA QOC amount is reported on their W-2
 form in Box 12 using Code TT. FLSA QOC is referenced in following areas in
 Vista:

- PR W-2 Employee Edit form, [QOC
 Premium Amount](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/w-2s/pr-w-2-employee-edit-form/field-definitions-pr-w2-employee-edit-form#concept-6ea5bf4d-ace7-4251-8598-087aacbb4217--en) field

- PR W2
 Preview Report, #867

- [PR
 W2 Employee Copies Report](/en/vista/vista/reports-catalog/payroll-reports/payroll-reports-united-states-specific-reports/pr-w2-employee-copies-report), #1334

- PR W2 FLSA
 Qualified Overtime Premium Report, #1340

- Aatrix W-2
 file

Report Parameters
Description
Company
*Required*
Accept the default, or press F4 to select a company.

Tax Year
*Required*
Enter the tax
 year.
Beginning Employee Number
Select the Field Lookup button or press F4 to select the beginning employee number.

Ending Employee Number
Select the Field Lookup button or press F4 to select the ending employee number.

Beginning Employee Sort Name
Select the Field Lookup button or press F4 to select the beginning employee sort name.

Ending Employee Sort Name
Select the Field Lookup button or press F4 to select the ending employee sort name.

Show Only Employees with FLSA QOC
Select the checkbox to limit the report to only show
 employees with some QOC (premium hours) in the tax year.

Sort By Employee (S)ort Name or
 (N)umber
Enter S or N.

Page by Employee
Select the checkbox to have the report create a new page per
 employee.

Truncate Employee SSN
Select the checkbox to hide all but the last four digits of
 the employee's SSN.
