---
title: "Field Definitions: AR Company Parameter Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/about-the-ar-company-parameters-form/field-definitions-ar-company-parameter-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/about-the-ar-company-parameters-form/field-definitions-ar-company-parameter-form"
---

# Field Definitions: AR Company Parameter Form

The following is a list of field descriptions for the AR Company Parameter form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  AR Company

 Enter a valid company number. Companies must first be set up in Headquarters.
 The groups assigned to this company in HQ Company Setup identify which Customer, Material, JC Phase/Cost Type, EM Cost Codes, and Tax files this Accounts Receivable company will use.

##  GL Company

 Enter the GL company that will be updated with all receivables transactions.
 The Accounts Receivable, discount, tax, finance charge, and write-off accounts associated with any AR transaction posted will be updated to this company’s General Ledger. Also, the revenue accounts on non-contract related invoices will update this company’s GL. The account that offsets Cash in Miscellaneous Cash Receipts will update this company’s GL unless redirected to another’s as can be done on a Job Cost or Equipment entry.

##  Receivable Type

 Enter a valid receivable type (set up in AR Receivable Types) to be used as default when entering transactions in AR Invoice Entry, AR Cash Receipts (‘on account’ payments), or AR Finance Charge. Only used as a default if no receivable type is specified for the customer. (Note: Default may be overridden during transaction entry if you check the Allow Override of Receivable Type option below.)
 Receivable types are used to define the General Ledger accounts for Accounts Receivable, non-contract revenue, retainage, discounts, and write-offs. Many companies may have only one receivable type, but it may be used for divisional reporting, or to define another type of receivables other than customer’s receivables, such as employee receivables.

##  Allow Override of Receivable Type

 Check this box to allow overriding the default receivable type (specified above) when entering transactions in AR Invoice Entry), AR Cash Receipts (‘on account’ payments), or AR Finance Charge.
 Leave this box unchecked if you do not allow overrides to the default receivable type. Invoices, ‘on account’ payments, and finance charge transactions will use the receivable type specified for the customer or, if none specified for the customer, the default receivable type specified above. Receivable type inputs will be disabled in related posting forms.

##  Release Retainage to Current A/R

 Check this box to treat released retainage as current receivables. The released retainage transactions will be included in the aged columns on the Aged Analysis reports based on the invoice date or due date assigned to the transaction, and the retainage due column will be reduced accordingly. If you are using a different GL account for AR Retainage, the use of this option will cause the released retainage transaction to credit the Retainage account and debit the Accounts Receivable account.
 Leave this box unchecked if you do not want released retainage aged. Although released retainage invoices will be created, transactions will show in the Retainage column. If you are using a different GL account for AR Retainage, released retainage amounts will remain in the AR Retainage account.

##  Automatically Number Invoices

 Check this box to have the system automatically generate invoice numbers using the Last Invoice Number specified below.
Note: If you are using Material Sales and/or Job Billing, and you elect to use AR invoice numbers for either module, the system will automatically include invoices generated in each of those modules when determining the next invoice number to use for AR invoices.
 Leave this box unchecked if you do not want the system to ‘auto-generate’ invoice numbers. You will need to assign invoice numbers manually.

##  Last Invoice Number

 If using the ‘auto-generate invoice numbers’ feature, this field is updated automatically with the last invoice number used. Before using AR or the other invoicing modules for the first time, enter the number prior to the first invoice number you want the system to use (e.g. if you want to start auto numbering with 100, enter ‘99’ here).
Note: You may use this field to manually reset the invoice number if needed. The system will check invoice numbers so that they are not duplicated.

## Report Overrides: Bal Forward

Bal Forward field in the Report Overrides section of the AR Company Parameters form, Info tab.
Enter an override for the Balance Forward Statement report. Press F4 for a list of reports to use instead of the default Balance Forward Statement report for statement delivery.

Related information

- [Accounts Receivable](/en/vista/vista/accounting/accounts-receivable)

