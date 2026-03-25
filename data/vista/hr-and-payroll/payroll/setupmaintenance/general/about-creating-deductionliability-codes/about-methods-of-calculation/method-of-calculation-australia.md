---
title: "Method of Calculation: Australia | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/about-methods-of-calculation/method-of-calculation-australia"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/about-methods-of-calculation/method-of-calculation-australia"
---

# Method of Calculation: Australia

(Australia only) Table describing the available method of
 calculation options from the Method drop-down field in the PR
 Deductions/Liabilities form.
Method
Description
Typical Use

A - Amount
Use this method to set a standard amount per pay period. You can override this setting for an individual employee using the PR Employee Dedns/Liabs form.
Note: If a deduction or liability using this method is assigned to multiple crafts/classes or craft/class templates, and an employee works on more than one craft/class for the same day, the system calculates the deduction/liability for each craft/class/template. Setting a limit prevents duplicate calculations. The system then distributes the liability to only the first entry.
Health Insurance

D - Rate Per Day
Use this method to set a flat amount per day, based on the number of days worked (posted). If you select the Posting to All checkbox in the PR Employees form, the system uses the number of days specified in the pay period in the PR Pay Period Control form.
Note: If a deduction or liability using this method is assigned to multiple crafts/classes or craft/class templates, and an employee works on more than one craft/class for the same day, the system calculates the deduction/liability for each craft/class/template. Setting a limit prevents duplicate calculations. The system then distributes the liability to only the first entry.
Not applicable

F - Factored Rate per Hour
Uses the formula: [Earnings factor x deduction rate] x hours worked. The Earnings factor is typically 1 for regular time, 1½ for overtime and 2 for double time.
Union deductions / liabilities

G - Rate of Gross
Uses the formula: Rate x gross earnings.
Superannuation, CoInvest, Fringe Benefit Tax (FBT)

H - Rate per Hour
Rate per hour worked.
Union deductions / liabilities that do not change with the earnings factor.

N - Rate of Net
Uses the formula: Rate x net pay amount. Use this method for personal deductions only, which are set up in PR Employees Dedns/Liabs form.
Note: If an override rate is not set up for an employee, the system uses the standard rate specified in PR Deductions/Liabilities to calculate the deduction amount.
Garnishments

S - Rate of Straight Time Equivalent
Uses the formula: Rate x straight time equivalent earnings (total number of hours worked times the regular pay equals the gross amount on which to calculate).
Most workers' compensation

DN - Rate based on Selected Deduction Code
Uses the formula: Rate x the amount of a selected deduction code that is already set up in PR Deductions/ Liabilities.
Not applicable

V - Variable Factored Rate
This method allows you to specify the factor of the deduction/liability.
Union vacation. For example, your vacation deduction is $1.00/hr for hours with an earnings factor of 1, $2.00/hr for hours with an earnings factor of 1.5, and $2.50/hr for hours with an earnings factor of 2.

R - Routine
Use this method for special routines that the system
 cannot calculate by any other method. You must
 first set up the routine in PR Routines.

Related concepts

- [About Determining the Method of Calculation for D/L Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/about-methods-of-calculation/about-determining-the-method-of-calculation-for-dl-codes)

- [PR Deductions/Liabilities Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form)

Related tasks

- [Create Deduction and Liability Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/create-deduction-and-liability-codes)

Related information

- [About Determining the Method of Calculation for D/L Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/about-methods-of-calculation/about-determining-the-method-of-calculation-for-dl-codes)

- [Create Deduction and Liability Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/create-deduction-and-liability-codes)

- [PR Deductions/Liabilities Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form)
