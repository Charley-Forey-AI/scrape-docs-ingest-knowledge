---
title: "Field Definitions: PM Contracts Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/contracts/pm-contracts-form/field-definitions-pm-contracts-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/contracts/pm-contracts-form/field-definitions-pm-contracts-form"
---

# Field Definitions: PM Contracts Form

The following is a list of field descriptions for the PM
 Contracts form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Contract

Enter a contract number, as defined when your system was installed. Up to 10 characters allowed.
Note:If this is a new contract, and the specified contract number exists in the JCHC (JC History by Contract) and JCHJ (JC History by Job) tables (because it was previously deleted), you will receive a message informing you that the number was previously used and cannot be reused until the contract is purged from contract/job history. You will then need to purge the contract/job history (in JC Contract Purge) before you can reuse the number.

[About Project Setup](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)
[Set up a Contract](/en/vista/vista/project-management/projects-and-contracts/contracts/set-up-a-contract)

##  Description

 Enter a description of the contract, up to 60
 characters. If this contract was set up automatically when the project was set up (in PM
 Projects), defaults the project’s description. May be overridden.

##  Department

Each contract must be assigned a department to identify the set of
 default GL accounts (from the JC Departments) to which revenue and related job costs will
 be posted. Departments are assigned at the contract header level, and then default on each
 contract item.
If this contract was set up automatically when
 the project was set up, this field defaults the department specified in PM Projects.
Note: If you change the department, upon saving the record,
 a message displays indicating the change and asking if you want to update any existing
 contract items having the old value to the new value. Select Yes to save the change to the
 header and to all applicable contract items (i.e. those having the same 'old' department).
 Select No to save the change to the header only.

## Customer

Enter the customer of the contract or press
 F4
 to select a customer from a list. This is where invoices for this contract will be posted.
Customers are created and maintained using the
 [
 AR Customers ](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form) form.
If this contract was set up automatically when
 the project was set up, this field defaults the customer specified in PM Projects.
 Customer’s name appears to the right of this field.
Note: Customer must have a status of “Active”. If customer
 has a status of “On Hold”, you will receive a warning, but the system will still accept the
 customer.

## Pay Terms

Enter the default payment terms that should be used when posting to this contract in AR Transaction Entry. If you added a customer to the contract in the Customer field, this field will populate with the payment terms defined on the customer. You can add payment terms to an AR customer using the Payment Terms field on the Additional Information tab of [AR Customers ](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form).
Payment terms are created and maintained using [HQ Payment Terms ](/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form).
Once you enter the payment terms, a description of the terms will appears to the right of the field.

[About Project Setup](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)
[Set up a Contract](/en/vista/vista/project-management/projects-and-contracts/contracts/set-up-a-contract)

## Default Retainage %

Enter the default retainage percent. When contract items are created, by default this will be used as the retainage amount.
If this contract was set up automatically when the project was set up, this field defaults the retainage percent selected in [PM Projects](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form).
Changing the default retainage %
If you change the default retainage percent and click Save (), a message displays. Click Yes to save the change and apply the new retainage percentage to all contract items that previously had the default retainage percent.

[About Project Setup](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)
[Set up a Contract](/en/vista/vista/project-management/projects-and-contracts/contracts/set-up-a-contract)

##  Bill Day

 Specify the day (or days) of the month billings are to be processed for this contract in Job Billing (JB). Up to 10 characters allowed.

## Security Group

This field will only display if you have
 secured the 'bContract' datatype (in VA Secure Tables and Datatypes) and checked the In Use
 flag for the JCCM (Contract Master) table.
Specify the security group for this contract.
 Users assigned to this security group will be allowed access to information about this
 contract. Initially defaults the security group assigned in VA Secure Tables and Datatypes.
Note: It is important to note that in addition to the
 security group specified here, access to information about this contract is automatically
 granted to the Default Security Group you specified in VA Data Security Setup. In addition,
 access may be granted to additional groups in VA Data Security Access.

## Margin %

The Margin % field on the PM Contracts form, Info tab.
Enter the contract revenue margin percentage to use for calculating the
 orginal contract margin in PM Cost Projections and JC Cost Projections.

Related concepts

