---
title: "Field Definitions: AP Company Parameters | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form/field-definitions-ap-company-parameters"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form/field-definitions-ap-company-parameters"
---

# Field Definitions: AP Company Parameters

The following is a list of field descriptions for the AP
 Company Parameters form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## AP Company

Enter the AP Company in which invoice and payment processing occurs. This must be a valid company number set up in HQ Companies.

## GL Co#

Specify the GL Company to update when posting invoices and making payments. The GL Company should be the same as your AP Company, but it is not required.
The specified company is used to validate Journals and GL Accounts, and is the default company when entering Expense transactions (AP Transaction Entry, AP Recurring Invoices).

## Expense Journal

The Expense Journal field on the AP Company Parameters form, GL Expense Posting tab.
Enter the GL journal to which invoice transactions are posted when interfacing to GL. Press F4 to select from a list of valid GL journals.

## GL Expense Interface Level

Summary – Invoice entries will be summarized,
 and one entry will be posted to GL per each Batch, GL Co#, and GL Account. If you select
 this option, the description entered (in the Summary GL Description field) is used as
 the GL transaction description, as well as select items for the Line level description.
 Even though summary is chosen here, if an account is set up in GL Chart of Accounts for
 interface detail, then that account receives detail entries at the Line level.
Transaction - One entry will be posted to GL per each Batch, GL Co#, GL Account, and Trans#. If you select this option, use the Select Available Items for Transaction Level GL Descriptions box to select the fields you want included as part of the GL transaction description. Available fields are:

- InvDesc

- Vendor#

- SortName

- APRef

- InvDate

- Trans#

Selected items display to the right of the option box, in the order they are selected. Selected items are highlighted in blue; to deselect an item click it again and the blue highlight is removed. More than one item can be selected at once.
Line – One entry will be posted to GL per each
 Batch, GL Co#, GL Account, Trans#, and Line. If you select this option, use the Select Line Type and
 Available Items for Line Level Gl Descriptions boxes to select the fields
 you want included as part of the GL transaction description for each of the Line Types.
 Available Line Types and Items are discussed in the table below.
Available Line Types
Available Items

Exp
InvDesc, Vendor#, SortName, APRef, InvDate, Trans#, Line, LineDesc, Matl

Job
InvDesc, Vendor#, SortName, APRef, InvDate, Trans#, Line, LineDesc, JCCo, Job, Phase, JCCT

Inv
InvDesc, Vendor#, SortName, APRef, InvDate, Trans#, Line, LineDesc, INCo, Loc, Matl

Equip
InvDesc, Vendor#, SortName, APRef, InvDate, Trans#, Line, LineDesc, INCo, Loc, Matl

Selected items display to the right of the option box, in the order they are selected. Selected items are highlighted in blue; to deselect an item click it again and the blue highlight is removed. More than one item can be selected at once.
Note:For PO line types, if you checked the Interface
 Detail box in GL Chart of Accounts for the GL account, the line type
 descriptions specified here will be used for job, inventory, or equipment PO's. Expense
 type POs will use the GL expense detail description specified in PO Company. If you did
 not check the Interface Detail box, all POs use the GL expense detail description in
 PO Company, regardless of line type.

None – GL entries created when posting expenses are not interfaced to GL.

## Summary GL Description

Enabled only when Summary is selected as the
 GL Expense Interface Level (field above).
Enter the description you want used each time
 a summarized invoice entry is interfaced to GL.

## Payments Journal

Indicate the GL journal (set up in GL
 Journals) to which AP payment transactions are posted when interfacing to GL.

## Select Line Type

The Select Line Type drop-down on the AP Company Parameters form, GL Expense Posting tab.
From the drop-down select the line type for which to set the GL line level description.

- 0-Expense

-
1-Job

- 2-Inv

- 3-Equip

 Then use the selection box (to the right) to select the description items to use for the selected line type.

Repeat the process for each of the line types.

## GL Payments Interface Level

Summary – Payment entries will be summarized and one entry will be posted to GL per each batch, GL Co#, and GL Account. If you select this option, the Summary GL Description you enter (the field below) is used as the GL transaction description.
Payment - One entry will be posted to GL per
 each Batch, GL Co#, GL Account, and Payment#. If you select this option, use the Select Available Items for
 Payment Level GL Descriptions box (below) to select the fields you want
 included as part of the GL transaction description. Available fields are:

- CMCo

- CMAcct#

- Vendor

- SortName

- Check#

- Paid Date

Selected items display to the right of the option box, in the order they are selected. Selected items are highlighted in blue; to deselect an item click it again and the blue highlight is removed. More than one item can be selected at once.
None – GL entries created when posting payments are not interfaced to GL.

## Summary GL Description

 Enabled only when Summary is selected as the GL Payment Interface Level (field above).
 Enter the description you want used each time a summarized payment entry is interfaced to GL.

## Using Payable Category

The Using Payable Category checkbox on the AP Company Parameters form, Pay Types/Discounts/ICR tab.
Select this checkbox to enable payable categories. If you
 implement multi-divisional accounting, this allows you to define separate expense, job,
 subcontract, and retainage pay types as well as discount accounts for each division (location, region, division, office, branch, etc.) that requires separate GL accounting. It
 also enables the Payable Category Default field, allowing you to specify the
 default pay category to use when entering transactions in AP, PO (if
 the PO Company flag is set to do so), and MS. Additionally, posting forms that prompt for pay type
 also prompt for pay category.
Leave this checkbox unselected if you are not using payable
 categories. Pay category prompts will not display in posting forms and pay type prompts
 default from the company payable types specified below.

## Payable Category Default

Enabled only when the 'Using Payable Category' option is checked.
Specify the pay category to use as a default when entering transactions in AP and PO Purchase Order Entry (if PO Company flag set to do so). This pay category is used in conjunction with the transaction's line type to determine the default pay type.
If you have defined a default pay category at the F3 Properties level (not recommended) or in VA User Profile, it will override the default pay category specified here. If no override defaults are specified and this field is null, transaction pay types default from the 'AP Company Payable Types', depending on line type.

## Payable Types: Expense

Specify the default payable type (set up in AP Payable Types) for non-job transactions. If you are not using the payable categories feature (above), this pay type defaults when posting non-job transactions. If you are using pay categories, this pay type is only used if a default pay category has not been specified in AP Company Parameters, F3 Properties, or VA User Profile.
This payable type determines the AP GL Account to credit when the invoice batch is posted, and to debit when it is paid.

