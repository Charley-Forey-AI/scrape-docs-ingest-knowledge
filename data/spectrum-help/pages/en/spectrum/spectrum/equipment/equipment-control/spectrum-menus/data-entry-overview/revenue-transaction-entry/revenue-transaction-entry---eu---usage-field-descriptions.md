---
title: "Revenue Transaction Entry - EU - Usage Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/data-entry-overview/revenue-transaction-entry/revenue-transaction-entry---eu---usage-field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/data-entry-overview/revenue-transaction-entry/revenue-transaction-entry---eu---usage-field-descriptions"
---

# Revenue Transaction Entry - EU - Usage Field Descriptions

The Equipment Control module tracks two different dollar
 amounts: usage and cost (EU).
When a piece of equipment is being used for a job or is rented to another company, there
 is a benefit from that usage that the computer tracks on a dollars-per-hour basis.

- This screen also provides additional information for multi-company transactions. If the inter-company G/L accounts are invalid for the inventory or job companies, or the Job cost option in the G/L Master File Maintenance direct cost section is selected, then an error report will print and the transaction will not be included in the update.

- If Document Imaging is being used, any images stored for this screen are saved in the EC cabinet, by default.

- For consistency and control, equipment transactions are always recorded in the "equipment company" (rather than the job or rental company).

Fields
Descriptions

Equipment code Description
Enter the equipment code or select from a list of valid equipment codes. The equipment description will display.

Type
Select Job rate type or Rental rate type.

Company
For consistency and control, equipment transactions are always recorded in the equipment company.

Job Phase Ct
If a Job rate type has been specified, enter or select a job, phase and cost type.
Note: If the phase status is Complete, data entry is not allowed.
 If the phase status is Inactive, a warning message displays.

Rate type
Select the billing rate type from the drop-down menu: Hourly, Daily, Weekly, or Monthly. After a rate type has been selected, another field displays prompting you to select whether there is a Full Charge or Operating rate for this job/rental rate.

Tran type
Select the transaction type: Full or Operating.

Hours
Enter the number of hours to be charged to this transaction (when posted, these hours will be added to the last meter reading value). Meter reading changes also may be entered in the [Meter Readings](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/meter-reading-transaction-entry/meter-readings) window, but you must use the [Meter Reading Transaction Entry](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/meter-reading-transaction-entry) screen to delete unwanted meter transactions. To view the more information about meter replacement, click [Meter Replacement](/en/spectrum/spectrum/equipment/equipment-control/troubleshooting/meter-replacement).
If the current meter reading was previously recorded, the Hours default value is the difference between the current meter reading and the last meter reading (for example, current meter reading of 778 hours - last meter reading of 710 hours = 68 hours). If the difference in meter readings is a negative number, nothing defaults. Either number may be manually overwritten.

U/m
The unit of measure displays. All equipment types on this screen are hourly.

Rate
Enter the transaction rate (the amount to be charged per hour, per day, per week, or per month); entries of up to 99,999.99 per period are allowed.
Hierarchy for charge rates:
If applicable, this rate information will default the amount set up in the Job-Specific Equipment Charge Rates screen. If no job-specific record is found (or rate is blank), the system will determine if this job is a sub job of a master job and use the job-specific rate from the master job. If there is no job-specific rate for the job or master job, the system will read for the standard job rate of the equipment code.

Extension
The extension total displays. Press Enter to accept the calculated default or enter a new extension amount (entries up to 9,999,999.99 are allowed). The extension is computed as the "hours" multiplied by the "rate".

Bill rate
If this is a Time + Material job, the bill rate defaults. Press Enter to accept the default billing rate, or enter a new billing rate (entries up to 999,999.999 are allowed). Entry in this field will be transferred to the T+M module upon updating the [Transaction Report / Update](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/data-entry-overview/transaction-report--update).
If this is a sub-job billed from a master job, the software will read for job-specific setup rates for the master job, and if none are found use standard settings. If this is a sub-job billed at the sub-job level, the software will read for job-specific setup rates for the sub-job first, and if billing rates are not found then the master job, and if none are found there use standard settings.

G/L debit
The default debit G/L account code displays. Enter to accept the default, or enter the desired account for this transaction. The account description will display.
Multi-Company Entry: The Rental debit is for a G/L account in the company using the equipment, not the company where the equipment is set up.

G/L credit
Enter the credit G/L account code for this transaction. The account description will display. Select the No direct cost option in the G/L Master File MaintenanceDirectcost option group for the company holding the equipment.

- For "Job" type transactions: The default credit G/L account code displays from the Job credit field in the Equipment Control Installation screen. If the installation field is blank, the credit will default from the latest saved job credit entry.

- For "Rental" type transactions: The default credit G/L account code displays from the Rental credit field in the Equipment Control Installation screen. If the installation field is blank, the credit will default from the latest saved rental credit entry.

Note Regarding Multi-Company Entries:
For rental credits, the system defaults the G/L account from the equipment company, and if not specified in that company, the latest saved rental credit defaults. For job credits, the system always defaults the cost type G/L account from the job company, if not specified in that company, then the latest saved job debit defaults.

Remark
Enter any pertinent remarks. Information recorded in this field is stored in the Equipment Cost History file when it is updated.

Related information

- [Transaction Entry by Equipment Usage - Cost Center Information](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/data-entry-overview/revenue-transaction-entry/transaction-entry-by-equipment-usage---cost-center-information)
