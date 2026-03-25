---
title: "PR 401(k) Catch-up Eligibility | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/payroll-reports/payroll-reports-united-states-specific-reports/pr-401k-catch-up-eligibility"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/payroll-reports/payroll-reports-united-states-specific-reports/pr-401k-catch-up-eligibility"
---

# PR 401(k) Catch-up Eligibility

You can use the US-specific PR 401(k) Catch-up Eligibility
 report to verify compliance with the SECURE 2.0 Act of 2022. The report is designed as an
 audit tool to identify high-earning employees who still have a non-Roth (pre-tax) catch-up
 deduction assigned. To run the report, go to Payroll > Reports > PR 401(k) Catch-up Eligibility.
Report ID: 1339
Eligibility for 401(k) catch-up is determined by an employee's age as of
 December 31st of the current tax year. If an employee's previous year's FICA wages
 exceed the threshold, the catch-up contribution must be Roth. The threshold comes
 from the Pre-Tax Deduction Group linked to the deduction code (see [Roth Catch-up FICA Wage Threshold](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-pre-tax-deduction-groups-form/field-definitions-pr-deduction-groups-form#concept-73e42c7f-240c-4fc3-9743-0d4316bac5e1--en) field), or the company's first Pre-Tax Deduction Group if unassigned.
The report displays employee information including name, hire date, termination date, birth date, active status, and age as of December 31st.
Report Parameters
Description
PR Company
*Required*
Accept the default, or press F4 to select a company.

Tax Year
*Required*
Enter the tax year.
Employees
Enter specific employee numbers. Separate with commas.

Beginning PR Group
Click the Field Lookup
 button or press F4 to select the beginning PR group.

Ending PR Group
Click the Field Lookup
 button or press F4 to select the ending PR group.

Print (A)ll Eligible, (R)oth Required, Has
 (C)atch-up Deductions, or (E)xceptions
*Required*
A: All Eligible Employees – displays all
 employees age 50 or older regardless of wages or deduction
 codes
R: Roth Required – displays employees age
 50 or older whose FICA wages exceed the threshold
C: Has Catch-Up Deductions – displays only
 employees age 50 or older who exceed the wage threshold and have
 at least one catch-up deduction code assigned
E: Exceptions – displays only employees
 age 50 or older who exceed the wage threshold and have at least
 one non-Roth (traditional) catch-up deduction code, specifically
 identifying employees using traditional catch-up contributions
 who may need to transition to Roth contributions for SECURE 2.0
 Act compliance

Active employees only?
Select the checkbox to limit the report to show only active
 employees.
Leave blank to include active employees plus inactive employees
 with earnings in the current tax year.

Display catch-up codes only?
Select the checkbox to show only catch-up deductions.
Leave blank to display all deductions marked pre-tax.
