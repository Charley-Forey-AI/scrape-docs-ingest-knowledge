---
title: "Payroll Formula - Round a Payroll Deduction (or Add-on) to the Nearest Dollar | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/in-depth-overview/payroll-formula---round-a-payroll-deduction-or-add-on-to-the-nearest-dollar"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/in-depth-overview/payroll-formula---round-a-payroll-deduction-or-add-on-to-the-nearest-dollar"
---

# Payroll Formula - Round a Payroll Deduction (or Add-on) to the Nearest Dollar

Companies who have Payroll deductions (or add-ons) that must be rounded as part of the calculation may use this formula.
This formula is used for calculations when any of the following are true.

- A deduction (or add-on) needs to be rounded as one of the calculation steps.

- A union specifies that a fringe, union deduction, or union add-on amount needs to be stated as a whole dollar amount with no cents.

- Rounding needs to take place in some way other than using standard rounding rules where a fraction of .49 and below rounds down and a fraction of .50 and above rounds up.

Example 1:
In the following example, a deduction calculation requires that 15.55% of a specific employee's gross wages be deducted from the employee's check after it is rounded to the nearest whole dollar.
Gross amount= $1,000
Employee % = 15.55%
In this example, the percentage can be different for each employee that
 elects the deduction, so Variable 1 (V1) will be used instead of entering 15.55% directly
 into the formula. The 15.55% will be specified in Payroll > Formula File Maintenance for each employee affected by this deduction.

Result:
15.55% of the $1,000 = $155.50. Using common rounding rules, $155.50 rounds up to $156.00, which displays in the Answer field on the Formula Test window.

Explanation:
Lines 1 and 2 apply the rate to the gross Payroll dollars and allow 15.55% to be entered as 15.55 into Spectrum instead of .1555. This makes the input consistent with other Spectrum entry screens.
Lines 3 and 4 convert the number from line 2 into a fractional number with enough decimal places (to the right of the decimal point) to reach where Spectrum rounds numbers within formulas.
Line 4 is the answer.
Rounding down a fractional amount of $.50 or lower and rounding up a fractional amount of $.51 or greater.
Example 2:
In the following example, numbers equal to and lesser than $.50 will round down and numbers equal to and above $.51 will round up. One more line needs to be inserted into the formula used in example #1. Line number 3 is the new line.

Explanation:
Lines 1 and 2 apply the rate to the gross Payroll dollars and also allow 15.55% to be entered as 15.55 into Spectrum instead of .1555. This makes the input consistent with other Spectrum entry screens.
Line 3 (new line) converts the fractional amount of $.50 to $.49 so that
 the number will round down using common rounding rules.Note: This
 will be added to all formula results. However, the number $1.00 will round correctly
 because it will become $1.01 before rounding and round down to $1.00 after
 rounding.

Lines 4 and 5 convert the number from line 2 into a fractional number with enough decimal places (to the right of the decimal point) to reach where Spectrum rounds numbers within formulas.
Line 5 is the answer.