- [About the AR Company Parameters Form](/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/about-the-ar-company-parameters-form)

## Report Overrides: Open Item

Open Item field in the Report Overrides section of the AR Company Parameters form, Info tab.
Enter an override for the Open Item Statement report. Press F4 for a list of reports to use instead of the default Open Item Statement report for statement delivery.

Related information

- [About the AR Company Parameters Form](/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/about-the-ar-company-parameters-form)

- [Accounts Receivable](/en/vista/vista/accounting/accounts-receivable)

##  Discounts

 Specify whether you are using discounts.

- Discounts Not Used – Select this option if you will not be using discounts.

- Allow Discounts on Invoices & Receipts – Select this option to allow discounts to be entered with invoices and/or payments.

- Allow Discounts Taken on Receipts – Select this option to allow discounts to be taken when posting payments in AR Cash Receipts.

## Allow TaxDisc on Invoices & Receipts

Specify whether to allow tax discounts (i.e. whether tax liability will be based on amounts received, rather than amounts billed).
Check this box to allow tax discounts when posting invoices and receipts. If you allow discounts on invoices and receipts and this option is checked, a tax discount will be calculated when entering invoices, based on the line's tax rate and payment discount. For example, a $100 invoice with $5 tax (5%) and a discount of $3 (3%) would have a tax discount of $.15 (5% x $3). If you allow discounts on receipts only, tax discounts will not be calculated during invoice entry, but can be taken when posting cash receipts.
Leave this box unchecked if you do not use tax discounts.

##  Post Taxes: On Invoices

 Check this box to allow posting sales tax when entering invoices (in AR) or progress billings (in JB). If checked, all tax-related inputs will be enabled on the AR Invoice Entry and JB Progress Billing. In addition, enables retainage tax options below.
Note: If you do not allow posting taxes on AR invoices, but do allow posting taxes on progress billings in JB, you will need to check this box. However, you can use the F3 function to hide the tax-related fields on the AR Invoice Entry form and then either set the Tax Code input to a Default Type of ‘2-Fixed Value’ with a Value of ‘blank’ or remove any tax code designations for customers in AR Customers or contracts (those not used in JB).
 Leave this box unchecked if you will not be posting taxes with invoices or progress billings. All tax-related inputs will be disabled in AR Invoice Entry and JB Progress Billing.
Important: Although allowed, it is recommended that you do not change this flag once you begin processing invoices and billings, as it can have a serious impact on this and other modules relative to input defaults and release retainage processing. If changed, a warning displays, but gives you the option to continue. Make sure you only continue with the change if you are sure it is the correct action to take.

## Post Taxes: Calculate Tax on Retainage

This field is enabled only if you selected to
 post taxes on invoices (On Invoices box checked).
Check this box to include retainage in tax calculations on invoices (in AR) and progress billings (in JB). Retainage will be included in the tax basis and the full tax amount updated to the tax payables account (the Credit GL Account specified in HQ Tax Codes, Info tab) when the invoice is posted.
Note: If you do not allow posting taxes on AR invoices, but
 do allow posting taxes on progress billings in JB and want retainage included in tax
 calculations, you will need to check this box. However, you can use the F3 function to hide
 the tax-related fields on the AR Invoice Entry form and then either set the Tax Code field
 to a Default Type of 2-Fixed Value with a Value of ‘blank’ or remove any tax code
 designations for customers in AR Customers or contracts (those not used in JB).
Leave this box unchecked to exclude retainage from tax calculations on invoices and progress billings.
Note: Excluding retainage from tax calculations on invoices
 does not prevent taxes from being calculated on retainage when it is released (in AR
 Release Retainage). When retainage is released, a new invoice is created and the amount
 taxed as applicable. Although allowed, it is recommended that you do not change this flag
 once you begin processing invoices and billings, as it can have a serious impact on this
 and other modules relative to input defaults and release retainage processing. If changed,
 a warning displays, but gives you the option to continue. Make sure you only continue with
 the change if you are sure it is the correct action to take.

