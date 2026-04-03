---
title: "New/Edit Union - Fringes tab - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/union-file-maintenance/newedit-union---fringes-tab/newedit-union---fringes-tab---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/union-file-maintenance/newedit-union---fringes-tab/newedit-union---fringes-tab---field-descriptions"
---

# New/Edit Union - Fringes tab - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields/Buttons
Descriptions

Fringe code
Select a fringe code from the drop-down list to add to the selected union code.

Type
Select the fringe type from the drop-down list.
Percent of gross:
The calculation for this method is total earnings multiplied by the designated rate.
For example, if the percentage of gross is set to 3%:
regular pay 10hrs x $10 = $100 will deduct $3.00
overtime pay 10hrs x $15 = $150 will deduct $4.50
double-time pay 10hrs x $20 = $200 will deduct $6.00
Percent of base:
 The base rate is found at Payroll > Maintenance > Union > Rates, by pressing F4 in the Regular field. The
 calculation for the 'percent of base' is similar to the 'percent of gross',
 except the wages upon which the rate is applied are determined in the union
 file or pay group. The base is recorded on the wage rates screen of
 Union File Maintenance by windowing at wage rate
 or in the Non-Union Pay Group Maintenance > Prevailing Wage window.
For example, if the percentage of gross is set to 3% & the base is $9/hr:
regular pay 10hrs x $(10-1) = $90 will deduct $2.70
overtime pay 10hrs x $(15-1) = $140 will deduct $4.20
double-time pay 10hrs x $(20-1) = $190 will deduct $5.70
Regular equivalent hours= (REG + OVT +DBL)
Overtime equivalent hours = [REG + ((OVT + DBL) *1.5)]
Double-time equivalent hours = [REG + (OVT +*1.5) + (DBL *2)]
All hours = (REG + OVT + DBL + OTHER HOURS)
User-defined formula

Rate
Enter the rate percent that you want to apply to the fringe.
If you are adding a fringe rate revision, select the Formula code to automatically calculate the rate revision.

Fringe payable
Enter the General Ledger liability account code for the fringe payable, or double-click on this field to select from a list of available General Ledger account codes. The account description will display. The account must have the No direct cost option selected in the G/L Master File Maintenance direct cost menu in order to display this information.

Effective date
Enter the date on which the new fringe should take effect, or double-click on
 this field to select a date from the Date Change
 window. This field can be used to schedule a future fringe adjustment.

Status
The status of the selected fringe code displays.

Fringes button
Clicking this button in Spectrum displays the Fringe
 Maintenance window. Use this window to view and manage the
 fringe codes that are currently set up in the system.
