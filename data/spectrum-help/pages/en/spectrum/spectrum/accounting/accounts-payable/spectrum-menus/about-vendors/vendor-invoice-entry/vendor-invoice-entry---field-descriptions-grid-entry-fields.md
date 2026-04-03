---
title: "Vendor Invoice Entry - Field Descriptions: Grid Entry Fields | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-invoice-entry/vendor-invoice-entry---field-descriptions-grid-entry-fields"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-invoice-entry/vendor-invoice-entry---field-descriptions-grid-entry-fields"
---

# Vendor Invoice Entry - Field Descriptions: Grid Entry Fields

Use the descriptions in table below for reference when
 completing the grid portion of the Vendor Invoice Entry screen.
The grid column descriptions vary depending on the transaction type.
Columns
Descriptions

Company
If multiple companies are not set up, the company code
 field is irrelevant and does not display. If multiple companies are set
 up, the cursor will be in the "account code" field, ready for entry of a
 G/L account; the company code displays on the second line.
In posting an invoice to only one company, the A/P G/L
 account entered in the header is credited, and the account entered in
 line transactions is debited.
In posting an invoice to multiple companies, the A/P
 G/L account entered in the header is credited for company A, and company
 A's intercompany account is debited. Company B's intercompany account is
 then credited and the company B account entered in line transactions is
 debited. This posting is done automatically by the system when the A/P
 Transaction Update is run (which follows the A/P Transaction Register).
 For every company, the inter-company clearing account must be entered in
 the chart of accounts. These accounts must also be defined in each
 company's Accounts Payable Installation screen. The system performs a
 validation to assure that inter-company accounts in both the source and
 destination companies are valid and Direct Cost = No.

G/L account
The default General Ledger account to which this
 vendor's invoices should be posted displays (as entered in the Vendor
 Defaults screen). The default may be overwritten, if desired.
Note: To enter
 equipment line, select an equipment cost G/L code instead of a vendor G/L
 code.
If the invoice should be distributed to a job, the
 General Ledger account MUST have the Job Cost option selected in G/L
 Master File Maintenance Direct cost menu. If the No Direct Cost option is
 selected in the G/L Master File Maintenance Direct cost menu, the system
 will skip the job and phase prompts. This validation ensures that
 Work-in-Progress direct costs in the General Ledger are always in balance
 with the job cost system. The system also verifies whether the Job
 division with G/L department checkbox is selected in Job Cost
 Installation for this company, and if so, requires the job division to
 match the General Ledger department. A search window is available for
 viewing valid General Ledger account codes.
If a related-party vendor is entered, the override A/P trade G/L account
 will default when updated. If left blank, the G/L account from the
 Install screen will default.
If the 'Automate G/L defaults' option was selected in
 Accounts Receivable Installation, you can enter a shortcut in this field
 to automatically default the G/L direct cost codes defined on the
 installation screen:

- J - This will set the G/L code to the direct job cost
 setting

- E - This will set the G/L code to the direct equipment
 cost setting

- W - This will set the G/L code to the direct work
 order cost setting

- N - This will set the G/L code to pass in the
 non-direct cost setting

If this option is selected and you do not enter a
 shortcut, the Select Type
 of Distribution window will open to select the G/L account
 codes specified in the installation screen. If no direct-cost G/L account
 was specified, the Search G/L accounts window will open instead.

Amount
Enter the amount to be distributed to the entered
 General Ledger account (and, as appropriate, the job/phase/cost type or
 equipment/cost category).
The sales or use tax code will default based on the
 Job or Vendor setup, depending on the entry in the Job Cost Installation
 screen. When tax classification is not selected in Job Cost Installation,
 the tax code will default from the vendor, if specified. When tax
 classification is used, the tax code will default based on the job or
 vendor, depending on the Job Cost Installation setting for Tax class
 Default. You can set up either a sales tax code or a use tax code. A
 sales tax code will add the sales tax amount to the vendor invoice, and
 this amount will be posted to the invoice total amount. A use tax code
 will accrue use tax to a separate G/L liability account and will not add
 the tax amount to the vendor invoice. Any changes made will become the
 new tax setting for the line.

