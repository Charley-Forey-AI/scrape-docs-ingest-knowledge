---
title: "Pre-Time Card Auto-Overtime | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/pre-time-card-auto-overtime"
fetched_at: "2026-04-03T20:47:07.463050+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/pre-time-card-auto-overtime"
---

# Pre-Time Card Auto-Overtime

Use this screen to calculate the overtime rate for pre-time
 cards.
Calculate based on criteria discussed in [Auto-Overtime Processing](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/time-card-entry/auto-overtime-processing).
The software looks for the last job/wage code on the last job to see whether to calculate overtime or not. If there is no job for the employee for the pay cycle, no auto overtime will be calculated, but the Edit List may be run. The calculation for auto overtime is performed across all checks for an employee (not each sequence number). After previewing and printing the listing, the Pre-Time Card Auto-Overtime Update screen displays. Select Continue to update the time cards, or Cancel to exit.
When the overtime or double-time card line is created, it will be assigned the same work order #, site equipment, component, contract and WO/TC control codes associated with the source time card entry, and the software will set the 'Available for billing' flag based on the setting in the original time card line. When the overtime or double-time card line is created from an entry that has already been billed, then the Employee billing rate and Equipment billing rate values will be set equal to the values in the original time card line.
Note: Vacation, Holiday, Sick, and JX hours are not used
 when calculating overtime, and they do not appear on edit lists. The Auto Overtime default
 first looks at the wage code information in Job File Maintenance and then at the Job File
 window.
