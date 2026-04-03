---
title: "A/P Invoice Detail - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-invoice-detail/ap-invoice-detail---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-invoice-detail/ap-invoice-detail---field-descriptions"
---

# A/P Invoice Detail - Field Descriptions

The following are the field descriptions for the
 A/P Invoice Detail screen.
Fields
Descriptions

Account code
The default General Ledger account to which this vendor's invoices should be
 posted displays (as entered in the [About Vendors](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors)
 screen). The default may be overwritten, if desired. Note: To enter equipment line, select an
 equipment cost G/L code instead of a vendor G/L code.

If the invoice should be distributed to a job, the General Ledger account MUST
 have the Job Cost option selected in
 G/L Master File Maintenance Direct cost
 menu. If the No Direct Cost option is
 selected in the G/L Master File Maintenance > Direct cost menu, the software will skip the job and phase
 prompts. This validation ensures that Work-in-Progress direct costs
 in the General Ledger are always in balance with the job cost
 system. The system also verifies whether the Job division with
 G/L department checkbox is selected in
 Job Cost
 Installation for this company, and if so, requires
 the job division to match the General Ledger department. A search
 window is available for viewing valid General Ledger account
 codes.

Description
The description associated with the selected General Ledger account displays. No entry is allowed.

Job
Equip
WO
The previously entered General
 Ledger account must be a work-in-progress account (Direct
 cost menu has the Job cost
 option selected) to allow entry in this field.

- If this is a subcontract invoice, the
 subcontract job will default. Otherwise, enter the number of
 the job to which this invoice is to be distributed; the job
 name will display on the second line.

- An invoice may be distributed to multiple
 jobs, phases, and cost types. If you have an invoice with
 multiple jobs in the detail lines, please note that the
 invoice will only display once on the [Aged Payables Report](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-reports/aged-payables-report) (in the section for the last job
 on the invoice).Note: If you need to
 show the job amounts separately, it is recommended that
 you enter separate invoices.

Equip
The previously entered General Ledger account
 must have its direct cost flag equal to Equipment in order to enter
 an equipment code (G/L
 Master File Maintenance Direct Cost menu is set to
 Equipmentcost.) Enter the code for the piece of equipment used for
 this invoice. The full equipment name will display on the next line.
 A search window is available for viewing valid equipment
 codes.

- If the checkbox in the Preventive
 Maintenance Installation screen is selected,
 a maintenance work order number must be entered and it must
 be valid. If this checkbox is selected, the following window
 appears.

- If the equipment code you select is
 flagged as Retired in the Equipment File
 Maintenance screen, the software will
 prevent further invoice entry for this piece of equipment.
 If the equipment code you select is flagged as Inactive, a
 warning will display.

WO
If the Work Order module is present,
 this field will change to Job/Equip/WO and
 the Work
 Order button will appear at the bottom of the
 window. Enter the maintenance work order number, or window to
 search. If an invoice has already been selected for billing, changes
 will not be allowed.

Phase
Cat
Enter the phase to which this invoice is to be distributed; the description
 will display on line two. If this is a subcontract invoice, the
 subcontract phase will default.Note: Data
 entry is prevented if the phase status is set to Complete. A
 warning displays if the status is set to Inactive.

Cat
The previously entered General Ledger account must have the
 Equipment cost option selected in the
 Direct cost menu in order to enter a
 Category code. Enter the cost category for this invoice/piece of
 equipment.
Once a cost category is entered or selected, the software evaluates whether to
 prompt for an equipment work order number by checking the Equipment Control > Cost Category File Maintenance page's Data entry radio group. If the radio group it is
 set to None, the cursor continues to Amount field. If
 the radio group is set to Optional or
 Require equipment
 work order, then the cursor stops in the Ct/Eq WO
 field.

Ct
Eq WO
Enter the cost type or equipment work order number to which this invoice is to be distributed; the description will display on line two. If this is a subcontract invoice, the subcontract cost type will default, but may be overwritten.
Invoices may be distributed to multiple jobs, phases, and cost types. Note, however, that the chart of accounts and cost types file may be set up such that a specific cost type MUST be charged to a specific account.

- If this transaction line is related to a subcontract phase and/or cost type,
 the Contract Hours window may
 display, depending upon your installation settings, once you
 press Enter to exit this field.

- If this transaction line is related to an equipment work order and the
 Equipment
 Control > Cost
 Category File Maintenance > Data
 entry radio group is set to Require equipment
 work order, then entry in this field is
 required.

Bill item
The bill item displays. Only users with a security level of 2 or 3 may enter information in this field.

Amount
Enter the amount to be distributed to the entered General Ledger account (and,
 as appropriate, the job/phase/cost type or equipment/cost category).
 A window is available to allow entry of the applicable A/P tax
 percent information for this line. The sales or use tax code will
 default based on the Job or Vendor setup, depending on the entry in
 the Job Cost Installation screen. When tax
 classification is not selected in Job Cost
 Installation, the tax code will default from the
 vendor, if specified. When tax classification is used, the tax code
 will default based on the job or vendor, depending on the
 Job Cost Installation setting for tax
 class default.
You can set up either a sales tax code or a use tax code. A sales tax code will add the sales tax amount to the vendor invoice, and this amount will be posted to the invoice total amount. A use tax code will accrue use tax to a separate G/L liability account and will not add the tax amount to the vendor invoice.
The tax code default can be overwritten by opening the Tax Percent window. Any changes made by the operator will become the new tax setting for the line unless the operator re-opens the window and records different tax settings.

cc
If multiple companies are not set up, the company code field is irrelevant and does not display.
If multiple companies are set up, the cursor will be in the account
 code field, ready for entry of a G/L account; the
 company code displays on the second line. To distribute the invoice
 to a different company, use SHIFT + TAB to
 move the cursor to this company code field, then enter the desired
 company code. Pressing Enter will return the cursor to the account code
 field.
In posting an invoice to only one company, the A/P G/L account entered in the
 header is credited, and the account entered in line transactions is
 debited. In posting an invoice to multiple companies, the A/P G/L
 account entered in the header is credited for company A, and company
 A's intercompany account is debited. Company B's intercompany
 account is then credited and the company B account entered in line
 transactions is debited. This posting is done automatically by the
 software when the A/P Transaction Update is run (which follows the
 A/P Transaction Register). For every company, the inter-company
 clearing account must be entered in the chart of accounts. These
 accounts must also be defined in each company's Accounts
 Payable Installation page. The system performs a
 validation to assure that inter-company accounts in both the source
 and destination companies are valid and Direct Cost = No.

Expand
Click this button to view additional entry fields.

Contract Hours
Click this button to open the [Contract Hours](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-recurring-invoice-entry/vendor-recurring-invoice-entry---field-descriptions-grid/contract-hours) window.

Taxes
Click this button to open the [Tax Information window](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-invoice-detail/tax-information-window) window, where you can modify tax details.

Related information

- [Contract Hours](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-recurring-invoice-entry/vendor-recurring-invoice-entry---field-descriptions-grid/contract-hours)

- [Tax Percent window](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-invoice-entry/tax-percent-window)