## Payable Types: Job

Specify the default payable type (set up in AP Payable Types) for job transactions. If you are not using the payable categories feature (above), this pay type defaults when posting job transactions. If you are using pay categories, this pay type is only used if a default pay category has not been specified in AP Company Parameters, F3 Properties, or VA User Profile.
This payable type determines the AP GL Account to credit when the invoice batch is posted, and to debit when it is paid.

## Payable Types: Subcontract

Specify the default payable type (set up in AP Payable Types) for subcontract transactions. If you are not using the payable categories feature (above), this pay type defaults when posting subcontract transactions. If you are using pay categories, this pay type is only used if a default pay category has not been specified in AP Company Parameters, F3 Properties, or VA User Profile.
This payable type determines the AP GL Account to credit when the invoice batch is posted, and to debit when it is paid.
Note: It is suggested that a separate pay type be set up
 for subcontracts even if you do not have a separate GL account for Subcontract Payables.
 Pay types are also used when selecting invoices for payment in AP Payment Posting. If you
 pay subcontractors under a different schedule than other job payables, this will allow for
 separate payment selection. It is particularly useful if paying subcontracts on a “pay when
 paid” basis.

## Payable Types: Retainage

Specify the payable type (set up in AP Payable Types) for retainage. If you are not using the payable categories feature (above), this pay type will be assigned to any retainage amount entered for a transaction. If you are using pay categories, this pay type will only be used if no default pay category has been specified in AP Company Parameters, F3 Properties, or VA User Profile. The system uses this payable type to determine the AP GL Account to credit when posting the expense batch, and to debit when it is paid.
Note: Although not required, it is strongly recommended
 that the payable type assigned for retainage differ from those assigned for Expense, Job,
 and Subcontract transactions.
The system automatically assigns this payable type to the retainage portion of the transaction line; it does not display on the screen and cannot be overridden.

## Payble Types: SM Work Order

Specify the default payable type (set up in AP Payable Types) for SM work order transactions. If you are not using the payable categories feature (above), this pay type defaults when posting SM work order transactions (in AP Transaction Entry and AP Unapproved Invoice Entry). If you are using pay categories, this pay type is only used if a default pay category has not been specified in AP Company Parameters, F3 Properties, or VA User Profile.
This payable type determines the AP GL Account to credit when the invoice batch is posted, and to debit when it is paid.

## Allow Payable Type Override

The Allow Payable Type Override checkbox on the AP Company Parameters form, PayTypes/Discounts/ICR tab.
Select this checkbox to allow overrides to the Pay Type when posting transactions (AP Transaction Entry, AP Recurring Invoices, AP Unapproved Invoices, and SL to AP Update). If you are using pay categories (above), selecting this checkbox also enables the pay category input on these forms.
Leave this checkbox unselected if you do not want the default Pay Type overridden when posting transactions (AP Transaction Entry, AP Recurring Invoices, AP Unapproved Invoices, and SL to AP Update). Additionally, if you are using pay categories, leaving this checkbox unselected disables the pay category input on these forms.

## Post Discounts Offered to GL and Net Amounts to Subledgers

Check this box if you want only the net amounts of payable transactions posted to subledgers. When the payable transaction is posted, the discount amount is subtracted from the gross amount and is debited to the Discount Offered GL Account (specified below) in the AP GL Co#. If you are using pay categories, you must specify a Discount Offered GL Acct for the pay category in AP Pay Category.
Do not check this box if you want the full amount of payable transactions posted to subledgers. When unchecked, the Discount Offered GL Account input is disabled.
Although this feature is available for users who want the net amount of invoice transactions expensed, it is not the recommended method. If used, you will not be able to adjust the discount using AP Payment Control or when paying the invoices in AP Payment Posting. Discounts can only be changed by calling up and changing a transaction or by posting an adjustment transaction in AP Transaction Entry.

## Discount Offered GL Account

Specify the GL account (from GL Accounts) to
 debit with discounts posted in AP Transaction Entry, AP Recurring Invoices, and AP
 Unapproved Invoices. This account is only updated if you are posting net amounts to
 subledgers (the Post Discounts Offered to GL and Net Amounts to Subledgers box is checked).
Note: If you are using pay categories, you must specify a
 Discount Offered GL Acct for the pay category in AP Pay Category. This account is only used
 if you are not using pay categories.

## Discount Taken GL Account

Specify the GL account (from GL Accounts) to
 credit with discounts actually taken with a payment. This account is used regardless of
 whether posting net or full amounts to subledgers.
Note: If you are using pay categories, you must specify an
 account in the Discount Offered GL Acct field for the pay category (in AP Pay Category).
 This account is only used if you are not using pay categories.

## Retainage Hold Code

Enter the hold code to place on the retainage
 portion of a transaction. The system assigns this hold code automatically when you enter
 retainage for a transaction and cannot be overridden.

## T5 Program Account

T5 Program Account on AP Company Parameters form, PayType/Discounts/ICR tab.
This field displays for Canadian companies only.
Enter the GST/HST program account number for this company. This number must begin with RZ and be followed by a four-digit reference number.
During T5018 reporting (in AP T5018 Payments), the
 system derives the Payer's Account Number by appending this account number to the
 nine-digit Business Number in HQ Company Setup. The full business number is
 included in the generated efile, on the AP Canada T5018 Summary report, and on the T5018
 slip (if you did not select the Suppress Payer's Account Number on T5018
 Slip checkbox in AP Electronic File Generate).

Related information

- [AP Company Parameters Form](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form)

## Independent Contractor Reporting Info

There are two steps to setting up independent contractor reporting. You
 must first set some information in AP Company Parameters and then set up required reporting
 information for each applicable vendor in AP Vendors.

1.  In AP Company Parameters (Pay Types/Discounts/ICR tab), check the
 Independent
 Contractor Reporting box. When this box is checked, the system triggers a
 search function during payment processing to locate vendors meeting reporting requirements.

1.  Enter a threshold in the Threshold Payment Amount field. The system
 enables this field when you check the Independent Contractor Reporting box. The
 payment threshold may differ by state, ranging from $0 to $2,500; however, it will typically
 be $600. Contractors meeting or exceeding this amount (and meeting other reporting
 requirements) are included when printing the AP Independent Contractors Report.

