---
title: "Field Definitions: AP Recurring Invoices Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/recurring-invoices/ap-recurring-invoice-forms/ap-recurring-invoices-form/field-definitions-ap-recurring-invoices-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/recurring-invoices/ap-recurring-invoice-forms/ap-recurring-invoices-form/field-definitions-ap-recurring-invoices-form"
---

# Field Definitions: AP Recurring Invoices Form

The following is a list of field descriptions for the AP Recurring Invoices form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Vendor

 Enter the vendor (from AP Vendors) to which this recurring invoice applies.

## Invoice

The Invoice field on the AP Recurring Invoices form.
Enter the invoice number, up to 10 characters.
 The system uses this number to create the AP reference number. When you post the invoice, the system combines the invoice number with a sequence number (up to 4 digits) to generate the AP Reference number. For example, if you enter an invoice number of 1100000000, the first invoice you post has an AP Reference number of 1100000000-1.
If the invoice number you enter has less than 10 characters, the system adds trailing spaces. For example, if you enter an invoice number of 11000, your posted invoices has an AP Reference of 11000     -1.

## Description

 Enter the description for this invoice, up to 30 characters. This description becomes the transaction header description when posted.

## Pay Terms

 Specify the payment terms (from HQ Payment Terms) that will be used to calculate discount and due dates when this invoice is posted. May be overridden in AP Transaction Entry once the invoice is added to an expense batch (AP Recurring Invoice Posting).

Related information

- [Intercompany Transactions](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/about-accounts-payable-invoices/intercompany-transactions)

## Hold Code

The Hold Code field in the AP Recurring Invoices form
Entry in this field is not required. However, if entry is made, must be valid.
Specify the hold code (from HQ Hold Codes) for this invoice, if applicable. Hold codes prevent the invoice from being paid until the hold code is released. The hold code entered here is in addition to any hold code automatically placed on the transaction (or any portion of the transaction) because of retainage or a vendor hold.

## Frequency

 Indicate the frequency code (from HQ Frequency Codes) for this invoice. The frequency indicates how often the invoice is posted (such as Monthly, Weekly, Always, etc.), and may be used when selecting invoices to post (AP Recurring Invoice Posting).

## Pay Control

Enter the pay control code for this invoice. This field defaults the
 pay control code from AP Vendors (Pay Control field).
 You can override this setting in AP Transaction Entry once the invoice is added to an expense batch (AP Recurring Invoice Posting).
The pay control code is used to group invoices together for payment. For example, you could code all loan payments with the same control code. Then when initializing the payment batch, you can select all invoices with that pay control code.

## Pay Method

Pay Method drop down on the AP Recurring Invoices form.

Specify the payment method for this invoice. Initially defaults from the Pay Method field in the AP Vendors form (Payment Method tab) for the selected vendor.

- N-ePayments (U.S. only) - If you intend to use this pay method, you're not required to select it here because at the moment you generate the ePayments file, you are given the option to change the pay method originally assigned. For details, see the field help for [Payment Methods](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-epayments-export-form/field-definitions-ap-epayments-export-form#ID-000063380001--en) in the AP ePayments Export form.

- C-Check - If this is a prepaid transaction, you must select this option.

- E-EFT

- S-Credit Service - If you select this option, you must have completed the following:

- In the AP Company Parameters form, Payment Services tab, selected 1-Comdata or EFS from the Credit Service drop-down, entered the CM Acct #, and entered all required information in the applicable section.

- In the AP Company Parameters form, Subledgers tab, entered a CM Co# and CM Acct.

- In the AP Vendors form, Payment Method tab, selected S-Credit Service in the Pay Method field and entered the vendor's email address for receiving remittance information from Comdata in the Payment Service Email field.

## CM Account

This field initially defaults from the CM Account
 field in the AP Vendors form (Info tab). If the CM Account field in the AP Vendors form
 is blank, the system uses the number from the CM Account field in the AP Company
 Parameters form (Subledgers tab).
If you are paying this vendor by credit card,
 this field will default from the CM Acct # field in the AP Company
 Parameters form (Payment Services tab).
