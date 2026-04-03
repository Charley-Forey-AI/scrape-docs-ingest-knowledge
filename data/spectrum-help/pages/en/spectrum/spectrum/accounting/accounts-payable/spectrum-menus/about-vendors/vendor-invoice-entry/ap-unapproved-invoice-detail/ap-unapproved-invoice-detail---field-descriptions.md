---
title: "A/P Unapproved Invoice Detail - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-invoice-entry/ap-unapproved-invoice-detail/ap-unapproved-invoice-detail---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-invoice-entry/ap-unapproved-invoice-detail/ap-unapproved-invoice-detail---field-descriptions"
---

# A/P Unapproved Invoice Detail - Field Descriptions

Use this table for reference when completing the fields on this screen.
FieldsDescriptions
Vendor, Entry type, Invoice no.No entry is allowed in these fields. The vendor code and description, the entry type (invoice or credit memo), and recurring invoice number display.
SeqSequence numbers are assigned and maintained by the software.
Account codeThe default General Ledger account to which this vendor's invoices should be posted displays (as entered in the Vendors).If the invoice should be distributed to a job, the General Ledger account MUST
 have the Direct cost option button set to
 Job cost in G/L Master File
 Maintenance. If the Direct cost option
 button is set to No direct cost, then the software
 will skip the job and phase prompts. This validation ensures that
 Work-in-Progress direct costs in the General Ledger are always in balance
 with the job cost system. The system also verifies whether the Job division
 with G/L department checkbox in the Job Cost
 Installation is selected, and if so, requires the job
 division to match the General Ledger department.

DescriptionThe description associated with the selected General Ledger account displays.Recall that in the chart of accounts, every account has a direct cost setting,
 which is set up in G/L Master File Maintenance.

- This setting should be set to Job cost for accounts which track work-in-progress for job costing.

- To track equipment cost information, the flag should be set to Equipment cost.

- If neither equipment nor job cost information is tracked in the G/L account, this setting should be set to No direct cost.

When an account code is entered during invoice entry, the software checks the direct cost flag in the chart of accounts. If the setting is set to No direct cost, the cursor will advance to the Amount column and allow entry of a dollar amount. If the flag set to either Job cost or Equipment cost, the cursor will request entry of job costing information before the amount is entered. If the flag is Equipment, the software will prompt for equipment cost information before the amount is entered.
Job/Equip/WOThe previously entered General Ledger account must be a work-in-progress
 account (Direct cost is set to Job
 Cost in G/L Master File Maintenance)
 to allow entry in this field. G/L CODE IS A DIRECT JOB COST ACCOUNT
 (Direct cost is set to Job
 Cost in G/L Master File
 Maintenance).Job
If this is a subcontract invoice, the subcontract job will default. Otherwise, enter the number of the job to which this invoice is to be distributed; the job name will display on the second line. The job entered must be a valid job in the job cost system.
Note that an invoice may be distributed to multiple jobs, phases, and cost
 types. The defaults are for convenience only, and may be overwritten. A
 search window is available for viewing valid job numbers. Within this is
 another window, the
 add/chg>
 job window, in which a new project manager information
 field has been added.
Equip
Note that the previously entered General Ledger account must have its
 Direct cost setting set to Equipment
 cost in order to enter an equipment code. G/L CODE IS A
 DIRECT EQUIPMENT ACCOUNT (Direct cost is set to
 Equipment cost in G/L Master File
 Maintenance). Enter the code for the piece of equipment used
 for this invoice. The full equipment name will display on the next line. A
 search window is available for viewing valid equipment codes.
If the equipment code you select is flagged as Retired
 in the Equipment File Maintenance screen, the
 software will prevent further invoice entry for this piece of equipment. If
 the equipment code you select is flagged as Inactive,
 a warning will display.
If the checkbox in the Preventive Maintenance
 Installation screen is selected, a maintenance work order
 number must be entered and it must be valid. If this checkbox is selected,
 a window with the following field appears.
WO
If a work order module is present, this field will change to
 Job/Equip/WO and the Work
 Order button will appear at the bottom of the window. Enter
 the maintenance work order number, or window to search.

Phase/CatEnter the phase to which this invoice is to be distributed; the description will display on line two. If this is a subcontract invoice, the subcontract phase will default. Note that an invoice may be distributed to multiple jobs, phases, and cost types. The defaults are for convenience only, and may be overwritten. A search window is available for viewing valid phase codes. Data entry is prevented if the phase status is set to Complete. A warning displays if the status is set to Inactive.Cat
The previously entered General Ledger account must have the Direct
 cost setting in G/L Master File
 Maintenance set to Equipment cost in
 order to enter a Category code. Enter the cost
 category for this invoice/piece of equipment. The cost category description
 will display on the next line. A search window is available for viewing
 valid equipment cost categories.

Ct/Eq WOEnter the cost type or equipment work order number to which this invoice is to be distributed; the description will display on line two. If this is a subcontract invoice, the subcontract cost type will default, but may be overwritten.Invoices may be distributed to multiple jobs, phases, and cost types. Note, however, that the chart of accounts and cost types file may be set up such that a specific cost type MUST be charged to a specific account. A search window is available for viewing valid cost types.

- If an invoice has already been selected for billing, the work order number will be in lookup mode only and changes will not be allowed.

- If this transaction line is related to a subcontract phase and/or cost type,
 the Contract Hours window may display,
 depending upon your installation settings, once you press
 Enter to exit this field.

- If this transaction line is related to a equipment work order and the Equipment Control > Cost Category File MaintenanceData entry
 radio group is set to Require equipment work order, then entry in this field
 is required.[Contract Hours](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-recurring-invoice-entry/vendor-recurring-invoice-entry---field-descriptions-grid/contract-hours)

Bill itemThis field appears only when entering a subcontract invoice or credit memo.
 The billing item displays based on information entered in the
 Subcontract File Maintenance screen. If multiple
 bill items have been recorded on this subcontract for this phase of the job,
 enter the applicable bill item. A search window is available for selecting
 the appropriate bill item.
ccThe company code defaults when the Enter multi-company invoices checkbox is
 selected on the Accounts Payable Installation > Properties tab. No entry is allowed.
MsgAny messages corresponding with the terms discount displays.
UmThe unit of measure, if any, displays.
QtyThe quantity associated with the distribution amount displays. No entry is allowed.
