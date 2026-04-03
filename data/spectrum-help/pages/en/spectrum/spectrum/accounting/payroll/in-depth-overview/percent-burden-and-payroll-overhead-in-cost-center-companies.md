---
title: "Percent Burden and Payroll Overhead in Cost Center Companies | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/in-depth-overview/percent-burden-and-payroll-overhead-in-cost-center-companies"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/in-depth-overview/percent-burden-and-payroll-overhead-in-cost-center-companies"
---

# Percent Burden and Payroll Overhead in Cost Center Companies

## Question

How does Spectrum treat Percentage Burden and Payroll Overhead in a cost center company? The best way to explain this is to use an example.
Setup Job Details: Job 800 is assigned to cost center 401. It also has a 15% burden, and a 10% payroll overhead set up on it. This job has one phase, 01-0200 with cost types (L)abor, (B)urden, (M)aterials and (O)ther. The phase has no cost center assigned to it.
Employee: My employee has a home cost center of 201.
Payroll Cash Account: My payroll cash account has a cost center of 101.
Payroll Department: This is the information found in the PR Department File.
Labor
10-5100 (Direct Labor)

Burden Components
40-9200 (Indirect PR Taxes)

% PR Burden DR
10-5200 (Direct PR Taxes)

% PR Burden
CR 40-9250 (Allocated Burden)

% Overhead DR
10-5255 (Direct OH)

% Overhead CR
40-9255 (Allocated OH)

Cost Centers "Approved" to use: All

## Processing Steps

- Create a new pay cycle using: Employee Cost Group: ALL Check Cost Group: 101 Bank Account: 5 (defaulted to this account per setup) Shut off all add-ons and deductions as this makes it easier to reconcile.

- In Time Card Entry, charge 40 hours to job 800, phase 01-0200, cost type L.

- Calculate the pay cycle, print reports and review findings.

## Findings

Direct Labor
Direct labor is charged to the job's cost center. The offset is inter-post.
JE # 1
CC
GL Code
DR
CR

DR
401
Direct Labor
$1,400.00

CR
401
Inter-Post
$1,400.00

Actual Taxes, Workmen's Comp and Union Fringes (aka Indirects)
 The actual taxes, workmen's comp and union fringes will be charged to the job's cost center with an offset to inter-post.
JE # 2
CC
GL Code
DR
CR

DR
401
Indirect PR Taxes
$182.43

CR
401
Inter-Post
$182.43

JE # 3

DR
101
Inter-Post
$182.43

CR
101
PR Taxes Payable
$182.43

Employer's Portion of Taxes Expanded
CC
GL Code
DR
CR

CR
101
PR Taxes Payable
$107.10

CR
101
PR Taxes Payable
$28.00

CR
101
PR Taxes Payable
$7.84

CR
101
PR Taxes Payable
$4.90

CR
101
PR Taxes Payable
$34.59

JE # 4

DR
101
Inter-Post
$1,400.00

CR
101
Cash
$1,105.69

CR
101
PR Taxes Payable
$294.31

Employee's Portion of Taxes Expanded
These amounts are offset by the reduction of the cash outlay to employee, also within the same cost center, 101. In other words, no inter-post entries are needed for this portion of the journal entry.
CC
GL Code
DR
CR

CR
101
PR Taxes Payable
$154.00

CR
101
PR Taxes Payable
$107.10

CR
101
PR Taxes Payable
$10.50

CR
101
PR Taxes Payable
$22.71

Percentage Burden Calculations
The job was properly charged 15% of direct labor ($1,400 x 15% = $210.00). As we charged the actual burden items to cost center 401, we must also credit them out using cost center 401.
JE # 5
CC
GL Code
DR
CR

DR
401
Direct PR Taxes
$210.00

CR
401
Inter-Post
$210.00

Payroll Overhead (% Method)
The job was properly charged 10%. ($1,400 + $210 = $1,610. $1,610 x 10% = $161.00).
JE # 6
CC
GL Code
DR
CR

DR
401
Direct overhead
$161.00

CR
401
Inter-Post
$161.00

Note that the pool of costs that are to be allocated to jobs must also be charged to cost center 401!
Assets

Cash - 101
Inter-Post - 101
Inter-Post - 401

1,105.69
4
1,400.00
1

3
182.43
182.43
2

4
1,400.00

Liabilities

PR Taxes Payable - 101

182.43
3

294.31
4

Direct Cost Section

Direct Labor - 401
Direct Burden - 401
Direct Overhead - 401

1
1,400.00
5
210.00
6
161.00

Indirect Cost Section

Indirect Burden - 401
Indirect OH - 401

2
182.43
210.00
5
161.00
6