1.  Enter a report title in the Report Title field. The system enables this
 field when you check the Independent Contractor Reporting box. This
 field indicates the report to use when the system generates an independent contractors
 report. Entry in this field is required only if you are using a custom report. Otherwise,
 leave the field blank to use the standard report (AP Independent Contractors Report). Note: The standard report follows California's reporting
 requirements. However, because reporting requirements may vary from state to state, you
 may choose to create your own report.

1.  In AP Vendors, enter the reporting information on the I.C. Report
 Info tab. The information on this tab is required for all states that require independent
 contractor reporting. Note: You must fill out this
 information for vendors who are independent contractors that you have hired and: you are
 required to file a 1099-MISC form for their services; to whom you pay $600 or more or
 enter into a contract for $600 or more; and who are individuals or sole
 proprietorships.
Note: The Last Reported
 Activity display field shows the date on which the contractor was last
 reported. It is updated each time the Independent Contractors report is run for the vendor
 and is used to determine whether or not a contractor has been reported for the calendar
 year.

## JC Co#

Specify the Job Cost company that defaults when posting job transactions (AP Transaction Entry, AP Recurring Invoices). May be overridden.

## JC Interface Level

Transaction – One JC detail entry is created per Batch, JC Co#, Job, Phase, JC Cost Type, and AP Trans#. Costs and units are accumulated and units are converted to the JC U/M if possible.
Line – One JC detail entry is created per Batch, JC Co#, Job, Phase, JC Cost Type, AP Trans#, and AP Line#.
None – Actual costs on Job transactions created in AP Transaction Entry and/or AP Recurring Invoices are not updated to Job Cost. However, adjustments to committed costs for invoices posted to a PO or Subcontract are updated.

## EM Co#

Specify the default EM company to update with Equipment and Work Order transactions. May be overridden.

## EM Interface Level

Transaction – One EM cost detail entry is created per Batch, EM Group, Equipment, Cost Code, EM Cost Type, and AP Trans#. Cost and units are accumulated, while units are converted to the EM U/M, if possible. No line-level information (i.e. Material, Work Order, Work Order Item, PO, PO Item, etc.) is written to EM.
Line – One EM cost detail entry is created per Batch, EM Group, Equipment, Cost Code, EM Cost Type, AP Tran#, and AP Line#. Line-level information (i.e. Mat'l Group, Material, Work Order, Work Order Item, PO, PO Item, Units, Dollars, etc.) is written to EM.
None – No Equipment and Work Order transactions are updated to EM.

## IN Co#

Specify the default IN company to update with Inventory transactions. May be overridden.

## IN Interface Level

Line – One IN detail entry is created per Batch, IN Co#, Location, Material, AP Trans#, and AP Line#. All units are converted to the Material’s standard unit of measure.
None – Inventory transactions are not updated to Inventory.

## CM Co#

Specify the Cash Management company used for
 validating CM Accounts, and to which payment information from this AP company will be
 posted.
Note: Changing this field and saving the record triggers a
 message asking if you want to update all open AP transactions. Click Yes to update
 all open transactions or No to change the account number without
 updating open transactions.This applies to only those transactions that have a pay
 method of check or electronic funds transfer (EFT).

## CM Account #

Specify the bank account for making payments. This account is the default when posting payment information, but may be overridden.
Note: Changing this field and saving the record triggers a
 message asking if you want to update all open AP transactions. Click Yes to update
 all open transactions or No to change the account number without
 updating open transactions.This applies to only those transactions that have a pay
 method of check or electronic funds transfer (EFT).

## CM Interface Level

Payment – One CM detail entry is created per Batch, CM Co#, and CM Reference. If the entry corresponds to a check number, the vendor is included in the detail. If the payment is an EFT, only its total amount is recorded.
None – Payment transactions are not updated to Cash Management.

## Audit Options

The audit options determine
 when new records of changes are added to the HQ Master Audit (HQMA) database table. For
 example, if you change a setting on the company parameters form, the system creates a new
 record of the change in the HQMA table.
You can view records in the HQMA table using the HQ Audit Detail report in the HQ module. See [About Viewing the Master Audit Log](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log) for more information about viewing audit records in the HQMA table.

Selecting this checkbox
records changes to

Company Parameters
AP Company Parameters form (always selected)

Pay Types/Pay Category
AP Payable Types form
AP Pay Category form

Vendor Master and Totals
AP Vendors form
AP Vendor Activity form
AP 1099 Processing form

Vendor Hold Codes
AP Vendor Hold Codes form

Vendor Compliance
AP Vendor Compliance form

Transactions
AP transaction records

Recurring Invoices
AP recurring invoice records

Payment History
AP payment history records

Unapproved Invoices
AP unapproved invoice records

*Transaction Hold Codes
Hold codes assigned to AP transaction records

*The system also
 records hold codes released via the AP Hold and Release form and the AP Payment Control
 Detail form, accessed by selecting File > Tasks >  Additional Pay
 Control Functions from the AP Payment Workfile form.

## Allow Add From PM

The Allow Add From PM checkbox o the AP Company Parameters form, Audit Options tab.
Check this box to allow adding vendors from PM. If a vendor is specified for a firm in PM Firms, and that vendor does not already exist in AP Vendors, upon saving the record and answering Yes to the update message, the vendor is added to AP Vendors. If you answer No, the vendor needs to be added manually.
Do not check this box if you do not want vendors added to AP Vendors from PM Firms. If a vendor is specified for a firm in PM Firms, and that vendor does not already exist in AP Vendors, it will not be added automatically; you will need to add the vendor manually.
Click [here](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firms-form) for more information.

## Allow Update From PM

Check this box to allow updating vendor information from PM. When
 changes are made to a firm with a designated vendor in PM Firms, and if you answer Yes to
 the update message, the information is updated for the vendor in AP Vendors. If you answer
 No, you will need to update the information manually.
Do not check this box if you do not want
 vendor information updated to AP Vendors from PM Firms. Information will need to be updated
 manually.
Click [here](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firms-form) for more information.
Note: If you elect to allow updates from PM Firms, you will
 typically also specify to allow updates to PM Firms by checking the update option in PM
 Company Parameters. This will ensure that records remain in sync.

## Subcontracts: Allow Transactions to Exceed Current Total Cost

