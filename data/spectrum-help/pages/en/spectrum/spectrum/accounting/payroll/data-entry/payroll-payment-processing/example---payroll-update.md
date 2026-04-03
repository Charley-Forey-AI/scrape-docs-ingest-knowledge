---
title: "Example - Payroll Update | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/example---payroll-update"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/example---payroll-update"
---

# Example - Payroll Update

If the G/L account of the add-on code is set up as 20-5350
 (G/L department 20, G/L code 5320), the code portion (5350) will come from the information
 entered in the Deduction / Add-on File Maintenance screen.
The G/L department will be reset (from 20) to the G/L department specified in Payroll
 Department File Maintenance. In this example, if the G/L department associated with the
 department code of the time card line was 50, the new G/L account code would be created as
 50-5350.
For add-ons using the '% of gross by time card' calculation method, the software will look to the 'direct cost' flag of the Payroll department code assigned to that time card line and then find the corresponding G/L account in the Deduction/Add-on master table for the particular add-on code.
