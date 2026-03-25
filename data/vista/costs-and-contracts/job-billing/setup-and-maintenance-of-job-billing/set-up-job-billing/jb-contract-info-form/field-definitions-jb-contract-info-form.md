---
title: "Field Definitions: JB Contract Info Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form/field-definitions-jb-contract-info-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form/field-definitions-jb-contract-info-form"
---

# Field Definitions: JB Contract Info Form

The following is a list of field descriptions for the JB
 Contract Info form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Contract

 Specify the contract (from JC Contracts) for which to enter additional
 information. New contracts cannot be entered here. To enter a new contract, use JC
 Contracts.
Note: If you enter a soft- or hard-closed contract, the
 status displays in red to the right of the contract description. Information added for the
 contract will be saved (and updated to JC Contracts, JB Info tab), regardless of whether
 you allow posting to soft- or hard-closed jobs (flags in JC Company Parameters).
For related information, see [JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form).

##  Processing Group

 Specify the processing group (from JB Processing Group) to assign to this contract.
Note: If you add a contract to a processing group (in JB Processing Group), the system updates this field for the contract.
For related information, see [JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form).

##  Customer Reference

 Enter additional information (e.g., customer's PO number), up to 30 characters, to print on the JB invoice. The description entered here will be used as a default for T&M billings (entered manually or by initialization) where a contract is specified and all items on the contract have a bill type of “T&M.”
For related information, see [JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form).

##  Bill on Completion

 Check this box to have this contract billed only upon its completion in progress billing. Typically, this option is only used for small jobs, where a one-time billing occurs after the entire job is completed. However, this option can be checked for contracts that have previous billings. When using checks, the JB Complete Bill form can be run to initialize billings for the contract. The system uses the difference between the previous billed amounts and the contract total to create a new bill for the balance.
 Leave this box unchecked when doing multiple billings on this contract as phases of work are completed.
For related information, see [JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form).

##  Report Retainage at Item Level

 Use this field for Progress Billing only.
 Check this box if retainage will be reported at the item level.
 Leave this box unchecked if retainage will be reported at the contract level.
For related information, see [JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form).

##  Receivable Type

 Enter the default receivable type (from AR Receivable Types) to use when entering billings for this contract. The receivable type determines which GL accounts are updated when a billing is interfaced.
 If a receivable type is not specified, the default is the Receivable Type assigned in AR Customers for the customer specified on the billing. If a receivable type is not specified for the customer, the default is the receivable type from AR Company Parameters.
For related information, see [JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form).

## Misc Dist Code

Specify the default miscellaneous distribution code for this contract. Default will be used as follows:
In AR Miscellaneous
 Distributions:

- From AR Invoice Entry – If a contract is specified for the invoice, defaults the miscellaneous distribution code assigned to the contract. If a miscellaneous code is not specified for the contract, or a contract is not specified for the invoice, the default is the miscellaneous distribution code assigned to the customer in AR Customers. If a code is not assigned there, the default is null.

- From AR Cash Receipts – Defaults a miscellaneous code based on the first invoice line in the batch (i.e. the first invoice that has a payment applied). If the first invoice has a contract specified, the miscellaneous code defaults from that contract. If a miscellaneous code is not specified for the contract, or a contract is not specified for the invoice, the default is from the customer. If a code is not assigned to the customer, defaults as null.

In JB Progress Bill Misc
 Dist:

- From JB Progress Billing – When adding miscellaneous distributions, default is null.

- From JB T&M Bill Edit – When adding miscellaneous distributions manually, defaults as null. When initializing T&M billings with 'Miscellaneous' type sequences and a miscellaneous distribution code for the template sequence is assigned, defaults from the template sequence. If a code is not specified for the template sequence, defaults from the billing's contract. If a miscellaneous code is not specified for the contract, or a contract is not specified for the billing, defaults from the customer. Otherwise, defaults as null.

For related information, see [JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form).

## T&M Template

Specify the T & M Template used by job billing to determine how job
 cost detail accumulates for this contract.
If this is a new contract, and the bill type
 was set to “T&M” or “Both” for this contract in JC Contracts, this field defaults the
 template specified in the "JB T&M Template" field in JB Company Parameters.
If the contract already exists, and this field
 is left blank, this field defaults the template from JB Company Parameters when a change is
 made to the contract in JC Contracts (and the bill type is either “T&M” or “Both”).
For related information, see [JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form).

## T&M Flat Bill Amount

Enter the flat amount to be used on T&M billings for sequences flagged as type “A-Amount” with a Flat Amt Option of “F-Flat Amount.”
This field is typically used for one-time billings, but can be used for any sequence on a template that should be billed this flat amount.
For related information, see [JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form).

## JB T&M Limit Option

- None - Select this option if
 there is no billing limit.

- Contract - Select this option
 if the billing limit will be based on the current contract amount.

- Item - Select this option if
 the billing limit will be based on the current amount for the contract item.

For contract and item limits, the current contract amount is compared against the billed-to-date amount plus the current invoice amount.
For related information, see [JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form).

##  Rounding Option

 This field is for use with Progress Billing only.

- No Rounding - Select this option if rounding should not occur on billings or retainage amounts.

- Round Billing Only - Select this option to have billing amounts rounded to the nearest whole dollar.
Note: Use of this option does not round the bill's "amount due". Only the bill amounts are rounded. If retainage amounts are not rounded, the total "amount due" will reflect the dollars and cents.

- Round Billing and Retainage - Select this option to have billing and retainage amounts rounded to the nearest whole dollar. Retainage will be rounded based on the Report Retainage at Item Level option (above).
If the Report Retainage at Item Level checkbox is selected, retainage is rounded at the item level and the total retainage is updated after all the item amounts have been rounded. If the checkbox is not selected, retainage is rounded at the contract level and the item's retainage is rounded, with the difference between the rounded contract retainage and total items' retainage added to the last item so that total retainage is equal to the retainage total of the items.

For more information about this feature, see [About the Rounding Option for Progress Bills](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/about-the-rounding-option-for-progress-bills).

##  Override Billing Information: Address

 Enter the override billing address for this contract, up to 60 characters. This address will default when entering progress and/or T&M billings and will print on JB invoices for the contract (if not overridden during bill entry).
Note: If you do not enter an address here, billings will use the standard billing address for the customer (defined in AR Customers). The customer’s billing address displays in the Customer Billing Address section above.
For related information, see [JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form).

##  Override Billing Information: City

 Enter the city, up to 30 characters, to use when printing JB invoices for this contract. If left blank, billings default the city specified for the contract’s customer in AR Customers (shown in the Customer Billing Address section above).
For related information, see [JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form).

## Override Billing Information: State

Enter a valid state (as defined in HQ States). The system validates the state based on the Default Country specified in HQ Company Setup for the active company. If not valid, an error displays, but entry is allowed. You must then enter a valid country for this state in the Country field.
The state specified here will print on JB invoices for this contract. If left blank, billings default the state specified for the contract’s customer in AR Customers (shown in the Customer Billing Address section above).
Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.
For related information, see [JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form).

##  Override Billing Information: Zip Code

 Enter the zip code, up to 12 characters, to use when printing JB invoices for this contract. If left blank, billings default the zip code specified for the contract’s customer in AR Customers (shown in the Customer Billing Address section above).
For related information, see [JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form).

##  Override Billing Information: Country

 Enter the 2-character country code. Entry in this field is required when the address exists outside the Default Country specified in HQ Company Parameters for the active company. Country must be valid for the specified state (e.g. state, province, territory, etc.) as defined in HQ States.
Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.
For related information, see [JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form).

##  Override Billing Information: Add'l Address

 Enter an additional override billing address, up to 60 characters, to use when printing JB invoices for this contract. If left blank, billings default the additional address specified for the contract’s customer in AR Customers (shown in the Customer Billing Address section above).
Assign multiple contacts to a single customer
 If you assign multiple contracts to a single customer, you can use this field to enter ‘Attention’ information specific to this contract. The system defaults each address line on a billing separately, so even if you do not enter an override address for the contract, it will default any information entered in this field. This allows you to use the same address for each contract billing, but have the ‘Attention’ information be different.
Note: You may use this address on any custom reports created in Crystal Reports.
For related information, see [JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form).

##  Additional AIA Info: Architect Name

 Specify the architect’s name, up to 30 characters. This name prints in the Architect field in the heading of the AIA reports. This field is optional and is not validated.
For related information, see [JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form).

##  Additional AIA Info: Architect Project

 Specify the architect’s project number, up to 30 characters. This name prints in the Project Nos field in the heading of the AIA reports. This field is optional, and is not validated.
For related information, see [JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form).

##  Additional AIA Info: Contract for Description

 Enter a description of the contract, up to 30 characters. This description will print in the Contract For field in the heading of the AIA reports. This field is optional.
For related information, see [JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form).

##  Additional AIA Info: Start Date

 Enter the starting date for this contract. This date prints in the Contract Date field in the heading of the AIA reports. This field is optional.
For related information, see [JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form).

## Review Level

The Review Level drop-down on the JB Contract Info form.Deb Bryan <deb.bryan@viewpoint.com>
This field is enabled only when the Use Review and Approval Workflow checkbox in the JB Company Parameters form is selected.
This field initially defaults based on the review level selected in the Review Level for AR Interface drop-down in the JB Company Parameters form. You may override the default as needed. Available options are as follows:

- 0 - Any

- 1 - Ready for Review

- 2 - Draft Approved

- 3 - Sent to Customer

- 4 - Approved for Billing

 The option you select here determines the minimum level of the review process that is required to interface billings to Accounts Receivable for this contract. For example, if you select 4 - Approved for Billing, you must select the Approved for Billing checkbox for the selected billing (in either the JB Progress Billing or JB T&M Bill Edit form) before you can interface that bill. If you select any of the other options (0-3) for the billing, that billing will not be available for selection in JB Interface.
Note: The JB Contract Info, JC Contracts, and PM Contracts forms share the same table (bJCCM). Therefore, entry in this field in any of the three forms will automatically update the corresponding field in the other two forms.

## JB Reviewer Group

The JB Reviewer Group field on the JB Contract Info form.
This field is enabled only if you selected the Use Review and Approval Workflow checkbox in the JB Company Parameters form.
Enter the reviewer group for the selected contract. The reviewer group must be set up in the HQ Reviewer Groups form with a Reviewer Group Type of 3-Job Billing.
The reviewer group specified here defaults for each Progress or T&M billing associated with this contract. However, even if you opt to make a selection here, you may override the reviewer group on the billing.
Note: The JB Contract Info, JC Contracts, and PM Contracts forms share the same table (bJCCM). Therefore, entry in this field in any of the three forms will automatically update the corresponding field in the other two forms.

Related concepts

- [JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form)

Related tasks

- [Create Reviewer Groups for Job Billing Invoices](/en/vista/vista/administration/headquarters/reviewer-setup/create-reviewer-groups-for-job-billing-invoices)
