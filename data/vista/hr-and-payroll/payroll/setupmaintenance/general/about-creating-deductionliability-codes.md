---
title: "About Creating Deduction/Liability Codes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes"
---

# About Creating Deduction/Liability Codes

 Deduction codes define amounts deducted from an employee's pay, such as federal or state/provincial taxes and pre-tax deductions. Liability codes define employer expenses, such as craft benefits.
The system uses a specific hierarchy for processing and displaying codes, so it is recommended that you develop a numbering scheme, or code sequence, to enable easier maintenance.
When processing deduction/liability codes, the system first processes pre-tax deductions assigned at the craft level, and then pre-tax deductions assigned to the employee. The system then processes standard deduction/liability codes by their associated category (the Calculation Category field) and in the following order: Federal, State/Provincial, Local, Craft, Insurance, Employee, and Any.
Note: When processing State/Provincial codes, the system applies pre-tax deduction amounts proportionately to each state/province that the employee worked in.

When processing a particular category, the system processes codes in numerical order. For example, if an employee has two federal deductions (Federal Code #3 and Federal Code #25, for example), the one with the lower number is processed first (#3).
Additionally, codes print in numeric order on checks and reports, and the system sorts them numerically when displaying F4 lookups.
Due to this hierarchy, the following suggestions are recommended when creating deduction and liability codes:

- Group deductions and liabilities separately. For example, assign deductions to code numbers 1-499 and liabilities to numbers 500-999. This makes it convenient to view codes in the system and on reports. If you are using pre-tax deductions, you should keep them separate from other deductions in their own grouping. However, pre-tax deductions are always processed first, so their numbering system is not as crucial as other deductions.

- Group code categories together (e.g., all Federal-type codes together, all Local-type codes together, etc.). This makes it convenient to look up codes in the system and on reports.

- Assign numbers to codes associated with a specific category in processing order. That is, if the system should process one Federal code before another, it should have a lower deduction/liability code number.

- Consider leaving blank code numbers between individual codes or category groups; this enables you to add additional codes in the future, as necessary.

## Preserve Zero-Amount Records in Pay Sequence

By default, once you've processed a payroll, the PR Employee Pay Seq Control form only shows non-zero amount deduction/liability records for an employee/pay sequence. However, if you prefer to see all payment sequence records, even if they have zero amounts, you can do so by selecting the Preserve zero-amount records in pay sequence checkbox for each applicable deduction or liability in PR Deductions/Liabilities. When you assign the deduction/liability codes to employees (in PR Employee Dedns/Liabs), make sure you select the Employee-Based checkbox.

## Canadian Users

When processing CPP and CPP2 deduction codes, the system checks the age of an employee before calculating CPP. If the employee is over 18 years old or less than 70 years old, the system will calculate CPP. Otherwise, the system does not calculate CPP. The system uses the pay period ending date to determine the last pay day in the month for when employees turn 70. For more information, see [Set up CPP / CPP2 Deductions: Canada](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-cpp--cpp2-deductions-canada).

## Quebec Users

The system also processes Quebec Pension Plan (QPP and QPP2) and Quebec Parental Insurance Plan (QPIP) deductions for employees who meet pay-period employment requirements as defined by Quebec. See [Set up QPP / QPP2 Deductions: Canada](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-qpp--qpp2-deductions-canada) for more information.

## Australian Users

The PAYG Tax deduction should be set up as deduction code 1. For more information, see [Setting Up a PAYG Deduction Code](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-a-payg-deduction-code-australia).

Select the link below for information about creating deduction and liability codes.
[Create Deduction and Liability Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/create-deduction-and-liability-codes)