Job
The previously entered General Ledger account must be
 a work-in-progress account (Direct cost menu has the Job cost option
 selected) to allow entry in this field.
 If this is a subcontract invoice, the subcontract job
 will default. Otherwise, enter the number of the job to which this
 invoice is to be distributed; the job name will display on the second
 line. The invoice may be distributed to multiple jobs, phases, and cost
 types. If you have an invoice with multiple jobs in the detail lines,
 please note that the invoice will only display once on the Aged Payables
 Report (in the section for the last job on the invoice).
Note: If you need to show the job amounts separately,
 it is recommended that you enter separate invoices.

Phase
 If this is a subcontract invoice, the subcontract
 phase will default. The invoice may be distributed to multiple jobs,
 phases, and cost types. This field may be left blank when adding an
 unapproved transaction.
Blank phase and cost type are only allowed when
 entering a 'standard' transaction that does not reference a subcontract.
 For subcontract invoices, the phase must be set up for the subcontract;
 for purchase order receiving, the phase and cost type will always be from
 the Purchase Order detail.
If the "Enable Phase over revised estimate' warning in
 invoice detail?" option is selected in the AP Installation screen, a
 warning displays in the detail grid when you enter a phase that is over
 budget.
If this is a sub-job transaction set up on a master
 job, double-click on this field to search phases for the sub-job. This
 will allow you to easily select a phase set up on a master job, but not
 present on the sub-job. Spectrum will add a new phase to the sub job if
 the current job is a sub-job of a valid master job, the phase lengths of
 both jobs match, and the Phase + Cost type combination for the current
 job is valid and not 'Complete'.
Note: Data entry is
 prevented if the phase status is set to Complete. A warning displays if
 the status is set to Inactive.

Ct
Enter the cost type to which this invoice is to be
 distributed. If this is a subcontract invoice, the subcontract cost type
 will default, but may be overwritten. [Contract Hours](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-recurring-invoice-entry/vendor-recurring-invoice-entry---field-descriptions-grid/contract-hours)
This field may be left blank when adding an unapproved
 transaction. Blank phase and cost type are only allowed when entering a
 'standard' transaction that does not reference a subcontract. For
 subcontract invoices, the phase must be set up for the subcontract; for
 purchase order receiving, the phase and cost type will always be from the
 Purchase Order detail.
If the 'Automate G/L Defaults' and 'Job G/L account
 defaults from cost type' options are selected in AP Installation, and the
 'Validate job division with G/L department' option in Job Cost
 Installation is not selected, the G/L account stored in the Cost Type
 Master Table will be assigned to this distribution line.
Invoices may be distributed to multiple jobs, phases,
 and cost types. The chart of accounts and cost types file may be set up
 such that a specific cost type MUST be charged to a specific account.


Billing item
The bill item displays when entering a standard
 subcontract invoice. Only users with a security level of 2 or 3 may enter
 information in this field.

Equipment
This field is only available if the Equipment Control
 module is present.
The previously entered General Ledger account must
 have its direct cost flag equal to Equipment in order to
 enter an equipment code (G/L Master File Maintenance Direct Cost menu is
 set to Equipment
 cost.) Enter the code for the piece of equipment used for
 this invoice.
 If the checkbox in the Preventive Maintenance
 Installation screen is selected, a maintenance work order number must be
 entered and it must be valid.

-  If the equipment code you select is flagged as
 Retired in the Equipment File Maintenance screen, the system will
 prevent further invoice entry for this piece of equipment.

- If the equipment code you select is flagged as
 Inactive, a warning displays.

Cost category
This field is only available if the Equipment Control
 module is present.
The previously entered General Ledger account must
 have the Equipment
 cost option selected in the Direct cost menu in
 order to enter a category code. After you select a cost category, if the
 code is set to Inactive, a warning displays but does not prevent further
 data entry.
When adding a new cost category, Spectrum will verify
 that the selected G/L account is not a restricted G/L account for the
 cost category code.

- If both the 'Automate G/L Defaults' and
 'Equipment G/L account defaults from cost category' options in AP
 Installation are selected, the G/L account will default from the
 Equipment Cost Category table.

- If the G/L account is restricted, a Search
 window will open displaying allowed G/L accounts for this cost
 category.

Once a cost category is entered or selected, the
 system evaluates whether to prompt for an equipment work order number by
 checking the Equipment Control > Cost Category File Maintenance screen's Data entry radio group.

Equipment W/O
This field is only available if the Equipment Control
 module is present.
