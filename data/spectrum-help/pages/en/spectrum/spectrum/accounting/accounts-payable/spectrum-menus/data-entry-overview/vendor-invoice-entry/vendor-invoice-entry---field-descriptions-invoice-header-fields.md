---
title: "Vendor Invoice Entry - Field Descriptions: Invoice Header Fields | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-invoice-entry/vendor-invoice-entry---field-descriptions-invoice-header-fields"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-invoice-entry/vendor-invoice-entry---field-descriptions-invoice-header-fields"
---

# Vendor Invoice Entry - Field Descriptions: Invoice Header Fields

Use the field descriptions in table below for reference when completing the header portion of the Vendor Invoice Entry screen.
Fields/ButtonsDescriptions
Route for approval?Select this checkbox if Invoice Approval Routing is being used (as determined by the Accounts Payable Installation setting to Use Invoice Approval?). This field always defaults to cleared when adding a new invoice and it only controls the initial default for users that have permission to enter both unapproved and unposted invoices.
See also:
[AP Invoice Routing Hierarchy for an Equipment Direct Cost Expense](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-hierarchies/ap-invoice-routing-hierarchy-for-an-equipment-direct-cost-expense)
[Detail Approval Performance Report By Job - Sample Report](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/detail-approval-performance-report-by-job---sample-report)

Current reviewerThe current reviewer defaults based on the routing code.
BatchThis field displays only when the invoice is not being routed for approval. Enter the batch code for this group of invoices or use the search window to select. The batch code defaults to the operator code, but may be overridden.
The screen provides on-screen information about the current batch of unposted invoices, continuously displaying the number of invoices and credit memos and the total dollar amount currently contained in the current batch. You can also drill-in to these items.

VendorAssign a vendor to the invoice or credit memo you are entering. An indicator displays if the selected vendor has any open subcontracts. Vendors with a status of Not used may not be selected.
Invoice #Enter an invoice number. If the invoice already exists, the job number associated with the invoice displays. Duplicate invoice numbers are not allowed.
Validation is provided to make sure the invoice number entered is not a rejected invoice, as set up in [Vendor Rejected Invoices](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-financial-summary/vendor-rejected-invoices)

Invoice typeEnter Invoice when entering an invoice. Otherwise, enter Credit memo when entering a credit memo. The software proceeds based on the following scenarios:

- If the entered invoice exists, is unapproved, and you have authorization for Invoice Approval, the transactions already in the approval routing process display.

- If the entered invoice exists, is unposted, and you have authorization to access unposted transactions, these transactions display.

- If the entered invoice is new, proceed to the entry fields. Important: Credits are entered with positive dollar amounts. The system automatically recognizes credit memos as negative dollars.

Purchase orderPress Enter to leave this field blank if the invoice being entered will not be applied against a purchase order. Otherwise, enter the number of the purchase order against which this invoice will be applied. If the purchase order entered is not valid, the status of the purchase order is 'Closed' or 'Proposed', or if the Operator does not have cost center authorization to the purchase order, entry will be disallowed. If the Purchase Order module is not present, any purchase order number can be entered in this field.
As soon as the Operator specifies a valid purchase order, Spectrum will verify that the vendor code associated with the purchase order is the same as the one specified above. If the vendor code matches the one specified for the selected purchase order, the cursor will move to the G/L date field. If the vendor code is different that the one specified above, the software will determine if the P.O. code can be overwritten based on the setting defined in Purchase Order Installation > Properties.
Once the purchase order being received is determined, the following fields will appear in the header:

- If the purchase order was purchased with credit card (as indicated in Purchase Order Entry), the Check/Credit Card button below will indicate it is paid.

- If a job code is assigned in the Purchase Order Header Table, the Job number associated with the P.O. will display to the right of the Invoice # field.

- If the purchase order receiving method is set to one-step, the Receive in full? checkbox will display beneath the Purchase order field. Select this checkbox to determine how the Quantity column defaults in the grid.