Check this box to allow a transaction's invoiced amount to exceed the total cost of the subcontract item or subcontract. Warning displays, but amount will be allowed.
Do not check this box if invoiced amounts cannot exceed the total cost of the subcontract item or subcontract. Warning displays and you will need to correct the invoiced amount before the batch can be posted. For unapproved invoices, a warning displays, but entry is allowed. However, once the invoice is approved and added to an AP batch, you will need to correct the invoiced amount before you can post the batch.
Note:Entering negative items to a subcontract in SL after you have already invoiced the subcontract in AP can potentially cause the invoiced amount to exceed the subcontract total. If this flag is unchecked, an invoice that is entered for a negative item causes the system to inform you that the invoiced amount has exceeded the subcontract total. The entry will be accepted; however if you do not post ALL of the negative items, batch validation will throw an additional error and not allow you to post the batch. To allow for posting of the batch you will need to:

- invoice ALL negative items for the subcontract to ensure the invoiced amount and subcontract total balance or,

- if not invoicing all of the negative items, set this flag to Y (checked), invoice the desired items, post the batch, then reset this flag to N (unchecked). However, if you use this method, you may need to repeat this process until the entire negative amount is accounted for (i.e. all negative items have been invoiced, thereby balancing with the subcontract total).

## Subcontracts: Check Compliance on Transaction Entry, Warning Only

If you check this box, compliance is checked
 whenever posting invoices against subcontracts. You will receive a warning if the
 subcontract is out of compliance (based on the invoice date or the complied flag), but the
 entry will be allowed.
Do not check this box if you do not want
 compliance checked when posting subcontract transactions.

## Subcontracts: Don't Add to Payments Batch
 if "Out of Compliance"

If you check this box, subcontract entries are checked for compliance when initializing payment batches. If a subcontract is out of compliance, it is not added to the batch.
Note: Checking this box prevents out-of-compliance
 transactions from being initialized into payment batches; it does not prevent the ability
 to add an out-of-compliance transaction to a payment batch manually.
Do not check this box if you want out-of-compliance invoices initialized into payment batches. You can then use the AP Payment Preview with Compliance report to review compliance status.

## POs: Allow transactions to exceed item line's current total cost

The POs: Allow transactions to exceed item line's current total cost checkbox on the AP Company Parameters form, Audit Options tab, Purchase Orders section.
Select this checkbox to allow users to enter an invoiced amount that exceeds the current total cost of the purchase order item line. In this case, the system will display a warning, but will allow entry.
Important: It is important to note that when you process a batch that includes invoice lines that exceed the total cost of the PO item line, the system will allow you to post the batch. If this is not your intention, do not select this checkbox.

Leave this checkbox unselected if you do not allow entering invoiced amounts that exceed the current total cost of the purchase order item line. In this case, the system displays a warning and you must correct the invoiced amount before posting the batch.
For unapproved invoices, the system displays a warning, but allows the entry. However, once the invoice is approved and added to an AP batch, you will need to correct the invoiced amount before posting the batch.
Note: Standing purchase order items (those with a non-zero unit cost and 0.00 units) are exempt from the invoice amount checks, since the associated PO's current total cost is 0.00.

## POs: Allow Transaction to Exceed Item's Current Total Cost

The POs: Allow Transaction to Exceed Item's Current Total Cost checkbox on the AP Company Parameters form, Audit Options tab, Purchase Orders section.
Select this checkbox to allow a transaction's invoiced amount to exceed the current total cost of the purchase order item. In this case, the system displays a warning, but allows the entry.
Important: It is important to note that when you process a batch that includes invoices that exceed the total cost of the PO item, the system will allow you to post the batch. If this is not your intention, do not select this checkbox.

Leave this checkbox unselected if invoiced amounts cannot exceed the purchase order item’s current total cost. The system displays a warning and you must correct the invoiced amount before posting the batch.
For unapproved invoices, the system displays a warning, but allows the entry. However, once the invoice is approved and added to an AP batch, you will need to correct the invoiced amount before posting the batch.
Note: Standing purchase order items (those with a non-zero unit cost and 0.00 units) are exempt from the invoice amount checks, since the associated PO's current total cost is 0.00.

## POs: Allow Transaction to Exceed PO's Current Total Cost

The POs: Allow Transaction to Exceed PO's Current Total Cost checkbox on the AP Company Parameters form, Audit Options tab, Purchase Orders section.
Select this checkbox to allow a transaction's invoiced amount to exceed the current total cost of the purchase order. Warning displays, but amount is allowed.
Important: It is important to note that when you process a batch that includes invoices that exceed the total cost of the PO, the system will allow you to post the batch. If this is not your intention, do not select this checkbox.

Leave this checkbox unselected if invoiced amounts cannot exceed the purchase order's current total cost. The system displays a warning and you must correct the invoiced amount before posting the batch.
For unapproved invoices, the system displays a warning, but allows the entry. However, once the invoice is approved and added to an AP batch, you will need to correct the invoiced amount before you can post the batch.
Note: Standing purchase order items (those with a non-zero unit cost and 0.00 units) are exempt from the invoice amount checks, since the associated PO's current total cost is 0.00.

## POs: Allow Invoiced to Exceed PO Item Line Received

The Allow Invoiced to Exceed PO Item Line Received checkbox on the AP Company Parameters form, Audit Options tab, Purchase Orders section.
Select this checkbox to allow users to enter an invoiced amount that exceeds the received units or amounts for the purchase order item line. In this case, the system displays a warning, but allows entry.
Important: It is important to note that when you process a batch that includes invoices exceeding received units/amounts, the system will allow you to post the batch. If this is not your intention, do not select this checkbox.

Leave this checkbox unselected if invoiced units and/or amounts must be equal to or less than the received units and/or amounts for a purchase order item line. If you enter units or an amount that exceed the received units or amount, the system displays a warning and will not save the entry. You must correct the units or amount before you can save the item line.
For unapproved invoices, the system will display a warning, but will allow entry. However, once the invoice is approved and added to an AP batch, you will need to correct the invoiced units or amount before posting the batch.
Note: If you post job-related POs, you may want to consider leaving this option unchecked. Restricting users from invoicing more than received helps ensure that job cost detail and GL detail are in sync.

## POs: Allow Invoiced to Exceed PO Item Received

