---
title: "Accounts Receivable Installation - Properties | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/installation-overview/accounts-receivable-installation---properties"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/installation-overview/accounts-receivable-installation---properties"
---

# Accounts Receivable Installation - Properties

Use this tab to select default properties settings for the Accounts Receivable module. These settings can be changed as needed at any time.
When the Installation screen is selected for the
 first time, a message displays: "Control record for A/R not set up. OK to proceed." Once the
 Accounts Receivable Installation screen has been completed and
 the information saved, this message will not appear again.
Field
Description

Enter equipment on non-job invoices?
Select this checkbox if you want the software to prompt for an equipment code (if equipment is installed) after the quantity is entered in Invoice Entry. The software will then ask for the rate type Hourly, Daily, Weekly, Monthly and then the equipment rental rate will default automatically in the invoice price. When the invoice is updated to the General Ledger and Accounts Receivable, it will also update the equipment rental revenue in the equipment module.
If this checkbox is left clear, then the equipment code and rate type will not be displayed during Invoice Entry. You will not be able to charge equipment rental rates to the Equipment Control module.

Post to Job Cost from A/R invoice?
Select this checkbox to update invoice and credit memo information from the Accounts Receivable module to Job Cost. If this checkbox is selected, your Job Cost files will be updated with billing amounts (before sales tax) according to the Sales Journal report. If this checkbox is left clear, then during the Sales Journal Update, no information will pass to the Job Cost module when you update the Sales Journal.
Normally, this checkbox will be left clear during the conversion process as the open invoice balance figures are recorded; thereafter, this checkbox will be selected so invoices and credit memos will be recorded in your Job Cost files. If you do not have Job Cost module installed in this company, this checkbox should be left clear permanently.

Change requests update projected cost?
Select this checkbox if you want change request projected costs (quantity and hours) to update to Job Cost. If this checkbox is selected, then estimate revisions will increment phase and job projected fields.
If a change request is assigned to a change order with a different approval date than the change request, in Accounts Receivable, change request projected costs stay in the approved year/period of the change request when the change request status is type 1, 2, or 3. When a change request with status type 4 is attached to a change order, the change order date is used to assign projected cost to the job. If this checkbox is selected and you are entering a change order or a change request (with an action type of 1, 2 or 3), the software will add a record to the projected cost history file. There will be no 'backing out' entry created for the change, even if there are later projected dates for that phase on the job.

Use automatic customer numbers?
Select this checkbox if you want the software to assign a new customer number and enter "blank" for customer code in the Customers screen. If this checkbox is left clear, a customer number must be used when adding a new customer.
The software will also prompt for the next customer number. The number will be automatically incremented every time this feature is used.

Invoice date must be in G/L period?
Select this checkbox to verify the invoice date during Invoice Entry and Reverse Open Invoice Entry. If this checkbox is selected, the invoice date must be in the same period as the General Ledger date. If this checkbox is left clear, the invoice date may be outside the G/L date, but it still must be in the fiscal calendar.
This default is used during Invoice Entry and Reverse Open Invoice Entry. This feature is valuable for operations wanting to closely control the revenue per G/L with the invoice dates for the corresponding items; monthly revenue per G/L will match revenue based on invoices dated during the same period.
Date validation in AR and AP invoices
AR Customer invoices allow you to require that the invoice dates are validated. This protection helps you to make sure that you balance your monthly billings with G/L revenue for the period.
AP Vendor invoices, on the other hand, do not require (or offer) date validation. This is because you may wish to wait before sending an invoice due to disputes or not wanting the invoice on the aging yet, and more.

Must print invoices before posting?
Select this checkbox if your office will typically print A/R invoices after entry. If this checkbox is selected, you will be required to print invoices before they can be updated to customer accounts, General Ledger and Job Cost files during Invoice Entry. If this checkbox is left clear, then invoices are assumed to have been printed when you enter them, and can be updated without printing. You may "reprint" an invoice at any time if you wish, before or after update.
Operations that issue invoices in the field will likely leave this checkbox clear to avoid unnecessary print activity; companies that process most invoices at the main office are likely to select this checkbox so that all invoices will be printed and issued.

Print pay-when-paid subcontract worksheets for fixed price contracts?
Select this checkbox if you want the software to print the Fixed Subcontract Payment Worksheet during Cash Receipts Processing when a payment is received on the invoice generated from the particular draw request application.
Note: Clear this checkbox if the vendor and job are set up to use pay-when-paid terms because this feature takes the place of the worksheet process.
The payment worksheet provides a convenient method for determining when a payment for an AIA draw applicable is associated with a subcontractor payable for that same job and application and includes the payment amount and invoice balance information.
The key to making the pay-when-paid process work is to create a one to one relationship between revenue and cost. This relationship is accomplished by using the AR billing items. When the contract is created in Contract Maintenance and the schedule of values is broken down using billing items, the billing items are then attached to the individual phases in Job Cost Phase Maintenance. This creates the one to one relationship.

Print pay-when-paid subcontract worksheets for unit price contracts?
Select this checkbox if you want the software to print the Unit Subcontract Payment Worksheet during Cash Receipts Processing when a payment is received on the invoice generated from the particular draw request application.
Note: Clear this checkbox if the vendor and job are set up to use pay-when-paid terms because this feature takes the place of the worksheet process.
The payment worksheet provides a convenient method for determining when a payment for an AIA draw applicable is associated with a subcontractor payable for that same job and application and includes the payment amount and invoice balance information.