- [PM Contracts Form](/en/vista/vista/project-management/projects-and-contracts/contracts/pm-contracts-form)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

- [JC Contracts Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)

- [About the JC Cost Projections Form](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)

## Tax Code

Enter the tax code that will be used as the
 default when posting to this contract in Accounts Receivable (AR) or Job Billing (JB).
 Because tax codes are assigned by contract item, this default can be overridden for each
 contract item.
Note: If you change the tax code assigned here, upon saving
 the record, a message displays indicating the change and asking if you want to update any
 existing contract items having the old value to the new value. Select Yes to save the
 change to the header and to all applicable contract items (i.e. those having the same 'old'
 tax code). Select No to save the change to the header only.

## Interface Taxes

Check this box if tax amounts posted to this
 contract will be included in the revenue amounts interfaced to Job Cost.
Leave this box unchecked if tax amounts posted
 to this contract will not be interfaced to Job Cost.

## Default Bill Type

Indicate the default bill type for this
 contract. Each contract item set up for this contract will automatically default the
 designated bill type, which may be overridden.

- Progress - Select this option if you
 want costs billed on a percent complete or units complete basis.

- T & M - Select this option if you
 want costs billed on a Time and Materials basis.

- Both - Select this option if you want to
 be able to bill costs using both the Progress and Time & Materials methods.

- None - Select this option if you are not
 billing costs through Project Billing.

Note: If you change the bill type, upon saving the record,
 a message displays indicating the change and asking if you want to update any existing
 contract items having the old value to the new value. Select Yes to save the change to the
 header and to all applicable contract items (i.e. those having the same 'old' bill type).
 Select No to save the change to the header only.

## Potential Project

This field is only applicable if you have the Pre-Construction Module.
Enter the PC module potential project associated with this contract or press F4 to select one from a list. Potential projects are created and maintained using [PC Potential Projects](/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/potential-project-setup/about-the-pc-potential-projects-form).
If you created this contract using [PC Create PM Project](/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/potential-project-setup/about-the-pc-create-pm-project-form), this field will display the potential project used to create the PM project.
Entering a potential project here populates the Contract and Assigned to Contract fields on the Info tab of [PC Potential Projects](/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/potential-project-setup/about-the-pc-potential-projects-form).

[About Project Setup](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)
[Set up a Contract](/en/vista/vista/project-management/projects-and-contracts/contracts/set-up-a-contract)

##  Set Work Complete Maximum Retention

Select the correct option for setting a
 maximum retention setting for this contract.

- None - Select this option if you do not
 want to set a maximum retention amount for the contract.

- Percent of Contract - Select this option
 if you want to set the maximum retention amount for the contract by percentage. When
 you select this option, the system enables the % of Contract, Include Chg Orders
 in Max Ret %, and the Adjust Maximum Bill fields.

- Maximum Amount - Select this option if
 you want to set a flat amount for maximum retention. When you select this option, the
 system enables the Retainage Amount and Adjust Maximum
 Bill fields.

## Percentage of Contract

The system enables this field when you select
 the Percent of
 Contract option.
Enter the percent of the contract amount that
 is subject to retention.

##  Retainage Amount

The system enables this field when you select Maximum Amount for setting maximum retention amounts.
Enter the maximum retention amount for this contract.

[About Project Setup](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)
[Set up a Contract](/en/vista/vista/project-management/projects-and-contracts/contracts/set-up-a-contract)

##  Include Change Orders in Max Retention %

The system enables this checkbox when you
 select Percent of
 Contract for setting maximum retention amounts.
Check this box if you want to include change
 order amounts in maximum retainage calculations by percent. When you check this box, the
 system calculates the maximum retention amount based on the current contract value. If you
 do not check this box, the system calculates the maximum retention amount based on the
 original contract value.

## Adjust Maximum Bill

There are two options for retention amount
 distribution:

- Composite Percentage - With this option,
 the system takes the final retention amount and calculates an overall percentage rate
 which it applies to all contract items equally.

- Item Percentage from Invoice - With
 this option, the system distributes the final retention amount based on the work
 completed retainage percent value for each line. The system continues to distribute
 in this manner until the retention amount is depleted. The system places any leftover
 amount on one final item on the contract, resulting in a calculated retention
 percentage value for that item only. The system sets the work completed retainage
 percent to zero for all remaining items on the contract.