Enter the equipment work order number to which this
 invoice is to be distributed.
 If this transaction line is related to an equipment
 work order and the Equipment Control > Cost Category File MaintenanceData entry
 radio group is set to Require equipment work order, then entry in this field is
 required.

Work order
If the Work Order module is present in the current
 company and G/L account is set to Direct cost = work order, enter the
 maintenance work order number, or use the available drop-down to select.
 If an invoice has already been selected for billing, changes will not be
 allowed.
If the 'Automate G/L Defaults' and 'Work order G/L
 account defaults from department assigned to work order type' options are
 selected in Accounts Payable Installation, the
 non-inventory material cost of goods sold G/L account from the Work Order
 G/L Department Table will be assigned to this distribution line.
Note: Entry of a
 work order with a dispatch status of 'proposed' will be
 disallowed.

Item code
This field is only available if the Work Order module
 is present in the current company or if the item has not been assigned an
 item code when originating from Purchase Order
 Receiving. Items with a 'Not used' status are not allowed.

Item description
This is a display-only field, unless the item is a
 non-stock item or the Inventory Control module is not present.

Unit cost
This column displays the result of the Amount column divided
 by the Quantity
 column.

Quantity
Enter the item quantity for this line.

Um
When 'phase + cost type' is changed,the system
 automatically reassigns the unit of measure of the new phase to this
 detail line.

Site equipment
This field is only available when the Work Order
 module is present in the current company and G/L account is set to Direct
 cost = work order. Enter a site equipment code or use the
 Search Equipment for Site window to select.

Component
This field is only available when the Work Order
 module is present in the current company and G/L account is set to Direct
 cost = work order. Enter a component or use the Search
 Components window to select.

Service contract
This field is only available when the Service Contract
 module is present in the current company and G/L account is set to Direct
 cost = work order. This column is only applicable when the referenced
 work order is for a service contract.

Unit bill
This field is only available when the Service Contract
 module is present in the current company and G/L account is set to Direct
 cost = work order.
When a direct work order cost entry is added, the
 software automatically calculates the Unit bill price, including material
 markup rates. If the Work order #, Unit cost, or Quantity is changed the
 software will automatically recalculate and default a new Unit bill
 value.

Unit cost
This column always displays (not just when the detail
 line is for Work Order), showing the simple math calculation of "Amount
 column divided by Quantity column" unless used for non-stock work order
 costing. This field is used when the current row is for a Work Order
 entry and you have specified a non-stock item on this row (or Inventory
 Control module is not present).

Remark
Any remarks entered in the More Info window
 display here.

Tax code
Enter the tax code (up to 15 characters) for this
 line. This field resets if if you edit the Job, Phase, or Cost type (Ct) fields.

Tax type
Either Use Tax or Sales Tax displays (based on the
 setting in Use Tax Code Maintenance). This field is display only.

Tax amount
The system calculates the tax
 amount.

Discount
This field shows the total calculated discounts. Display only since discount decisions are made at time of payment.

Cost center

Contract
If one or more cost types are entered in the
 Contract labor cost
 types field in the Accounts Payable
 Installation screen, then during the detail entry in
 Invoice/Credit Memo Entry, the system will
 automatically open the Contract Hours window. This
 window is only available when the cost type of the transaction line is
 specified in the Accounts Payable Installation
 screen as a contract labor type.

-  During the A/P Transaction Register Update,
 hours recorded in this window will be recorded in the Job Cost
 history files and the A/P invoice history files. The Job Cost
 Payroll Hours Analysis Report offers an option to include these
 contractor labor hours.

-  If the total contractor labor amount, billing
 code, or message text is adjusted, the new information will display
 on the main screen.

- Enter the regular, overtime, and double time
 hours worked and the corresponding pay rates. The system will
 automatically calculate the extension amounts. Use the Message name
 field to enter the worker's name or a note about the labor. Entry
 in this field is optional.

- Labor billing code: Enter the Time + Material labor
 billing rate code, or accept the system default from the
 Accounts Payable Installation screen of
 the company in which the job is set up. This field will not display
 if this is not a Time + Material job or phase. If this field is
 left blank, the system will update the A/P transaction to Time +
 Material files as an AP transaction. If a billing code is
 specified, the update to Time + Material will store the entry as a
 PR transaction with the applicable billing rate associated with the
 code.
Note: Negative
 hours may be entered and will display a negative extension amount;
 however the rate will remain a positive number.