The POs: Allow Invoiced to Exceed PO Item Received checkbox on the AP Company Parameters form, Audit Options tab, Purchase Orders section.
Select this checkbox to allow a transaction's invoiced units or amount to exceed the
 received units or amount. Warning displays, but entry is allowed.
Important: It is important to note that when you process a batch that includes
 invoices exceeding received units/amounts, the system will allow you to post the batch.
 If this is not your intention, do not select this checkbox.

Leave this checkbox unselected if invoiced units or amounts must be equal to or less than
 the received units or amounts. If a transaction's invoiced units or amount exceed the
 received units or amount, a warning displays and entry cannot be saved. You must correct
 the units or amount before you can save the line.
For unapproved invoices, warning displays, but entry is allowed. Once you have approved the
 invoice, it can be added to an AP batch, but you will need to correct the invoiced units or
 amount before you can post the batch.
Note: If you post job-related POs, you may want to consider leaving this option unchecked.
 Restricting users from invoicing more than received helps ensure that job cost detail
 and GL detail are in sync.

## POs: Check Compliance on Transaction Entry, Warning Only

If you check this box, compliance is checked
 whenever posting invoices against purchase orders. Warning displays if the purchase order
 is out of compliance (based on the invoice date or the complied flag), but entry is
 allowed.
Do not check this box if you do not want
 compliance checked when posting purchase order transactions.

## POs: Don't Add to Payments Batch if "Out
 of Compliance"

If you check this box, purchase order entries are checked for compliance when initializing payment batches. If a purchase order is out of compliance, it is not added to the batch.
Note: Checking this box prevents out-of-compliance
 transactions from being initialized into payment batches; it does not prevent the ability
 to add an out-of-compliance transaction to the payment batch manually.
Do not check this box if you want out-of-compliance invoices to be initialized into payment batches. You can then use the AP Payment Preview with Compliance report to review compliance status.

## Require invoice total to equal sum of all lines

Require invoice total to equal sum of all
 lines checkbox in the AP Company Parameters form, Invoice Options tab.
Check this box if you want to require that the amount in the
 Invoice Total
 field in the transaction’s header be equal to the sum of the transaction’s line totals.
Line total is defined as Gross + Misc Amt +
 Tax Amt
 (where Tax Type <> 2) - Ret Amt (in CA/AU).
Do not check this box if the sum of a transaction’s line totals does not have to equal the amount in the
 Invoice Total
 field. A warning still displays if the totals do not match, but you can still save the record.