Example : Composite Percentage
If you have set the maximum retention
 amount for a contract at $10,000, and you have already created invoices with
 retention amounts totaling $8,000, you will only have $2,000 left before you reach
 the maximum retention setting. If you invoice $3,000 retention for two more items (as
 seen in Table 1), the system will calculate a composite retention percentage and
 apply it to each item.
The system uses this calculation to
 determine the composite retention percentage: Maximum retention remaining ($2,000) /
 New Invoice Items Total ($30,000) = Composite Retention Percentage (.066666). The
 system then updates the work completed retention percentage and work completed
 retention amounts based on the composite retention percentage (as seen in Table
 2).
Table 1. Retention Amounts Prior to
 DistributionThis Invoice
Invoice Amount
Retention %
Retention Amount

Item #1
$10,000
10%
$1,000

Item #2
$20,000
10%
$2,000

Table 2. Retention Amounts After
 DistributionThis Invoice
Invoice Amount
Retention %
Retention Amount

Item #1
$10,000
6.67%
$668

Item #2
$20,000
6.66%
$1,332

Example: Item Percentage
 from Invoice
Tables 3 and 4 display how the system
 would distribute the retention amount for a contract with a maximum retention of
 $400. Table 3 shows the retention amounts prior to distribution, while Table 4
 displays the retention amounts after the distribution.
Table 3. Retention Amounts Prior to
 DistributionThis Invoice
Invoice Amount
Retention %
Retention Amount

Item #1
$1,000
10.00%
$100

Item #2
$2,000
10.00%
$200

Item #3
$3,000
10.00%
$300

Item #4
$3,000
10.00%
$300

Table 4. Retention Amounts After
 DistributionThis Invoice
Invoice Amount
Retention %
Retention Amount

Item #1
$1,000
10.00%
$100

Item #2
$2,000
10.00%
$200

Item #3
$3,000
3.33%
$100

Item #4
$3,000
0.00%
$0

## Contract Status

Display only, indicating the status of the contract.
0 = Pending. This status is automatically applied to all new contracts set up here in PM. Status will remain as ‘pending’ until contract is interfaced to Job Cost.
1 = Open. This status is automatically applied to all new contracts set up in JC and to pending projects (set up in PM) that have been interfaced to Job Cost.
2 = Soft-Closed. Posting is restricted, but closing GL entries have not been made. This status is automatically applied when the contract is Soft Closed in the JC Contract Close program.
3 = Final-Closed. This status is automatically applied when the contract is Final Closed in the JC Contract Close program.
Note: You should not use this program to change the status of a contract unless you need to change from Soft Close to Open, or from Final Close to Soft Close. You cannot change a Final Close to an Open status unless you are NOT updating GL (GL Close Interface set to No Update in JC Company Parameters). If you need to Soft or Final Close a contract, use the Contract Close program to ensure that the close is performed accurately.
[About Project Setup](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)
[Set up a Contract](/en/vista/vista/project-management/projects-and-contracts/contracts/set-up-a-contract)

## Contract Start Month

Required.
Enter the starting month for this contract.
 Informational only; used as a default for contract item start months.
Note:If you change the contract's start month,
 you will receive a message asking if you want to update contract items with the old
 month to the new month. Because original estimates follow the contract item start month,
 consider the ramifications before selecting to update contract items.

##  Month Closed

 Indicates the month this contract was closed.
 You can use this field to enter a projected closing month, and when the contract is closed
 in JC Contract Close, the projected month will be replaced by the actual close month.
 Additionally, if using the As of Closed Month
 option (JC Contract Close) to cycle through contracts for closing, the system will use this
 date to determine whether the contract should be added to the close list.

##  Projected Completion Date

The Projected Completion Date field on the PM Contracts form, Info tab.
 Indicate the target completion date for this contract.
 If you specify a new completion date when setting up change orders (in PM Contract Change Orders) for this contract, the system will automatically update this field accordingly.

##  Actual Close Date

 This is a display-only field. Once the
 contract is closed in JC Contract Close, this field defaults the close date specified
 during the close process.