## Post Taxes: Distribute Tax to Retainage

This field is enabled only if you selected to
 post taxes on invoices (On Invoices box checked) andyou have
 checked the Calculate Tax on Retainage option.
Check this box to track retainage tax
 separately. Retainage is excluded from the tax basis and calculated separately as
 ‘retainage x tax rate’. The resulting amount is displayed in the Retainage Tax
 field (which displays only when this option is checked). When the invoice is posted, the
 retainage tax amount is updated to the Credit GL Retg Account specified for the tax code
 (HQ Tax Codes, Add’l Opts tab) and is not due for payment until the retainage is released.
 Once retainage is released, the retainage tax is moved to the tax payables account (the
 Credit GL Account specified in HQ Tax Codes, Info tab) and is due for payment.
Note: If you do not allow posting taxes on AR invoices, but
 do allow posting taxes on progress billings in JB and want retainage tax tracked
 separately, you will need to check this box. However, you can use the F3 function to hide
 the tax-related fields on the AR Invoice Entry form and then either set the Tax Code field
 to a Default Type of 2-Fixed Value with a Value of ‘blank’ or remove any tax code
 designations for customers in AR Customers or contracts (those not used in JB).
Leave this box unchecked if you are not tracking retainage tax separately. When entering invoices (in AR) and progress billings (in JB), retainage will be included in the tax basis and the full tax amount updated to the tax payables account (the Credit GL Account specified in HQ Tax Codes, Info tab) when the invoice is posted.
Important: Although allowed, it is recommended that you do not change this flag once you begin processing invoices and billings, as it can have a serious impact on this and other modules relative to input defaults and release retainage processing. If changed, a warning displays, but gives you the option to continue. Make sure you only continue with the change if you are sure it is the correct action to take.
If you check this flag after you have already begun processing invoices and billings, it will affect existing retainage that has not yet been released. When you release retainage, the system will calculate tax on the released portion. Since retainage has already been included in the invoice’s tax calculation, this results in the retainage being taxed twice. To prevent this from happening, consider processing existing retainage transactions before you implement this option. Otherwise, you will need to apply a negative adjustment to each released retainage transaction (in AR Invoice Entry).

##  Post Taxes: On Receipts

 Check this box to allow posting sales tax when entering miscellaneous cash receipts. If checked, all tax-related inputs will be enabled in AR Miscellaneous Receipts.
 Leave this box unchecked if you will not be posting taxes with miscellaneous cash receipts. All tax-related inputs will be disabled in AR Miscellaneous Receipts.

## Audits

The audit options determine when new records of changes are added to the HQ Master Audit (HQMA) database table. For example, if you change a setting on the company parameters form, the system creates a new record of the change in the HQMA table.
You can view records in the HQMA table using the HQ Audit Detail report in the HQ module. See [About Viewing the Master Audit Log](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log) for more information about viewing audit records in the HQMA table.
The following is a detailed list of the audit options.

- Companies – This option is disabled and will always be checked. Any changes made to the AR Company Parameters program will be tracked in the Master Audit file.

- Customers - Check this box to keep an audit trail of changes to the AR Customers table.

- Receivable Types - Check this box to keep an audit trail of changes to AR Receivable Types.

- Transactions - Check this box to keep an audit trail of transaction details. This will track any changes made to transactions within AR posting forms (AR Invoice Entry, AR Cash Receipts, AR Finance Charges, AR Release Retainage).

Note: When setting up a company, the entry of invalid data in certain fields will cause a warning; however, entries will be allowed and you will be able to save the record. This primarily applies to (but is not limited to) required data such as the ‘interface to’ companies and journals, since it is sometimes necessary to set up the company information before you can set up the data being requested.

## GL Invoice Interface

Indicate the level of detail that will be sent to GL when posting invoice entries from AR Invoice Entry, AR Finance Charges, or AR Release Retainage.