You can enter a new account in this field as necessary. You can also override this account number in AP Transaction Entry once you add the invoice to an expense batch in the AP Recurring Invoice Posting form.
Note:If you have specified a credit service CM account in the AP Company Parameters form, and you are paying this vendor with a different method (either check or EFT), the system will display a warning if you enter the credit service CM account. You will be allowed to save the record, however.

## Post Monthly

The Post Monthly checkbox on the AP Recurring Invoices form, header Info tab.
 Select this checkbox if this invoice is to be posted only once a month. If a transaction for this invoice already exists in an expense month, another will not be added for the same month.
 Leave this checkbox unselected if this invoice may be posted more than once a month.

## Monthly Invoice Day

The Monthly Invoice Day field on the AP Recurring Invoice form, header Info tab.
This field is enabled once the Post Monthly checkbox is selected.
Specify the day of the month to use as the Invoice Date. When you post this invoice, the batch month and this day will become the invoice date. If this field is left blank, the Invoice Date entered when generating the batch will be used. May be overridden in AP Transaction Entry once the invoice has been added to an expense batch (AP Recurring Invoice Posting).

## Limit

 A limit for recurring invoices may be set. Each time this invoice is posted, the invoice’s total, plus the total amount invoiced to-date is added and compared to Invoice Limit. If the combined amount exceeds the limit, only the amount up to the limit is posted.
 If you do not want to set a limit, leave this field at its 0.00 default.

## Include in 1099 Totals (United
 States)

The Include in 1099 Totals checkbox on the AP Recurring
 Invoices form, header Info tab.
 This field defaults based on how you set the
 Subject To 1099 Reporting option
 in the AP Vendors.
Select this checkbox to include this invoice’s amounts in the specified vendor’s
 1099 totals.



 Leave this checkbox unselected if not including this invoice's amounts in the specified vendor’s
 1099 totals.


You may override this setting in AP Transaction Entry once you add the invoice
 to an expense batch (AP
 Recurring Invoice Posting).