Print pay-when-paid worksheets for active subcontracts only?
This checkbox is only available when one of the preceding "pay when paid" checkboxes is selected and is used to control how the Cash Receipts Journal starting screen works.Select this checkbox if you only wish to print the worksheets for active subcontracts, or leave this checkbox clear if you wish to include all subcontracts on the worksheet.
Note: Clear this checkbox if the vendor and job are set up to use pay-when-paid terms because this feature takes the place of the worksheet process.

Default finance charge transaction code
Enter the primary finance charge transaction code you plan to use in the software. Up to 10 characters are allowed.
For example, you might want to type "FC", which would stand for 'Finance Charge'. Be sure to include this transaction code when you enter Transaction Code File Maintenance. Enter a default transaction code even if you do not intend to perform Finance Charge Calculation.

Default finance charge percentage
Enter the default finance charge percentage. This number will default whenever the finance charge code is changed in the customer setup.
When the AR module is first installed, this field will default to 0.00%.

Default unit price mask
Enter the display mask for the unit price field in Contracts, Contract File Listing, Draw Request Billing Entry, Print Draw Request Billing, Subcontract Billing Worksheet and the Print Draw Billing Worksheet for contracts using unit pricing.
The default display mask is "ZZZZZ.ZZZZ-", but you can enter any combination of "Z", "9", "," and "." as long as the total length of the mask is equal to no more than 10 characters and no more than one decimal point is used. The 11th character is always the minus (-) sign, which the user may either include at the end of the display mask or let the software automatically add it in.
Examples of valid masks: "ZZZZ.9999-" and "ZZ,ZZZ,ZZZ-".
This display mask will be used as a default only; the user may override this mask in the Contracts screen by pressing F4 or double-clicking on the unit price field to select from a list of available masks, or entering in a new display mask for the billing group/item detail line. Entry in this field is irrelevant if you do not have unit price contracts.

Default quantity mask
Enter the display mask for the quantity field in A/R Contracts, Contract File Listing, Draw Request Billing Entry, Print Draw Request Billing, Subcontract Billing Worksheet and Print Draw Billing Worksheet for contracts using unit pricing.
The default display mask is "ZZZZZZZ.ZZ-", but the user may enter any combination of "Z", "9", "," and "." as long as the total length of the mask is equal to 10 characters and no more than one decimal point is used. The 11th character is always the minus (-) sign, which the user may either include at the end of the display mask or let the software automatically add it in.
Examples of valid masks: "ZZZZ.9999-" and "ZZ,ZZZ,ZZZ-".
This display mask will be used as a default only; you can override this mask in the A/R Contracts screen by pressing F4 or double-clicking on the quantity field and entering in a new display mask for the billing group/item detail line. Entry in this field is irrelevant if you do not have unit price contracts.

Default retention percentage
Enter the most common revenue retention percentage your company encounters in contract activity. For example, enter "10" if your customers typically hold 10% retention.
Example: If a customer has billed an amount of $5,000, but $500 of this amount is categorized under retention and is in the retention A/R G/L account, the current due is now $4,500. This amount is stored under the trade AR G/L account. When the job is complete, the user will want this $500 to move from the retention AR G/L account to the trade AR G/L account. This information can then be printed on the A/R Aged Open Items Report under the current due, not retention. To accomplish this, call up the latest draw request (which is 100% billed) in the draw request Summary Billing Entry screen and enter 0% retention. The software will then show $5,000 billed, less $4,500, and it will show current due as the $500. When this is posted through the software, the $500 will move from retention AR G/L to the trade AR G/L and it will appear appropriately in the current due column on the A/R Aged Open Items Report. The invoice that is created is a zero amount invoice, so the customer would not send it. The software will offer this retention percentage when you add A/R contracts, and will also use this percentage when automatically creating contract entries when jobs are added. You can override this percentage in the Contracts and during Invoice Entry, as needed.

Next invoice number
Enter the next invoice number the software should assign for during Invoice Entry. Spectrum features auto-count invoice numbers, or the operator may specify the desired invoice number while adding invoices.
If entity tracking is enabled for the current company, the Entity-Specific Numbering button will be available to the right of this field. Click this button to view all entity codes and specify a next invoice # to assign to each entity.

- If the 'Use invoice numbering sequence' checkbox is not selected, the Draw Request Update will assign the invoice number, regardless of entity.

- If 'Accounts receivable invoice #' option on Work Order Installation is set to 'Work order number', the work order number will be used as the invoice number, regardless of entity.

It is recommended that this number be initialized at some point significantly higher or lower than invoice numbers presently in use so that auto-counted invoice numbers will not interfere with invoices already issued to customers. For example, if invoices are currently numbered 1500 to 1600, you may choose to set the next invoice number to 5001. Alternately, if invoices are presently numbered in the 80000 range, you may elect to commence the Spectrum invoices at 10001.

Use online tax calculation service?
Select this checkbox to use the Avatax online tax calculation service. This service will only be available to hosted or SaaS customers.
Click the Online Tax Setup button to enter the Avalara service hyperlink, account ID, license key and company code.

Sales tax report based on
Select one of the following options, depending on what you want the sales tax report based on:

- Invoice date - choose this option if you want the A/R Sales Tax Report to use the accrual method of accounting (all invoices will be included, whether or not they have been paid).

- Payment date - choose this method if the A/R Sales Tax Report uses cash-based accounting (if a partial payment is made, the pro-rated portion of the sales tax will be included).
