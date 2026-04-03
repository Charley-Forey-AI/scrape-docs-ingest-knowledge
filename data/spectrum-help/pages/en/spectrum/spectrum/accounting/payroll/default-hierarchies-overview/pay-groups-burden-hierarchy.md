---
title: "Pay Groups Burden Hierarchy | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/default-hierarchies-overview/pay-groups-burden-hierarchy"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/default-hierarchies-overview/pay-groups-burden-hierarchy"
---

# Pay Groups Burden Hierarchy

Common pay group burden hierarchy questions are addressed
 below.
Question:
Where will the burden rate come from when using pay groups?
Answer:
The answer depends on whether or not the company is using actual or percentage Payroll burden.
The following hierarchy only applies when the Actual Payroll Burden prompt is set to (N)o in the job file.
Spectrum will select the first non-zero burden rate it finds using the following hierarchy.
The software searches for the appropriate burden rate regardless of where it found the pay rate or the T+M bill code.
This table shows showing how Spectrum's pay rate default hierarchy is affected when you select the Phase rate overrides ALL other rates checkbox. Number 1 receives the highest priority. Based on the table below, Spectrum will use the first burden rate it finds.
If the phase override checkbox IS selected…
If the phase override checkbox IS NOT selected…

The burden rate found in the phase rate override will default.
(If no rate exists, refer to the Default pay rate setting in the Payroll Installation – Defaults screen.)
The software refers to the Default pay rate selection in the Payroll Installation – Defaults screen.

If the Default pay rate is set to Employee pay rate, the burden rate defaults from Employees.
If the Default pay rate is set to Union/pay group or Higher of the two, the burden rate will default from the employee-specific phase override.

The burden rate defaults from the employee-specific phase override.
The burden rate defaults from the phase rate override.

The burden rate defaults from the phase rate override.
The burden rate defaults from the employee-specific rate.

The burden rate defaults from the employee-specific rate.
The burden rate defaults from the rate found in the pay group.

The burden rate defaults from the rate found in the pay group.
The burden rate defaults from the rate found in the job file.

The burden rate defaults from the rate found in the job file.
The burden rate defaults from the rate found in Employees.