Note: Your selection
 in this box affects the conditions required to automatically flag invoices as ready for
 review. See [Automatically mark unapproved invoices Ready](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form/field-definitions-ap-company-parameters#ID-00005a89--en).

## Default Header Description to Lines on Job Type

Check this box if you want the line description to default from the header description on job type lines (AP Transaction Entry, AP Unapproved Invoice Entry).
Do not check this box if you want the line description to default the phase description on job type lines.
Note: If a material code is entered, the description always
 defaults the material description defined in HQ Materials, regardless of how this option is
 set.

## Default Header Description to Lines on Equipment Type

Select this checkbox to have the line Description field default from the header Description field on equipment type lines (AP Transaction Entry, AP Unapproved Invoices, AP Recurring Invoices).
If you do not select this checkbox, the line Description field defaults the Cost Code description.

## Default JC Job Phase UM on Job Lines

Check this box to have the UM default from the CT entered for job lines in AP Transaction Entry, AP Unapproved Invoices, and AP Recurring Invoices.
If you do not select this checkbox, the line UM defaults from the Material field. If no material is specified, the UM defaults as LS.
Note: Regardless of whether you check or uncheck this box,
 if you specify a material on the job line, the system will always default the purchase UM
 defined for the material in HQ Materials.

## Check Vendor Compliance on Trans Entry, Warn Only

The Check Vendor Compliance on Trans Entry, Warn Only checkbox on the AP Company Parameters form, Invoice Options tab.

Select this checkbox to have vendor compliance checked when entering non-PO/SL AP invoices. If the vendor is out of compliance, display a warning, but allow the entry.
Note: In order to implement this feature, compliance codes must be flagged as 'all invoice' (that is, the Use This Code for All Invoice Compliance checkbox is selected in HQ Compliance Codes) and assigned to applicable vendors in AP Vendor Compliance. Then when entering invoices, vendors are checked for compliance based on the assigned 'all invoice' compliance codes. If out of compliance, a warning displays, but entry is allowed.
Do not select this checkbox if not checking for vendor compliance on non-PO/SL invoices.

## Don't Add Vendor to Payment Batch if "Out
 of Compliance"

Check this box to restrict initialization of non-PO or SL transactions to a payment batch when the vendor is out of compliance. If checked, out-of-compliance invoices cannot be initialized into payment batches.
Note: The system pulls out of compliance transactions into
 AP Payment Workfile, but you will unable to check the Initialize to be paid button and pass
 the transaction into the payment posting batch.
Do not check this box if allowing out-of-compliance invoices to be initialized into payment batches.

## Allow Vendors to be added from Payroll

Allow Vendors to be added from Payroll checkbox on the AP Company Parameters form, Audit Options tab.

Select this checkbox if you want to be able to create/add an AP Vendor from within the PR Employees form.
If the vendor number you enter in the Vendor field is not already on file, the system assigns it to a new vendor in the AP Vendors form and assigns these values from the PR Employees form:

- Name

- Address info

-  Email address

- Phone

- Direct deposit info

Note: If you do not select this checkbox, you must use the AP Vendors form to create the vendor record first, then insert the number in the Vendor field in the PR Employees form.

## Allow Vendors to be updated from Payroll

Allow Vendors to be updated from Payroll checkbox on the AP Company Parameters form, Audit Options tab.
Select this checkbox to automatically update the corresponding vendor record (in AP Vendors) when changes are made to the following sections:

- Name

- Address info

- Email address

- Phone

- Direct deposit info

Note: This checkbox only affects vendor records that are already paired to employee records. It does not affect the system's ability to update the vendor record based on information in the employee record when you are first creating the link.

## Using Tax Discount

Check this box if you are using tax discounts. Taxes will be
 calculated on the discounted invoice amount rather than the gross amount.
Do not check this box if not using tax discounts.

## Tax basis is net of retainage

This box applies when you are processing AP transactions with an associated Value Added Tax (VAT) code. Primarily, this applies to Australian and Canadian users. See additional information below.
Australia
The name of this box displays as Tax basis is net of
 retention. Check this box to withhold retention from the tax basis of AP
 transactions with an associated Value Added Tax (VAT) code. When you check this box, the
 system calculates the tax basis as the line amount minus retention. This enables you to
 track retainage Input Tax Credits (ITCs) separate from standard ITCs. See [Tracking Retainage Input Tax Credits: Australia](/en/vista/vista/accounting/accounts-payable/payments/retainage/retention-input-tax-credits-australia) for more
 information.
Canada
The name of this box displays as Tax basis is net of
 holdback. Check this box to withhold holdback from the tax basis of AP
 transactions with an associated VAT code. When you check this box, the system calculates
 the tax basis as the line amount minus retainage. This enables you to track retainage Input
 Tax Credits (ITCs) separate from standard ITCs. See [Tracking Holdback Input Tax Credits: Canada](/en/vista/vista/accounting/accounts-payable/payments/retainage/holdback-input-tax-credits-canada) for more
 information.

## Automatically mark unapproved invoices Ready

Automatically mark unapproved invoices Ready checkbox in the AP Company Parameters form,
 Invoice Options tab
Select
 this checkbox to make the system automatically set all future unapproved invoices' review
 status to 1 - Ready at the moment the invoice meets the minimum
 requirements for releasing it into the review process.
In order for an invoice to be considered valid for review, the following must be true for the invoice:

- The invoice must have at least one line

- Each invoice line must have at least one
 reviewer assigned

- If the Require
 invoice total to equal sum of all lines checkbox is selected (Invoice
 Options tab), the amount in the header Invoice Total field must equal the sum
 of the line totals. Line total is defined asGross + Misc Amt
 + Tax
 Amt (where Tax Type <> 2) - Ret Amt (in CA/AU).

After
 the invoice is marked as ready, if you make any changes to the invoice that would cause any
 of the above to become untrue, the system automatically changes the invoice status to
 0 - Not
 Ready. After the required changes/corrections are made, the system
 automatically updates the invoice status to 1 - Ready.
Leave this checkbox unselected to require the user to manually change the status on each invoice even if the required minimum data is present.

Related information

- [Change Status](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form/field-definitions-ap-unapproved-invoice-entry-form#ID-00007205--en)

## Warn if line coding exists on an open PO or SL

Warn if line coding exists on an open PO or SL checkbox in the AP Company Parameters form,
 Invoice Options tab
This checkbox is selected by default. When selected, the system provides warnings to users
 entering new AP invoices when it detects a possible match to an existing purchase order or
 subcontractor. Instead of potentially duplicating committed costs and units, the user can
 determine whether the invoice they are entering should instead relieve an existing
 item.
If you clear this checkbox, the system will not provide warnings for potential matches
 between new invoices and purchase orders/subcontracts.
Vista compares
 specific field values for each line type. In order for an invoice to be considered a
 potential match to an existing PO or subcontract, the following invoice field values must
 match:
Line Type
Warning provided if values from
 each of these fields match

1-Job
Vendor | JC Co | Job | Phase |
 CT

2-Inv
Vendor | IN Co | Loc |
 Material

3-Exp
Vendor | GL Co | GL Acct

4-Equip
Vendor | EM Co | Equipment |
 Cost Code | Cost Type

5-EM Work Order
Vendor | EM Co | WO | WO Item |
 Cost Code | Cost Type

8-SM Work Order
Vendor | SM Co | SM Work Order
 | Scope Seq

## Check for unique AP Reference

The Check for unique AP Reference dropdown on the AP Company Parameters form, Invoice Options tab.
Select one of the following options to indicate how this company will handle validation for duplicate AP Reference numbers (AP Transaction Entry, AP Unapproved Invoice Entry). The level set here applies to all vendors in the same vendor group, but may be overridden at the vendor level.

- 1-By Vendor & Co – Select this option to check for duplicate numbers by vendor within the current company. If a duplicate number is entered for a vendor in the current company, display warning and only allow entry if the "Prevent Duplicate AP Reference" option (above) is ‘N’ (unchecked).

- 2-By Vendor, Cross-Co – Select this option to check for duplicate numbers by vendor across companies. If a duplicate number is entered for a vendor in any company sharing the same vendor group, display warning and only allow entry if the "Prevent Duplicate AP Reference" option (above) is ‘N’ (unchecked).

- 3-By Master Vendor & Co – Select this option to check for duplicate numbers by master vendor/sub vendor and company. If a duplicate number is entered for a vendor within a master vendor/sub vendor group in the current company, display warning and only allow entry if the "Prevent Duplicate AP Reference" option (above) is ‘N’ (unchecked).Note: You will typically not set this validation level at the company level unless all your vendors are set up using the master vendor/sub vendor theme. If you only set up a few vendors using the master vendor/sub vendor theme, it is suggested that you select the 1-By Vendor & Co option here, and then assign this level to the selected vendors in AP Vendors.

- 4-By Master Vendor, Cross-Co – Select this option to check for duplicate numbers by master vendor/sub vendor across companies. If a duplicate number is entered for a vendor within a master vendor/sub vendor group in any company sharing the vendor group, display warning and only allow entry if the "Prevent Duplicate AP Reference" option (above) is N (unchecked).Note: You will typically not set this validation level at the company level unless all your vendors are set up using the master vendor/sub vendor theme. If you only set up a few vendors using the master vendor/sub vendor theme, it is suggested that you select 2-By Vendor X-Co here, and then assign this level to the selected vendors in AP Vendors.

## Enable Case-Insensitivity on AP References

Select this checkbox to make the system consider both the upper and lower case of each letter as identical when you enter an AP Reference (invoice) number. For example, if you select this checkbox, "ABC123" and "abc123" are considered to be the same invoice number.
Leave this checkbox unselected to make the system consider the upper and lower case of each letter as different.
The following table provides a visual example of how the system behaves based on the setting of this checkbox.
checkbox
Policy
APRef Status

Unselected (default)
A ≠ a (case sensitive)
ABC123 and abc123 are not the same

Selected
 A = a (not case sensitive)
ABC123 and abc123 are the same

## Prevent duplicate AP Reference

The Prevent duplicate AP Reference checkbox on the AP Company Parameters for, Invoice Options tab.
Select this checkbox to prevent entry of duplicate AP Reference numbers in
 AP Transaction Entry and AP Unapproved Invoice Entry. When a duplicate reference number is
 encountered, the system displays a warning and you will be unable to save the record.
If you leave this checkbox unselected, when a duplicate reference number is encountered, the system displays a warning, but allows you to save the record.
Note: The definition of duplicate is based in part on your
 validation selection for all vendors for this company in the Check for unique AP Reference field, or
 by vendor (in AP Vendors).

## Report Title for Check Print

The Report Title for Check Print (US) or Report Title for Cheque Print (AU/CA) field on the AP Company Parameters form, Payment Reports tab.

Accept the default report or enter the report to use for printing AP checks/cheques.
United States: Report Title for Check PrintYou can specify a standard report (those provided by Vista™) or a user-created report. Available standard reports are:

- AP Check Print (default) - Used for printing on pre-printed checks with pre-printed check stubs.

- AP Check Print Stub - Used for printing on pre-printed checks with blank check stubs.

If this field is blank, the system uses the AP Check Print report.
Australia: Report Title for Cheque PrintYou can specify a standard report (those provided by Vista™) or a user-created report. Available standard reports are:

- PR Cheque Print - A/NZ - Used for printing on pre-printed cheque stock with pre-printed cheque stubs.

- PR Cheque Print Stub - A/NZ - Used for printing on pre-printed cheque stock with blank cheque stubs.

 If this field is blank, the system uses the PR Cheque Print - A/NZ report.
Canada: Report Title for Cheque PrintYou can specify a standard report (those provided by Vista™) or a user-created report. Available standard reports are:

- AP Cheque Report - Canada (default) - Used for printing on pre-printed checks with pre-printed check stubs.

- AP Cheque Stub - Canada - Used for printing on pre-printed checks with blank check stubs.

If this field is blank, the system uses the AP Cheque Report - Canada report.

## Report Title for Check Overflow

The Report Title for Check Overflow (US) or Report Title for Cheque Overflow (AU/CA) field on the AP Company Parameters form, Payment Reports tab.

Accept the default report or enter a user-created report for printing overflow checks.
The default reports are as follows:

- United States: AP Check Overflow

- Australia: AP Cheque Overflow - A/NZ

- Canada: AP Cheque Overflow - Canada

Note: If you clear this field, the system automatically uses the default report.

## Maximum Lines Per Check Stub

The Maximum Lines Per Check Stub (US) or Maximum Lines Per Cheque Stub (AU/CA) field on the AP Company Parameters form, Payment Reports tab.

Specify the maximum number of lines that can fit on a check/cheque stub. Initial default value is 29.
This number determines the amount of lines allowable on a check/cheque stub before overflow occurs and an overflow voucher must be printed. Although this field allows an entry of up to 99, it is recommended that you do not exceed a maximum of 29, as any number larger than this may cause additional form feeds between checks/cheques (depending on your printer's capabilities).
Note: If you are using Vista™ checks, you should not need to change
 this number.

## Report Title for EFT Remittance

The Report Title for EFT Remittance field on the AP Company Parameters form, Payment Reports tab.

Enter the report name that the system uses to create EFT remittance reports. The system will use this report when you select Tasks > EFT Remittance Report from AP Payment Posting.
United States UsersThe AP EFT/ePayments Remittance report (Report ID 26) is the only standard report provided. This report initially defaults in this field. If you do not enter a report name in this field, the system uses this report as the default. If you want to use a custom report you have created, enter the name or press F4 to locate it.Note: This standard report functions for EFTs, even if you are not using ePayments.

Australian UsersThe AP EFT Remittance - A/NZ report is the only standard report provided. This report initially defaults in this field. If you do not enter a report name in this field, the system uses this report as the default. If you want to use a custom report you have created, enter the name or press F4 to locate it.Canadian UsersThe AP AFT Remittance - Canada report is the only standard report provided. This report initially defaults in this field.If you do not enter a report name in this field, the system uses this report as the default. If you want to use a custom report you have created, enter the name or press F4 to locate it.

## Report Title for Payment Service

Enter the report name that the system will use to
 create credit service remittance reports. The system will run this report when you
 select Tasks > Credit
 Service Remittance Report from AP Payment Posting.
The AP Credit Service Remittance report is the only
 standard report provided. This report initially defaults in this field. If you do not
 enter a report name in this field, the system uses this report as the default. If you
 want to use a custom report you have created, enter the name or press F4 to
 locate it.

## Attach Vendor Payment Report to Pay History

Select this checkbox if you want the system to attach payment reports to vendor pay history records.
The system attaches reports (in PDF format) to payment history records (located in the AP Payment History form) once you post an AP Payment Posting batch. Additionally, the system attaches payment reports to the AP Vendor Payment History Drilldown report.
The system uses the payment reports that you
 specify in the Check Print Report Title by Vendor and EFT Remittance Report Title by Vendor
 fields, which are enabled when you select this checkbox.

## Vendor Pay Attachment Type ID

 Enter the attachment type for attachments that the system is assigning to payment history records. Attachment types allow you to set security based on the type.

## Report Title for Check Print by Vendor

The Report Title for Check Print by Vendor (US) or Report Title for Cheque Print by Vendor (AU/CA) field on the AP Company Parameters form, Payment Reports tab.

Enter the report to use for creating the check/cheque print report that is attached to the payment history record. Press F4 for a list of reports.
United StatesThe AP Check by Vendor report is the only standard report provided. If you do not enter a report name in this field, the system uses this report as the default. If you want to use a custom report you have created, enter the name or press F4 to locate it.
AustraliaThe AP Cheque Print by Vendor - A/NZ report is the only standard report provided. If you do not enter a report name in this field, the system uses this report as the default. If you want to use a custom report you have created, enter the name or press F4 to locate it.
CanadaThe AP Cheque Print by Vendor - Canada report is the only standard report provided. If you do not enter a report name in this field, the system uses this report as the default. If you want to use a custom report you have created, enter the name or press F4 to locate it.

## Report Title for EFT Remittance by Vendor

The Report Title for EFT Remittance by Vendor field on the AP Company Parameters form, Payment Reports tab

Enter the report to use for creating the EFT remittance that is attached to the payment history record. Press F4 for a list of valid standard or custom reports.
United StatesThe AP EFT/ePayments Remittance Vendor report is the only standard report provided. If you do not enter a report name in this field, the system uses this report as the default.
Note: If you are not using ePayments, this report functions as the standard report.

AustraliaThe AP EFT Remittance Vendor - Australia report is the only standard report provided. If you do not enter a report name in this field, the system uses this report as the default.
CanadaThe AP EFT Remittance by Vendor - Canada report (Report ID 1099) is the only standard report provided. If you do not enter a report name in this field, the system uses this report as the default.

## Report Title for Payment Service Remittance by Vendor

Enter the report you want the system to use to
 create the remittance report that is attached to the payment history record. Press
 F4 for a list of reports.
The AP Credit Service Remittance by Vendor report
 (Report ID 1210) is the only standard report provided. If you do not enter a report name
 in this field, the system uses this report as the default. If you want to use a custom
 report you have created, enter the name or press F4 to locate it.

## Secure File Path

The Secure File Path fields on the AP Company Parameters form, Payment Reports tab.

You can optionally specify a secure network location where all AP EFT and ePayments data files are saved upon creation to restrict access to the data files, even to the user prompting its creation.
If you do not select the checkbox and insert a file location, the system prompts the user to select a location for each newly created AP EFT or ePayments data file.
To specify a secure network location:

1. Select the Use Secure File Path checkbox to enable the Secure File Path field.

1. Select Browse to navigate to and select your chosen location.

1. Select OK.

If you enter a valid file location, the system sends EFT and ePayments data files to that location instead of offering the user a Save As dialog box.
To create AP EFT data files, use the AP EFT Download form. For more information, see [AP EFT Download](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-eft-download-form).
To create ePayment data files, use the AP ePayments Export form. For more information, see [AP ePayments Export Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-epayments-export-form).

## Company ID

The Company ID field in the AP Company Parameters form, Payment Services tab (ePayments section).
Required only if you are using ePayments (U.S. only) as a payment method.
Enter the 32-character account number you received from Corpay during enrollment. In combination with your Client ID and Client Secret, this ID number allows Vista to communicate with the Corpay servers which receive your ePayment data files.

## Client ID

The Client ID field on the AP Company Parameters form, Credit Services tab.

Required if using ePayments.
Enter the ePayments client ID that you received from Corpay. This is essentially the username for your API environment.

## Client Secret

The Client Secret field on the AP Company Parameters form, Credit Services tab.

Required if using ePayments.
Enter the ePayments client secret that you received from Corpay. This is essentially the password for your API environment.

## Upload Invoice Attachments to ePayments?

The Upload Invoice Attachments to ePayments? checkbox on the AP Company Parameters form, Credit Services tab.

Only applicable if using ePayments.
Select this checkbox to upload invoice header and line attachments to ePayments. During invoice processing in AP Transaction Entry, if attachments exist for an invoice, the system adds those attachments to a "queue" and then uploads them to Corpay after the batch processing step completes successfully. Then, when you export and upload invoices in AP ePayments Export (accessed via AP Payment Posting), the attachments are linked to the payments on Corpay's website.
Note: You must have also entered your credentials (from Corpay) in the Client ID and Client Secret fields in order upload attachments.

Leave this checkbox unselected if you do not want invoice attachments uploaded to ePayments.

## Credit Service

The Credit Service drop down in the AP Company
 Parameters form, Payment Services tab.
Select the credit service that you want to use:

- 0-None

- 1-Comdata

- 2-EFS

Each selection enables the appropriate fields.

Related information

- [Credit Card Payments](/en/vista/vista/accounting/accounts-payable/payments/credit-card-payments)

## CM Acct #

The CM Acct # field in
 the AP Company Parameters form, Payment Services tab
Enter the default CM account to use when entering payment service information. This account must be different from the account specified in the
 CM Account #
 field on the Subledgers tab.
This account will exclusively track payment
 service transactions, and provides a contra account to credit when you initialize those
 payments to the vendor through the specified credit services vendor (Credit Service
 field).
Note:When changing this field and saving the company
 record, the system displays a message asking if you want to update all open AP
 transactions.

- Click Yes to update all open
 transactions.

- Click No to change the account number without
 updating open transactions.

Note:The system updates only open transactions whose
 Pay Method
 field is set to S-Payment Service.

## Company #

The system enables this field when you select
 2-EFS from the Payment Service drop-down.
Enter your EFS company number.

## Account #

Enabled when you select 2-EFS from the
 Payment
 Service drop-down.
Enter your EFS account number.

## Comdata FTP Settings

These fields apply only if you are using Comdata as your credit service provider.
The URL, Port, and User ID fields
 initially default from the Comdata FTP settings in the VA Site Settings form.
If you want to override the Comdata FTP
 settings in VA Site Settings for this AP company, enter the URL, Port,
 User
 ID, and Password for the SFTP server. These
 values are provided to you by Comdata.
You can override these values per FTP session in the AP FTP form.

Related information

- [Set up Credit Services with Comdata](/en/vista/vista/accounting/accounts-payable/payments/credit-card-payments/set-up-credit-services-with-comdata)

- [AP Company Parameters Form](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form)

- [Comdata FTP Settings](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-000499d4--en)

## Account Code

The system enables this field when you select
 1-Comdata from the Payment Service drop-down.
Enter your Comdata account code.

## Customer ID

The system enables this field when you select
 1-Comdata from the Payment Service drop-down.
Enter your Comdata customer identification number.

## Code Word

Enabled when you select 1-Comdata from
 the Payment
 Service drop-down.
Enter your Comdata code word.

## Location Code

Enabled, but optional when you select
 1-Comdata from the Payment Service drop-down.
Press F4 to look up available AP Invoice Header
 fields that can be mapped into the Comdata Location field within the Comdata PS20 Payment
 Request file. Values (up to 10 characters) from the selected AP Invoice Header field will
 be written into the Comdata file and can be used to provide additional information to
 Comdata with each paid invoice.

## Inv Comments

Enabled, but optional when you select
 1-Comdata from the Payment Service drop-down.
Press F4 to look up available AP Invoice Header
 fields that can be mapped into the Comdata Comments field within the Comdata PS20 Payment
 Request file. Values (up to 60 characters) from the selected AP Invoice Header field will
 be written into the Comdata file and can be used to provide additional information to
 Comdata with each paid invoice.
