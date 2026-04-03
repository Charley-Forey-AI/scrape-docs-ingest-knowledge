---
title: "Formula File Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/formula-file-maintenance/formula-file-maintenance---field-descriptions"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/formula-file-maintenance/formula-file-maintenance---field-descriptions"
---

# Formula File Maintenance - Field Descriptions

Use the table below as a reference when completing or editing fields in the Formula window.
Fields/Buttons
Descriptions

Code
Enter a formula code.

Description
The description for the chosen code displays. Another description may be entered, and a window is available to a user-defined variable description field.

Formula calculation

Result
Enter a result code: T1 through T15 are temporary variables, or press Enter to accept the system default to (A)nswer.

1st factor
Enter a variable (G, N, R, O, D, A, V1, V2, V3, F, S, C, L, W), number, or result code, or press F4 to select from a list of available formula variables.

> G
=
Gross Amount (relates to pay types, not total wage bucket)

N
=
Net Amount (Gross - Taxes)

R
=
Regular Equivalent Hours (REG + OVT + DBL)

O
=
Overtime Equivalent Hours (REG + ((OVT + DBL) * 1.5))

D
=
Double Time Equivalent Hours (REG + (OVT * 1.5) + (DBL * 2))

A
=
All Hours (REG + OVT + DBL + OTHER HRS)

V1
=
User-Defined Variable 1

V2
=
User-Defined Variable 2

V3
=
User-Defined Variable 3

F
=
Federal subject-to wages

S
=
State subject-to wages

C
=
County subject-to wages

L
=
Local subject-to wages

W
=
Workdays included on the paycheck (applies to 'Union total' basis only)

Operator
Enter the operation to be performed (+, -, *, D, MIN, MAX), or press F4 to select from a list of available operators.

> +
Add

-
Subtract

*
Multiply

D
Divide

MIN
Take the smaller of the two amounts.

MAX
Take the greater of the two amounts.

2nd factor
Enter a variable (G, N, R, O, D, A, V1, V2, V3, F, S, C, L, W), number, or result code, or press F4 to select from a list of available formula variables.

> G
=
Gross Amount

N
=
Net Amount (Gross - Taxes)

R
=
Regular Equivalent Hours (REG + OVT + DBL)

O
=
Overtime Equivalent Hours (REG + ((OVT + DBL) * 1.5))

D
=
Double Time Equivalent Hours (REG + (OVT * 1.5) + (DBL * 2))

A
=
All Hours (REG + OVT + DBL + OTHER HRS)

V1
=
User-Defined Variable 1

V2
=
User-Defined Variable 2

V3
=
User-Defined Variable 3

F
=
Federal subject-to wages

S
=
State subject-to wages

C
=
County subject-to wages

L
=
Local subject-to wages

W
=
Workdays included on the paycheck (applies to 'Union total' basis only)

Basis / allocation
Is this formula based on each Time card line or Union total? Following the basis designation, the software will advance to the test section of the screen and allow the user to double-check the formula by entering information in the test box.
When Time card line is specified, the calculation will occur for each line independently. When Union total is specified, then all lines for the union are grouped together for purposes of the calculation. This is necessary when a fixed calculation is performed, for example, such as [(% of Gross) – (Fixed Amount)].
Example:
When Union total is specified as the basis for the calculation, an additional field appears, prompting for the allocation method across applicable time card lines. Available options are Gross percentage, Regular hours, Overtime hours, Double time hours or All hours. This is relevant for allocating the union fringe costs across multiple lines of the time card file.

> Pay type
Hours
Gross

001
R
10
@ $10
$100
Job 1

002
O
10
$15
$150
Job 2

003
D
12.5
$20
$250
Job 3

32.5
$500

Select the allocation type. Examples of each option are:

- Allocation based on Gross for a $50 fringe would be $10 to Job 1, $15 to Job 2, and $25 to Job 3.

- Allocation based on Regular hours for a $50 fringe would be $15.38 for Job 1, $15.38 for Job 2, and $19.24 for Job 3.

- Allocation based on Overtime hours for a $50 fringe would be $11.43 for Job 1, $17.14 for Job 2, and $21.43 for Job 3.

- Allocation based on Double time hours for a $50 fringe would be $10 for Job 1, $15 for Job 2, and $25 for Job 3.

- Allocation based on All hours for a $50 fringe would be $15.38 for Job 1, $15.38 for Job 2, and $19.24 for Job 3.

User-defined variables
Enter variable descriptions. Descriptions may be up to 30 characters long.

Formula Test button
Click this button to display the [Formula Test](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/formula-file-maintenance/formula-test) window where you can enter values to test the formula you set up in the main screen.
