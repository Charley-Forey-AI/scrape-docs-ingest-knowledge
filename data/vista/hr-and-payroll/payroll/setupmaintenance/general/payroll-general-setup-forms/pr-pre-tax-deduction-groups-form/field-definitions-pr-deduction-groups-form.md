---
title: "Field Definitions: PR Deduction Groups Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-pre-tax-deduction-groups-form/field-definitions-pr-deduction-groups-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-pre-tax-deduction-groups-form/field-definitions-pr-deduction-groups-form"
---

# Field Definitions: PR Deduction Groups Form

The following is a list of field descriptions for the PR Deduction Groups form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Pre-Tax Group

The Pre-Tax Group field on the PR Pre-Tax Deduction Groups form.
Enter a number (0-255) to identify this pre-tax deduction group.

## Description

The Description field on the PR Pre-Tax Deduction Groups form.
Enter a description of this pre-tax deduction group, up to 30 characters.

## Standard Contribution Limit

The Standard Contribution Limit field on the PR Pre-Tax Deduction Groups form, Annual Limits section.
Enter the standard annual limit amount for employee 401(k) contributions. The annual limit must be a positive number (greater than 0.00).
The limit you set here applies to all deduction codes associated with this pre-tax deduction group (Pre-Tax Group field, PR Deductions/Liabilities). This limit cannot be overridden.

## Catch-up Contribution Limit #1

The Catch-up Contribution Limit #1 field on the PR Pre-Tax Deductions Groups form, Annual Limits section.
Enter the annual 401(k) catch-up contribution limit for employees aged 50 and over.
The system applies the limit specified here across multiple catch-up deductions. For example, if an employee contributes to both a traditional 401(k) and a Roth 401(k), with an annual limit of $6,000, the system applies this limit across both plans.
Note: Secure Act 2.0 allows for an increased catch-up limit for employees meeting the minimum/maximum age requirements. The system automatically applies the higher limit (designated in the Catch-up Contribution Limit #2 field), when the employee reaches the minimum age, and then returns to the standard limit specified here when the employee reaches the maximum age. For an explanation of how the system determines an employee's minimum/maximum age eligibility, see [PR Pre-Tax Deduction Groups Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-pre-tax-deduction-groups-form).

## Compensation Limit

The Compensation Limit field on the PR Pre-Tax Deduction Groups form, Annual Limits section.
Enter the annual compensation limit to apply to all 401(k) employer match liabilities.
The system applies the limit specified here across multiple 401(k) employer match liabilities. For example, if you set up employer match liabilities for both traditional 401(k) and Roth 401(k) employee contributions, the system applies this limit across both plans.

## Catch-up Contribution Limit #2

The Catch up Limit #2 field on the PR Pre-Tax Deduction Groups form, Secure Act 2.0 Annual Limit section.
Enter the annual contribution limit (defined by the IRS) for Secure Act 2.0 catch-up contributions. Applies to employees within the specified Minimum Age / Maximum Age range.
The system applies the limit specified here across multiple catch-up deductions. For example, if an employee contributes to both a traditional 401(k) and a Roth 401(k), with an annual limit of $6,000, the system applies this limit across both plans.
Note: The system determines an employee's eligibility for this contribution based on the age of the employee by December 31st of the tax year. If the employee reaches the minimum age by December 31st, the system applies this limit beginning in January of that year. If the employee exceeds the maximum age by December 31st of the tax year, the standard catch-up limit applies beginning in January of that year.

##  Minimum Age

The Minimum Age field on the PR Pre-Tax Deduction Groups form, Secure Act 2.0 Annual Limit section.
Enter the minimum age requirement (defined by the IRS) employees must meet to be eligible for the Secure Act 2.0 catch-up contribution limit.
Note: The value defined here is used in conjunction with the specified Maximum Age to determine an employee's eligibility. Eligibility is based on the employee's age by December 31st of the tax year. If they reach the minimum age by that date, the higher limit applies from January 1st of that year. If they exceed the maximum age by December 31st of the tax year, the standard limit applies beginning January 1st of that year.

##  Maximum Age

The Maximum Age field on the PR Pre-Tax Deduction Groups form, Secure Act 2.0 Annual Limit section.
Enter the maximum age (defined by the IRS) employees must meet to be eligible for the Secure Act 2.0 catch-up contribution limit.
Note: The value defined here is used in conjunction with the specified Minimum Age to determine an employee's eligibility. Eligibility is based on the employee's age by December 31st of the tax year. If they reach the minimum age by that date, the higher limit applies from January 1st of that year. If they exceed the maximum age by December 31st of the tax year, the standard limit applies beginning January 1st of that year.

## Roth Catch-up FICA Wage Threshold

The Roth Catch-up FICA Wage Threshold
 field on the PR Pre-Tax Deduction Groups form, Secure Act 2.0 Annual Limit
 section.
Enter the specific dollar amount of the FICA wage limit for the prior calendar
 year.
If an employee's previous year's FICA wages exceed the threshold, and that employee is
 age 50 or older, any additional catch-up contributions for the current year must be Roth
 (after-tax).
You can run the PR 401(k) Catch-up Eligibility report to identify
 high-earning employees who still have a non-Roth (pre-tax) catch-up deduction assigned.
 For more details, see [PR 401(k) Catch-up Eligibility](/en/vista/vista/reports-catalog/payroll-reports/payroll-reports-united-states-specific-reports/pr-401k-catch-up-eligibility).