- If the purchase order receiving method is set to two-step, the Packing lists field will display beneath the Purchase order field. When the cursor advances to this field, the Packing Lists window opens automatically. If no packing lists exist for this purchase order, this field will remain blank. If only one packing list is present, the packing list sequence will automatically be selected and display in this field. If multiple packing lists are selected in this window, the sequence numbers will be displayed in order in this field.

- The More Invoice Information window will display info from the purchase order. If no packing lists are selected, this field will remain blank. If only one packing list is present, this item will be selected automatically and display in this field.

- Purchase order current totals will display in the upper right hand side of the header, as described below. These totals will only display when creating a new receiving invoice.

- Once the header fields are completed, the [Purchase Order Receiving Detail](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/purchase-order-receiving-detail) window will automatically open. If accessing an existing vendor invoice that originated from Purchase Order Receiving, the details will appear in the grid below. Separate security restrictions are available (in Function Security Maintenance) for the Close P.O. now? option when saving a new P.O. invoice.

SubcontractPress Enter to leave this field blank if the invoice being entered will not be applied against a subcontract. Otherwise, enter the number of the subcontract against which this invoice will be applied. Subcontract current totals will display in the upper right hand side of the header, as described below. Invoices can be distributed to jobs without setting up a subcontract. However, that information cannot then be displayed or printed by job in the subcontract management inquiries and reports.
If a subcontract # has been specified, the [Subcontract Invoice Entry Type](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/subcontracts/subcontract-invoice-entry-type) window displays (slightly different offerings display in this window based on whether the subcontract is fixed price or unit price).

G/L dateThis field only displays for unposted transactions.
Entry dateThis field only displays for unapproved transactions.
Invoice dateThis invoice date is used to age the invoice, and is also used for calculating the invoice due date. Entry in this field is validated against the Accounts Payable maximum date if the Stop entry if invoice date after maximum date option is selected in the Accounts Payable Installation in the current company. Note: If the Stop entry if invoice date after maximum date checkbox is selected in the Accounts Payable Installation > Properties tab, the date entered in this field must fall before the maximum Accounts Payable processing date.

Total before taxEnter the total invoice dollar amount (without tax) as a positive number, whether it is an invoice or a credit memo. The amount total will evaluate whether a subcontract is fully-billed, including any unposted invoices or credit memos assigned to the subcontract. The system will check the dollar amount entered and display an error message if the amount entered exceeds the revised contract amount in the subcontract file. If the Accounts Payable Installation checkbox for subcontract stop payment is selected, then amounts in excess of the revised contract amount will be disallowed.
When two-step purchase order receiving is used, the total before tax amount will default to the packing list total.

Sales taxIf applicable, enter the sales tax amount.
Total amountThe combined total, including sales tax, displays. No changes are allowed.
Payment Plans[ Vendor Invoice Entry - Field Descriptions: Payment Plans Fields](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-invoice-entry/vendor-invoice-entry---field-descriptions-payment-plans-fields) for field descriptions.
Buttons
More InfoSelect this button to display secondary invoice details, such as routing and discount information. Depending on your settings, this window may display automatically after completing the header fields. If cost centers are being used, the Administrator can specify a cost center to default into the heading of all new invoices.
More Invoice Information windowFieldsDescriptions
Routing codeThis field only displays if approval routing is being used (set up in Accounts Payable Installation).
Invoice remarkEnter any remarks that you want to appear on the Remittance Advice. This field may be useful for describing what was purchased on this invoice. These remarks display in the Payment Inquiry screens and on the separate remittance advice printed during A/P Payment Processing. Entries there will then update to Job Cost History and the Time + Material modules.
Tip: Type a plus sign (+) to duplicate the last entry into the Remarks field in the screen.

Cost centerThis field only displays if cost centers are being used in the current company.
A/P G/L accountThe Accounts Payable General Ledger account code displays from the Installation menu.

- If this is a subcontract invoice (for example, a subcontract number was entered above) then the subcontract payable account will display.

