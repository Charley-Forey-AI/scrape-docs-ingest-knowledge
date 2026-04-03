---
title: "Allocating Earnings | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/period-end-procedures/payroll-year-end-processing-canada/allocating-earnings"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/period-end-procedures/payroll-year-end-processing-canada/allocating-earnings"
---

# Allocating Earnings

Certain values from the State Tax History tables need to be allocated across an employee's T4 Slips whenever the employee worked in multiple provinces.
This is provided to assist in troubleshooting any potential issues within the allocations. Also, the term "state" is used as the underlying tables all use that term. For purposes of this exercise, the term 'state' is synonymous with 'province' or 'territory'.

## Special Case #1 – Allocate Taxes & Earnings Based on Income

Certain values are calculated at the federal level in Spectrum. Whenever an employee works in multiple provinces, these values must be allocated across an employee's T4 slips. The following items are calculated and maintained at the federal level and will be allocated proportional to 'income':

- CPP contributions (box 16)

- QPP contributions (box 17)

- Income tax deducted (box 22)

- CPP/QPP earnings (box 26)

- Use the 'Income' column as the basis for allocation for the following values, summing the subject-to earnings of all provinces and then proportionally allocating the particular amount to all T4 Slips. Plug any rounding issues as needed.

Example: Say that total to allocate = 1,345.75
Alberta 20,350.80
Manitoba 6,125.50
British Columbia 242.12
Total Income 26,718.42
Calculate allocation:
Alberta 20,350.80 / 26,718.42 x 1,345.75 1,025.03
Manitoba 6,125.50 / 26,718.42 x 1,345.75 308.53
British Columbia 242.12 / 26,718.42 x 1,345.75 12.20
Totals 26,718.42 1,345.76

- Test for full allocation.

- Here, the software will reduce one amount to make the total components equal the amount full amount to allocate.

## Special Case #2 – Allocate Add-ons

Certain add-ons need to be allocated across an employee's T4 Slips whenever they worked multiple provinces. Specifically, these items will use this method of allocation:

- Pension adjustment (box 52)

- Other Information amounts for add-on codes

-  When one of these add-on codes is found, read for the assigned 'work state' of that time card record and then add the amount of that record to the assigned province.

- If there is no 'work state' present, the amount will be allocated based on income as defined below.

- Test for full allocation.

- Time Card History Total: Sum up all time card history amounts for that add-on recorded for a province (that is, read across the employee's T4 slips)

- Employee Total: Sum up the Employee total for this add-on (from Deduction / Add-on History Table)

- When the allocated amounts from Time Card History does not match the Employee total for that add-on, allocate any remaining amounts based on income (see Special Case #1).

- Example (using same 'Income' values as in the above example):

- After reading Time Card History, the following records are found:

Alberta 0.00
Manitoba 100.00
British Columbia 25.00

- After reading the Deduction / Add-on History for the employee, the total was $155.00 which means that the software needs to allocate the remaining $30 across all three provinces.

Alberta 20,350.80 / 26,718.42 x 30.00 22.85
Manitoba 6,125.50 / 26,718.42 x 30.00 6.88
British Columbia 242.12 / 26,718.42 x 30.00 0.27
Total 30.00

- Total amount to appear on T4 Slip will be:
Timecard History
Allocated
Total T4 Amounts

Alberta
0.00
22.85
22.85

Manitoba
100.00
6.88
106.88

British Columbia
25.00
0.27
25.27

## Special Case #3 – Allocate Union Dues

Union dues need to be allocated across an employee's T4 Slips whenever they worked multiple provinces.

- Union dues (box 44)

- If the particular deduction or add-on codes are found, read for the assigned 'work state' on the associated time card history record and then add the amount of that record to the assigned province.

- After recording all Union Dues history amounts from the time card history tables, test for 'full allocation'. If the amount allocated from Time Card History does not match the Employee total, use the same 'Allocation based on Income' (detailed in Special Case #1 above) to allocate the difference.

## Special Case #4 – Allocate All Other Deductions

Certain deductions need to be allocated across an employee's T4 Slips whenever they worked multiple provinces. Specifically, these items will use this method of allocation:

-  RPP contributions (box 20)

- Charitable contributions (box 46)

- Other information amounts for deduction codes

- If the particular deduction codes are found, read for the assigned 'work state' on the associated time card history record and then add the amount of that record to the assigned province.

- Test for full allocation. Allocate any differences using the 'Allocation based on Income (detailed in Special Case #1 above) to allocate the deduction amount across T4 Slips.

Related information

- [Payroll Year-End Processing (Canada)](/en/spectrum/spectrum/accounting/payroll/period-end-procedures/payroll-year-end-processing-canada)
