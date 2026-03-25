---
title: "About Determining the Method of Calculation for D/L Codes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/about-methods-of-calculation/about-determining-the-method-of-calculation-for-dl-codes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/about-methods-of-calculation/about-determining-the-method-of-calculation-for-dl-codes"
---

# About Determining the Method of Calculation for D/L Codes

When you create deduction and liability codes (PR
 Deductions/Liabilities), you must set a method for calculating the deduction or
 liability amount (using the Method drop-down).
Available methods include: Amount, Rate per Day, Factored Rate per Hour, Rate of Gross, Rate per Hour, Rate of Net, Rate of Straight Time Equivalent, Rate based on Selected Deduction Code, Variable Factored Rate, and Routine. For a detailed explanation of each method of calculation, click [here](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/about-methods-of-calculation).
Depending on the selected method, you may have additional tasks to perform. The rest of this topic discusses these additional tasks.

## Garnishments

You will typically select
 Rate of Net
 from the Method field
 when setting up a garnishment deduction. In this case, you will
 enter a garnishment group in the Garn Group field. The system multiplies the
 rate you specify for this deduction by the employee's net amount,
 which determines the garnishment amount. For more information on
 garnishments, see [PR Garnishment Groups Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-garnishment-groups-form). For more information on setting a
 deduction/liability rate amount, see [About Deduction and Liability Rates](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/about-deduction-and-liability-rates).

## Basing State
 Withholding on Federal Tax

If you base state
 withholding on Federal taxes, select Rate of Deductionfrom the Method field. The system multiplies the rate
 you specify for this deduction by the amount from the referenced
 deduction code (Federal amount) which determines the state
 withholding. For more information on setting a deduction/liability
 rate, see Assigning Rates to
 Deductions and Liabilities.

## Using Payroll Routines

Certain deductions (federal
 tax and most state/provincial taxes) are too complex to calculate
 using a standard method. Vista™ contains
 specific payroll routines for these calculations. You can initialize
 these routines in PR Routines. To use an initialized routine, select
 Routine from
 the Method field
 and enter the routine name in the Routine field.
For additional information
 on how to set up deductions and withholding information, see [About Payroll Routines](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines).
Note: When states change withholding
 information that affects tax routines, Viewpoint Construction
 Software must update the routines. To expedite change, please
 contact Viewpoint if your state informs you of any
 changes. All other rates, limits, and other pieces of calculation
 information are your responsibility to maintain.

## Overriding the
 Method for Bonus Payments (US users only)

If you want to override the
 method of calculation for bonus payments, select the Calculate as Rate of Gross on Bonus Seq check
 box. Then specify the rate for bonus payments in the Bonus Rate field, using a percentage (a value
 between 0 and 1, such as .28). When you override the method of
 calculation, it applies to all employees subject to this deduction
 or liability and is typically used to override federal tax
 calculations.
Note: Bonus tax calculations for Australia
 and Canada are calculated using a special routine-based procedure
 that is initiated during payroll processing. To enable bonus tax
 calculations for a pay period, you must select the Bonus checkbox for the appropriate payment
 sequence in PR Pay Period Control (Payment Sequence tab).

Related information

- [PR Deductions/Liabilities Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form)

- [Create Deduction and Liability Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/create-deduction-and-liability-codes)