Click here for the Australian field definition: [Include in Payments Reporting](/en/vista/vista/accounting/accounts-payable/invoices/recurring-invoices/ap-recurring-invoice-forms/ap-recurring-invoices-form/field-definitions-ap-recurring-invoices-form#ID-00051a58--en).
Click here for the Canadian field definition: [Include in T5018 Totals](/en/vista/vista/accounting/accounts-payable/invoices/recurring-invoices/ap-recurring-invoice-forms/ap-recurring-invoices-form/field-definitions-ap-recurring-invoices-form#ID-00051a60--en).

## Include in Payments Reporting (Australia)

Check this box if this invoice's vendor/subcontractor is subject to
 Taxable Payments reporting.
Note: This box is checked by default if the
 vendor/subcontractor is set as subject to Taxable Payments in AP Vendors (you checked the
 Subject to
 taxable payments reporting box, Add'l Info tab).
For more information see [Generating Taxable Payments Annual Reports](/en/vista/vista/accounting/accounts-payable/year-end-reporting/taxable-payment-reporting/generate-taxable-payments-annual-reports-australia).

## Include in T5018 Totals (Canada)

 This field initially defaults based on the
 vendor’s T5018 setup in AP Vendors (T5018 Info fields, Add'l Info tab)
Check this box if this transaction should be included in T5018 totals.
Additional Information
[T5018 Reporting: Canada](/en/vista/vista/accounting/accounts-payable/year-end-reporting/t5018s/about-t5018-reporting-canada)
[Setting Vendors Subject to T5018 Reporting](/en/vista/vista/accounting/accounts-payable/year-end-reporting/t5018s/set-vendors-subject-to-t5018-reporting-canada)

## Type

This field defaults to the 1099 type specified for this vendor (in AP
 Vendors).
If 1099 amounts are to be included when printing 1099s or creating 1099 electronic files (AP 1099 Processing), you must specify a 1099 type of “MISC” (Miscellaneous Income), “INT” (Interest Income), or “DIV” (Dividends/Distributions).
Note:If you are using 1099 types only for informational or reporting purposes, any type is acceptable.

## Box#

 Defaults from the value specified in the Box # field in the AP Vendors.
Accept the default, or press F4 to select
 from a list of valid boxes on the 1099 form that will be used to accumulate and print 1099
 amounts.

## Expire Date

Specify the last date this invoice can be posted. Leave this field blank if no expiration date is to be used.
The expiration date indicates the date after which the recurring invoice is no longer valid for posting. For example, if you set up a recurring invoice for a one-year lease, and you want to ensure that no invoices are processed once the lease is ended, you would assign an expiration date. If you try to post an invoice after the expiration date, the transaction will not be added to the batch.

## Address Seq

 Specify the payment address sequence to use for this transaction. Must be a valid address sequence defined for the vendor in AP Additional Addresses, and must be an address sequence flagged as 'Payment' or 'Both'.

## Invoiced to Date

 Indicate the amount invoiced to date. This field is updated each time an invoice is posted.

## Line

 Enter the existing line number to work on, or enter 'N', 'New', or '+' to add a new line. System will assign the next available line number.

## Type

Specify the line type:

- 1-Job

- 2-Inventory

- 3-Expense

- 4-Equipment

- 5-Work Order

- 6-Purchase Order

- 7-Subcontract

## JC Co#

 Specify the Job Cost company in which job/phase/cost type information for this invoice item will be validated, and to which the job expense will be posted.

## Job

Specify the job to be expensed by this invoice item. If you enter a closed job, the system will display a label in red next to the Line Description field indicating whether it is a hard- or soft-closed job. Additionally, to the left of this field, the system displays the word "Closed" in red.

## Phase

Specify the phase to which this invoice item
 applies.
Note:If the specified job’s Lock Phases option is checked
 (JC Jobs), must be a valid job phase (as set up in JC Job Phases).

## CT

 Specify the Job Cost cost type for this invoice item.

## Material

Optional, unless posting an Inventory type transaction. Not applicable to SL type transactions.
Enter the material to which this invoice item applies.
If this is a Job, Expense, Equipment, or Work Order item, you can enter any material, valid or non-valid. If the material is a valid HQ material, the description, unit of measure, and unit cost will default from HQ Materials. If a non-valid material, description defaults as 'Not in Material File', and UM defaults as LS. Unit cost defaults as 0.00 and is disabled.
If this is an Inventory item, you must enter a valid stocked material (as defined in HQ Materials), and the material must be set up for the specified location in IN Materials. The unit cost will default from IN Location Materials.
If a PO item, material defaults from PO and field is disabled. Material description, UM, and unit cost default from PO item.
Note:If the material is set up for the vendor in PO Vendor Materials, the unit cost will default based on the vendor's setup, regardless of the line type.

## IN Co#

 Specify the Inventory company in which material/location information for this invoice item will be validated, and to which material purchases will be posted.

## Loc

 Specify the Inventory location from which this material was purchased. Location must be set up in IN Location Setup, and material must be assigned to this location in IN Materials.

## EM Co

 Specify the EM company in which equipment information for this invoice item will be validated, and to which the eqipment expense will be posted.

## Comp Type

 Specify the component type (from EM Component Types) for the equipment, if applicable.
 If this is a Work Order line, this field is display only, and will default the component type assigned to the work order item, if applicable.

## Component

 If you entered a component type in the previous field, this field will default the first component of this type for the indicated equipment (as defined in EM Equipment). May be overridden, but must be a valid component for this equipment.
 If this is a Work Order line, this field is display only, and will default the component assigned to this work order, if applicable.

## Equipment

 Specify the equipment (from EM Equipment Master) to which this invoice item applies.
 If this is a work order line, this field is display only, and will default the equipment assigned to the work order item.

## Cost Code

 Specify the cost code (as defined in EM Cost Codes) to which this invoice item applies.
 If this is an Equipment line, and you entered a component for this equipment (previous field), this field defaults the cost code assigned to the component’s type in EM Component Types. May be overridden.
 If this is a Work Order line, this field will default the cost code assigned to the specified work order item (in EM Work Order Edit). Cost code may only be changed if the Allow Cost Code Changes option (for Work Orders) in EM Company Parameters is checked. Otherwise, this field is display only.

## Cost Type

 Specify the equipment cost type (as defined in EM Cost Types) to which this invoice item applies.

## WO

 Enter the work order (as set up in EM Work Orders) to which this invoice item applies.

## WO Item#

 Indicate the work order item to which this invoice item applies. Once you have entered the item number, the Equipment, Component Type and Component (if applicable), and Cost Code assigned to this work order item are displayed to the right of this field. The Equipment, Component Type, and Component cannot be changed.

## PO

 Enter the purchase order (as set up in PO Purchase Order Entry) to which this invoice item applies.

## PO Item#

 Indicate the purchase order item to which this invoice item applies. The fields displayed are based on the type of purchase order it is. Some fields may be grayed out; these cannot be changed.

## SL

 Enter the subcontract (as set up in SL Entry) to which this invoice item applies.

## SL Item

 Enter the subcontract item to which this invoice item applies. The item’s assigned job, phase, and cost type (as set up in SL) and the job/phase/cost type’s U/M (as set up in JC) are displayed. These fields cannot be changed.

## Description

Enter the description of this invoice item, up to 30 characters. Initially defaults the header description, but may change depending on the line type entered.

- Job – If you checked the "Default Header Description to Lines on Job Type" option (AP Company Parameters), the header description will be used as the line description. If you did not check this option, the phase description will default as the line description.

- Inventory – Defaults the material description.

- Expense – Defaults the header description.

- Equipment, Work Order – Defaults the cost code description. If you selected the ‘Default header description to lines on equipment type’ checkbox in AP Company Parameters, this field defaults the value in the header Description field.

- PO & SL – Defaults the PO item description or SL item description, respectively.

If a material is specified for the line, description defaults as follows:

- Job or Expense – Defaults the material description from HQMT (HQ Materials). If an non-valid material, description will default as 'Not in material file'.

- Equipment or Work Order – Defaults the material description from EMEP (Equipment Parts), HQMT (HQ Materials), or POVM (PO Vendor Materials). If a work order may also default from EMWP (Work Order Parts). If the material exists in more than one table, it will use the description from the first table in which the material is located. For example, if the material exists in both Equipment Parts and Vendor Parts, but you select the material from Vendor Parts in the F4 lookup, it will return the description from Equipment Parts because EMEP is checked before POVM.

## GL Co#

 Specify the GL company for this invoice item.

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

Enter a valid unit of measure for this invoice item. Initially defaults as follows:

- If you specified a non-valid material (Job, Exp, Equip, and WO lines only), this field defaults as LS. May be overridden with any valid unit of measure. May be overridden, but must be a valid unit of measure for that material.

- For Job, Inv, and Exp lines, if you specif a valid HQ Material, this field defaults the purchase unit of measure. You may override with any valid unit of measure.
If overrides exist for the specified material/vendor in PO Vendor Materials
 (POVM), this field defaults the vendor material UM if it matches the HQMT Purchase
 UM; otherwise, defaults the lowest UM (in POVM) for the vendor/material
 group/material.
Note: This field defaults from the value entered in the CT field when you select the Default JC Job Phase UM on job lines checkbox in AP Company Parameters.

- For Equipment lines, if the selected material exists in EMEP (Equipment Parts) for the equipment, the UM will default from EMEP if it matches the HQMT Purchase UM; otherwise, default will be the HQMT Purchase UM.
If you selected a vendor material that does not also exist in EMEP, defaults the vendor material UM if it matches the HQMT Purchase UM; otherwise, defaults the lowest UM (in POVM) for the vendor/material group/material.
If material does not exist in EMEP or POVM, defaults the HQMT Purchase UM.

- For Work Order lines, if the selected material exists in EMWP (Work Order Parts) for the work order, UM will default from EMWP, regardless of whether it matches the HQMT Purchase UM.
If you select a material from EMEP (Equipment Parts) that does not also exist in EMWP for the work order, UM will default from EMEP if matches the HQMT Purchase UM; otherwise, default will be the HQMT Purchase UM.
If you select a vendor material that does not also exist in EMWP and/or EMEP for the work order, defaults the vendor material UM if it matches the HQMT Purchase UM; otherwise, defaults the lowest UM (in POVM) for the vendor/material group/material.
If the material does not exist in EMWP, EMEP, or POVM, defaults the HQMT Purchase UM

- For PO and SL lines,this field defaults the unit of measue specified for the PO or SL item. This default cannot be overridden.

-

## Units

 Indicate the number of units for this invoice item.

## UC

Indicate the cost per unit for this invoice item. If you skip this field and enter the Gross amount, the unit cost will be calculated for you.
If a material is specified for this item, this field will default the unit cost based on the line type. If a job, expense, equipment, or work order line, will default from HQ Materials. If an inventory line, will default from IN Location Materials. If the material is set up for the vendor (in PO Vendor Materials), unit cost default will be based on vendor's setup, regardless of line type.
Note:If this is a PO or SL line, and you change the unit cost, you will receive a warning. Changes made will not be updated to related PO/SL files.

## ECM

 Specify which quantity the unit cost represents:
 E = Cost is per each unit.
 C = Cost is per 100 units.
 M = Cost is per 1000 units.

## Gross

The Gross field on the AP Recurring Invoices form, items Info tab.
Specify the total amount for this invoice item, or accept the default. If unit of measure is other than LS (lump sum), changes to the Gross amount will cause the unit cost to be recalculated.

Purchase Order Lines
If you enter an amount and the item's units are 0.00 and the UM is not LS, the system provides a warning, but entry is allowed.
The invoiced amount for each item
 is checked to see if it exceeds the current total cost of the PO item and/or PO. If it
 does, a warning is displayed, but the entry is accepted. However, if the Allow Transactions to
 Exceed Item's Current Total Cost and/or Allow Transactions to Exceed PO's Current Total
 Cost checkboxes are selected in the AP Company Parameters form, you will be unable to
 post the batch until the invoiced amounts are corrected.
The invoiced amount will also be checked to
 see if it exceeds the PO's received amount. If it does, a warning is displayed.
If the
 Allow Invoiced
 to Exceed Received checkbox is selected in the AP Company Parameters form, the entry will
 be allowed. However, if not selected, you will be unable to save the line until the invoiced
 amount is corrected.
Subcontract Lines
The invoiced amount for each item will be checked to see if it exceeds the current total cost of the subcontract item or subcontract. If it does, a warning is displayed. If the Allow Transactions to Exceed Current Total Cost checkbox is selected in the AP Company Parameters form, the amount will be allowed. Another check will be done at the header level once all items have been entered and accepted. If the total of all items exceeds the total remaining amount available on the subcontract, another warning is displayed. Total amount will be allowed if the “Allow transactions…” checkbox is selected. This verification allows for the condition of a deduct item (subcontracts) not invoiced, which could then result in an overpayment.

### Amt

Specify the payable amount for this invoice item, or accept the default. If unit of measure is other than LS (lump sum), changes to this amount will cause the unit cost to be recalculated.
Purchase Order Lines
If you enter an amount and the item's units are 0.00 and the UM is not LS, the system provides a warning, but entry is allowed.
The invoiced amount for each item
 is checked to see if it exceeds the current total cost of the PO item and/or PO. If it
 does, a warning is displayed, but the entry is accepted. However, if the Allow Transactions to
 Exceed Item's Current Total Cost and/or Allow Transactions to Exceed PO's Current Total
 Cost checkboxes are selected in the AP Company Parameters form, you will be unable to
 post the batch until the invoiced amounts are corrected.
The invoiced amount will also be checked to
 see if it exceeds the PO's received amount. If it does, a warning is displayed.
If the
 Allow Invoiced
 to Exceed Received checkbox is selected in the AP Company Parameters form, the entry will
 be allowed. However, if not selected, you will be unable to save the line until the invoiced
 amount is corrected.
Subcontract Lines
The invoiced amount for each item will be checked to see if it exceeds the current total cost of the subcontract item or subcontract. If it does, a warning is displayed. If the Allow Transactions to Exceed Current Total Cost checkbox is selected in the AP Company Parameters form, the amount will be allowed. Another check will be done at the header level once all items have been entered and accepted. If the total of all items exceeds the total remaining amount available on the subcontract, another warning is displayed. Total amount will be allowed if the “Allow transactions…” checkbox is selected. This verification allows for the condition of a deduct item (subcontracts) not invoiced, which could then result in an overpayment.

## Misc Amt

 Use this field to enter freight or other miscellaneous charges.

## Included

 Check this box to have the miscellaneous amount (Misc Amt) included on the invoice.

## Ret%

Specify the percentage at which retainage will be calculated for this item, or accept the default.
Note:Retainage can be entered with any line, but is typically only used with job-related transactions.

## Ret Amt

If a Ret% was entered, this field defaults an amount based on the percentage specified and the invoice line’s gross amount (including tax and freight or miscellaneous).
Note:The retainage portion of tlhe invoice line is automatically placed on hold using the Retainage hold code specified in AP Company Parameters.

## Disc%

 Specify the percentage at which discounts for this invoice item will be calculated, or accept the default. Discount rate initially defaults from the Vendor’s payment terms (specified in invoice header).

## Disc Amt

If a Disc % was entered, this field defaults an amount based on the percentage specified and the invoice line’s gross amount (less retainage, if any). Accept the default, or enter the discount amount. If you change the default amount, the discount percentage is recalculated.
Note:Discounts are not calculated on Tax or Freight/Misc amounts.

## Tax Type

The Tax Type field on the AP Recurring Invoices form, items Info tab.
Specify the tax type for this item.

- 1-Sales – Tax amounts are payable to the vendor and are added to the invoice total. This tax amount is directly charged to Job Cost, Equipment, and GL.

- 2-Use - Tax amounts are accrued, and will be paid at a later date to the appropriate State or Local taxing authority. Calculated tax amounts do not affect the gross or net balance due to the vendor. Instead, the transaction’s gross amount and tax amount is charged to Job Cost, Equipment, and GL account with an offsetting liability account as defined in HQ Tax Codes. Use the AP Tax Report to obtain an itemization of use tax amounts.

- 3-VAT – (Value Added Tax) This tax is paid on goods and services at each stage of production or distribution, and is based on the value added at each stage. This tax is tracked in the GL and reduces the payment to a taxing authority through an Input Tax Credit (ITC). This tax is not directly expensed. This option is the default for Canadian and Australian companies (Default Country field, HQ Company Setup). Use the AP Value Added Tax Report to obtain an itemization of VAT amounts.

## Tax Code

If posting taxes to this item, specify the tax code, or accept the
 default. Default is based on the following:

- Job Lines — The default for this field is determined
 by the setting of the Base Tax On drop-down field
 in JC Jobs. If the field is set to J-Job, the tax code defaults
 from JC Jobs (Tax Code field). If the field
 is set to V-Vendor, the tax code
 defaults from AP Vendors (Tax Code field). If the field
 is set to O-Vendor Override, the tax
 cod defaults from AP Vendors. If a tax code is not specified there, the tax code
 will default from JC Jobs. You can override the default as necessary.

- Inventory Lines — Defaults tax code from IN
 Locations, unless material is not taxable, in which case, defaults as null.

- Exp, Equip, Work Order Lines – Defaults tax code
 from AP Vendors.

- PO Lines – Defaults tax code as defined on the purchase order.

- SL Lines – Defaults tax code as null.

- If a valid, non-taxable material is entered for the line, the tax code will default as null. If a non-valid material is entered, the tax code will default based on the line type.

- If you leave the tax code blank for a job cost line (JC, PO, or SL type), and you post the line with tax, the system relieves committed costs from the phase/cost type in JC Cost Detail table for the tax amount as follows:

- if phase or cost type overrides do not exist for the tax code, the system uses the phase and cost type specified for the PO item.

- if phase and cost type overrides exist for the tax code, the system uses the tax code phase and cost type.

- if a phase override exists for the tax code, but a cost type override does not exist, the system uses the tax code phase and the cost type from the PO line.

- if a cost type override exists for the tax code, but a phase override does not exist, the system uses the phase from the PO line and the tax code cost type.

For Intercompany transactions, if the tax type is Sales or VAT (Value Added Tax), the tax
 code defaults based on the Tax Group assigned to the AP Company. If the tax type is Use, the tax code defaults based on the Tax Group
 assigned to the 'posted to' company.

## Tax Basis

The Tax Basis field on the AP Recurring Invoices form, items Info tab.
Indicates the portion of the gross amount that is taxable. Initially defaults the full gross amount. May be overridden.
Note:Tax amounts posted to subcontract lines will not be included in the invoiced amount updated to SLIT (SL Items). Therefore, if you have set up a subcontract to include sales tax, it is suggested that you post invoices with the tax amount included as part of the gross amount and set this field to 0.00. If the subcontract is set up without tax and sales tax applies, then gross and sales tax amounts should be entered separately on the invoice line.

## Tax Amt

The Tax Amt field on the AP Recurring Invoices form, items Info tab.
Defaults an amount based on the Tax Rate (defined
 for tax code in HQ Tax Codes) and the Tax Basis. May be overridden.
Note: Tax amounts posted to subcontract lines will not be
 included in the invoiced amount updated to SLIT (SL Items). Therefore, if you have set
 up a subcontract to include sales tax, it is suggested that you post invoices with the
 tax amount included as part of the gross amount (i.e. not posted separately here). If
 the subcontract is set up without tax and sales tax applies, then gross and sales tax
 amounts should be entered separately on the invoice line.

## Pay Category

This field displays only if you selected the
 Using
 Payable Category checkbox in AP Company Parameters.
Specify a valid pay category for this line. The pay
 category specified here, along with the line type (Type field), will determine the
 default pay type (next input).
Initially defaults a pay category as follows:

- If you have set up a standard or user pay category override in F3 Properties (not recommended), defaults the F3 pay category.

- If no F3 override exists, defaults the pay category specified for the current user in VA User Profile.

- If no override pay category is specified for the user, defaults the pay category defined in AP Company Parameters.

- If no default pay category is defined for the company, default will be null. (In this case, the pay type will default from AP Company Parameters based on the line's type.)

The default may be overridden if you allow overrides
 to pay type (you selected the Allow Payable Type Override checkbox
 in AP Company Parameters); otherwise, input is disabled.
For Purchase Order lines (line type 6), the pay category and pay type will always default from the PO item, regardless of whether overrides exist in F3, VA User Profile, or AP Company Parameters. This is true even if you turn off the "Using Payable Category" flag in AP Company Parameters after you have already implemented its use. Although the pay category will not be visible, its assignment will remain in effect.

If you did not specify a pay category and pay type for the PO item, the pay category and pay type default based on the standard hierarchy (F3, VA User Profile, AP Company Parameters) and the PO item's line type.

## Pay Type

The Pay Type field in AP Recurring Invoices, Lines section.
Required.
Specify the pay type for this item. If you are using pay categories (flag in AP Company Parameters), defaults the pay from this line's pay category based on the line type. The pay type used for each line type is as follows:

- Job lines - Use the Job pay type

- Inv, Exp, Equip, and EM Work Order lines - Use the Expense pay type

- PO lines - Use the pay type assigned to the PO item.

- SL lines - Use the Subcontract pay type

- SM Work Order lines - Use the SM Work Order pay type

If you allow pay type overrides (flag in AP Company Parameters), you may override the default.
 If you are using pay categories, the pay type must be either assigned to the specified pay category (in AP Pay Category) or an 'unassigned' pay type (a pay type that has not been restricted to a pay category in AP Payable Types). If you are not using pay categories, you can specify any pay type, regardless of whether the pay type is restricted to a pay category.Note: You can only enter a pay type that is not designated for retainage in AP Company Parameters or for a pay category in AP Pay Category.

## Supplier

 Indicate the supplier (from AP Vendors) for
 this item, if applicable. Note that if a supplier is entered here, payment will be made
 with a 2-party check.
