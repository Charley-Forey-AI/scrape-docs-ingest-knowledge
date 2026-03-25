---
title: "Field Definitions: JC Contracts Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form/field-definitions-jc-contracts-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form/field-definitions-jc-contracts-form"
---

# Field Definitions: JC Contracts Form

The following is a list of field descriptions for the JC
 Contracts form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Contract

The Contract field on the JC Contracts form.
 Enter the code, up to 10 characters (including dashes), that identifies this contract.
The length and format of your contract code was defined when your system was installed by Viewpoint. Once established, the format should not be changed.
Note: If this is a new contract, and the specified contract number exists in the JCHC (JC History by Contract) and JCHJ (JC History by Job) tables (because it was previously deleted), you will receive a message informing you that the number was previously used and cannot be reused until the contract is purged from contract/job history. You will then need to purge the contract/job history (in JC Contract Purge) before you can reuse the number. 

## Description

Enter a description of the contract.
 If the contract was set up automatically when
 the job was created using the [JC
 Jobs ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form) form, this field defaults with the job description.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Department

Enter a department or press F4 to select one from a list. The
 department selected in this field will default on contract items.
Departments are created and maintained using
 the [JC Departments ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-departments-form) form, and they define which GL accounts will be used when
 posting contract revenue and job costs.
Important: If you change the department assigned in the
 contract header, a message gives you the option of assigning existing contract items the
 new department. If you change the department on contract items after contract revenue or
 job costs has been posted, the system WILL NOT transfer previously posted amounts into the
 GL accounts of the new department. You must manually make those GL adjustments.
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Customer

Enter an AR customer number or press F4 to select one from a list. This is the
 customer that will be billed from the contract.