## Days in Contract: Original

Enter the targeted number of
 days the contract will take to complete.
Days in Contract:
 Current
This field displays the
 original days in contract plus any change in days on approved
 change orders.
Note: You can add a change in days to a
 pending change order item using the Change in
 Days field on the Info tab in the lower
 portion of [PM Pending Change Orders
 ](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form). When the item is approved, the change in days amount
 will be added to the current days in contract. 

##  Std Region

 Indicate the location or region of the
 standard item codes (i.e. WA, OR, PDX, Fed.) assigned to each contract item.

##  Use Metric U/M

 This option is for use with Standard Item
 Codes only.
 Check this box if you will be using metric
 units of measure when posting to this contract. When a Std Item Code is assigned to a
 contract item, the metric unit of measure assigned to the Std Item Code (in JC Standard
 Item Codes) will default as the unit of measure for the contract item.
 Leave this box unchecked if you will be using
 standard units of measure.

## Using CM Trust Accounts

Using CM Trust Accounts checkbox on the PM Contracts form, Australia only.
Select this checkbox to indicate eligibility for PBA tracking and reporting. When you apply payments against subcontracts (SL Subcontract Claims), includes those payment amounts when computing results for the CM PBA Reconciliation report.

## General CM Acct

General CM Acct field on the PM Contracts form, Australia only

Required only if the Using CM Trust Accounts checkbox is selected.

Your selection in this field identifies the primary Cash Management account used to track principle contract and subcontract claim payments and receipts (GST inclusive) under this contract.

Press F4 to select from a list of CM Accounts assigned as PBA type General.

## Disputed CM Acct

Disputed CM Acct field on the PM Contracts form, Australia only
Your (optional) selection in this field identifies the Cash Management account used to track any disputed subcontract claim amounts related to this contract.

Press F4 to select from a list of CM Accounts assigned as PBA type Disputed.

## Retention CM Acct

Retention CM Acct field on the PM Contracts form, Australia only
Required only if the Using CM Trust Accounts checkbox is selected.

Your selection in this field identifies the Cash Management account used to track held retention (GST inclusive) for all qualifying subcontracts linked to jobs within this contract.

Press F4 to select from a list of CM Accounts assigned as PBA type Retention.

## Qualification Date

Qualification Date field on the PM Contracts form, Australia only
Required only if the Using CM Trust Accounts checkbox is selected.
Enter the date when the contract qualified as subject to PBA tracking and reporting (not necessarily the contract start date).

## CMCo

CMCo field on the PM Contracts form, Australia only
Required only if the Using CM Trust Accounts checkbox is selected.

Enter the Cash Management company associated with this contract’s PBAs. Press F4 to select from a list.

##  Processing Group

 Specify the processing group (from JB
 Processing Group) to assign to this contract.
Note: Information entered here will update JB Contract
 Info. Likewise, information entered in JB Contract Info will be updated here.
 If you add a contract to a processing group
 (in JB Processing Group), it will update this field for the contract.

## Customer Reference

Enter additional information (e.g. customer's
 PO number), up to 30 characters, that you want to print on the JB invoice. The description
 entered here will be used as a default for T&M billings only (entered manually or by
 initialization) where a contract is specified and all items on the contract have a bill
 type of 'T&M'.
Note: Information entered here will update JB Contract
 Info.

## Bill on Completion

Check this box if you want this contract
 billed only upon its completion in progress billing. Typically, this option is only used
 for small jobs, where a one-time billing occurs after the entire job is completed. However,
 this option can be checked for contracts that have previous billings. When checked, the JB
 Complete Bill program can be run to initialize billings for the contract. The system will
 use the difference between the previous billed amounts and the contract total to create a
 new bill for the balance.
Leave this box unchecked if you do not want to
 bill this contract upon its completion only (i.e. you will be doing multiple billings on
 this contract as phases of work are completed).
Note: Information entered here will update JB Contract
 Info.

## Report Retainage at Item Level

For Progress Billing only.
Check this box if retainage will be reported
 at the item level.
Leave this box unchecked if retainage will be
 reported at the contract level.
Note: Information entered here will update JB Contract
 Info.

## JB Reviewer Group

