---
title: "Calculating Union Fringe Rates Up to 40 Hours | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/union-file-maintenance/unions--wage-code-procedures/calculating-union-fringe-rates-up-to-40-hours"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/union-file-maintenance/unions--wage-code-procedures/calculating-union-fringe-rates-up-to-40-hours"
---

# Calculating Union Fringe Rates Up to 40 Hours

Follow the steps below to set up a formula that can be used
 to calculate the Union Fringe Rate up to a maximum of 40 hours.

1. On the Site Map, click Payroll  >  Maintenance  >  Formula.

1. At the Code field, enter a new code for this formula (for example, MAX40).

1. At the Descriptions field, enter a code description (for example, UNION FRINGE MAX 40 HOURS).

1. In row 1 enter the following information:

- Result = T1

- 1st factor = A

- Operator = MIN

- 2nd factor = 40

1. In row 2 enter the following information:

- Result = A

- 1st factor = T1

- Operator = *

- 2nd factor = V1

1. Click the User Defined
 button.

1. In the V1 description
 field, type UNION FRINGE
 RATE(S) and click OK.

1. Click OK again to save
 your formula.
