---
title: "Prevailing Wage and Davis-Bacon Processing | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/in-depth-overview/summary-of-prevailing-wage-benefits/prevailing-wage-and-davis-bacon-processing"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/in-depth-overview/summary-of-prevailing-wage-benefits/prevailing-wage-and-davis-bacon-processing"
---

# Prevailing Wage and Davis-Bacon Processing

On Federal Davis-Bacon jobs, non-union employers pay a
 Federally-mandated pay rate and fringe benefit rate to employees.

## Overview

Because there is no union involved, fringe benefit amounts are paid to
 employees as wages. If an employer pays health or certain other fringe benefits for
 employees, these amounts may be deducted from the Federally-mandated rates. For example,
 if the required fringe benefit amount is $5.00 per hour, but the employer pays $3.00 per
 hour in benefits, only $2.00 per hour needs to be paid to the employee as wages.
The Davis-Bacon and prevailing wage calculations have to be done AFTER figuring the total wages plus benefits, including the benefit reduction based on health and other benefits already paid on the employees' behalf. Spectrum offers the flexibility to calculate adjusted gross pay amounts for specific add-ons and deductions by allowing you to set up matching 401(k) non-cash add-on codes. This feature makes it easier for employers to calculate 401(k) matching amounts based on the gross pay amount without worrying about how allowances, fringe benefits, or deductions might affect the gross pay.
For non-union companies that pay fringe benefits on prevailing wage jobs, the
 software can automatically calculate multiple fringe benefit rates for certain jobs,
 including Davis-Bacon and prevailing wage jobs. The Non-Union Pay Group File Maintenance > Prevailing Wage window allows prevailing wage adjustment benefit add-ons to be set up and
 then paid directly to the employee or the user can set up non-cash add-ons to be paid to
 a third party, such as a retirement trust.
Furthermore, the software allows for fringe rate overrides for the employer
 benefit computation by phase, employee, or employee phase using the Phase Overrides, Employee, or Employee Phase buttons. You can only
 enter fringe overrides when there is a prevailing wage adjustment code entered in the
 Pension or Prevailing wage adjustment fields of
 the Prevailing Wage window. This fringe amount can be overwritten
 manually (if the fringe is blank then the fringe for this override rate will be zero
 <$0>).
In short, the fringe rate default hierarchy is as follows when the fringe is a non-zero amount. Number 1 receives the highest priority.

- The fringe rate associated with the phase override defaults.

- The fringe rate associated with the employee-specific phase override defaults.

- The fringe rate associated with the employee-specific rate override defaults.

- The fringe rate associated with the pay group rate defaults.
Specific system features relating to these gross pay and fringe calculations include:

- If the Calculate actual pension benefits for the D-B/Prevailing wage employer benefit credit checkbox in Payroll Installation is selected, the prevailing wage adjustment is reduced by the 401(k) amount and the employer benefits (Health & Welfare) are increased.

- The Non-Union Pay Group File Maintenance > Prevailing Wage window includes one fringe rate per pay level (up to nine standard
 pay levels are included). Two checkboxes allow you to disable the Davis-Bacon /
 Prevailing wage benefits and/or to disable the certified job status. These check
 boxes display in every fringe override window, but the Disable D-B/PW benefits check
 box is only available if the prevailing wage codes are completed, while the
 Disable certified
 checkbox is always available.

- Non-cash add-ons can be set up in the Deduction / Add-on Code
 Maintenance screen or in the Deduction
 section of the Union File Maintenance screen. The ability
 to charge fringe benefits to a non-cash add-on code allows employers to pay excess
 fringe amounts directly to a third party, such as a pension.

- The Crystal-Link Expanded Certified Payroll Report details amounts paid to the
 employee, as well as fringe amounts (not paid to employee).

- The Employer Pension Contribution Report allows you to see all non-cash add-ons in detail or summary view.
Please refer to the sections on Deduction / Add-on Code Maintenance, Union File Maintenance, Non-Union Pay Group File Maintenance, and Employees for screen-level details.

Related information

- [Example - Check Calculation for Davis-Bacon and Prevailing Wage Jobs](/en/spectrum/spectrum/accounting/payroll/installation-overview/payroll-installation---defaults/example---check-calculation-for-davis-bacon-and-prevailing-wage-jobs)