Customers are created and maintained using the [ AR Customers ](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form) form.
You can select a customer that is on hold, but
 a message will display. [More](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form/field-definitions-ar-customers-form#ID-00008307--en)
Note: When the contract is billed in the JB or AR module,
 the customer on a contract can be changed if necessary.
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Pay Terms

 Enter the payment terms or press F4 to select them from a list. The
 payment terms selected in this field will be used as the default when entering invoices in
 AR or billings in JB that reference the contract.
Payment terms are created and maintained using
 the [ HQ Payment Terms ](/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form) form. You can open this form by pressing
 F5
 in this field.
If you selected a customer in the Customer field,
 this field will default the payment terms set up on the customer (Payment Terms
 field in the AR Customers form, Add'l Info tab).

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Default Retainage %

Use this field to enter the retainage percent that will be used as the
 default when posting transactions in Accounts Receivable (AR) and Job Billing (JB). Default
 may be overridden for each contract item.
Note: If you change the retainage percent assigned in the contract header, upon saving the record, a message displays indicating the change and asking if you want to update any existing contract items having the old value to the new value. Select Yes to save the change to the header and to all applicable contract items (i.e. those having the same 'old' retainage percent). Select No to save the change to the header only.
This field will also be used to set the default retainage amount when creating contract items using the Items tab. The retainage set up on the Items tab will then be used to set the default retainage on subcontract items created in the PM and SL modules.
The diagram below outlines how the system determines the default retainage % for subcontract items.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Bill Day

Enter the day (or days) of the month billings that the contract should be
 processed in the Job Billing module.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

##  Security Grp

 This field will only display if you have secured the 'bContract' datatype
 (in VA Data Security Setup) and checked the In Use flag for JCCM (Contract Master).
 Specify the security group for this contract. Users assigned to this security group will be allowed access to information about this contract. Initially defaults the security group assigned in VA Data Security Setup.
Note: It is important to note that in addition to the security group specified here, access to information about this contract is automatically granted to the Default Security Group you specified in VA Data Security Setup. In addition, access may be granted to additional groups in VA Data Security Access.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Margin Percentage

Margin
 % field on the Info tab of the JC Contracts form.
Enter the contract revenue margin percentage to be used to calculate the original contract margin in the [JC Cost Projections](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form) and [PM Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form) forms.

Related information

- [JC Contracts Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)

- [About the JC Cost Projections Form](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)

- [PM Contracts Form](/en/vista/vista/project-management/projects-and-contracts/contracts/pm-contracts-form)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

## Tax Code

Enter a tax code or press F4 to select one from a list. This will
 be used as the default tax code when creating new contract items on the Items tab.
Tax codes are created and maintained using the [HQ Tax Codes ](/en/vista/vista/administration/headquarters/tax-code-setup/about-the-hq-tax-codes-form) form.
Important: If you change the tax code in this field, the
 system allows you to update any existing contract items with the new tax code.
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Interface Taxes

Select this checkbox if tax amounts for this contract entered in the PM module should be included in the revenue amounts when they are interfaced to the Job Cost, Job Billing and Accounts Receivable modules using the [PM Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form) form.
 Leave this box unchecked if tax amounts entered in PM should not be interfaced to the Job Cost module.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Default Bill Type

 Indicate the default bill type for this contract. Each contract item set
 up for this contract will automatically default the designated bill type, which may be
 overridden.

- Progress - Select this option to bill costs on a percent complete or units complete basis.

- T & M - Select this option to bill costs on a Time and Materials basis.

- Both - Select this option to bill costs on a Time & Materials basis with a Progress backup. Contract items with a bill type of both can only be initialized to T&M billings; however, once the T&M billing is generated, the system produces a progress billing with the same dollars.

- None - Select this option if you are not billing costs through Job Billing.

Note: If you change the bill type assigned in the contract header, upon saving the record, a message displays indicating the change and asking if you want to update any existing contract items having the old value to the new value. Select Yes to save the change to the header and to all applicable contract items (i.e. those having the same 'old' bill type). Select No to save the change to the header only.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Contract Status

The Contract Status drop-down in the JC Contracts form, Info tab.
Use this field to set the status of the contract.

- Pending - This status is automatically applied to all new contracts set up in PM Contracts and is changed to 1 (Open) when interfaced.

- Open - This status is automatically applied to all new contracts that are set up in JC Contracts.

- Soft Closed - Posting is restricted, but closing GL entries have not been made. This status is automatically applied when the contract is Soft-Closed in the JC Contract Close form.

- Hard Closed - This status is automatically applied when the contract is Final Closed in the JC Contract Close form.

Note: If you allow posting to soft-closed jobs (flag in JC Company Parameters), you can change the status of a contract from Open to Soft Closed in this form; however, you will need to use JC Contract Close to change the status from Open or Soft Closed to Hard Closed. If you do not allow posting to soft-closed jobs, you cannot change the status from Open to Soft Close or Hard Close in this form; you will need to use JC Contract Close.
 You can also use this form to change the status from Soft Closed to Open. If the GL Close Interface level is set to 'Summary' or 'Detail' and there is existing cost detail (in JCJP or JCCD) or revenue detail (in JCID) for the contract, you cannot change the status from Hard Closed to anything less. If no cost or revenue detail exists, changing the status from Hard Closed to Soft Closed or Open is allowed.

## Contract Start Month

Enter the starting month of the contract. This field is used as a default
 for the start month of contract items.
Note: If you change this field, the system allows you to update the existing contract items.
Note: Original estimates follow the contract item start month, so you should consider the ramifications before using this feature.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Month Closed

Indicates the month this contract was closed. You can use this field to
 enter a projected closing month, and when the contract is closed in JC Contract Close, the
 projected month will be replaced by the actual close month.
Note: The contract’s actual close date is displayed below.
Additionally, if using the ‘As of Closed Month’ option (JC Contract Close) to cycle through contracts for closing, the system will use this date to determine whether the contract should be added to the close list.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

##  Projected Completion Date

 Indicate the target completion date for this contract.
 If you specify a new completion date when setting up change orders for this contract, the system will automatically update this field accordingly.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

##  Actual Close Date

 This is a display-only field. Once the contract is closed in JC Contract
 Close, this field defaults the close date specified during the close process.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Days in Contract: Original

Enter the targeted number of days the contract will take to complete. This
 field requires a value and cannot be blank.
Note: The Days in Contract: Current display field shows the sum of the original contract days and additional days from change orders. This number is automatically revised by any number you designate in the Change In Days field in JC Change Orders for this contract.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Standard Region

Enter a standard region or press F4 to select one from a list. This is the
 location or region of the standard item codes that will be applied to the contract items
 using the Standard
 Item Code field on the Items tab.
Click [here](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-standard-item-codes-form) for more information on standard region and item codes.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

##  Use Metric U/M

 Check this box if you will be using metric units of measure when posting
 to this contract. All items will automatically default to using metric units of measure.
 Leave this box unchecked if you will be using standard units of measure.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Using CM Trust Accounts

Using CM Trust Accounts checkbox on the JC Contracts form, CM
 Trust Account section. Australia only.
Select this checkbox to indicate eligibility for PBA tracking and reporting.
 When you apply payments against subcontracts (SL Subcontract Claims), Vista includes those payment amounts when computing results for the CM
 PBA Reconciliation report.

## Qualification Date

Qualification Date field on the JC Contracts form, CM Trust
 Account section. Australia only.
Required only if the Using CM Trust Accounts checkbox is selected.

Enter the date when the contract qualified as subject to PBA tracking and reporting (not necessarily the contract start date).

## CMCo

CMCo field on the JC Contracts form, CM Trust Accounts
 section. Australia only.
Required only if the Using CM Trust Accounts checkbox is selected.
Enter the Cash Management company associated with this contract’s PBAs. Press F4 to select from a list.

## General CM Acct

General CM Acct field on the JC Contracts form, CM Trust
 Accounts section. Australia only.
Required only if the Using CM Trust Accounts checkbox is selected.

Your selection in this field identifies the primary Cash Management account used to track principle contract and subcontract claim payments and receipts (GST inclusive) under this contract.

Press F4 to select from a list of CM Accounts assigned as PBA type General.

## Retention CM Acct

Retention CM Acct field on the JC Contracts form, Australia
 only.
Required only if the Using CM Trust Accounts checkbox is selected.

Your selection in this field identifies the Cash Management account used to track held retention (GST inclusive) for all qualifying subcontracts linked to jobs within this contract.

Press F4 to select from a list of CM Accounts assigned as PBA type Retention.

## Disputed CM Acct

Disputed CM Acct field on the JC Contracts form, CM Trust
 Accounts section. Australia only.
Your (optional) selection in this field identifies the Cash Management account used to track any disputed subcontract claim amounts related to this contract.
Press F4 to select from a list of CM Accounts assigned as PBA type Disputed.

## Set Work Complete Maximum Retention

Select the correct option for setting a maximum retention setting for this
 contract.

- None - Select this option if you do not want to set a maximum retention amount for the contract.

- Percent of Contract - Select this option if you want
 to set the maximum retention amount for the contract by percentage. When you select
 this option, the system enables the % of Contract,  Include Chg Orders
 in Max Ret %, and the Adjust Maximum Bill fields.

- Maximum Amount - Select this option if you want to
 set a flat amount for maximum retention. When you select this option, the system
 enables the Retainage Amount and Adjust Maximum Bill fields.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## % of Contract

The system enables this field when you select the Percent of
 Contract option.
Enter the percent of the contract amount that is subject to retention.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Retainage Amount

The system enables this field when you select Maximum Amount
 for setting maximum retention amounts.
Enter the maximum retention amount for this contract.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Include Change Orders in Maximum Retainage %

The system enables this checkbox when you select Percent of
 Contract for setting maximum retention amounts.
Check this box if you want to include change order amounts in maximum retainage calculations by percent. When you check this box, the system calculates the maximum retention amount based on the current contract value. If you do not check this box, the system calculates the maximum retention amount based on the original contract value.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Adjust Maximum Bill

There are two options for retention amount distribution:

- Composite Percentage - With this option, the system takes the final retention amount and calculates an overall percentage rate which it applies to all contract items equally.

- Item Percentage from Invoice - With this option, the system distributes the final retention amount based on the work completed retainage percent value for each line. The system continues to distribute in this manner until the retention amount is depleted. The system places any leftover amount on one final item on the contract, resulting in a calculated retention percentage value for that item only. The system sets the work completed retainage percent to zero for all remaining items on the contract.
Example : Composite Percentage
If you have set the maximum retention amount for a contract at $10,000, and you have already created invoices with retention amounts totaling $8,000, you will only have $2,000 left before you reach the maximum retention setting. If you invoice $3,000 retention for two more items (as seen in Table 1), the system will calculate a composite retention percentage and apply it to each item.
The system uses this calculation to determine the composite retention percentage: Maximum retention remaining ($2,000) / New Invoice Items Total ($30,000) = Composite Retention Percentage (.066666). The system then updates the work completed retention percentage and work completed retention amounts based on the composite retention percentage (as seen in Table 2).
Table 1. Retention Amounts Prior to DistributionThis Invoice
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

Table 2. Retention Amounts After DistributionThis Invoice
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

Example: Item Percentage from Invoice
Tables 3 and 4 display how the system would distribute the retention amount for a contract with a maximum retention of $400. Table 3 shows the retention amounts prior to distribution, while Table 4 displays the retention amounts after the distribution.
Table 3. Retention Amounts Prior to DistributionThis Invoice
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

Table 4. Retention Amounts After DistributionThis Invoice
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

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

##  Processing Group

 Specify the processing group (from JB Processing Group) to assign to this
 contract.
Note: Information entered here will update JB Contract Info. Likewise, information entered in JB Contract Info will be updated here.
 If you add a contract to a processing group (in JB Processing Group), it will update this field for the contract.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Customer Reference

Enter additional information (e.g. customer's PO number), up to 30
 characters, that you want to print on the JB invoice. The description entered here will be
 used as a default for T&M billings only (entered manually or by initialization) where a
 contract is specified and all items on the contract have a bill type of 'T&M'.
Note: Information entered here will update JB Contract Info.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

##  Bill on Completion

 Check this box if you want this contract billed only upon its completion
 in progress billing. Typically, this option is only used for small jobs, where a one-time
 billing occurs after the entire job is completed. However, this option can be checked for
 contracts that have previous billings.When checked, the JB Complete Bill program can be run
 to initialize billings for the contract. The system will use the difference between the
 previous billed amounts and the contract total to create a new bill for the balance.
 Leave this box unchecked if you do not want to bill this contract upon its completion only (i.e. you will be doing multiple billings on this contract as phases of work are completed).
Note: Information entered here will update JB Contract Info.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

##  Report Retainage at Item Level

 For Progress Billing only.
 Check this box if retainage will be reported at the item level.
 Leave this box unchecked if retainage will be reported at the contract level.
Note: Information entered here will update JB Contract Info.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

##  Receivable Type

 Enter the receivable type (from AR Receivable Types) to use as a default
 when entering billings for this contract. The receivable type specified here determines
 which GL accounts will be updated when a billing is interfaced and overrides the receivable
 type specified for the customer (in AR Customers) or company (in AR Company Parameters).
 If no receivable type is specified here, default will be the Receivable Type assigned to the customer specified on the billing. If no receivable type specified for the customer, defaults the receivable type specified for the AR company.
Note: Information entered here will update JB Contract Info.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Misc Dist Code

Specify the default miscellaneous distribution code for this contract.
 Default will be used as follows:
In AR Miscellaneous Distributions:

- From AR Invoice Entry – If a contract is specified for the invoice, defaults the miscellaneous distribution code assigned to the contract. If no miscellaneous code is specified for the contract, or no contract is specified for the invoice, defaults the miscellaneous distribution code assigned to the customer in AR Customers. If no code assigned there, default will be null.

- From AR Cash Receipts – Defaults the miscellaneous code from the customer. If no code assigned to the customer, defaults as null.

In JB Progress Bill Misc Dist:

- From JB Progress Billing – When adding miscellaneous distributions, default will be null.

- From JB T&M Bill Edit – When adding miscellaneous distributions manually, defaults as null. When initializing T&M billings with 'Miscellaneous' type sequences, if you have specified a miscellaneous distribution code for the template sequence, defaults from the template sequence. If no code is specified for the template sequence, defaults from the billing's contract. If no miscellaneous code specified for the contract, or no contract specified for the billing, defaults from the customer. Otherwise, defaults as null.

Note: Information entered here will update JB Contract Info.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## T&M Template

Specify the T & M Template that will be used by job billing to
 determine how to accumulate job cost detail for this contract.
If this is a new contract, and the bill type is set to 'T&M' or 'Both' (Info tab), this field will default the template specified in the "JB T&M Template" field in JB Company Parameters.
Note: Information entered here will update JB Contract Info.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## T&M Flat Bill Amount

Enter the flat amount to be used on T&M billings for sequences flagged
 as Type A (Amount) with a Flat Amt Option of F (Flat Amount). This option is typically used
 for one-time billings, but can be used for any sequence on a template that should be billed
 this flat amount.
Note: Information entered here will update JB Contract Info.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## JB T&M Limit Option

Specify the basis for billing limits.

- None - Select this option if there is no billing limit.

- Contract - Select this option if the billing limit will be based on the current contract amount.

- Item - Select this option if the billing limit will be based on the current amount for the contract item.

For contract and item limits, the current contract amount is compared against the billed-to-date amount plus the current invoice amount.
Note: Information entered here will update JB Contract Info.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

##  Rounding Option

 This feature is for use with Progress Billing only.

- No Rounding - Select this option if no rounding will occur on billings or retainage amounts.

- Round Billing Only - Select this option to have billing amounts rounded to the nearest whole dollar.

Note: Use of this option does not round the bill’s “amount due”. Only the bill amounts are rounded. If retainage amounts are not rounded, the total “amount due” will reflect the dollars and cents.

- Round Billing and Retainage - Select this option to have billing and retainage amounts rounded to the nearest whole dollar. Retainage will be rounded based on the Report Retainage at Item Level option (above).

 If the Report Retainage at Item Level option is checked, retainage is rounded at the item level, and the total retainage is updated after all the item amounts have been rounded. If not checked, retainage is rounded at the contract level, and the item’s retainage is rounded, with the difference between the rounded contract retainage and total items’ retainage added to the last item so that total retainage is equal to the retainage total of the items.
Note: Information entered here will update JB Contract Info.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

##  Override Billing Information: Address

 Enter the override billing address for this contract, up to 60 characters. This address will be used as the billing address when printing JB invoices for this contract. If no address is entered here, billings will default the address specified for the contract’s customer (in AR Customers).
Note: Information entered here will update JB Contract Info.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

##  Override Billing Information: City

 Enter the city, up to 30 characters, to be used as the override billing
 city when printing JB invoices for this contract. If left blank, billings will default the
 city specified for the contract’s customer (in AR Customers).
Note: Information entered here will update JB Contract Info.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

##  Override Billing Information: State

 Enter a valid state (as defined in HQ States) to use when printing JB
 invoices for this contract. If left blank, billings will default the state specified for
 the contract’s customer (in AR Customers).
 The system validates the state based on the Default Country specified in HQ Company Parameters for the active company. If not valid, an error displays, but entry is allowed. You must then enter a valid country for this state in the Country field.
Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.
Note: Information entered here will update JB Contract Info.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

##  Override Billing Information: Zip

 Enter the zip code, up to 12 characters, to use when printing JB invoices
 for this contract. If left blank, billings will default the zip code specified for the
 contract’s customer (in AR Customers).
Note: Information entered here will update JB Contract Info.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

##  Override Billing Information: Add'l Address

 Enter an additional override billing address for this contract, up to 60
 characters. For example, if the billing address is a Post Office box, then you might enter
 the P.O. Box in the Address field above, and use this field to enter the street address.
 The address entered here will default on progress and T&M billings, and if not deleted
 or overridden on the billing, will print on certain reports. May also be used on any
 reports that you create in Crystal Reports.
Note: Information entered here will update JB Contract Info.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

##  Additional AIA Info: Architect Name

 Specify the architect’s name, up to 30 characters. This name will print in
 the Architect field in the heading of the AIA report. This field is optional and is not
 validated.
Note: Information entered here will update JB Contract Info.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

##  Additional AIA Info: Architect Project

 Specify the architect’s project number, up to 30 characters. This name
 will print in the Project Nos field in the heading of the AIA report. This field is
 optional and is not validated.
Note: Information entered here will update JB Contract Info.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

##  Additional AIA Info: Contract for Desc

 Enter a description of the contract, up to 30 characters. This description
 will print in the Contract For field in the heading of the AIA report. This field is
 optional and is not validated.
Note: Information entered here will update JB Contract Info.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

##  Additional AIA Info: Start Date

 Enter the starting date for this contract. This date prints in the
 Contract Date field in the heading of the AIA report. This field is optional.
Note: Information entered here will update JB Contract Info.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Review Level

The Review Level drop-down on the JC Contracts form, JB Info
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

- [JC Contracts Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)

- [JB Company Parameters Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-company-parameters-form)

- [JB Progress Billing Form](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/jb-progress-billing-form)

- [JB T&M Bill Edit Form](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-edit-form)

## JB Reviewer Group

The JB Reviewer Group field on the JC Contracts form,
 JB Info tab.
This field is enabled only if you selected the Use Review and Approval Workflow checkbox in the JB Company Parameters form.
Enter the reviewer group for the selected contract. The reviewer group must be set up in the HQ Reviewer Groups form with a Reviewer Group Type of 3-Job Billing.
The reviewer group specified here defaults for each Progress or T&M billing associated with this contract. However, even if you opt to make a selection here, you may override the reviewer group on the billing.
Note: The JB Contract Info, JC Contracts, and PM Contracts forms share the same table (bJCCM). Therefore, entry in this field in any of the three forms will automatically update the corresponding field in the other two forms.

Related tasks

- [Create Reviewer Groups for Job Billing Invoices](/en/vista/vista/administration/headquarters/reviewer-setup/create-reviewer-groups-for-job-billing-invoices)

## Progress Bills Invoice Format

The Progress Bills Invoice Format field on the JC Contracts form, JB Info tab.
Enter the custom or standard invoice report to use when delivering progress invoices (via JB Invoice Delivery) for this customer/contract. Press F4 for a full list of custom reports.
Note: The value entered here must be the exact title name of the report; therefore, it is recommended that you use the F4 lookup to specify the invoice format.

Note: You will only need to enter a value in this field if this contract requires an invoice format that differs from the Progress Bills Invoice Format specified for the customer in AR Customers or at the company level in JB Company Parameters.

### Invoice Format Hierarchy

You can define invoice formats at the company, customer, and contract levels. However, you only need to assign invoice formats at the customer level (in AR Customers) or contract level (in JC Contracts) if the customer or contract (respectively) requires a different invoice format than the one specified at the company level.
 When delivering invoices (via JB Invoice Delivery), the system automatically defaults the invoice format defined for the Job Billing company. If you specified an invoice format at the customer level, the system uses the customer's invoice format instead. However, if you also specified an invoice format for a contract associated with that customer, the contract's invoice format overrides the invoice format specified for the customer.
 If no invoice format is defined at the company, customer, or contract levels, the system will not know what format to use and therefore, will be unable to deliver invoices.

Related information

- [Set Invoice Delivery Options](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/set-invoice-delivery-options)

- [Set Up Recipients for JB Invoice Delivery](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/set-up-recipients-for-jb-invoice-delivery)

## T&M Invoice Format

The T&M Invoice Format field on the JC Contracts form, JB Info tab.
Enter the custom or standard invoice report to use when delivering T&M invoices (via JB Invoice Delivery) for this customer/contract. Press F4 for a full list of custom reports.
Note: The value entered here must be the exact title name of the report; therefore, it is recommended that you use the F4 lookup to specify the invoice format.

Note: You will only need to enter a value in this field if this contract requires an invoice format that differs from the T&M Bills Invoice Format specified for the customer in AR Customers or at the company level in JB Company Parameters.

### Invoice Format Hierarchy

You can define invoice formats at the company, customer, and contract levels. However, you only need to assign invoice formats at the customer level (in AR Customers) or contract level (in JC Contracts) if the customer or contract (respectively) requires a different invoice format than the one specified at the company level.
 When delivering invoices (via JB Invoice Delivery), the system automatically defaults the invoice format defined for the Job Billing company. If you specified an invoice format at the customer level, the system uses the customer's invoice format instead. However, if you also specified an invoice format for a contract associated with that customer, the contract's invoice format overrides the invoice format specified for the customer.
 If no invoice format is defined at the company, customer, or contract levels, the system will not know what format to use and therefore, will be unable to deliver invoices.

Related information

- [Set Invoice Delivery Options](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/set-invoice-delivery-options)

- [Set Up Recipients for JB Invoice Delivery](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/set-up-recipients-for-jb-invoice-delivery)

## JB Bill Notes

Use this window to enter any miscellaneous notes about this contract. The
 space allowance is virtually unlimited. Notes entered here are available for printing on JB
 invoices.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools > Spelling
  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Period

If you initialized this forecast (in JC Forecast Initialize), this field
 defaults a set of forecast periods based on the Contract Start Month and Projected Completion
 Date specified for this contract (Info tab). If no projected completion date
 is specified, forecast periods will be determined by the Contract Start
 Month and the 'number of months past current month' specified during
 initialization.
If you did not initialize a forecast, enter a period to which this forecast applies.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Revenue %

The Revenue % field on the JC Contracts form, Forecast tab.

The percent specified here represents the percent of revenue complete expected for the selected period.
If you initialized this forecast, this field defaults the revenue forecast percent for the selected period. Percentage is calculated as follows:

- If the forecast method is Linear (as specified in JC Company Parameters, Forecast tab), monthly percentages are equally distributed based on the number of months in the forecast. For example, on a 12-month contract, the first month will be 8.33% of the total contract amount (100% / 12 = 8.33), the second month will forecast another 8.33% for an accumulated 16.66%, and so forth.

- If the forecast method is Curve, monthly percentages will be based on number of forecast months, number of forecast intervals, and the interval percentages. For more information, see [Revenue/Cost Forecast Options](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/revenuecost-forecast-options).

If you did not initialize a forecast for this contract, enter the revenue percent that applies to the selected period.
Note: If the contract's amount has not increased since the prior month forecast, you must enter a percentage that is equal to or greater than the prior month's percentage. If you enter a revenue percent that is less than the prior month's percent, an error displays indicating that the "Revenue Forecast % cannot be less than the previous month." The system only allows entering a percentage that is less than the prior month if the contract's amount has increased since the prior month.

## Revenue Amount

This field automatically defaults an amount based on the Revenue % x
 Current Contract. This amount represents the revenue complete amount expected for the
 selected period.
Note: If you change this amount, the revenue percent will be recalculated for the period. 
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Cost %

The Cost % field on the JC Contracts form, Forecast tab.

The percent specified here represents the percent of cost complete expected for the selected period.
If you initialized this forecast, this field defaults the cost forecast percent for the selected period. Percentage is calculated as follows:

- If the forecast method is Linear (as specified in JC Company Parameters, Forecast tab), monthly percentages are equally distributed based on the number of months in the forecast. For example, on a 12-month contract, the first month will be 8.33% of the total contract amount (100% / 12 = 8.33), the second month will forecast another 8.33% for an accumulated 16.66%, and so forth.

- If the forecast method is Curve, monthly percentages will be based on number of forecast months, number of forecast intervals, and the interval percentages. For more information, see [Revenue/Cost Forecast Options](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/revenuecost-forecast-options).

If you did not initialize a forecast for this contract, enter the cost percent that applies to the selected period.
Note: If the contract's amount has not increased since the prior month forecast, you must enter a percentage that is equal to or greater than the prior month's percentage. If you enter a cost percent that is less than the prior month's percent, an error displays indicating that the "Cost Forecast % cannot be less than the previous month." The system only allows entering a percentage that is less than the prior month if the contract's amount has increased since the prior month.

## Cost Amount

This field automatically defaults an amount based on the Cost % x Current
 Estimate. This amount represents the cost complete amount expected for the selected
 period.
Note: If you change this amount, the cost percent will be recalculated for the period. 
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Notes

Enter any notes that apply to this forecast/period. For additional space,
 double-click on this field. The Grid Notes window displays, allowing virtually unlimited
 space for your notes and information.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools > Spelling
  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts

## Customer PO

The Customer PO field on the JC Contracts form, Customer
 POs tab.
Enter the customer PO number associated with this contract (typically the purchase order created by the customer for billing purposes).
Note: You must set up a Customer PO here before you can assign it to field tickets in JC Field Ticket.

## Description

The Description field on the JC Contracts form, Customer POs
 tab.
Enter a description for the customer PO.

## Limit Amount

The Limit Amount field on the JC Contracts form, Customer POs
 tab.
If applicable, enter a limit amount for the customer PO.

## Separate Inv

The Separate Inv checkbox on the JC Contracts form, Customer
 POs tab.
Select this checkbox to create a separate billing for ticketed costs associated with this contract/customer purchase order. When initializing bills (in JB Bill Initialization), the system creates a separate billing for the customer PO PO, and groups all costs for approved field tickets associated with the customer PO on the same billing.
Leave this checkbox unselected if you do not want a separate billing created for this customer purchase order. Instead, the system will include approved ticketed costs associated with the customer purchase order on the same bill as other non-ticketed costs for the contract.

## Inactive

The Inactive checkbox on the JC Contracts form, Customer POs
 tab.
This field defaults to an "indeterminate" state (meaning that it is neither selected nor unselected).
 Select the checkbox to indicate the Customer PO is active or deselect (clear) the checkbox to indicate an "inactive" status.

## Notes

The Notes field on the JC Contracts form, Customer POs
 tab.

### Add a Standard Note

Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the HQ Standard Note form.
To insert a standard note into this field, double-click in the field to open the Grid Notes window. Then click the Standard Notes button () in the toolbar, which opens the Std Note Copy window. Then enter the standard note to copy (or select from F4 lookup) and click OK. The system inserts the selected note into the field.

### Spelling Check

 Click the Spelling icon on the toolbar or select Tools> Spelling to spell check the text in this field.
