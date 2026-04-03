---
title: "Recurring Transaction Entry - ES - Standby Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/data-entry-overview/recurring-transaction-entry/recurring-transaction-entry---es---standby-field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/data-entry-overview/recurring-transaction-entry/recurring-transaction-entry---es---standby-field-descriptions"
---

# Recurring Transaction Entry - ES - Standby Field
 Descriptions

Use this grid to enter equipment revenue transaction lines
 for equipment with a standby status.

- If the Automatically add transactions for attached equipment checkbox is
 selected in the Equipment Control Installation screen, and if the specified
 equipment code has any attached equipment, additional transaction lines will be
 generated for the attached equipment codes when the update is run.

- When entering transactions by equipment standby (ES),
 transactions can be entered by Job or by Rental.

- If Document Imaging is being used, any images stored for this
 screen are saved in the EC cabinet, by default.

Fields
Descriptions

Equipment code Description
Enter the equipment code or select from a list of
 valid equipment codes. The equipment description will display.

Type
Select Job rate type or Rental rate type.

Company
For consistency and control, equipment transactions
 are always recorded in the equipment company.

Job Phase Ct
If a Job rate type has been specified, enter or select
 a job, phase and cost type.
Note: If the phase status is Complete,
 data entry is not allowed. If the phase status is Inactive, a warning
 message displays.

Rate type
Select the billing rate type from the drop-down menu:
 Hourly, Daily, Weekly, or Monthly. After a rate type has been selected,
 another field displays prompting you to select whether there is a Full
 Charge or Operating rate for this job/rental rate.

Hours
Enter the number of hours to be charged to this
 transaction (when posted, these hours will be added to the last meter
 reading value). Meter reading changes also may be entered in the [Meter Readings](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/meter-reading-transaction-entry/meter-readings) window, but you
 must use the [Meter Reading Transaction Entry](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/meter-reading-transaction-entry) screen to delete unwanted meter transactions.
 To view the more information about meter replacement, click [Meter Replacement](/en/spectrum/spectrum/equipment/equipment-control/troubleshooting/meter-replacement).
If the current meter reading was previously recorded,
 the Hours
 default value is the difference between the current meter reading and the
 last meter reading (for example, current meter reading of 778 hours -
 last meter reading of 710 hours = 68 hours). If the difference in meter
 readings is a negative number, nothing defaults. Either number may be
 manually overwritten.

U/m
The unit of measure displays. All equipment types on
 this screen are hourly.

Rate
Enter the transaction rate (the amount to be charged
 per hour, per day, per week, or per month); entries of up to 99,999.99
 per period are allowed.
Hierarchy for charge rates
If applicable, this rate information will default the
 amount set up in the Job-Specific Equipment Charge Rates screen. If no
 job-specific record is found (or rate is blank), the system will
 determine if this job is a sub job of a master job and use the
 job-specific rate from the master job. If there is no job-specific rate
 for the job or master job, the system will read for the standard job rate
 of the equipment code.

Extension
The extension total displays. Press Enter to accept
 the calculated default or enter a new extension amount (entries up to
 9,999,999.99 are allowed). The extension is computed as the "hours"
 multiplied by the "rate".

Bill rate
The billing rate assigned to the equipment and any
 attachments will default from the stand-by rates defined on the Time + Material > Job Equipment Billing Rate Maintenance screen, based on Hourly, Daily, Weekly or Monthly rates.
 If there is no rate defined there, Spectrum will look to the Equipment
 Billing Rate Maintenance table for the stand-by billing rate. If no rate
 is defined there, the billing rate is zero.

G/L debit
The default debit G/L account code displays. Enter to
 accept the default, or enter the desired account for this transaction.
 The account description will display.

- Multi-Company Entry:The Rental debit is for a G/L
 account in the company using the equipment, not the company where
 the equipment is set up.

G/L credit
Enter the credit G/L account code for this
 transaction. The account description will display. Select the No direct
 cost option in the G/L Master File MaintenanceDirectcost option group for
 the company holding the equipment.

- For "Job" type transactions: The default credit
 G/L account code displays from the Job credit field
 in the Equipment Control Installation screen. If the installation
 field is blank, the credit will default from the latest saved job
 credit entry.

- For "Rental" type transactions: The default
 credit G/L account code displays from the Rental credit
 field in the Equipment Control Installation screen. If the
 installation field is blank, the credit will default from the
 latest saved rental credit entry.

Note
 Regarding Multi-Company Entries
For rental credits, the system defaults the G/L
 account from the equipment company, and if not specified in that company,
 the latest saved rental credit defaults. For job credits, the system
 always defaults the cost type G/L account from the job company, if not
 specified in that company, then the latest saved job debit defaults.

Remark
Enter any pertinent remarks. Information recorded in
 this field is stored in the Equipment Cost History file when it is
 updated.

Related information

- [Transaction Entry by Equipment Standby - Cost Center Information](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/data-entry-overview/revenue-transaction-entry/transaction-entry-by-equipment-standby---cost-center-information)
