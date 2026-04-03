---
title: "Calculation Method Detail | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/calculation-method-detail"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/calculation-method-detail"
---

# Calculation Method Detail

View calculation method detail for time cards.

## Calculations for add-ons which are set to 'Allocate across time cards'

When the 'Allocate across time cards?' checkbox is selected in the [New/Edit Deduction/Add-on Code - Properties](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code/newedit-deductionadd-on-code---properties) window, six
 calculation method options are available, each 'by time card'.
These by-time-card options include:

- Fixed Amount

- Percent of Gross Amount

- Percent of Straight Time Equivalent

- Regular Equivalent Hours (REG + OVT +DBL)

- Overtime Equivalent Hours (REG + ((OVT + DBL) *1.5))

- All Hours (REG + OVT + DBL +OTHER HRS

For each of these calculation methods, recurring add-ons distribute expense based on employees' time card lines. This means if the time card is a 'Direct job cost' line, the add-on is charged to the same job and phase. Likewise, if the line is assigned to a 'Direct equipment cost' or 'Direct work order cost' line, the add-on is charged to the particular equipment code or work order, respectively.
Fixed Amount:Enter F for a fixed amount. No calculation is performed for this method. Fixed amount does not mean that all employees must have the same fixed amount; likewise, percents may vary by employee. The software also offers two special calculation methods: Prevailing Wage Adjustment, and Employer Health & Welfare Benefit. These methods are only applicable to prevailing wage jobs. (Please refer to the "Prevailing Wage Job Processing" discussion for more details.)
Percent of Gross Amount:Enter G for percent of gross. The Gross Pay Adjustments button will be enabled. Use this window to enter any deductions or add-ons that will be included in the employee gross pay calculations. The calculation for this method is total earnings multiplied by the designated rate.
For example, if the percentage of gross is set to 3%:
Regular pay10hrs x $10 = $100will deduct $3.00
Overtime pay10hrs x $15 = $150will deduct $4.50
Double-time pay10hrs x $20 = $200will deduct $6.00

Percent of Net Amount:Enter N for percentage of net amount. The percentage amount will be deducted from the employee's earnings after tax deductions have been made (the gross check amount minus any tax deductions). This feature is generally used for garnishment calculation purposes.
For example, if the percentage of Net is set to 25%:
Regular (gross) pay 40 hours x $10 =$400.00
Less Federal income tax$45.00
Less FICA$24.80
Less State taxes$10.20
Total applicable net amount$320.00
Amount that will be deducted$80.00 ($320 X 25%)

Percent of Straight Time Equivalent:Enter S for straight-time equivalent. This method works similar to percentage of gross pay, except if the employee has overtime, the amount is divided by 1.5. If the employee has double time overtime, the amount is divided by 2.0.
For example, if the percentage of straight time is set to 3%:
Regular pay10 hrs X $10 = $100will deduct $3.00
Overtime pay10 hrs X $15 = $150will deduct $3.00
Double time pay10 hrs X $20 = $200will deduct $3.00

## Percent of Base

Base is the gross amount before the "add to gross pay" hourly amount is added.
Example: vacation deduction, added to gross pay.

- Regular hourly earnings are $20/hour.

- Enter $1.00 hour vacation deduction and select the "add to gross pay" checkbox.

- When you enter the hourly pay in union rates, press F4 in the Regular field and enter $20.

Spectrum correctly adds the $1.00 hour to each of the hourly rates. In this way, the percent of base is calculated on $20/hour, not $21.00
Regular Equivalent Hours (REG + OVT + DBL):
Enter R for regular hours. This method calculates the amount by summing the number of hours associated with regular, overtime and double-time (R, ER, O, EO, D, ED) then multiplying the total by the specified hourly rate.
Regular hours10
Overtime hours4
Double time hours2
Total hours for "R" calculation16 [10 + 4 + 2]

Overtime Equivalent Hours (REG+((OVT + DBL) * 1.5)):
Enter O for overtime hours. This method calculates the amount similarly to the Regular method, except that the overtime and double time hours are included at 1.5 times their total.
Regular hours10
Overtime hours4
Double-time hours2
Total hours for "O" calculation19 [10 + (4+2) x 1.5)]