- No update — Do not update the General Ledger.

- Summary — Create summary entries for each affected GL account code in a batch. Enter the description that will be used for each of these transactions in the 'Summary Transaction Description in GL' field below.

Also define a detail description by selecting items from the selection box below. Even if you elect to interface at the summary level, if a GL account is set up to interface detail (in GL Chart of Accounts), that account will receive detail entries.

- Transaction — Create GL transactions for each AR transaction in a batch. From the selection box below, select each of the items you want included in the GL transaction description. As you select an item, it is added to the 'Transaction Description in GL' line below. Items may be selected in any order, and the transaction description will appear in the same order in GL. When posting the transactions, the system will extract this data to create the transaction description.

##  GL Invoice Interface: Summary Transaction Description in GL

 Enabled only if the GL Invoice Interface level is ‘Summary’.
 Enter the description that will be used for each invoice transaction posted from AR to GL.

##  GL Invoice Interface: Journal

 Enter the journal that will accumulate any invoice transactions posted from AR to GL. The corresponding description will display to the right of this field.

##  GL Receipt Interface

 Indicate the level of detail that will be sent to GL when posting payment entries from AR Cash Receipts.

- No update — Do not update the General Ledger.

- Summary — Create summary entries for each affected GL account code in a batch. Enter the description that will be used for each of these transactions in the 'Summary Transaction Description in GL' field below.

 Also define a detail description by selecting items from the selection box below. Even if you elect to interface at the summary level, if a GL account is set up to interface detail (in GL Chart of Accounts), that account will receive detail entries.

- Transaction — Create GL transactions for each AR transaction in a batch. From the selection box below, select each of the items you want included in the GL transaction description. As you select an item, it is added to the 'Transaction Description in GL' line below. Items may be selected in any order, and the transaction description will appear in the same order in GL. When posting the transactions, the system will extract this data to create the transaction description.

##  GL Receipt Interface: Summary Transaction Description in GL

 Enabled only if the GL Receipts Interface level is ‘Summary’.
 Enter the description that will be used for each payment transaction posted from AR to GL.

##  GL Receipt Interface: Journal

 Enter the journal that will accumulate any payment transactions posted from AR to GL. The corresponding description will display to the right of this field.

## GL Misc Receipt Interface

Indicate the level of detail that will be sent to GL when posting miscellaneous cash receipts entries from AR Cash Receipts.

- No update — Do not update the General Ledger.

- Summary — Create summary entries for each affected GL account code in a batch. Enter the description that will be used for each of these transactions in the 'Summary Transaction Description in GL' field below.

Also define a detail description by selecting items from the selection box below. Even if you elect to interface at the summary level, if a GL account is set up to interface detail (in GL Chart of Accounts), that account will receive detail entries.

- Transaction — Create GL transactions for each AR transaction in a batch. From the selection box below, select each of the items you want included in the GL transaction description. As you select an item, it is added to the 'Transaction Description in GL' line below. Items may be selected in any order, and the transaction description will appear in the same order in GL. When posting the transactions, the system will extract this data to create the transaction description.

##  GL Misc Receipt Interface: Summary Transaction Description in GL

 Enabled only if the GL Receipts Interface level is ‘Summary’.
 Enter the description that will be used for each miscellaneous cash receipt transaction posted from AR to GL.

##  GL Misc Receipt Interface: Journal

 Enter the GL journal to update when posting miscellaneous cash receipts. A description of the journal displays to the right of this field.

##  CM Company

 Enter the Cash Management company in which cash account detail for this AR company is located. If you elect to update CM when posting cash receipts, this is the CM company that will be updated.
 Additionally, if you have any open Cash Receipts or Miscellaneous Cash Receipts batches, this field is grayed out and no longer accessible.

##  CM Account

 Enter the default Cash Management bank account to which all deposits for this AR company will be made. This account can be overridden when posting payments in AR Cash Receipts.

## CM Interface