The JB Reviewer Group field on the PM Contracts form, JB Info
 tab
This field is enabled only if you selected the Use Review and Approval Workflow checkbox in the JB Company Parameters form.
Enter the reviewer group for the selected contract. The reviewer group must be set up in the HQ Reviewer Groups form with a Reviewer Group Type of 3-Job Billing.
The reviewer group specified here defaults for each Progress or T&M billing associated with this contract. However, even if you opt to make a selection here, you may override the reviewer group on the billing.
Note: The JB Contract Info, JC Contracts, and PM Contracts forms share the same table (bJCCM). Therefore, entry in this field in any of the three forms will automatically update the corresponding field in the other two forms.

Related tasks

- [Create Reviewer Groups for Job Billing Invoices](/en/vista/vista/administration/headquarters/reviewer-setup/create-reviewer-groups-for-job-billing-invoices)

## Receivable Type

Enter the receivable type (from AR Receivable
 Types) to use as a default when entering billings for this contract. The receivable type
 specified here determines the GL accounts updated when interfacing a billing, and overrides
 the receivable type specified for the customer (in AR Customers) or company (in AR Company
 Parameters).
If no receivable type is specified here,
 default will be the Receivable Type assigned to the customer specified on the billing. If
 no receivable type specified for the customer, defaults the receivable type specified for
 the AR company.
Note: Information entered here will update JB Contract
 Info.

## Misc Dist Code

Specify the default miscellaneous distribution
 code for this contract. Default will be used as follows:
In AR Miscellaneous Distributions:

- From AR Invoice Entry – If a contract is
 specified for the invoice, defaults the miscellaneous distribution code assigned to
 the contract. If no miscellaneous code is specified for the contract, or no contract
 is specified for the invoice, defaults the miscellaneous distribution code assigned
 to the customer in AR Customers. If no code assigned there, default will be null.


- From AR Cash Receipts – Defaults a
 miscellaneous code based on the first invoice line in the batch (i.e. the first
 invoice to which payment has been applied). If the first invoice has a contract
 specified, the miscellaneous code defaults from that contract. If no miscellaneous
 code is specified for the contract, or no contract specified for the invoice,
 defaults from the customer. If no code assigned to the customer, defaults as null.
In JB Progress Bill Misc Dist:

- From JB Progress Billing – When adding
 miscellaneous distributions, default will be null.

- From JB T&M Bill Edit – When adding
 miscellaneous distributions manually, defaults as null. When initializing T&M
 billings with 'Miscellaneous' type sequences, if you have specified a miscellaneous
 distribution code for the template sequence, defaults from the template sequence. If
 no code is specified for the template sequence, defaults from the billing's contract.
 If no miscellaneous code specified for the contract, or no contract specified for the
 billing, defaults from the customer. Otherwise, defaults as null.

Note: Information entered here will update JB Contract
 Info.

## T&M Template

Specify the T&M Template that will be used
 by job billing to determine how to accumulate job cost detail for this contract.
If this is a new contract, and the bill type
 is set to 'T&M' or 'Both' (Info tab), this field will default the template specified in
 the "JB T&M Template" field in JB Company Parameters.
Note: Information entered here will update JB Contract
 Info.

## T&M Flat Bill Amount

Enter the flat amount to be used on T&M
 billings for sequences flagged as Type A (Amount) with a Flat Amt Option of F (Flat
 Amount). This option is typically used for one-time billings, but can be used for any
 sequence on a template that should be billed this flat amount.
Note: Information entered here will update JB Contract
 Info.

## JB T&M Limit Option

Specify the basis for billing limits.

- None- Select this option if there is no
 billing limit.

- Contract- Select this option if the
 billing limit will be based on the current contract amount.

- Item- Select this option if the billing
 limit will be based on the current amount for the contract item.

For contract and item limits, the current
 contract amount is compared against the billed-to-date amount plus the current invoice
 amount.
Note: Information entered here will update JB Contract
 Info.

## Rounding Option

This feature is for use with Progress Billing only.

- No Rounding - Select this option if no rounding will occur on billings or retainage amounts.

- Round Billing Only - Select this option to have billing amounts rounded to the nearest whole dollar.

