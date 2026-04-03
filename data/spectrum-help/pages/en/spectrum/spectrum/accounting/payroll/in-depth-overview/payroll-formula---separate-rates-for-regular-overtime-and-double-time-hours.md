---
title: "Payroll Formula - Separate Rates for Regular, Overtime, and Double Time Hours | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/in-depth-overview/payroll-formula---separate-rates-for-regular-overtime-and-double-time-hours"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/in-depth-overview/payroll-formula---separate-rates-for-regular-overtime-and-double-time-hours"
---

# Payroll Formula - Separate Rates for Regular, Overtime, and Double Time Hours

Existing Spectrum calculation methods combine regular,
 overtime, and double time hours.
The example below is used to take regular + overtime + double time hours and separate them
 from each other.
Intended User:
The operator has thoroughly reviewed the list of existing Spectrum methods for deductions/add-ons and has concluded that another calculation is required.
This formula is used for calculations when any of the following are true.

- The deduction (add-on) is calculated only on regular hours.

- The deduction (add-on) is calculated only on overtime hours.

- The deduction (add-on) is calculated only on double time hours.

- The deduction (add-on) is calculated on the total of regular + overtime hours but not on double time hours.

- The deduction (add-on) is calculated on the total of regular + double time hours but not on overtime hours.

- The deduction (add-on) is calculated on the total of overtime + double time hours but not on regular hours.

- The deduction (add-on) is calculated on all three (regular, overtime, and double time) hours, but each at a different hourly rate.
In this example, rates apply separately to regular, overtime, and double time hours as shown below.
Regular hour rate = $1.00
Overtime rate = $4.00
Double time rate = $7.00

Result:
If regular, overtime, and double time hours are all 1.00, the calculated amount, using the rates above, is 12.00.

Explanation:
Lines 1, 2, and 3 separate out the regular time hours.
Lines 4 and 5 separate out the double time hours.
Line 6 separates out overtime hours.
Line 7 applies the regular rate to regular hours.
Line 8 applies the overtime rate to overtime hours.
Line 9 applies the double time rate to double time hours.
Line 10 adds the regular and overtime amounts.
Line 11 is the answer and adds the double time amount to the sum of the regular and overtime amounts from line 10.
Note: Do not use this formula if the deduction (add-on) matches one of
 the following examples. The following calculations correspond to existing methods for
 Payroll deductions and add-ons.

## Example A

This example corresponds to the double time (D) calculation method for a Payroll deduction (add-on).
 Regular hours * 1 * regular hour rate

+ Overtime hours * 1.5 * overtime rate

+ Double time * 2.0 * double time rate

Total

## Example B

This example corresponds to the overtime (O) calculation method for a Payroll deduction (add-on). The total equals the sum of the following three lines.
 Regular hours * 1 * regular hour rate

+ Overtime hours * 1.5 * overtime rate

+ Double time * 1.5 * double time rate

Total