Indicate the level of detail that will be sent to CM when posting payments or miscellaneous cash receipts in AR Cash Receipts.

- No Update — Do not update Cash Management with payments or miscellaneous cash receipts posted in AR Cash Receipts. Typically used if not implementing Cash Management or during the AR implementation process when updating payment history prior to going live.

- Summary — Cash Management will be updated with one deposit transaction for each unique deposit number entered in AR Cash Receipts. It is therefore recommended that a unique deposit number be assigned for all checks in one batch that were, or will be, deposited together. A description of deposits to be interfaced to CM may be entered in the Summary Description field below.

##  CM Interface: Summary Transaction Description in CM

 Enter the description to be used for the deposit when interfacing payments and receipts from AR Cash Receipts to Cash Management.

##  JC Co #

 Enter the company that will be used as the default when entering transactions related to Job Cost contracts and/or jobs in AR posting forms. If using multiple Job Cost companies, you will be able to override the company number.

## JC Interface Level

- Transaction Line - Job Cost tables will be updated with billings and receipts at the line level.

- None - No update to Job Cost will occur on AR transactions.

##  EM Co#

 Enter the company that will be used as the default when entering equipment receipts in AR Miscellaneous Receipts. May be overridden during entry.

##  EM Interface Level

- Transaction Line – Equipment Management tables will be updated with receipts at the line level.

- None - No update to Equipment Management will occur on AR transactions.

##  Finance Charge Interface Level

 Indicate whether this company will be using finance/service charges.

- Finance Charge is not used – Finance/service charges are not in use for this company.

- Calculate Finance Charge – Finance/service charges will be used, and will be determined by customer. If finance charges are calculated for a customer, updates to Job Cost will exclude the finance charge portion of the invoice.

##  Finance or Service Charge

 This option determines the terminology to be used in assessing charges for non-payment on invoices and accounts. Regardless of which option you select, however, the system calculates service charges and finance charges in the same manner. (Finance/service charges are calculated and edited in the AR Finance Charge program.)

##  Receivable Type

 Enter the default receivable type to be used when finance/service charges are calculated. May be overridden when posting finance/service charges (in AR Finance Charge) if the customer's finance charge type is R (Rec Type) or, if the customer's finance charge type is A (Account) and the Allow Override of Receivable Type option is checked in AR Company Parameters.
 Receivable type cannot be overridden for customers with finance charge type of I (Invoice), regardless of how the Allow Override of Receivable Type option is set.

## Minimum Balance

If using finance/service charges, enter the minimum balance required for calculating finance/service charges on open invoices. If the invoice balance is less than the balance you specify here, no finance/service charges will be calculated.

##  Minimum Charge

 For 'Account' type finance charges only.
 If using finance/service charges, enter the minimum finance/service charge applied to overdue accounts. This amount will be used for if the amount overdue times the finance/service charge rate is less than the minimum finance/service charge.
Note: Used only for customers with an ‘Account’ Finance Charge Type.

##  Finance Charge %

 If using finance/service charges, enter the default finance/service charge rate for this company.
 If no finance/service charge rate is specified for a customer in AR Customers, the AR Finance Charge program will use the rate specified in this field to calculate finance/service charges.
Note: The rate entered here represents the rate per month. A rate of 2% should be entered as “2”, which will display as 2.00%.

##  Include Previous Finance Charge in Calculation

 Check this box if finance/service charges will be added to overdue invoices and accounts to calculate new finance/service charges.
 Leave this box unchecked if finance/service charges will not be calculated on previous finance charges.

## AR Invoice Discounts

For each AR company you set up, you can define how discounts are handled on invoices and/or receipts.
The discount options in AR Company Parameters determine whether you will use discounts and if so, how they are to be handled.

- Discounts Not Used

- Allow Discounts on Invoices & Receipts

- Allow Discounts Taken on Receipts