Note:Use of this option does not round the bill’s “amount due”. Only the bill amounts are rounded. If retainage amounts are not rounded, the total “amount due” will reflect the dollars and cents.

- Round Billing and Retainage - Select this option to have billing and retainage amounts rounded to the nearest whole dollar. Retainage will be rounded based on the Report Retainage at Item Level option (above).

If the Report Retainage at Item Level option is checked, retainage is rounded at the item level, and the total retainage is updated after all the item amounts have been rounded. If not checked, retainage is rounded at the contract level, and the item’s retainage is rounded, with the difference between the rounded contract retainage and total items’ retainage added to the last item so that total retainage is equal to the retainage total of the items.
Note:Information entered here will update JB Contract Info.

[About Project Setup](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)[Set up a Contract](/en/vista/vista/project-management/projects-and-contracts/contracts/set-up-a-contract)

## Override Billing Information: Address

Enter the override billing address for this contract, up to 60 characters. This address will be used as the billing address when printing JB invoices for this contract. If no address is entered here, billings will default the address specified for the contract’s customer (in AR Customers).
Note: Information entered here will update JB Contract
 Info.

## Override Billing Information: City

Enter the city, up to 30 characters, to use
 when printing JB invoices for this contract. If left blank, billings will default the city
 specified for the contract’s customer (in AR Customers).
Note: Information entered here will update JB Contract
 Info.

## Override Billing Information: State

Enter a valid state (as defined in HQ States)
 to use when printing JB invoices for this contract. If left blank, billings will default
 the state specified for the contract’s customer (in AR Customers).
The system validates the state based on the
 Default Country specified in HQ Company Parameters for the active company. If not valid, an
 error displays, but entry is allowed. You must then enter a valid country for this state in
 the Country field.
Information entered in this field updates JB
 Contract Info.

## Override Billing Information: Zip

Enter the zip code, up to 12 characters, to
 use when printing JB invoices for this contract. If left blank, billings will default the
 zip code specified for the contract’s customer (in AR Customers).
Note: Information entered here will update JB Contract
 Info.

## Override Billing Information: Country

Enter the 2-character country code. If left
 blank, billing will default the country specified for the contract’s customer (in AR
 Customers).
Entry in this field is required when the
 address exists outside the Default Country specified in HQ Company Setup for the active
 company. Country must be valid for the specified state (e.g. state, province, territory,
 etc.) as defined in HQ States.

## Override Billing Information: Add'l Address

Enter an additional override billing address
 for this contract, up to 60 characters. For example, if the billing address is a Post
 Office box, then you might enter the P.O. Box in the Address field above, and use this
 field to enter the street address. The address entered here will default on progress and
 T&M billings, and if not deleted or overridden on the billing, will print on certain
 reports. May also be used on any reports that you create in Crystal Reports.
Note: Information entered here will update JB Contract
 Info.

## Additional AIA Info: Architect Name

Specify the architect’s name, up to 30
 characters. This name will print in the Architect field in the heading of the AIA report.
 This field is optional and is not validated.
Note: Information entered here will update JB Contract
 Info.

## Additional AIA Info: Architect Project

Specify the architect’s project number, up to
 30 characters. This name will print in the Project Nos field in the heading of the AIA
 report. This field is optional and is not validated.
Note: Information entered here will update JB Contract
 Info.

## Additional AIA Info: Contract for Desc

Enter a description of the contract, up to 30
 characters. This description will print in the Contract For field in the heading of the AIA
 report. This field is optional and is not validated.
Note: Information entered here will update JB Contract
 Info.

## Additional AIA Info: Start Date

Enter the starting date for this contract.
 This date prints in the Contract Date field in the heading of the AIA report. This field is
 optional.
Note: Information entered here will update JB Contract
 Info.

## Review Level

The Review Level drop-down on the PM Contracts form, JB Info
 tab.
This field is enabled only when the Use Review and Approval Workflow checkbox in the JB Company Parameters form is selected.
This field initially defaults based on the review level selected in the Review Level for AR Interface drop-down in the JB Company Parameters form. You may override the default as needed. Available options are as follows:

- 0 - Any

- 1 - Ready for Review

- 2 - Draft Approved

