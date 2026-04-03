---
title: "Payroll Formula - Child Support Limited to a Percent of Income | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/in-depth-overview/payroll-formula---child-support-limited-to-a-percent-of-income"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/in-depth-overview/payroll-formula---child-support-limited-to-a-percent-of-income"
---

# Payroll Formula - Child Support Limited to a Percent of Income

This formula can be used by companies who need to calculate
 a fixed dollar amount deduction that is subject to an upper limit equal to a percent of
 income.
This formula is used for calculations when all of the following are true:

- A child support or garnishment order requires that a fixed amount be withheld from an employee's paycheck.

- The amount withheld from the employee's check cannot exceed a percentage (specified in the court order) of the employee's disposable wages for that check.

- If the required fixed amount is greater than the specified percentage of the employee's disposable earnings, the deduction is equal to the disposable earnings multiplied by the percentage limit.

- "Disposable earnings" is defined in the court order as gross earnings less any government mandated (for example, taxes). Disposable earnings equals gross earnings less taxes withheld.

Example:
In the following example, the court order states that $125.00 should be withheld from each check paid to the employee. The order also states that the court ordered deduction cannot exceed 50% of the employee's disposable earnings for the pay period.
Gross amount = $250.00
Net amount = $210.00
Court ordered deduction = $125.00
Deduction cannot exceed = 50% of the disposable earnings (net amount)
This formula can be set up in Formula File Maintenance and used for a single employee or multiple employees who have different court ordered withholdings.
Result:
The answer within the Formula Test window displays the deduction amount of $105.00.

Explanation:
In this example, the court ordered deduction amount of $125.00 (V1) exceeds 50% (V2) of the net earnings ($210.00).
Line 1
Net (1st factor = N) in Spectrum deduction methods or formula factors is equal to gross salary and wages less taxes withheld. This is the same as what most court ordered garnishments refer to as "disposable earnings." V2 (Variable 2) holds 50 for the 50% limitation.

Line 2
Converts the number from line 1 to the court ordered upper limit for the
 deduction. Using this method for percentages in formulas allows the input of
 percentages in Employee > Maintenance > Payroll Deduction/Add on as a whole number, which is consistent with how
 percentages are entered throughout Spectrum.

Line 3
V1 (Variable 1) holds the fixed amount required by the court order. The minimum (MIN) operator takes the lesser of the two line 3 amounts. The other amount on line 3 is the calculated dollar limit from line 2 based on 50% of the net earnings.

Line 3
Line 3 is also the Answer and is equal to the lesser of 50% (V2) of the employee's net earnings or the fixed amount (V1) required by the court.
