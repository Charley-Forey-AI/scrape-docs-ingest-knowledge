---
title: "Field Definitions: AR Receivable Types Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/about-the-ar-receivable-types-form/field-definitions-ar-receivable-types-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/about-the-ar-receivable-types-form/field-definitions-ar-receivable-types-form"
---

# Field Definitions: AR Receivable Types Form

The following is a list of field descriptions for the AR Receivable Types form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Receivable Type

 Enter a number (0-255) that identifies this receivable type.
 Receivable types define various GL accounts that will automatically be updated when transactions are posted in AR. Many companies need only one receivable type. This will point all transactions to a single current Accounts Receivable account, and optionally a separate account for Accounts Receivable Retainage. However, some companies use additional receivable types to track Employee Receivables, or to easily separate the reporting for divisions, departments, or locations.

##  Description

 Enter a description of the receivable type, up to 30 characters.

##  Abbreviation

 Enter an abbreviated description of the receivable type, up to 5 characters, or accept the system default abbreviation. This may be used on reports where a shorter description is wanted

##  Accts Rec

 Enter the GL asset account (set up in GL Chart of Accounts) to use for current Accounts Receivable.

##  Revenue

 Enter the GL revenue account (set up in GL Chart of Accounts) to use as a default when entering non-contract invoices in AR Invoice Entry.

##  Retainage

 Enter the GL asset account (set up in GL Chart of Accounts) for AR Retainage. This may be the same as, or different from, the one used for current AR.

## Discount

Enter the GL account (set up in GL Chart of Accounts) for discounts taken
 when entering cash receipts in AR Cash Receipts.
Note: If you are using the MS module and will be posting
 cash receipts for MS invoices, this account will only be used for discounts taken when the
 MS invoice specifies a location and no “AR Discount” account has been specified for the
 location in IN Locations.

##  WriteOff

 Enter the default GL account (set up in GL Chart of Accounts) to use when entering Write-off transactions in AR Invoice Entry.

##  FinChg Rev

 Enter the GL account (set up in GL Chart of Accounts) for finance/service charge revenue. This is the account that will be credited when finance/service charges are calculated in the AR Finance Charge program.

##  FinChg Rec

 Enter the GL receivables account (set up in GL Chart of Accounts) for finance/service charges. This is the account that will be debited when finance/service charges are calculated in AR Finance Charge.
 If you are writing off finance/service charges, and this account was debited when the original finance/service charge was calculated, this account will be credited with the write-off amount.

##  FC WriteOff

 Enter the GL account (set up in GL Chart of Accounts) for finance charge write-offs. This is the account that will be debited when finance/service charges are written off in AR Automatic Write-Off.

## Receivable Types Assignment

When you set up your AR companies, the AR Company program
 prompts for a receivables type in two different locations.
When you set up your AR companies, the AR
 Company program prompts for a receivables type in two different locations:

- Info tab - You must enter the default
 Receivable Type that will be used to determine which GL accounts will be affected
 when posting invoices and payments.

- Finance Charges tab – You must enter the
 default Receivable Type that will be used to determine which GL accounts will be
 affected when posting finance charges.

You may also define a default Receivable Type
 when setting up customers (in AR Customers), contracts (JC Contracts), and/or inventory
 locations (in IN Locations or IN Location Category Override).

- AR Customers – Receivable types assigned
 to customers are used when entering AR transactions (e.g. invoices, receipts, finance
 charges, etc.). If no receivable type is assigned to the specified customer, the
 default receivable type defined in AR Company Parameters will be used.

- JC Contracts (JB Info tab) – Receivable
 types assigned to contracts will be used when entering job billings (in Job Billing),
 and will determine the GL accounts updated when the billing is interfaced. If no
 receivable type is assigned to the specified contract, the receivable type assigned
 to the contract’s customer will be used. If no receivable type is assigned to the
 customer, the receivable type assigned in AR Company Parameters is used.

- IN Location Category Override/ IN
 Locations – Receivable types assigned to a location/category or location will be used
 when entering invoices in Material Sales, and will determine the AR account updated
 when materials are sold to customers from the specified location. If no receivable
 type is assigned to the location/category level or the location (respectively), the
 receivable type assigned to the customer is used. If no receivable type is assigned
 to the customer, the receivable type assigned in AR Company Parameters is used.

Note: If you selected the Allow Overrides of Receivable Type
 option (Info tab, AR Company Parameters), any of the default receivable types may be
 overridden during transaction posting.