- 3 - Sent to Customer

- 4 - Approved for Billing

 The option you select here determines the minimum level of the review process that is required to interface billings to Accounts Receivable for this contract. For example, if you select 4 - Approved for Billing, you must select the Approved for Billing checkbox for the selected billing (in either the JB Progress Billing or JB T&M Bill Edit form) before you can interface that bill. If you select any of the other options (0-3) for the billing, that billing will not be available for selection in JB Interface.
Note: The JB Contract Info, JC Contracts, and PM Contracts forms share the same table (bJCCM). Therefore, entry in this field in any of the three forms will automatically update the corresponding field in the other two forms.

Related concepts

- [PM Contracts Form](/en/vista/vista/project-management/projects-and-contracts/contracts/pm-contracts-form)

- [JB Company Parameters Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-company-parameters-form)

- [JB Progress Billing Form](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/jb-progress-billing-form)

- [JB T&M Bill Edit Form](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-edit-form)

## JB Bill Notes

Use this window to enter any miscellaneous notes about this contract. The space allowance is virtually unlimited. Notes entered here are available for printing on JB invoices.
Spelling Check
 Click the Spelling icon on the toolbar or selectTools > Spelling to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field, right click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard note to copy (or select from F4 lookup) and click OK. The system inserts the selected note into the field.

## Period

If you initialized this forecast (in JC
 Forecast Initialize), this field defaults a set of forecast periods based on the Contract Start
 Month and Projected Completion Date specified for
 this contract (Info tab). If no projected completion date is specified, forecast periods
 will be determined by the Contract Start Month and the 'number of
 months past current month' specified during initialization.
If you did not initialize a forecast, enter a
 period to which this forecast applies.

## Revenue %

The percent specified here represents the percent of revenue complete expected for the selected period.
If you initialized this forecast, this field defaults the revenue forecast percent for the selected period. Percentage is calculated as follows:

- If the forecast method is 'Linear', monthly percentages will be equally distributed based on the number of months in the forecast. For example, if 12-month contract, first month will be 8.3% (100% / 12 = 8.33%), the second month will be 16.66%, the third month, 24.99%, and so forth.

- If the forecast method is 'Curve', monthly percentages will be based on number of forecast months, number of forecast intervals, and the interval percentages.

See [Forecast Options](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/revenuecost-forecast-options) for more information about how monthly percentages are calculated with the Curve method.
If you did not initialize a forecast for this contract, enter the revenue percent that applies to the selected period.

## Revenue Amount

This field automatically defaults an amount
 based on the Revenue % x Current Contract. This amount represents the revenue complete
 amount expected for the selected period.
Note: If you change this amount, the revenue percent will
 be recalculated for the period.

## Cost %

The percent specified here represents the
 percent of cost complete expected for the selected period.
If you initialized this forecast, this field
 defaults the cost forecast percent for the selected period. Percentage is calculated as
 follows:

- If the forecast method is 'Linear',
 monthly percentages will be equally distributed based on the number of months in the
 forecast. For example, if 12-month contract, first month will be .70% (100% / 12 =
 .70), the second month will be 1.40%, the third month, 2.10, and so forth.

- If the forecast method is 'Curve',
 monthly percentages will be based on number of forecast months, number of forecast
 intervals, and the interval percentages.

See [Forecast Options](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/revenuecost-forecast-options) for more information about how monthly
 percentages are calculated with the Curve method.
If you did not initialize a forecast for this
 contract, enter the cost percent that applies to the selected period.

## Cost Amount

This field automatically defaults an amount based on the Cost % x Current Estimate. This amount represents the cost complete amount expected for the selected period.
Note: If you change this amount, the cost percent will be
 recalculated for the period.

## Notes

Enter any notes that apply to this forecast/period. For additional space, double-click on this field. The Grid Notes window displays, allowing virtually unlimited space for your notes and information.
Spelling Check
 Click the Spelling icon on the toolbar or select Tools >  Spelling  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field, right click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard note to copy (or select from F4 lookup) and click OK. The system inserts the selected note into the field.

[About Project Setup](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)
[Set up a Contract](/en/vista/vista/project-management/projects-and-contracts/contracts/set-up-a-contract)
