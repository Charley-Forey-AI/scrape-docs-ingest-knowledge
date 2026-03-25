---
title: "Field Definitions: AP Transaction Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form/field-definitions-ap-transaction-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form/field-definitions-ap-transaction-entry-form"
---

# Field Definitions: AP Transaction Entry Form

The following is a list of field descriptions for the AP Transaction Entry form.Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Seq#

 Enter the existing sequence to work on, or enter 'N', 'New' or '+' to add a new sequence. The system assigns the next available sequence number. Use F4 to look up existing transactions for the month.

## Action

The Action drop-down on multiple forms throughout Vista.
When entering new records, this field defaults to A (Add) and cannot be accessed.
For existing records, select the action for this entry.

- C-Change - Use this action to make changes to records that have already been processed.

- D-Delete - Use this action to delete this record from all related module files. (The delete functions in the toolbar and Records menu only delete the entry from the batch.

##  AP Trans

 Display only, the transaction number assigned to each transaction once posted in AP Batch Process.

## Vendor

The Vendor field on the AP Transaction Entry form, header Info tab.
Enter the vendor that applies to this transaction. If you do not know the vendor number, you can enter alpha characters, which will be matched to the vendor sort name for the first closest match. Alternately, use F4 to view all available vendors.
Note: If you are tracking vendor compliance for non-PO/SL invoices (flag in AP Company Parameters) and this vendor is out of compliance, an ***Out of Compliance*** warning displays in red above the header; however, entry is allowed.

## AP Reference

The AP Reference field on the AP Transaction Entry form header.
Enter the invoice number supplied by the vendor for this transaction, up to 30 characters.

Related information

- [Check for Unique AP Reference Numbers](/en/vista/vista/accounting/accounts-payable/ap-company-setup/set-up-an-ap-company/check-for-unique-ap-reference-numbers)

- [Enable Case-Insensitivity on AP References](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form/field-definitions-ap-company-parameters#ID-00005b04--en)

##  Description

 Enter a description of this transaction, up to 30 characters. This description prints on the check stub, as well as on certain reports.

## Invoice Date

 Required field.
 Enter the invoice date. Once you enter the date, the system automatically defaults the date in the Due Date field.

## Disc Date

The Disc Date field on the AP Transaction Entry form, header Info tab.

Initially defaults a discount date based on the payment terms assigned to the specified vendor in AP Vendors; may be overridden.
Note: When entering a discount amount for this transaction, you must enter a date in this field. If a discount date is not entered, an error displays when you validate the batch (AP Batch Process). Also, if you enter and save PO or SL lines, and the payment terms for the PO or SL do not match those in the transaction header, a message displays providing you the option to update the header with the PO or SL payment terms. Select Yes to change this date to reflect the updated payment terms.

## Due Date

The Due Date field on the AP Transaction Entry form, header Info tab.

Initially defaults a due date based on the payment terms assigned to the specified vendor in AP Vendors. If you have not specified payment terms for the vendor, the field defaults to the invoice date.
Note: If you enter and save PO or SL lines, and the payment terms for the PO or SL do not match those in the transaction header, a message displays providing you the option to update the header with the PO or SL payment terms. Select Yes to change this date to reflect the updated payment terms.

## Invoice Total

 Enter the total amount of this invoice. If the Require Invoice Total to Equal Sum of all Lines option in AP Company Parameters is checked, this amount is compared to the total of all invoice lines, and if amounts do not match, a warning is displayed. Amounts must match before you can add or edit another transaction.

## Entered By

The Entered By field on the AP Transaction Entry form, header Info tab.
Display only, the user name of the person who entered this AP invoice, whether manually or by import.

## Hold Code

The Hold Code field on the AP Transaction
 Entry form, Payment Overrides tab.
Entry in this field is not required.
Specify a valid hold code for this transaction, if applicable. Hold codes prevent the invoice from being paid until the hold code is released. The hold code entered here is in addition to any hold code automatically placed on the transaction (or any portion of the transaction) because of retainage or a vendor hold.

## Pay Control

Defaults from the pay control code from the Pay Control
 field on AP Vendors.
Enter the pay control code for this transaction.
The pay control code is used to group invoices together for payment. For example, you could code all loan payments with the same control code. Then, when initializing the payment batch, you can select all invoices with that pay control code. For subcontract invoices, you might use the owner’s application number to facilitate the “pay when paid” process (the SL Worksheet updates this field for that purpose).

## Pay Method

The Pay Method field on the AP Transaction Entry form, Payment Overrides tab.

Specify the payment method for this invoice. Payment methods include:

- N-ePayments

- C-Check

- E-EFT

- S-Credit Service

This field's default value comes from the Pay Method field in the AP Vendors form (Payment Method tab) for the selected vendor.
Tip: If this is a prepaid transaction,you must select C-Check.

### N-ePayments

If you select the N-ePayments pay method, you must meet the setup requirements before you can generate and upload an ePayments file. For more information, see [AP ePayments Export Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-epayments-export-form).

### E-EFT

If you select the E-EFT pay method, and you have not set up bank routing information for the specified vendor in AP Vendors (Payment Method tab), the system displays a warning, but allows you to save the entry.
 Additionally, the system enables the Addenda drop-down on the Addenda Info tab, allowing you to include tax payments, child support, or invoice detail with your payments. For details, see [Addenda](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form/field-definitions-ap-transaction-entry-form#ID-00006e4a--en).

### S-Credit Service

You should only select the S-Credit Service pay method if you have set up the appropriate information in AP Company Parameters (Payment Services tab) and AP Vendors (Payment Method tab). For more information, see [Set up Credit Card Payments](/en/vista/vista/accounting/accounts-payable/payments/credit-card-payments/set-up-credit-card-payments).

## CM Acct

The CM Acct field on the AP Transaction Entry form, header Payment Overrides tab

Enter the CM Account for paying this transaction. The entry must be a valid account set up in CM Accounts.
Note: If you have specified a credit service CM account in the AP Company Parameters form, and you are paying this vendor with a different method (either check or EFT), the system will display a warning if you enter the credit service CM account. You will be allowed to save the record, however.

This field defaults depending on where you generate the transaction from:

- If you are entering the transaction directly into AP Transaction Entry, this field initially defaults from the CM Account field in the AP Vendors form (Info tab). If the CM Account field in the AP Vendors form is blank, the system uses the number from the CM Account # field in the AP Company Parameters (Subledgers tab).

- If you are creating transactions from PR (that is, using the PR AP Update form), and you enter an account number in the CM Account Override field, this field defaults that account number. If you leave the CM Account Override field blank, the system defaults the number from the CM Account field in the AP Vendors form. If that field is blank, the system uses the number from the CM Account # field in the AP Company Parameters form.

- If you are updating AP from SL (that is, using the SL Update to AP form, accessed from SL Worksheet), this field defaults the account number from the CM Account field in SL Worksheet. If that field is blank, the system defaults the number from the CM Account field in the AP Vendors form. If that field is blank, the system uses the number from the CM Account# field in the AP Company Parameters form.

- If you are paying this vendor by credit card, this field will default from the CM Acct field in the AP Company Parameters form (Payment Services tab).

## Separate Payment

The Separate Payment checkbox on the AP Transaction Entry form, header Payment Overrides tab.

Select this checkbox to pay this transaction separately. When payments are initialized (in AP Payment Posting), a separate payment generates for this transaction.
Note: If you are generating separate payments per job or subcontract, and this option is checked, this transaction will be paid separately from all other transactions for a subcontract or job.

Leave this checkbox unselected if you are not paying this transaction separately. When payments are initialized, this transaction will be grouped together with other transactions having the same vendor on a single invoice.

## Prepaid Transaction

The Prepaid Transaction checkbox on the AP Transaction Entry form, header Payment Overrides tab.

Select this box if this transaction has already been paid.
Leave this checkbox unselected if no payment was made on this transaction.
Note: If you void a prepaid check after it has been posted, the prepaid information is removed from the invoice header. If you need to make corrections to the invoice and reprocess the prepaid, recheck this box and re-enter the prepaid check information in order to process the prepaid once the corrected invoice is posted.

## Check / EPay #

The Check / EPay # field on the AP Transaction Entry form, Payment Overrides tab.
If this transaction has already been paid, enter the check number on which it was paid. The number must be a whole number; up to 10 digits (may include leading zeros).
Note: If paying multiple pre-paid transactions with a single check, a warning displays once you enter the check number. However, the entry is allowed.

## Paid Date

If prepaid, enter the payment date for this transaction. This date must match the payment batch month for processing prepaid transactions (AP Prepaid Process).

## Paid Mth

This field automatically defaults to the month indicated by the Paid Date (previous field). Accept the default, or enter the month in which this transaction was paid. If you override the default, the system displays a warning, although you will be allowed to continue. The month indicated here is the month in which the payment will be posted. In other words, this month must match the month in which the prepaid is processed in AP Prepaid Process.

## Include in 1099 Totals

 This field initially defaults based on the vendor’s setup (AP Vendors).
 Check this box if this invoice’s amounts are to be included in the specified vendor’s 1099 totals.
 Do not check this box if this invoice’s amounts are not to be included in the specified vendor’s 1099 totals.
Click for the Australian field definition: [Include in Payments Reporting](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form/field-definitions-ap-transaction-entry-form#ID-00051b75--en).
Click here for the Canadian field definition: [Include in T5018 Totals](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form/field-definitions-ap-transaction-entry-form#ID-00051b7d--en).

## Include in Payments Reporting

Check this box if this invoice's
 vendor/subcontractor is subject to Taxable Payments reporting.
Note:This box is checked by default if the
 vendor/subcontractor is set as subject to Taxable Payments in AP Vendors (you checked
 the Subject to
 taxable payments reporting box, Add'l Info tab).

For more information see [Generating Taxable Payments Annual Reports](/en/vista/vista/accounting/accounts-payable/year-end-reporting/taxable-payment-reporting/generate-taxable-payments-annual-reports-australia).

## Include in T5018 Totals

 This field initially defaults based on the vendor’s T5018 setup in AP Vendors (T5018 Info
 fields, Add'l Info tab)
Check this box if this transaction should be included in T5018 totals.
Additional Information
[T5018 Reporting: Canada](/en/vista/vista/accounting/accounts-payable/year-end-reporting/t5018s/about-t5018-reporting-canada)
[Setting Vendors Subject to T5018 Reporting](/en/vista/vista/accounting/accounts-payable/year-end-reporting/t5018s/set-vendors-subject-to-t5018-reporting-canada)

## Type

This field defaults to the 1099 type specified for this vendor (in AP
 Vendors); may be overridden.
If 1099 amounts are to be included when printing 1099s or creating 1099 electronic files (AP 1099 Processing), you must specify a 1099 type of “MISC” (Miscellaneous Income), “INT” (Interest Income), or “DIV” (Dividends/Distributions).
Note:If you are using 1099 types only for informational or reporting purposes, any type is acceptable.

Canadian users
See [Type](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form/field-definitions-ap-transaction-entry-form#ID-00051b87--en) for the Canadian field definition.

### Type

This
 field defaults the type set up in AP Vendors (T5 Type field, Add'l Info tab). Enter the
 appropriate T5 type, if necessary.

##  Box#

The Box # field on the AP Transaction Entry form, Payment Overrides tab.

 Defaults initially based on the vendor's setup (AP Vendors).
Enter the box number to use for this vendor/transaction to accumulate amounts for 1099 reporting. Press F4 to select from a list of valid boxes
 on the 1099 form.

## Address Seq

The Address Seq # field on the AP Transaction Entry form, Address Overrides tab.
Enter the payment address sequence to use for this transaction or press F4 to select from a list of valid address sequences (address sequence flagged as 1-Payment or 0-Both).
Address sequences are set up in the AP Vendors form, on the Add'l Addresses tab.
Note: If you previously entered an override address (to the left), entering an address sequence in this field clears the Override Payment Address checkbox and replaces the override address with the address defined for this address sequence.

## Override Payment Address

The Override Payment Address checkbox on the AP Transaction Entry form, Address Overrides tab.
Select this checkbox to override the name and/or address specified for this vendor (in AP Vendors). Use of this option allows for a single vendor number to be used for all one-time purchases from various vendors. The override name and address will be used on all checks, and stored with the transaction for check history. When invoices are pulled for payment, separate sequences, and therefore separate checks, are printed for each transaction in the batch where the override checkbox is selected.
Leave this checkbox unselected if not overriding the payment address for this vendor. The standard payment address defined in AP Vendors is used.
Note: This checkbox is only for use when entering an override payment address. If you select this checkbox and then enter an Address Seq#, the system clears this checkbox, defaults the original vendor name and payment address, and disables this checkbox and the address fields.

## Payment Address

The override payment address fields on the AP Transaction Entry form, Address Overrides tab.
If you selected the Override Payment Address checkbox, the system enables the following fields and you may enter override address information.

- Name - Enter an override name here, up to 80 characters. Overriding the name allows the system to use a single vendor for one-time purchases from various vendors. If left blank, defaults the name from AP Vendors.

- Add'l Info - Enter override information, up to 60 characters. Information that you enter here is included when printing checks for this vendor. If left blank, defaults the additional info from AP Vendors.

- Address - Enter an override address here, up to 60 characters. If left blank, defaults the address from AP Vendors.

- City - Enter an override city here up to 30 characters. If you do not enter anything here, the name defaults from AP Vendors ( City field, Payment Address section) when you save the record.

- State - Enter an override state. The state must be valid as defined in HQ States. The system validates the state based on the Default Country field in HQ Company Setup for the active company. If it is not valid, an error will display but the system will allow entry. At that point, you must enter a valid country for this state in the Country field. If you do not enter anything here, the name defaults from AP Vendors (State field, Payment Address section) when you save the record.

- Zip Code - ( Postal Code ) Enter an override zip code, up to 12 characters. If you do not enter anything here, the zip code defaults from AP Vendors ( Zip Code field, Payment Address section) when you save the record.

- Country - Enter an override country, up to 2 characters. You must enter a country in this field when the address exists outside the Default Country specified in HQ Company Parameters for the active company. The country must be valid for the specified state (e.g., state, province, territory) as defined in HQ States.

Note: If you enter any overrides in the above fields, a separate check will print for each transaction for the same vendor in the payment batch.
If you enter a value in the Address Seq # field, all override values are cleared and default the vendor's original name and payment address information (from AP Vendors)

## Addenda

The Addenda field in the AP Transaction Entry form, Addenda Info tab.
If EFT is the pay method on the Payment Overrides tab, you can include tax payments, child support, and invoice detail with the payment of this invoice. Based on the addenda type you select from this field, additional fields display to enter related information. This field initially defaults from the Addenda Type field in AP Vendors, if one is indicated for the vendor.

- 1-Tax Payment - Select this option if you want to include Federal tax payments with your EFT payments. When you select this option, additional fields display on the form (Form Code, Pd End Date, Amt Type, Amount, Amt Type 2, Amount 2, Amt Type 3, and Amount 3). The Amt Type and Amount fields identify the type of tax and the tax amount, respectively. The information in these fields depends on the form code and whether the fields represent subcategories defined for that form. For example, if you are using the Employer’s Quarterly Tax Return (Form Code 94105), the Amount Type and Amount fields are used to indicate the Social Security, Medicare, and Federal withholding amounts. Refer to your “EFTPS Payment Instruction Booklet" for more detailed information about individual field requirements. Information entered here is included when creating Federal tax invoices in PR AP Update

- 2-Child Support — Select this option for EFT-paid child support payments. When you select this option, the following fields display on the form (PRCo#, Employee, and DL Code). You can manually generate a payment to the child support agency by entering the information directly in AP Transaction Entry. Typically, however, a payroll deduction is set up for the child support payment and the deduction is added to the employee's deductions (PR Employee Deductions/Liabilities). When payroll is run, the child support payment is deducted from the employee's pay check. When PR AP Update is run, an invoice is generated for the state agency specified as vendor. When the invoice is accessed in AP Transaction Entry, the employee and deduction/liability code automatically default into these fields (if the deduction code is flagged to automatically update AP).

- 3-Stub Detail – Select this option if you want to include invoice detail with this vendor's EFT payment. This option can be used for any vendor (except for those requiring Tax or Child Support addenda). When the EFT Download is run, all EFT-paid vendor invoices in the batch with this addenda type automatically have CTX format addenda text records created in the download. One addenda for each line of detail will include the AP reference number, Invoice date, description, gross amount and net amount [gross - (retainage + discount)].

Note: The types of federal tax payments that can be entered here are limited to those outlined in the "EFTPS Payment Instruction Booklet."

Note:Viewpoint does not currently support state EFT tax payments.

## EFT Federal Tax Payment Info: Form Code

Used only if Addenda Type is “Tax Payment”.
Note:It is suggested that you refer to your “EFTPS Payment Instruction Booklet” for more detailed information about entry requirements for this field.

Specify the ACH Credit Tax Form Code Number
 (from the EFTPS Payment Instruction Booklet) for this transaction. Up to 10 characters
 allowed. If you are using the “Automatic Update to Accounts Payable” option for the
 deduction/liability code (in PR Deductions/Liabilities), the form code automatically
 defaults based on the option selected in the Federal Type drop-down for the
 deduction/liability code as follows:

- If set to 1–Withholding , defaults form code 94105

- If set to 2–FUTA, defaults form code 941052

- If set to 3–Soc Sec, defaults form code 941053

- If set to 4–Medicare, defaults form code 941054

- If set to null (blank), assumes 1–Withholding and defaults form code 94105

## EFT Federal Tax Payment Info: Period End Date

Used only if Addenda Type is “Tax Payment”.
Note:It is suggested that you refer to your “EFTPS Payment Instruction Booklet” for more detailed information about entry requirements for this field.

Enter the tax period ending date in MMDDYY format. This will be the tax period ending date for the IRS Return for which the liability is being paid, not the payment date.
Note:The date is converted to YYMMDD format in the text file, with the day set to '01'. For example, if you enter 121508 as the tax period ending date, it will be formatted as 081201 in the text file.

If you are using the “Automatic Update to Accounts Payable” option for the withholding deduction/liability code (PR Deductions/Liabilities), the period end date automatically defaults from Payroll.

## EFT Federal Tax Payment Info: Amount Type

Used only if Addenda Type is “Tax Payment”.
Note:It is suggested that you refer to your “EFTPS Payment Instruction Booklet” for more detailed information about entry requirements for this field.

Specify the Amount Type (Tax Information ID Number). This will be the Subcategory or IRS Number from the EFTPS Payment Instruction Booklet. If none, enter the Form Code specified above.
For example, if you are using Form Code "94105” (Employer’s Quarterly Tax Return – Forms 941), there are three Subcategories: Social Security=1, Medicare=2, and Withheld=3. Social Security would be the first subcategory, therefore, you would enter “1” in this field.

## EFT Federal Tax Payment Info: Amount

Used only if Addenda Type is “Tax Payment”.
Note:It is suggested that you refer to your “EFTPS Payment Instruction Booklet” for more detailed information about entry requirements for this field.

Enter the tax amount. If a Subcategory/IRS number was entered in the previous field, this amount will be the tax amount for the subcategory (Amount Type) specified above. For example, if using Form Code “94105”, where Amount Type is “1” (Social Security), this will be the Social Security tax amount.
Note:If subcategories exist, the total amount of all subcategories must equal the total tax amount (i.e. invoice amount). Otherwise, this amount will be the total tax amount.

## EFT Federal Tax Payment Info: Amount Type 2

Used only if Addenda Type is “Tax Payment” and Subcategories are being used.
Note:It is suggested that you refer to your “EFTPS Payment Instruction Booklet” for more detailed information about entry requirements for this field.

Specify the Amount Type (Tax Information ID Number). This will be the Subcategory or IRS Number from the EFTPS Payment Instruction Booklet. Using the previous example, where the Form Code is “94105” and the subcategories are Social Security=1, Medicare=2, and Withheld=3, you would enter “2” here.

## EFT Federal Tax Payment Info: Amount 2

Used only if Addenda Type is “Tax Payment” and Subcategories are being used.
Note:It is suggested that you refer to your “EFTPS Payment Instruction Booklet” for more detailed information about entry requirements for this field.

Enter the tax amount. If a Subcategory/IRS number was entered in the previous field, this amount will be the tax amount for the subcategory (Amount Type 2) specified above. For example, if using Form Code “94105”, where Amount Type is “2” (Medicare), this will be the Medicare tax amount.

## EFT Federal Tax Payment Info: Amount Type 3

Used only if Addenda Type is “Tax Payment”, and Subcategories are being used.
Note:It is suggested that you refer to your “EFTPS Payment Instruction Booklet” for more detailed information about entry requirements for this field.

Specify the Amount Type (Tax Information ID Number). This will be the Subcategory or IRS Number from the EFTPS Payment Instruction Booklet. Using the previous examples, where the Form Code is “94105” and the subcategories are Social Security=1, Medicare=2, and Withheld=3, you would enter “3” here.

## EFT Federal Tax Payment Info: Amount 3

Used only if Addenda Type is “Tax Payment”.
Note:It is suggested that you refer to your “EFTPS Payment Instruction Booklet” for more detailed information about entry requirements for this field.

Enter the tax amount. If a Subcategory/IRS number was entered in the previous field, this amount will be the tax amount for the subcategory (Amount Type 3) specified above. For example, if using Form Code “94105”, where Amount Type is “3” (Withheld), this will be the Federal Withholding tax amount.

##  EFT Child Support Payment Info: PR Co#

 Used only if Addenda Type is “Child Support”.
 Enter the PR company of the employee paying the child support. If the deduction code for this transaction has been flagged to auto update AP (i.e. the “Automatic Update to Accounts Payable” option in PR Deductions/Liabilities), this field will default from Payroll.

## EFT Child Support Payment Info: Employee

Used only if Addenda Type is “Child Support”.
Specify the employee paying the child support. If the deduction code for this transaction has been flagged to auto update AP (i.e. the “Automatic Update to Accounts Payable” option in PR Deductions/Liabilities), this field will default from Payroll.

## EFT Child Support Payment Info: DL Code

Used only if Addenda Type is “Child Support”.
Enter the deduction code for child support. If the deduction code for this transaction has been flagged to auto update AP (i.e. the “Automatic Update to Accounts Payable” option in PR Deductions/Liabilities), this field will default from Payroll.

##  Line #

 Enter a number (0-32,767) for this invoice line, or ‘N’, ‘New’, or '+' for the next available number.

## Action

The Action drop-down on multiple forms throughout Vista.
When entering new records, this field defaults to A (Add) and cannot be accessed.
For existing records, select the action for this entry.

- C-Change - Use this action to make changes to records that have already been processed.

- D-Delete - Use this action to delete this record from all related module files. (The delete functions in the toolbar and Records menu only delete the entry from the batch.

## Type

The Type field on the AP Transaction Entry form, items Info tab.

Select the line type. The screen displays additional fields related to the line type.

- 1-Job – Use for expenses related to a JC job.

- 2-Inv – Use for expenses related to an Inventory location.

- 3-Exp – Use for miscellaneous expenses.

- 4-Equip – Use for expenses related to equipment usage.

- 5-EM Work Order – Use for expenses related to an EM work order.

- 6-PO – Use for expenses related to a purchase order.

- 7-SL – Use for expenses related to a subcontract.

- 8-SM Work Order – Use for miscellaneous expenses related to an SM work order.

Note: For Equip and EM Work Order lines, if you selected the Display last
 used date for parts in AP/PO/EM checkbox (in EM Company Parameters), the Last Used
 Date of Part field displays in the header of this form. For PO
 and SL lines, additional display-only fields appear on the Other Info tab.
For SM Work Order lines, the system generates a work
 completed miscellaneous line on the Work Completed grid of the SM Work Orders
 form.

## JC Co#

 Specify the Job Cost company in which job/phase/cost type information for this invoice item will be validated, and to which the job expense will be posted.

## Job

Specify the job to be charged for this invoice item.

- If you enter a soft- or hard-closed job, the status displays in red to the right of the Line field. The system will only save the record if you allow posting to soft or hard-closed jobs (flags in JC Company Parameters).

- The update to AP from SL Worksheet creates invoice items for subcontracts posted to soft- or hard-closed jobs, regardless of whether you allow posting to closed jobs. However, if you do not allow posting to closed jobs, you will be unable to post the batch.

## Phase

Specify the phase to which this invoice item applies.
Note:If the specified job’s Lock Phases option is checked
 (JC Jobs), must be a valid job phase (as set up in JC Job Phases).

##  CT

 Specify the Job Cost cost type for this invoice item.

## Ticket

The Ticket field on the AP Transaction Entry form, Lines
 section, Info tab.
This field only displays for 1-Job lines and job-related 6-PO lines that reference a field ticket.

For Job lines: Enter the field ticket number for this invoice line or press F4 to select from a list of valid open field tickets for the specified job/contract.
For job-related PO lines: This field defaults the field ticket specified for the purchase order item and is disabled.Note: Costs associated with approved field tickets only impact T&M billings; therefore, assigning field tickets to job lines is only useful if the job's contract/contract item has a bill type of T&M or Both.

Once you post the invoice, the system updates the Cost Detail tab in JC Field Ticket with this line's transaction information, showing a Source of AP Entry.
For more information about field tickets, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

## Material

The Material field on the AP Transaction Entry form, items Info tab.

Entry in this field is not required unless posting an Inventory transaction (2-Inv).
This field is disabled for Subcontract transactions (7-SL).
Enter the material for this invoice item.
Job, Exp, Equip, EM Work Order, and SM Work Order LinesYou can enter any material, valid (in HQ Materials) or non-valid (not in HQ Materials). If you enter a valid HQ material, the description, unit of measure, and unit cost default from HQ Materials. If a non-valid material, the description defaults as 'Not in Material File', the unit of measure defaults as LS, and the unit cost defaults as 0.00 and is disabled. You can override all defaults as needed. Inventory LinesYou must enter a valid stocked material; that is, the material must be flagged as stocked in HQ Materials and be set up for the specified location in IN Materials. The system defaults the purchase UM and description from HQ Materials, and the last unit cost from IN Location Materials.PO LinesThe material defaults from PO and field is disabled. Material description, UM, and unit cost default from PO item.
Note: If the material is set up for the vendor in PO Vendor Materials, the unit cost will default based on the vendor's setup, regardless of the line type

##  IN Co#

 Entry in this field is not required. However, if entry is made, it must be valid.
 Specify the Inventory company in which material/location information for this invoice item will be validated, and to which inventory item will be posted.

## Loc

 Specify the Inventory location for which this material was purchased. Location must be set up in IN Location Setup, and material must be assigned to this location in IN Materials.

##  EM Co

The EM Co field on the AP Transaction Entry form, items Info tab.
This field only displays for line types 4-Equip and 5-EM Work Order.
Specify the EM company in which equipment information for this invoice item will be validated, and to which the equipment expense will be posted.

##  Equipment

 Specify the equipment (from EM Equipment Master) to which this invoice item applies.
 If this is a Work Order line, this field is display only, and will default the equipment assigned to this work order.

##  Comp Type

The Comp Type field on the AP Transaction Entry form, transaction lines Info tab.
 Enabled for 4-Equip lines only, where the specified equipment is flagged to post costs to components (in EM Equipment).
If applicable, specify the component type or press F4 to select from a list of valid components for the selected equipment.
 For 5-EM Work Order lines, this field is display only and defaults the component type assigned to the work order, if applicable.

## Component

 If you entered a component type in the previous field, this field will default the first component of this type for the indicated equipment (as defined in EM Equipment). May be overridden, but must be a valid component for this equipment.
 If this is a Work Order line, this field is display only, and will default the component assigned to this work order, if applicable.

##  Cost Code

 Specify the cost code (as defined in EM Cost Codes) to which this invoice item applies.
 If this is an Equipment line, and you entered a component for this equipment (previous field), this field defaults the cost code assigned to the component’s type in EM Component Types. May be overridden.
 If this is a Work Order line, this field will default the cost code assigned to the specified work order item (in EM Work Order Edit). Cost code may only be changed if the Allow Cost Code Changes option (for Work Orders) in EM Company Parameters is checked. Otherwise, this field is display only.

## Cost Type

The Cost Type field on the AP Transaction Entry form, transaction lines Info tab.
Displays for 4-Equip and 5-EM Work Order lines only.
Specify the equipment cost type for this invoice item or press F4 to select from a list of valid EM cost types.

## WO

The WO field on the AP Transaction Entry form, items Info tab.
 This field only displays for line type 5-EM Work Order.
Enter the EM work order to which this invoice item applies or press F4 to select from a list of valid work orders for the specified EM company.

##  WO Item

The WO Item field on the AP Transaction Entry form, items Info tab.
This field only displays for line type 5-EM Work Order.
Indicate the work order item to which this invoice item applies. Once you have entered the item number, the Equipment, Component Type and Component (if applicable), and Cost Code assigned to this work order item are displayed to the right of this field. The Equipment, Component Type, and Component cannot be changed.

## PO

Enter the purchase order that this invoice
 item applies to or press F4  to select it from a list.

- The vendor assigned to the specified purchase order must be the same as the
 vendor specified in the transaction header.

- If the Check Compliance On Transaction Entry, Warning
 Only box is checked for Purchase Orders in AP Company Parameters and the
 purchase order is out of compliance, you will receive a warning at this point stating
 that the “Purchase order is not in compliance”.

- If the purchase order is related to an SM work order, the associated SM Co, SM Work
 Order, and Scope display below the PO Item# and PO Item Line
 fields. If the PO is for a job-related SM work order, the system will also display the
 JC phase and cost type assigned to the PO item.

If you initialized the purchase order via the AP Purchase Order Initialize form (accessed
 by selecting File > Initialize from PO from the Line # field), the system automatically
 populates the PO, PO Item, and PO
 Item Line fields with the appropriate values. If you initialized by
 Receiver #, the system also populates the Rec
 # field with the specified receiver number. The Rec #
 field is display only and therefore, cannot be edited.
Note: If the job associated with the work order has been soft or
 hard-closed, the system will only allow the entry if you allow posting to closed jobs (i.e.
 the Allow Posting
 to Hard-Closed Jobs and/or Allow Posting to Soft-Closed Jobs boxes
 are checked in JC Company Parameters).If you do not allow posting to closed jobs, you
 will receive a message indicating the job is closed and you will be unable to save the
 record.

## PO Item

Enter the purchase order number for this invoice item. Additional fields will display based on the type of purchase order item (e.g. if a job line, screen will display the JC Co, Job, Phase, and CT). Some fields may be grayed out; these cannot be changed.
 If you initialized the purchase order via the AP Purchase Order Initialize form (accessed by selecting File > Initialize from PO from the Line # field), the system automatically populates the PO, PO Item, and PO Item Line fields with the appropriate values. If you initialized by Receiver #, the system also populates the Rec # field with the specified receiver number (which is assigned to the PO when you receive it in PO Receipts Entry). The Rec # field is display only and therefore, cannot be edited.
Note: Once you enter the item number, you can view additional information about the purchase order item by selecting the Other Info tab. This tab displays current totals for the PO item, such as the Current Units, Unit Cost, and Total Cost, and Received, Backordered, Invoiced, and Remaining amount.

## PO Item Line

If you distributed the PO item to multiple
 lines, enter the applicable line number. Press F4 to see a list of valid line numbers.
 If you have not distributed the PO item to multiple lines, this field will default
 automatically to 1 and the system will not allow you to change the number.
Note: If you are adding a transaction back to a batch and a
 PO line item has been paid, the system will disable this field.
If you have not already distributed the PO
 item to multiple lines, and want to, press F5 from this field to access the PO Item
 Distribution form. Use that form to distribute the item among multiple lines. You can also
 select Open PO Item
 Distribution from the Tasks drop-down  on the toolbar. When you save your
 changes, and exit the PO Item Distribution form, the PO line on this form refreshes to
 display the updated data. For more information, see [PO Item Distribution](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-item-distribution-form).
If you initialized the purchase order via the AP Purchase Order Initialize form (accessed
 by selecting File > Initialize from PO from the Line # field), the system automatically
 populates the PO, PO Item, and PO
 Item Line fields with the appropriate values. If you initialized by
 Receiver #, the system also populates the Rec
 # field with the specified receiver number. The Rec #
 field is display only and therefore, cannot be edited.

## Rec #

The Rec # field on the AP Transaction Entry form, Items section Info tab.
This field is only visible for items with a line Type of 6-PO.
Display only field showing the receiver number for the purchase order.
 This field only populates if all of the following are true:

- You received the purchase order via PO Initialize Receipts or PO Receipts Entry and provided a Receiver # on the receipts transaction.

- You added the purchase order to an AP Transaction Entry batch via initialization (via the AP Purchase Order Initialize form, which is accessed from AP Transaction Entry by selecting File > Initialize from PO).

- When initializing the PO, you used the Receiver # initialization option (that is, you entered the Receiver # on the Receiver # tab in AP Purchase Order Initialize).

## SL

Enter the subcontract (as set up in SL Entry) to which this invoice item applies.
Note:The vendor assigned to the specified subcontract must be the same as the vendor specified in the transaction header.

Also, if the “Check Compliance On Transaction Entry, Warning Only” option for Subcontracts in AP Company Parameters is checked, and the subcontract is out of compliance, you will receive a warning at this point stating that the “Subcontract is not in compliance”.

##  SL Item#

 Enter the subcontract item to which this invoice item applies. The item’s assigned job, phase, and cost type (as set up in SL) and the job/phase/cost type’s U/M (as set up in JC) are displayed. These fields cannot be changed.

## SM Co

The SM Co field on the AP Transaction Entry form, items Info tab.
This field only displays for line type 8-SM Work Order. It is disabled for PO lines associated
 with an SM work order.
Required.
Enter the SM company to which this invoice
 line applies. This will be the SM company in which the SM work order was set up. Press
 F4
 for a list of valid SM companies.

## SM Work Order

The SM Work Order field on the AP Transaction Entry form, items Info tab.
This field only displays for line type 8-SM Work Order. It is disabled for PO lines associated
 with an SM work order.
Required.
Enter the SM work order to which this invoice
 line applies or press F4 to select from a list of valid work orders for the specified SM company.
Note: If you specify a job-related work order and the job
 associated with the work order has been soft or hard-closed, you can save the record if you
 allow posting to closed jobs (that is, the Allow Posting to Hard-Closed Jobs and/or
 Allow Posting to
 Soft-Closed Jobs checkboxes are selected in JC Company Parameters). If you do not
 allow posting to soft or hard-closed jobs, a message displays indicating the job is closed
 and you will be unable to save the record.

## Scope Seq

The Scope Seq field on the AP Transaction Entry form, items Info tab.
This field only displays for line type 8-SM Work Order. It is disabled for PO lines associated
 with an SM work order.
Required.
Enter the work order scope to which this
 invoice line applies or press F4 to select from a list of valid scopes for the
 specified work order.

- If you enter a scope that is closed, a warning displays and you will be unable to save the record. You must either reopen the scope in SM Work Orders or select an open scope.

- If the transaction line is in an open batch and the
 scope is closed prior to processing the batch, you will be unable to post the batch
 until you either reopen the scope or change to an open scope.

 For job-related work orders:

- If the job associated with the work order has been soft or
 hard-closed, you can save the record if you allow posting to closed jobs (that is,
 the Allow
 Posting to Hard-Closed Jobs and/or Allow Posting to
 Soft-Closed Jobs checkboxes are selected in JC Company Parameters). If
 you do not allow posting to soft or hard-closed jobs, a message displays indicating
 the job is closed and you will be unable to save the record.

- If the work order has a Cost Method of Markup and you
 specify a scope that does not have a rate template assigned, you will be able to save
 the line; however, you will unable to post the batch until you assign a rate template
 to the scope.

- If the work order scope is not assigned a phase, a message displays indicating a
 phase is needed, but the system will allow you to save the record. However, you will
 be required to assign a phase to the work order scope before posting the invoice.Tip: You can press F5 from the Work
 Order or Scope fields to access SM
 Work Orders and assign a phase to the scope.

## SM Cost Type

The SM Cost Type field on the AP Transaction Entry form, Items Info tab.
This field only displays when the line type is 8-SM Work Order.
Enter the SM cost type that applies to this invoice line. Press F4 for a list of valid SM cost types.

Note: Entry in this field is required if taxes are applied to the invoice line (that is; the Tax Amt field is not 0.00).

## JC Cost Type

The JC Cost Type field on the AP Transaction Entry form, items Info tab.
This field is only displayed and enabled if the line Type is 8-SM Work Order and the SM work order is for a job.
Enter the JC cost type (from JC Cost Types) for this invoice line. Initially defaults as follows:

- If you entered an SM cost type for the line, defaults the JC cost type assigned to the SM cost type (in SM Cost Types). Default may be overridden.

- If you did not enter an SM cost type or if you entered an SM cost type, but no JC cost type is assigned to the SM cost type, defaults as blank and must be entered manually.

The system uses this cost type, in conjunction with the phase specified for the work order sequence, to post the costs to Job Cost.
Note: If the work order scope specified for this invoice line has not been assigned a phase, you will receive a message indicating the phase is missing; you will be unable to save the record until you assign a phase to the work order scope in SM Work Orders
Phase OverridesIf no phase override exists in JC Departments (Phase Overrides tab) for the phase specified on the work order scope, the cost type entered here must be set up with the appropriate GL accounts in JC Departments (Cost Types tab) based on the following:

- If the phase exists on the job (locked and non-locked jobs), the cost type must be set up for the department assigned to the phase's contract item.

- If the phase does not exist for the job (non-locked jobs only), the cost type must be set up for the department assigned to the first contract item associated with the job.

- If the phase does not exist for the job (non-locked jobs only), but the phase matches the "number of valid characters" of a phase that does exist on the job, the cost type must exist for the contract item assigned to the valid job phase.

Note: If the cost type is not found in JC Departments, you will be unable to post the batch. This applies regardless of how you set the JC interface checkbox in SM Company Parameters.

Locked Phases vs. Non-Locked PhasesIf the Phases on this job are locked checkbox is selected for the job in JC Jobs, the cost type specified here must be set up for the job/phase in JC Job Phases. If it is not, you will receive a warning and be unable to save the line until you specify a valid job/phase cost type.Tip: You can add the cost type to the job phase by pressing F5 from this field to access JC Job Phases. Once you set up the cost type and exit JC Job Phases, you can enter the cost type here.

If the Phases on this job are locked box is not checked in JC Jobs, you can use any cost type defined for the phase in JC Job Phases or JC Phases. If the cost type is not set up for the phase, you will receive a warning and be unable to save the line until you specify a valid phase cost type.
Phase OverridesIf no phase override exists in JC Departments (Phase Overrides tab) for the phase specified on the work order scope, the cost type entered here must be set up with the appropriate GL accounts in JC Departments (Cost Types tab) based on the following:

- If the phase exists on the job (locked and non-locked jobs), the cost type must be set up for the department assigned to the phase's contract item.

- If the phase does not exist for the job (non-locked jobs only), the cost type must be set up for the department assigned to the first contract item associated with the job.

- If the phase does not exist for the job (non-locked jobs only), but the phase matches the "number of valid characters" of a phase that does exist on the job, the cost type must exist for the contract item assigned to the valid job phase.

Note: If the cost type is not found in JC Departments, you will be unable to post the batch. This applies regardless of how you set the JC interface checkbox in SM Company Parameters.

Locked Phases vs. Non-Locked PhasesIf the Phases on this job are locked checkbox is selected for the job in JC Jobs, the cost type specified here must be set up for the job/phase in JC Job Phases. If it is not, you will receive a warning and be unable to save the line until you specify a valid job/phase cost type.Tip: You can add the cost type to the job phase by pressing F5 from this field to access JC Job Phases. Once you set up the cost type and exit JC Job Phases, you can enter the cost type here.

If the Phases on this job are locked checkbox is not selected in JC Jobs, you can use any cost type defined for the phase in JC Job Phases or JC Phases. If the cost type is not set up for the phase, you will receive a warning and be unable to save the line until you specify a valid phase cost type.

## Description

Enter the description of this invoice item, up to 30 characters. Initially defaults the header description, but may change depending on the line type entered.

- Job – If you checked the Default Header
 Description to Lines on Job Type box in AP Company Parameters, the
 header description will be used as the line description. If you did not check this
 option, the phase description will default as the line description.

- Inventory – Defaults the material description.

- Expense – Defaults the header description.

- Equipment, EM Work Order – If you checked the
 Default
 header description to lines on equipment typebox in AP Company
 Parameters, this field defaults the header description. If you did not check this
 option, this field defaults the cost code description.

- PO & SL – Defaults the PO item description or SL item description, respectively.

- SM Work Order - Defaults the header description.

If you specify a material for the line, the description defaults as follows:

- Job, Inventory, Expense, or SM Work Order – Defaults
 the material description from HQMT (HQ Materials). If an non-valid material is
 entered (does not apply to Inventory lines), the description will default as 'Not in
 material file'.

- Equipment or Work Order – Defaults the material description from EMEP (Equipment Parts), HQMT (HQ Materials), or POVM (PO Vendor Materials). If a work order may also default from EMWP (Work Order Parts). If the material exists in more than one table, it will use the description from the first table in which the material is located. For example, if the material exists in both Equipment Parts and Vendor Parts, but you select the material from Vendor Parts in the F4 lookup, it will return the description from Equipment Parts because EMEP is checked before POVM.

## GL Co#

The GL Co# field on the AP Transaction Entry form, items Info tab.

This field is enabled for Expense lines only (type
 3-Exp).
Enter the GL company for this invoice item. Initially defaults the GL company
 specified in AP Company Parameters.
For all other line types, this field defaults as follows:

- Job - Defaults the GL company assigned to the JC
 company in JC Company Parameters.

- Inventory - Defaults the GL company assigned to the
 IN Company in IN Company Parameters.

- Equip / EM Work Order -
 Defaults the GL company assigned to the EM company in EM Company
 Parameters.

- PO / SL - These two modules
 have a one-to-one relationship with AP; therefore, this field defaults the GL
 company assigned to the active AP company.

- SM Work Order - Defaults the GL company specified for
 the department assigned (in SM Departments) to the work order's service
 center.

## GL Acct

This field initially
 defaults a GL account based on the transaction line type:

- 1-Job - Defaults from the JC Departments form. If you did not
 select the Allow GL Account override
 when posting cost checkbox in the JC Company Parameters form (GL Cost
 tab), the system will disable this field. If the default is blank, the system will
 allow entry in this field; however, once the line is saved, the system disables the
 field. If you selected the Allow GL
 Account override when posting cost checkbox, the system enables this
 field and you can override the value.

- Defaults from IN Locations. If you did not select the Allow GL Account
 overrides checkbox in IN Company Parameters, the system will disable
 this field. If the default is blank, the system will allow entry in this field;
 however, once the line is saved, the system disables the field. If you selected the
 Allow GL
 Account overrides checkbox, the system enables this field and you can
 override the value.

- 3-Expense - Defaults from AP Vendors, unless a non-stocked
 material is specified, in which case, this field defaults from the Non-Stocked GL
 Account field in HQ Material Categories.

- 4-Equipment - Defaults from the EM Departments form. If you did not select the
 Allow GL Account Override checkbox in the EM Company
 Parameters form, the system will disable this field. If the default is blank, the
 system will allow entry in this field; however, once the line is saved, the system
 disables the field. If you selected the Allow GL Account
 Override checkbox, the system enables this field and you can override
 the value.

- 5-EM Work Order - Defaults from the EM Departments form. If you did not check the
 Allow GL Account Override checkbox in the EM Company
 Parameters form, the system will disable this field. If the default is blank, the
 system will allow entry in this field; however, once the line is saved, the system
 disables the field. If you checked the Allow GL Account
 Override checkbox, the system enables this field and you can override
 the value.

- 6-Purchase Order - Defaults from the purchase order. If a job PO item, defaults as
 follows:

- If the job is open and the JC Dept GL account is blank, this field defaults
 the GL account from the PO item.

- If the job is open and the JC Dept GL account is not blank, but you have
 checked the Allow GL Account override when posting
 revenue box in JC Company Parameters, this field defaults the GL
 account for the PO item. If you did not check the box, this field defaults the
 GL account from the JC department. The system will display a message warning
 that the defaulted GL account does not match the PO item's GL account.

- If the job is closed (final) and the JC Dept closed GL account is blank, the
 GL account defaults as blank. The system will display a message warning that
 the defaulted GL account does not match the PO item's GL account. If you did
 not check the Allow GL Account override when posting
 revenue box (JC Company Parameters), manual entry is required,
 as initialization cannot occur.

- If the job is closed and the JC Dept closed GL account is
 not blank, this field defaults the closed GL account from JC Departments. The
 system will display a message warning that the defaulted GL account does not
 match the PO item's GL account.

Note: For PO items referencing an
 SM work order, this field is disabled.

- 7-Subcontract - Defaults from the subcontract as follows:

- If the job is open and the JC Dept GL account is blank, this field defaults
 the GL account from the subcontract item.

- If the job is open and the JC Dept GL account is not blank, but you have
 checked the
 Allow GL Account override when posting revenue
 box in JC Company Parameters, this field defaults the GL account
 for the subcontract item. If you did not check the box, this field defaults the
 GL account from the JC department. The system will display a message warning
 that the defaulted GL account does not match the subcontract item's GL
 account.

- If the job is closed (final) and the JC Dept closed GL account is blank, the
 GL account defaults as blank. The system will display a message warning that
 the defaulted GL account does not match the subcontract item's GL account. If
 you did not check the
 Allow GL Account override when posting revenue
 box (JC Company Parameters), manual entry is required, as
 initialization cannot occur.

- If the job closed and the JC Dept closed GL account is not
 blank, this field defaults the closed GL account from JC Departments. The
 system will display a message warning that the defaulted GL account does not
 match the subcontract item's GL account.

- 8-SM Work Order - The
 GL
 Acct
 field is always disabled for this line type and will derive the Misc
 Cost account from the SM department as follows:

- If you specified a division on the work order scope and an alternate
 department is assigned to the division, the system uses the following hierarchy
 to determine the correct account to use:

1. The system looks for a cost type category/call type/cost type override
 (in SM Departments, Overrides tab) based on the SM cost type entered for
 the invoice line, the cost type category assigned to the SM cost type,
 and the call type specified for the work order scope. If one exists, it
 will use that account.

1. If no cost type category/call type/cost type override is defined, the
 system will then look for an override cost type category/call type or
 cost type category/cost type, and if found, use it.

1. If no override accounts are defined by cost type category/call type or
 cost type category/cost type, the system will use the standard account
 defined for the cost type category at the department level (SM
 Departments, Info tab).

1. If no SM cost type is specified for the invoice line, the system will
 use the standard Other account defined in SM Departments (if no material
 is entered) or the Material account defined in SM Departments.

- If no alternate department is assigned to the division or no division is
 assigned to the work order scope, the system will use the department assigned
 to the service center to determine the default account using the same process
 defined above.

## UM

The UM field on the AP Transaction Entry form, items Info tab.

Entry in this field is required if entering units and unit cost. If
 left blank, the Units and
 UC fields are
 disabled.
Enter a valid unit of measure for this invoice item or accept the default.
If you entered a material, this field defaults based on the line type as follows:

- Job, Inv, Exp, and SM Work Order - If you entered a valid HQ material or IN
 Material (2-Inv lines only), this field defaults the Purchase UM from HQ
 Materials (HQMT). You may override the default, but it must be a valid unit of
 measure for that material.If overrides exist for the
 specified material/vendor in PO Vendor Materials (POVM), this field defaults
 the vendor material UM matching the Purchase UM in HQMT. If no match is
 found, defaults the lowest UM for the vendor/material group/material.

- Equip - If the selected material exists in EM Equipment Parts (EMEP) for the equipment, this field defaults the UM from EMEP, if it matches the Purchase UM in HQ Materials; otherwise, defaults the Purchase UM from HQMT. If you selected a vendor material that does not also exist in EMEP, defaults the vendor material UM if it matches the HQMT Purchase UM; otherwise, defaults the lowest UM in POVM for the vendor/material group/material.
 If material does not exist in EMEP or POVM, defaults the HQMT Purchase UM.

- EM Work Order - If the selected material exists in EM Work Order Parts (EMWP) for the work order, defaults the UM from EMWP, regardless of whether it matches the HQMT Purchase UM.If you select a material from EM Equipment Parts that does not also exist in EMWP for the work order, the UM defaults from EMEP if matches the HQMT Purchase UM; otherwise, defaults the HQMT Purchase UM.
 If you select a vendor material that does not also exist in EMWP or EMEP for the work order, defaults the vendor material UM if it matches the HQMT Purchase UM; otherwise, defaults the lowest UM in POVM for the vendor/material group/material.
 If material does not exist in EMWP, EMEP, or POVM, defaults the HQMT Purchase UM.

- PO and SL - Defaults the unit of measure specified for the PO or SL item. This default cannot be overridden.

Note: If you entered a non-valid material (Job, Exp, Equip, EM Work Order, and SM Work Order lines only), the UM defaults as LS. You may override this default with any valid unit of measure.

If you did not enter a material (all line types except Inventory, which requires entry of a material), defaults are follows:

- Job - If the Default JC Job Phase UM on job lines checkbox is selected in AP Company Parameters, this field defaults the UM from the cost type specified for invoice line (as defined in JC Job Phases). If the Default JC Job Phase UM on job lines checkbox is not selected, this field defaults the unit of measure as LS (lump sum).

- Exp, Equip, EM Work Order, and SM Work Order - Defaults as LS.

- PO and SL - Defaults from the purchase order item or subcontract item; cannot be overridden.

## Units

The Units field on the AP Transaction Entry form, items Info tab.

This field is disabled and set to
 0.00 if the UM is LS (Lump Sum).
Required for non-LS units of measure.
Enter the number of units for this invoice item.
If this is a purchase order line and the invoiced
 units exceed the PO's received units, a warning
 displays. If the Allow Invoice to Exceed Received checkbox is selected in AP Company Parameters,
the entry is allowed and you can post the batch. However, if the checkbox is not selected, you must correct the invoiced units in order to save the line.
Note: Units posted to job lines are only updated to
 JC Cost Detail (JCCD) if you selected the Update Actual Units From AP option for the
 specified job in JC Jobs. If option is no selected, units are set to 0.00 in JCCD.

## UC

The UC field on the AP Transaction Entry form, items Info
 tab.

Enter the unit cost for this invoice item or accept the defaulted value.
If you specified a material for this invoice item that is set up for the vendor in PO Vendor Materials, the unit cost defaults based on the vendor's setup, regardless of line type. Otherwise, this field defaults for each line type as follows:

- Job, Exp, Equip, EM Work Order, and SM Work Order - If you specified a material, defaults the unit cost from HQ Materials. If you did not specify a material, defaults as 0.00.Note: For Job lines only, the system only updates the unit cost to JC Cost Detail (JCCD) if you selected the Update Actual Units From AP checkbox for the job in JC Jobs. If the checkbox is not selected, the unit cost is set to 0.00 in JCCD.

- Inv - Defaults the Last Unit Cost defined in IN Location Materials.

- PO and SL - Defaults the unit cost defined on the purchase order or subcontract.Note: If you change the unit cost for a PO or SL item, a warning displays indicating that the unit cost is different than the PO or SL unit cost, and that committed costs will be reduced by units at the PO or SL unit cost. Changes are not updated to the related PO or SL files.

##  ECM

 Specify which quantity the unit cost represents:
 E - Cost is per each unit.
 C - Cost is per 100 units.
 M - Cost is per 1000 units.

## Gross

The Gross field on the AP Transaction Entry form, items Info tab.

Enter the total amount for this invoice item or accept the default (units x unit cost).
If the unit of measure for this item is other than LS (lump sum), changes to this amount will cause the unit cost to be recalculated.
Purchase Order LinesIf you enter a Gross amount for an item with 0.00 units and a non-LS (lump sum) unit of measure, a message displays warning you that entering a gross amount without units could cause problems, and that for Job Type items, it will cause committed costs to be improperly updated. However, entry is allowed.In addition, the system checks the invoice amount for each item and if it exceeds the current total cost of the PO item and/or PO, a warning displays; however, the entry is allowed.
If the Allow Transactions to Exceed Item's Current Total Cost and/or Allow Transactions to Exceed PO's Current Total Cost checkboxes in AP Company Parameters are selected, the system will not allow you to post the batch until the invoiced amounts are corrected.
The system also checks to see if the invoiced amount exceeds the PO's received amount and if it does, a warning is displayed. If the Allow Invoiced to Exceed Received checkbox is selected in AP Company Parameters, the entry is allowed. If the checkbox is unselected, you cannot save the line until you correct the invoiced amount.
Subcontract LinesThe system checks the invoiced amount for each item and if it exceeds the current total cost of the subcontract item or subcontract, a warning displays. If the Allow Transactions to Exceed Current Total Cost checkbox is selected in AP Company Parameters, the amount is allowed. Another check is done at the header level once all items are entered and accepted. If the total of all items exceeds the total remaining amount available on the subcontract, another warning is displayed. The Total amount is allowed if the Allow Transactions to Exceed Current Total Cost checkbox is selected. This verification allows for the condition of a deduct item (subcontracts) not invoiced, which could then result in an overpayment.
SM Work Order LinesThe Gross amount is sent to the specified SM work order as "actual cost". If you also entered taxes and a miscellaneous amount (with Included checkbox selected), those amounts are included in the actual cost sent to SM.
Note: If the SM work order is job-related, the resulting actual cost is updated to Job Cost using the phase and JC cost type associated with this line.

## Misc Amt

The Misc Amt field on the AP Transaction Entry form, items Info tab.

Enter the miscellaneous amount for this invoice item. Typically used to enter freight or other miscellaneous charges.
If you select the Included
 checkbox (to the right), the system includes this amount in this line’s total. However,
 this amount is not included in this line's tax, discount, or retainage calculations.
The system also excludes this amount:

- When checking the item's invoiced amount against the current total cost of the
 PO/PO Item or SL/SL Item.

- From the total committed cost in APJC (AP JC Distributions) for standing PO's
 where the unit of measure is LS and the PO is not flagged for receiving.

- When updating the Received Cost and Invoiced Cost amounts in POIT (PO
 Items).

- When updating the Invoiced Cost amount in SLIT (SL Items).

### SM Work Orders

For SM work order related lines, this amount is handled as
 follows:

- For PO lines (type 6-PO) referencing a purchase order
 item that is associated with an SM Work Order, this amount is included in
 the actual cost updated to the work completed purchase line (in SM Work
 Orders, Work Completed tab).If multiple work completed
 purchase lines exist that reference the same PO item, the actual cost
 will be allocated proportionately across the work completed
 lines.

- For SM Work Order lines (type 8-SM Work Order), this
 amount is included in the Cost UC, Cost Subtotal, Cost Rate, and Total
 Actual Cost amounts updated to the work completed line.

## Included

The Included checkbox on the AP Transaction Entry form, items Info tab.

Select this checkbox to include the Misc Amt in this line's total amount. The
 Misc Amt is not included when calculating tax, discount, or retainage amounts for this
 line.
Leave this checkbox unselected to exclude the Misc
 Amt from this line's total amount.
 For all line types except Inventory and SM Work Orders, the Misc Amt is not charged to Job Cost, Equipment, or General Ledger. It is a memo entry only and is only useful if writing reports to pull this miscellaneous amount.
Inventory LinesIf you selected the Burdened Unit Cost - include AP Misc Amt and
 Tax checkbox in IN Company Parameters, the Misc amount is
 handled as follows:

- If this checkbox is selected, the Misc Amt
 is included in the AP invoice total, the Inventory and AP
 accounts are debited/credited with the total amount, and the
 total (including the Misc Amt) is included in the unit cost for
 the Inventory location.

- If this checkbox is not selected, the Misc
 Amt is excluded from the AP invoice total, but is included in
 the unit cost for the IN location. The Inventory account is
 debited with the total amount (including the Misc Amt), the AP
 account is credited with the gross amount (total less the Misc
 Amt), and the Misc Amt is credited to the location's
 Miscellaneous Expense account. When posting the freight vendor's
 invoice for the Misc Amt, the entry should be posted to offset
 the Miscellaneous Expense amount.

SM Work Order LinesInvoice items with this line type automatically generate a work completed line in SM Work Orders (Work Completed tab) once the batch is posted. The Misc work completed line is updated as follows:

- If this checkbox is selected, the Misc Amt is included in the AP invoice total, and the resulting Misc work completed line includes the Misc Amt in the Cost UC, Cost Subtotal, Cost Rate, and Total Actual Cost amounts.

- If this checkbox is not selected, the Misc Amt is excluded from the AP invoice total, and the resulting Misc work completed line excludes the Misc Amt from the Cost Rate and Total Actual Cost amounts; however, it does include the Misc Amt in the work completed line's Cost UC and Cost Subtotal amounts.

## Subject to On-Cost

This box defaults from the Subject to On-Cost box in AP Vendors.
If you specified a cost type in AP Vendors for
 generating on-cost invoices (JC Cost Type field), you must enter that
 cost type in the CT field for this invoice line, or the system will uncheck this box;
 however you may re-check this box, if necessary.
Check this box if the invoice for this vendor is subject to on-cost.
Note:If you check this box and the vendor is not set as
 subject to on-cost (Subject to On-Cost box in AP Vendors
 is not checked) or does not have associated on-cost types (On-Cost tab, AP Vendors), the
 system will display a warning but will allow you to save the record.
If you add the original invoice back into a batch and uncheck this box after posting the associated on-cost invoice, the system will not delete the on-cost invoice. So, if you uncheck this box and reprocess the original invoice, the system will generate duplicate on-cost invoices.

## Ret%

Specify the percentage at which retainage is calculated for this item, or accept the default.
Note:Retainage can be entered with any line, but is typically only used with job-related transactions.

## Ret Amt

If a Ret% was entered, this field defaults an amount based on the percentage specified and the invoice line’s gross amount. Accept the default, or enter the retainage amount. If you change the default amount, the retainage percentage is recalculated.

- A line’s retainage amount cannot exceed the line’s gross amount. If this occurs, a warning displays, and the amount must be corrected before the line can be saved).

- Retainage is not calculated on Tax or Misc amounts. Additionally, the retainage portion of the invoice line is automatically placed on hold using the Retainage hold code specified in AP Company Parameters.

## Disc%

Specify the percentage at which discounts for this invoice item will be calculated, or accept the default. Discount rate initially defaults from the Vendor’s payment terms (specified in invoice header). If the line’s type is PO or SL, the discount rate defaults from the payment terms specified for the purchase order or subcontract.

## Disc Amt

If a Disc % was entered, this field defaults an amount based on the percentage specified and the invoice line’s gross amount (less retainage, if any). Accept the default, or enter the discount amount. If you change the default amount, the discount percentage is recalculated.
Note:Discounts are not calculated on Misc amounts. Also, if you enter a discount amount here, a discount date must be entered in the header. If a discount date is not entered, a warning displays when you validate the batch (AP Batch Process).

If using tax discounts (flag in AP Company Parameters), the discount will be taken by subtracting this amount from the invoice's gross amount to get the tax basis.

## Tax Type

The Tax Type field on the AP Transaction Entry form, items Info tab.

Specify the tax type for this item.

- 1-Sales – Tax amounts are payable to the vendor and are added to the invoice total. This tax amount is directly charged to Job Cost, Equipment, and GL.

- 2-Use (US only) - Tax amounts are accrued, and will be paid at a later date to the appropriate State or Local taxing authority. Calculated tax amounts do not affect the gross or net balance due to the vendor. Instead, the transaction's gross amount and tax amount is charged to Job Cost, Equipment, and GL account with an offsetting liability account as defined in HQ Tax Codes. Use the AP Tax Report to obtain an itemization of use tax amounts.

- 3-VAT (Value Added Tax) - This tax is paid on goods and services at each stage of production or distribution, and is based on the value added at each stage. This tax is not directly expensed; it is tracked in the GL and reduces the payment to a taxing authority through an Input Tax Credit (ITC). Use the AP Value Added Tax Report to obtain an itemization of VAT amounts. This is the default tax type for Australian and Canadian companies.

Note: For non-SM Work Order lines, if you specify a material for the invoice item and the material is non-taxable, this field defaults as blank, but may be overridden.

### SM Work Completed Lines

For invoice lines posted to an SM Work Order (line type 8), the system defaults the tax information based on the SM Cost Type entered on the invoice line, and the Matl Tax Override and Tax Option Override options selected on the associated work order scope. You may override the defaults as needed.
SM Cost TypeMaterialTax Option OverrideMatl Tax OverrideDefault
Note: If the AP
 vendor is not assigned a tax code and the work order scope's
 tax source (service site or service center) is not assigned
 a tax code, all tax fields default as blank, but may be
 overridden.

Not TaxableBlankAllAllBlank
Not Taxable
Taxable
TaxableNot TaxableAllAllBlank
TaxableAllN - No TaxBlank
P - Taxable at Purchase Only, M - Taxable at
 Purchase/Markup at Billing, F - Full Tax at Purchase and
 BillingBlank or 1-Sales1-Sales (US) or 3-VAT (AU/CA)
2-Use (US only)2-Use (US only)
N - Not Taxable, B - Taxable at Billing OnlyAllBlank
BlankP - Taxable at Purchase Only, M - Taxable at
 Purchase/Markup at Billing, F - Full Tax at Purchase and
 BillingBlank or 1-Sales1-Sales (US) or 3-VAT (AU/CA)
2-Use (US only)2-Use (US only)
N - Not Taxable, B - Taxable at Billing OnlyAllBlank

When you post an AP Transaction Entry batch, the system auto-generates a separate Misc work completed line on the specified work order (in SM Work Orders) for each SM Work Order invoice line. The Tax Type specified here for each line updates the Cost Tax Type field on the generated miscellaneous work completed line.
Note: For invoice lines posted to a Purchase Order (line type 6), if the PO item is posted to an SM Work Order, the AP tax information will only update the AP History tab on the SM Work Completed Purchase form. Only the tax information posted to the purchase order item will appear on the work completed purchase line.

### Intercompany Transactions

The tax type you select determines whether the selling company or the purchasing company is responsible for paying tax. The system defaults the appropriate tax rate and tax code based on the responsible company's associated tax group (HQ Tax Codes and Rates field, HQ Company Setup, Add’l Info tab).
For sales and value added tax, the system validates/defaults the tax code based on the selling company's tax group. For use tax, the system validates/defaults the tax code based on the purchasing company's tax group.

##  Tax Code

The Tax Code field on the AP Transaction Entry form, items Info tab.

If posting taxes to this item, specify a valid tax code (HQ Tax Codes), or accept the default. This field defaults as follows:

- 1-Job – The tax code default is determined by the Base Tax On field in JC Jobs. If set to J-Job, the tax code defaults from JC Jobs. If set to V-Vendor, the tax code defaults from AP Vendors. If set to O-Vendor Override, the tax code defaults from AP Vendors. If a tax code is not specified for the vendor, the tax code defaults from JC Jobs. You can override the default as necessary.

- 2-Inv – Defaults the tax code from IN Locations, unless the material is not taxable, in which case, defaults as blank.

- 3-Exp – Defaults the tax code from AP Vendors. If no tax code is specified for the vendor, defaults as blank.

- 4-Equip – Defaults the tax code from AP Vendors. If no tax code is specified for the vendor, defaults as blank

- 5-EM Work Order – Defaults the tax code from AP Vendors. If no tax code is specified for the vendor, defaults as blank

- 6-PO – Defaults the tax code from the purchase order item

- 7-SL – Defaults the tax code from the subcontract item

- 8-SM Work Order – Defaults based on work order type:

- Customer Work Order - If Tax Type is Sales or VAT, defaults the vendor tax code. If no vendor tax code exists, defaults the tax code from the work order's tax source (service site or service center). If no tax code assigned to the tax source, defaults as blank.If the Tax Type is Use, defaults the tax code from the work order's tax source (service site or service center). If no tax code assigned to the tax source, defaults as blank.

- Job Work Order - For Sales, VAT, and Use tax types, this field defaults based on the Base Tax On field in JC Jobs. See the description for Job lines above.

Committed CostsIf you specified a job (JC, PO, or SL line types) for this line and you post taxes to the line, the system relieves committed costs from the phase/cost type in JC Cost Detail table for the tax amount as follows:

- if phase and cost type overrides exist for the tax code, the system uses the tax code phase and cost type.

- if a phase override exists for the tax code, but a cost type override does not exist, the system uses the tax code phase and the cost type from the PO line.

- if a cost type override exists for the tax code, but a phase override does not exist, the system uses the phase from the PO line and the tax code cost type.

- if phase or cost type overrides do not exist for the tax code, the system uses the phase and cost type specified for the PO item.

Intercompany TransactionsFor Sales or VAT tax, the tax code defaults based on the Tax Group assigned to the AP Company. For Use tax, the tax code defaults based on the Tax Group assigned to the 'posted to' company.Redirect PhaseFor 1-Job lines, job-related 6-PO lines, or job-related 8-SM Work Order lines, if the tax code entered here is assigned a redirect phase and/or cost type (in HQ Tax Codes), the system validates the phase and/or cost type based on the Phases on this job are locked checkbox in JC Jobs. Validation is as follows:

- Phases Locked - If the Phases on this job are locked checkbox is selected and the tax code specifies a redirect phase only, the phase must exist in JC Job Phases for the line's job. If the tax code specifies both a redirect phase and cost type, the phase/cost type combination must exist for the line's job in JC Job Phases. If the tax code specifies a redirect cost type only, the cost type must exist in JC Job Phases for the invoice line's phase (for PO and SM lines associated with a job work order, this will be the scope phase).

- Phases Not Locked - If the Phases on this job are locked checkbox is not selected and the tax code specifies a redirect phase only, the phase must exist in JC Job Phases (for the line's job) or in JC Phases. If the tax code specifies both a redirect phase and cost type, the phase/cost type combination must exist in JC Job Phases or JC Phases. If the tax code specifies a redirect cost type only, the cost type must exist in JC Job Phases or JC Phases for the invoice line's phase (for PO and SM lines associated with a job work order, this will be the scope phase).

If the conditions indicated above are not met, you must either use a different tax code or add the phase and/or cost type combination to JC Job Phases or JC Phases (depending on the "locked phases" flag) before you can post the batch.

## Tax Basis

The Tax Basis field on the AP Transaction Entry form, items Info tab.

This field is only enabled if you enter a Tax Type and Tax Code for the line.
Enter the amount of this transaction that is taxable or accept the defaulted value. Typically, the default value will be equal to the line's gross amount; however, if you are using tax discounts (the Using tax discounts checkbox is selected in AP Company Parameters), this field defaults the line's gross amount less the discount amount.
Note: If you entered an amount in the Misc Amt field, that amount is not included in the Tax Basis amount.

Note: Tax amounts posted to subcontract lines are not included in the invoiced amount updated to SLIT (SL Items). Therefore, if you have set up a subcontract to include sales tax, it is suggested that you post invoices with the tax amount included as part of the gross amount and set this field to 0.00. If the subcontract is set up without tax and sales tax applies, then gross and sales tax amounts should be entered separately on the invoice line.

## Tax Amt

The Tax Amt field on the AP Transaction Entry form, Items Info tab.
This field defaults a calculation of the Tax Basis x the Tax Code rate.
If the Tax Type and Tax Code are blank, this field defaults as blank.

### Subcontract Lines

Tax amounts posted to subcontract lines are not included in the invoiced amount updated to SLIT (SL Items). Therefore, if you have set up a subcontract to include sales tax, it is suggested that you post invoices with the tax amount included as part of the gross amount (not posted separately here). If the subcontract is set up without tax, and sales tax applies, the gross and sales tax amounts should be entered separately on the invoice line.

### SM Work Order Lines

When you process an AP Transaction Entry batch, the system automatically generates a work completed miscellaneous line (in SM Work Orders) for each invoice line posted to line type 8-SM Work Order. Tax information entered on these lines will populate the Cost Tax fields on the work completed line.
Note: If the value in this field is not 0.00, entry in the SM Cost Type field is required.

## Pay Category

This field displays only if you selected the
 Using Payable
 Category checkbox in AP Company Parameters.
Specify a valid pay category for this line. The pay
 category specified here, along with the line type (Type field), will determine the default pay type
 (next input).
Initially defaults a pay category as follows:

- If you have set up a standard or user pay category
 override in F3 Properties (not recommended), defaults the F3 pay category.

- If no F3 override exists, defaults the pay category specified for the current user in VA User Profile.

- If no override pay category is specified for the user, defaults the pay category defined in AP Company Parameters.

- If no default pay category is defined for the company, default will be null. (In this case, the pay type will default from AP Company Parameters based on the line's type.)

The default may be overridden if you allow overrides
 to pay type (you selected the Allow Payable Type Override checkbox in AP
 Company Parameters); otherwise, input is disabled.
Note:If you bring a posted transaction back into a batch
 and change the pay category for a line with retainage, the system debits the GL account
 associated with the pay type for the original pay category (Payable Type Retainage field in AP Pay
 Category).

Additionally, if the pay category has a discount GL
 specified (Discount Taken
 GL Acct field in AP Pay Category), and you have checked the Post Discounts Offered to GL and
 net amount to subledgers box in the AP Company Parameters form, the system debits
 the discount to the GL account specified for the original pay category.
For Purchase Order lines, the pay category and pay type always default from the PO item, regardless of whether overrides exist in F3, VA User Profile, or AP Company Parameters. This is true even if you deselect the Using Payable Category checkbox in AP Company Parameters after you have already implemented its use. Although
 the pay category is not visible, its assignment will remain in effect.

If a pay category and pay type were not specified for the PO item, the pay category and pay type default based on the standard hierarchy (F3, VA User Profile, AP Company Parameters) and the PO item's line type. However, you will be allowed to continue. The month indicated here is the month in which the payment will be posted.

## Pay Type

The Pay Type field in AP Transaction Entry, Lines section, Info tab.
Required.
Specify the pay type for this item. If you are using pay categories (flag in AP Company Parameters), defaults the pay from this line's pay category based on the line type. The pay type used for each line type is as follows:

- Job lines - Use the Job pay type

- Inv, Exp, Equip, and EM Work Order lines - Use the Expense pay type

- PO lines - Use the pay type assigned to the PO item.

- SL lines - Use the Subcontract pay type

- SM Work Order lines - Use the SM Work Order pay type

If you allow pay type overrides (flag in AP Company Parameters), you may override the default.
 If you are using pay categories, the pay type must be either assigned to the specified pay category (in AP Pay Category) or an 'unassigned' pay type (a pay type that has not been restricted to a pay category in AP Payable Types).
If you are not using pay categories, you can specify any pay type, regardless of whether the pay type is restricted to a
 pay category.Note: You can only enter a pay type that is not designated for retainage in AP Company Parameters or for a pay category in AP Pay Category.

##  Supplier

 Indicate the supplier (from AP Vendors) for this item, if applicable. Note that if a
 supplier is entered here, payment will be made with a 2-party check.
