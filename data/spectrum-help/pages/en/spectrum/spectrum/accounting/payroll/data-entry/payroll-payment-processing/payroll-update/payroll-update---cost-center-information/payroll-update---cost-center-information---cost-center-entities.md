---
title: "Payroll Update - Cost Center Information - Cost Center Entities | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/payroll-update/payroll-update---cost-center-information/payroll-update---cost-center-information---cost-center-entities"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/payroll-update/payroll-update---cost-center-information/payroll-update---cost-center-information---cost-center-entities"
---

# Payroll Update - Cost Center Information - Cost Center Entities

If entity tracking is enabled in Enterprise Installation, the software will look for the entity code stored in the check cost center for the pay cycle and will then store entity-specific taxes, deductions, add-ons and time off benefits for employees.
The Payroll Update will look for the entity-specific G/L breakdown of Worker's Compensation 'rate detail' when the pay cycle is for a particular entity (other than the 'main company entity'). The software will first determine if the particular worker's compensation code has an override record for the entity code assigned to this pay cycle, and if an override exists, the software will look for any 'Override' worker's Compensation $/100 component rate(s) for the entity code. These overrides are assigned using the Entity Override button in [Worker's Compensation Code Maintenance](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/workers-compensation-code-maintenance).
