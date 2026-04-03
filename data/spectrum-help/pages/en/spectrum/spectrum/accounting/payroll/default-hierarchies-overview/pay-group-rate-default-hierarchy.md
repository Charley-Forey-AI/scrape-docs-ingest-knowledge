---
title: "Pay Group Rate Default Hierarchy | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/default-hierarchies-overview/pay-group-rate-default-hierarchy"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/default-hierarchies-overview/pay-group-rate-default-hierarchy"
---

# Pay Group Rate Default Hierarchy

This table shows showing how Spectrum's pay rate default
 hierarchy is affected when you select the Phase
 rate overrides ALL other rates checkbox. Number 1 receives the highest
 priority, and number 5 the lowest.
In other words, the software will check for a non-zero pay rate in the order listed, and
 will default the first rate found.
If the phase override checkbox IS selected:
If the phase override checkbox IS NOT selected:

1. The phase rate override from the pay group file defaults.
1. If the Payroll Installation > Default pay rate field is set to Employee pay rate, then the employee home rate from the
 employee master file defaults.

2a. If the Payroll Installation > Default pay rate field is set to Employee pay rate, then the employee home
 rate from the employee master file defaults.
– OR –
2b. The employee-specific phase rate from the pay group file defaults.
2a. The employee-specific phase rate from the pay group file defaults.
 – OR –
2b. The phase rate override from the pay group file defaults.

3. The employee-specific rate from the pay group file defaults.
3. The employee-specific rate from the pay group file defaults.

4. The pay group rate from the pay group file defaults.
4. The pay group rate from the pay group file defaults.

5. The employee home rate from the employee master file defaults.
5. The employee home rate from the employee master file defaults.

Note: If the Higher of the two rates option is selected on the Payroll Installation > Default tab and if the rate is non-zero, the software compares the
 employee home rate to the pay rate and uses the higher of the two.
Note: If the Higher of the two rates option is
 selected on the Payroll
 Installation > Default tab and if the rate is non-zero, the software compares the
 employee home rate to the pay rate and uses the higher of the two.

Related information

- [Pay Groups Pay Rate Hierarchy Flow Chart](/en/spectrum/spectrum/accounting/payroll/default-hierarchies-overview/pay-group-rate-default-hierarchy/pay-groups-pay-rate-hierarchy-flow-chart)