All Hours (REG + OVT + DBL + OTHER HRS):Enter A for all hours. This method calculates just like the Regular hours method, except that it additionally includes other hours such as vacation, holiday and sick time in the total hours computation (V, H, S).
User-Defined:
Enter U for a user-defined amount. If this calculation method is used, a field appears after the method field to enter the formula code for the user-defined deduction method. A search window is available in this field to view valid codes and descriptions.
Prevailing Wage Adjustment:
The Wage method is calculated using the prevailing wage adjustment rate entered in Union File Maintenance, Non-Union Pay Group Maintenance, or Employee Recurring Deductions/Add-ons, less the employer benefit rate. This method can be used by companies who want to show a separate amount on the paycheck and the certified report for the fringe portion of the prevailing wage amount. The calculation method will be an amount per hour for regular equivalent hours (REG + OVT + DBL) except that the rate will be adjusted based on the employee's base wage rate, the employer benefit amount in the employee file, the pension add-on, if any, and the install option for defaulting wage rates. For overtime hours, the employer benefit rate is zero and the full cash benefit rate is taken.
Example:
A contractor must pay a 5% benefit on every dollar paid to an employee working on a Davis-Bacon job. This 5% can be included with the other benefits already paid to the employee. Therefore the contractor can pay less out-of-pocket, but the employee still receives the base pay plus the fringe amount. The employer can decide whether or not to show any applicable non-cash amounts on the employee's pay stub (this is the traditional Davis-Bacon method), but all non-cash amounts will display on the Certified Payroll Report. To see a numeric example, select [Calculation Method Example](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/calculation-method-example).
If the Calculate actual pension benefits for the D-B/Prevailing wage employer benefit credit checkbox is selected in the installation screen, the software will calculate the employer benefits as it always has, even for those employees who happen to be working on a Davis-Bacon or Prevailing Wage job.
If the Calculate actual pension benefits for the D-B/Prevailing wage employer benefit credit checkbox is selected in the installation screen, AND if the Is this computed as part of the D-B/Prevailing wage employer benefit? checkbox is selected for the add-ons in the Deduction/Add-on Code Maintenance screen, AND if the employee is working on a Davis-Bacon or Prevailing Wage job (as set up in Job File Maintenance), then the non-cash add-on logic will be changed so that the prevailing wage adjustment is reduced by the non-cash add-on amount and the employer benefits (Health & Welfare) are increased. In other words, the computed amount will be included as part of the employer benefits that have already been calculated in the check calculation for time card lines.
Employer Health & Welfare Benefit:Enter H for employer health & welfare benefit. This calculation method should be used with a non-cash add-on (for example, an add-on with the paid to employee checkbox is not selected). This will capture the amount stored in the employee file for employer health / welfare benefit and include it as an add-on in payroll. (If the Calculate actual pension benefits for the D-B/Prevailing wage employer benefit credit? checkbox is selected in the installation screen and the Is this computed as part of the D-B/Prevailing wage employer benefit checkbox is selected in the Deduction/Add-on Code Maintenance screen, other add-ons could also be included in this calculation. See the preceding paragraph for more information.)
This will then burden the job for this amount and allow the amount to print on the certified report (for example, to show that the total compensation to the employee meets the prevailing wage requirement). For regular hours, this amount will always be the amount in the employee file. For overtime and double-time hours, this will always be zero (since the rate is based on 40 hours per week).
The H method is calculated using the rate entered in Employees - Rates for "employer benefit."
Employer Non-Stated Fringe Benefit:
Use this calculation method to record fringe benefits for regular hours worked on prevailing wage jobs with non-stated fringe. This method is only applicable for add-ons that are not paid to the employee on the paycheck, and will only calculate amounts for Regular time (pay types R and ER).