If you select to allow discounts on invoices and receipts, the system calculates discounts at the time of invoice entry. Discounts posted for an invoice are considered 'offered' discounts; they are not actually taken until the payment is posted. Although discounts are usually offered for payment received within a specified amount of time, they can be taken regardless of whether payment is received in the specified time frame.
 If you select to allow discounts on receipts, no discount is calculated during invoice entry. You can only post discounts when processing payments.
 The Allow TaxDisc on Invoices & Receipts option determines whether you can take discounts when posting invoices and/or cash receipts. However, you can only use this feature if you allow discounts on invoices and/or receipts. If you allow discounts on invoices and receipts, tax discounts are calculated during invoice entry and then applied when posting cash receipts. Tax discounts are based on the line's tax rate times the discount offered. For example, a $100 invoice with $5 tax (5%) and a discount of $3 (3%) would also have a Tax Disc of $.15 (5% x $3).
 When initializing cash receipts (AR Receipt Initialize), if you check the Apply Discounts option, the system automatically takes the tax discount along with the payment discount, as long as the discount date is within the period specified by the customer's payment terms. If you are entering payments manually, you can apply the tax discount by accessing the invoice line, entering the payment amount in the Amount Applied column, then pressing Ctrl + E to apply the tax discount.

## About Posting Taxes

If you will be posting taxes in Accounts Receivable, you can
 specify whether to calculate taxes on invoices and/or cash receipts.
The Post Taxes section in AR Company Parameters allows you to specify whether to calculate taxes on invoices and/or cash receipts.
 If you elect to post taxes on invoices, additional options are available for including retainage in tax calculations/distributions.

- Calculate Tax on Retainage – If you select this option, the retainage amount is included in the tax basis. When posting an invoice, the full tax amount is updated to the tax payables account and is due for payment. When unchecked, retainage is excluded from tax calculations.

- Distribute Tax to Retainage – With this option, retainage tax is tracked separately and is made payable at the time retainage is released. The tax basis amount for the invoice will exclude retainage tax; retainage tax is calculated separately and displayed in the Retainage Tax field. When the invoice is posted, the retainage tax is updated to the Credit GL Retg Account specified for the tax code (HQ Tax Codes, Add’l Opts tab). Then when retainage is released, the retainage tax is moved to the tax payables account and due for payment.

Selecting to post taxes on receipts allows you to post taxes on miscellaneous cash receipts or ‘on account’ payments (typically posted for ‘balance forward’ customers). If you will be posting taxes on ‘on account’ payments, it is suggested that you also select the Post Taxes on Invoices option. This will ensure the customer’s account balance accurately reflects the tax amount posted to payments on account. If you do not select either option, taxes will not be calculated for AR invoices or cash receipts, regardless of whether the invoice/cash receipt is contract-related and the contract allows the posting of taxes.Note: It is important that you avoid changing these flags once you have set them, as they can seriously affect input defaults and retainage processing in AR and other modules. If you do change a flag, a warning message displays giving you the option to continue or cancel the change.

### Interfacing Taxes

The Interface
 Taxes option in the JC Contracts allows you to specify whether the
 tax amounts will be interfaced to Job Cost. If checked, tax amounts are interfaced
 to the Job Cost item detail. If not checked, tax amounts are not interfaced to Job
 Cost. This may cause AR and JB invoice amounts to be different from Job Cost revenue
 detail and totals.

## Auto Invoice Numbering

For each AR company you set up, you can specify whether to manually assign invoice numbers or have them generated automatically.
The Automatically Number Invoices checkbox (AR Company Parameters, Info tab) determines whether
 invoice numbers will be generated automatically.
 If selected, each time
 you enter an invoice (in AR Invoice Entry), the system will
 automatically assign the next sequential invoice number based on the
 Last Invoice Number (Info tab). If not selected, you must enter invoice numbers manually.


If you are using the Job Billing and/or Material Sales modules and you elect to use
 the AR numbering scheme for invoices created in those modules, the
 system will automatically include all invoices created in AR, JB, and
 MS when determining the next sequential number to use.