- If it is a non-subcontract invoice, then the trade payable account will display.

- If a related-party vendor is entered, the override A/P trade G/L account will default when updated.

Use the up arrow from the Payment date prompt to access this field for changes. After an account number is entered, the account name will display. Changes to direct work order cost G/L accounts are not allowed in Accounts Payable if the invoice originated in Purchase Order.
Cost Center Information
Spectrum allows entry of a G/L account code only if you have permission to assign that code. Spectrum compares the G/L account's list of shared cost centers with cost centers in your operator's assigned cost center scheme, and if there are no common cost centers, then that G/L account cannot be assigned.

Currency codeThis field is for use when multi-currency is available.

Discount dueThe discount date is calculated and displayed, based on the discount terms entered in the Vendors screen.

Discount amountFor companies that calculate term discounts by line item, this field shows the total calculated discounts. Discounts are based on the Total before tax amount. This is a display-only value allowing organizations to enforce the security rule that all discount decisions are to be made at time of payment, not at entry of an invoice.

Remit to alternate payment location?If the Default payment location? checkbox is selected in the [Vendor Locations](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-main-properties/vendor-locations) screen, the remit checkbox will automatically be selected and the Location code defaults, along with the corresponding name and address. You can use the available drop-down arrow to select a different location code.
If no location code is present, the vendor name and address displays.

Routing buttonIf this button is enabled, select it to display the [Invoice Approval Routing History Inquiry](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/invoice-approval-routing-history-inquiry) window. Depending on your settings, this window may display automatically after completing the More Information window. Use this window to view the history of the invoice selected in the line transaction portion of the screen. If there is no routing history for the selected invoice, this window will appear blank.

User-DefinedSelecting this button opens the [Invoice User-Defined Fields Maintenance](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/invoice-user-defined-fields-maintenance) window.
ReverseThis button only displays when you are not currently entering an invoice and is used to access the [Reverse Vendor Invoice](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/reverse-vendor-invoice) screen.
PreferencesThis button only displays when you are not currently entering an invoice and is used to access the Operator Vendor Invoices Preferences window where you can use configuration settings to streamline your navigation — including options to always offer a Billing Worksheet when adding a sub progress billing and always defaulting to NOT route for approval when adding a new invoice. Preferences to skip windows do not apply to existing transactions.

DetailsThis button only displays when you are receiving purchase orders. The Purchase Order Receiving Detail window will open immediately after entering the header information for the purchase order.
Edit
New
Insert
Delete
Use these action buttons to manage invoices.
 Revert to P.O. ReceivingThis button is applicable to One-Step Purchase Order Receiving only. When saving a P.O. receiving entry entered in Vendor Invoice Entry, the record is changed into a standard invoice. At this point, only those items that were received on are brought forward onto the invoice. There are scenarios when the receiving quantities were entered incorrectly. The Revert to PO Receiving button provides the ability to correct the quantities received on a one-step purchase order that is still open.
To move back a step in the process, call up the unposted or unapproved invoice and select the Revert to P.O. Receiving button. This will allow quantities received to be adjusted or modified as needed. When the invoice is saved, any revisions will be reflected on the purchase order as well as in open commitments.
This is only available on unposted and unapproved invoices. The Revert to P.O. Receiving button is only available on open purchase orders. In the event that a P.O. with items still on order is accidentally closed, you will only have to reopen the P.O. first and then make changes.
Important: Any additional rows added to the invoice are deleted when you select the Revert to P.O. Receiving button. Any modifications on the invoice will be lost as you are returning back to PO Receiving Entry.
Details Button
Before saving the invoice when the purchase order is first received, you can select Details to open to the Purchase Order Receiving Detail window. Once the transaction is saved, only the lines that were received are brought forward to the vendor invoice. Think of this as converting the P.O. receiving to an invoice.
Revert to P.O. Receiving Button
Now that the purchase order has been converted into an invoice, you can select the Revert to P.O. Receiving button to return back a step and modify the receiving once again.
