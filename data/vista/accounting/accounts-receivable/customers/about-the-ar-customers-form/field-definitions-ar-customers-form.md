---
title: "Field Definitions: AR Customers Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form/field-definitions-ar-customers-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form/field-definitions-ar-customers-form"
---

# Field Definitions: AR Customers Form

The following is a list of field descriptions for the AR Customers form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Customer

Enter a unique numeric code, up to 6 digits, to identify this customer or enter ‘+’ to have the system automatically assign the next sequential number.
Note: If the system determines that the next value exceeds the maximum value allowed (999999), you will receive a message that you must manually enter a number lower than the maximum.
If you wish to view/edit information for an existing customer, and you do not know the customer’s number, you can enter the sort name and the system will automatically pull up the customer’s number. If more than one customer uses the same sort name, the system will pull the first match found.

##  Name

 Enter the customer’s name, up to 60 characters. This name will be used when printing statements and reports.

##  Sort Name

 Enter the sort name for this customer, up to 15 characters. The sort name initially defaults as the first 15 characters of the customer name, but may be changed for an accurate alphabetic sort. Sort names entered in lower or mixed case will be converted to upper case.
 The sort name is used throughout the software whenever alphabetic sorting is used, such as on reports and lookups (F4). Forms where entry of a customer number is required, will in most cases, allow entry of the sort name and will return the customer number associated with the first match.
 In many forms prompting for customer number,
 you can enter the sort name and it will return the customer number associated with the
 first match. Therefore, if you have multiple customers with the same or similar name, you
 may override their sort name to identify them by including a location or number within the
 15 characters. When setting up a new customer (in AR Customers), the sort name will default
 the first 15 characters of the customer’s name. The default can be overridden, but it is
 normally suggested that you accept the system-provided sort name unless it would be
 alphabetically incorrect. For example, if the customer name is J. Smith Construction, you
 would enter the sort name as Smith, J.
Sort names can be entered upper, lower, or mixed case, but the program will convert and
 save as upper case so that there is consistency with all customers. You may choose to
 override the sort name on customers with similar names to provide a unique sort name for
 each. If the same sort name is used for multiple customers and you enter the sort name
 during data entry, the system will bring back the first match found. Having unique sort
 names and entering the full fifteen characters when names are similar will provide the
 greatest accuracy.
A customer’s sort name can be changed, even after transactions have been posted for that
 customer. If you change a sort name for any given customer, the system will automatically
 cycle through all existing transactions for that customer and adjust those records to show
 the new sort name so that all transactions for that customer remain grouped together.

##  Temporary Customer

 Check this box if this customer is temporary and will be deleted when purging temporary customers in AR Purge Paid Invoices. Customer will only be purged if no transactions exist.
 Leave this box unchecked if this is a permanent customer. Customer will be skipped during purge process.

## Mailing Address: Address

Enter the mailing address for this customer, up to
 30 characters.

## Mailing Address: City

Enter the city, up to 30 characters.

## Mailing Address: State

Enter a valid state (as defined in HQ States). The
 system validates the state based on the Default Country specified in HQ Company Setup
 for the active company.

## Mailing Address: Zip Code

Enter the zip code, up to 10 characters.

## Mailing Address: Country

Enter the 2-character country code. Entry in this
 field is required when the address exists outside the Default Country specified in HQ
 Company Parameters for the active company. Country must be valid for the specified state
 (e.g. state, province, territory, etc.) as defined in HQ States.

## Mailing Address: Additional Address

Use this field to enter additional mailing address
 information for this customer. For example, if the customer receives their mail at a
 P.O. Box, then you might enter the P.O. Box in the Mailing Address field, and use this
 field to enter the street address.
The address information entered here is not used by
 any of the posting programs, but may be used on certain reports.

## Billing Address: Address

Enter the billing address for this customer.

##  Billing Address: City

 Enter the city, up to 30 characters.

## Billing Address: State

Enter a valid state (as defined in HQ States). The
 system validates the state based on the Default Country specified in HQ Company Setup
 for the active company. If not valid, an error displays, but entry is allowed. You must
 then enter a valid country for this state in the Country field.

##  Billing Address: Zip Code

 Enter the zip code, up to 10 characters.
Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

##  Billing Address: Country

 Enter the 2-character country code. Entry in this field is required when the address exists outside the Default Country specified in HQ Company Parameters for the active company. Country must be valid for the specified state (e.g. state, province, territory, etc.) as defined in HQ States.
Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

##  Billing Address: Add'l Address

 Use this field to enter additional billing address information for this customer. For example, if the billing address is a P.O. Box, then you might enter the P.O. Box in the Billing Address field above, and use this field to enter the street address.
 The address information entered here is not used by any of the posting programs, but may be used on certain reports.

##  Phone

 Enter the phone number, up to 20 characters.

##  Fax

 Enter this customer’s fax number, up to 20 characters.

##  Contact

 Enter the name of the primary contact person, up to 30 characters.

##  Contact Ext.

 Enter the telephone extension number for the primary contact person.

## Email

Enter an email address. If you click the Email button () to the right of this field, the system opens Microsoft Outlook and sets up an outgoing message for you using the email address specified in this field.Note: You
 can enter multiple email addresses if applicable; however, you
 must separate them with a semi-colon. For example,
 jane.doe@email.com; johnd@email.com;
 joe.smith@email.com.

## URL

Enter the URL (Uniform Resource Location) for this customer, if applicable (i.e. the Internet address). This field is informational only.
Example: www.viewpointcs.com
Clicking the Go button () to the right of this field will take you directly to the Web site indicated in this field.

## ABN (Business Number)

Enter the Australian Business Number for the customer. This field is used for reporting purposes.
Note: The system displays this field when the current
 company's country is set to Australia in HQ Company Setup (Default Country
 field).
ABNs can be entered as 11 consecutive digits, or as 11 digits with a space separating the 2nd and 3rd digits, the 5th and 6th digits, and 8th and 9th digits (e.g. ## ### ### ###).
ABNs must be unique per customer within a customer group.

## ACN (Corporate Number)

Enter the Australian Corporate Number for the customer. This field is used for reporting purposes.
Note: The system displays this field when the current
 company's country is set to Australia in HQ Company Setup (Default Country
 field).

## Status

Indicate the status of this customer.

- Active - Select this option if this customer is active. Entries may be made in any AR form to this customer.

- Inactive - Select this option if this customer is inactive. This option allows you to post payments for this customer, but new invoices may not be posted.

- On Hold - Select this option if this customer is on hold. New invoices may be posted for this customer, but a warning is displayed when this customer is selected.

##  Payment Terms

 Enter the default payment terms code (from HQ Payment Terms) to use when entering invoices. This code will determine default values for discount and due dates, and discount rate.
 Although payment terms are not a required field, they must be set up for a customer if using discounts in the Material Sales module.

## Receivable Type

Enter the default receivable type (from AR Receivable Types) to use when entering transactions in AR (Invoice Entry, Cash Receipts, or Finance Charge). Initially defaults from AR Company Parameters unless no receivable type specified, in which case defaults from previous entry.
This default is used to determine the GL accounts to debit/credit for accounts receivable, non-contract revenue, retainage, discounts, and write-offs.
Note: If the Allow Override of Receivable Type option in AR Company Parameters is checked, this default may be overridden during transaction entry. If not checked, all transactions entered for this customer are automatically assigned this receivable type, which may not be overridden.

## Tax Code

Enter the default tax code (from HQ Tax Codes) to use when entering
 non-contract transactions referencing this customer. This tax code will be used to
 determine the amount of tax to be calculated, as well as which GL account will be affected.
If you enter contract-related invoices for this customer, taxes will be calculated based on the tax code assigned to the associated contract item. If the contract item does not have a tax code specified, no taxes may be posted to the invoice item.
Note: If you did not check the Post Taxes on
 Invoices or Post Taxes on Payments boxes in AR
 Company Parameters, no taxes may be entered for any customer, regardless of whether or not
 a tax code is specified here or for the associated contract in JC Contracts.

## Misc Dist Code

Enter the default code (from AR Misc Distribution Codes) to use when posting miscellaneous distributions for this customer (in AR Invoice or AR Cash Receipts), if applicable. You may override the default when entering or paying invoices, if desired.

##  Date Opened

 Enter the date that this customer’s account was opened. Defaults the current date. This date is informational only and not required.

##  Credit Limit

 If applicable, enter the credit limit for this customer. If you enter an invoice (in AR Invoice Entry) that puts the customer’s balance over the limit specified here, you will receive the following warning:
 Customer balance exceeds Credit Limit!

##  Markup/Discount Rate

 For use with Material Sales only.
 Enter the markup or discount rate that will be used to determine pricing for this customer in Material Sales.

## Finance Charge Type

Indicate the finance charge type for this customer.

- A=Account. Finance/service charges will be assessed against all outstanding invoice transactions, and a single invoice transaction generated for the amount. This option is available for both Open Item and Balance Forward statement types.

- I=Invoice. Finance/service charges will be calculated on, and applied to, specific invoices. This option is available for Open Item statement types only. If you select this type and then change the statement type to Balance Forward, the Finance Charge type will be automatically changed to A=Account.

-  R=RecType. Finance/service charges will be assessed against all outstanding invoice transactions and grouped according to invoice receivable type. A separate line will be generated for each invoice posted to the specified receivable type.

-  N=No Finance Charges. No finance/service charges will be assessed for this customer. Finance Charge % and Exclude Contract Invoices from Finance Charges fields are disabled. This option is available for both Open Item and Balance Forward statement types.

Note: For all options, except ‘N-No Finance Charges’, if the Exclude Contract Invoices from Finance Charges is checked (below), finance charges will only be calculated for non-contract invoices, except in the case where the non-contract invoice is flagged as ‘Exclude FC’ (via AR Exclude From Finance Charge).

##  Finance Charge %

 Disabled if Finance Charge Type is ‘N-No Finance Charges’.
 Enter the finance/service charge rate for this customer, or enter 0.00 if this customer will not be assessed finance/service charges. Initially defaults the finance charge specified in AR Company Parameters.

##  Exclude Contract Invoices From Finance Charges

 Disabled if Finance Charge Type is ‘N-No Finance Charges’.
 Check this box to exclude contract-related invoices from finance charge assessment. When checked, all contract-related invoices entered for this customer (in AR Invoice Entry) will automatically be flagged as exempt from finance charges.
 Leave this box unchecked if contract-related invoices for this customer are subject to finance charges.

## Statements

Specify the statement type for this customer.

- Open Item — Statements will show all invoices with an open balance. Cash receipts will generally be applied to specific invoices.

- Balance Forward — Statements will show the last statement’s balance forward and all activity for the current period. Cash receipts will generally be applied on account.

##  Print Statements

 Check this box if you will be printing statements for this customer.
 Leave this box unchecked if you will not be printing statements for this customer.

## JB Progress Bills Invoice Format

The JB Progress Bills Invoice Format field on the AR Customers form, Add'l Info tab.

Enter the custom or standard invoice report to use when delivering progress invoices (via JB Invoice Delivery) for this customer. Press F4 to select from a list of valid reports.
Note: The value entered here must be the exact title name of the report; therefore, it is recommended that you use the F4 lookup to specify the invoice format.

You will only need to enter a value in this field if this customer requires an invoice format that differs from the Progress Bills Invoice Format specified for the company in JB Company Parameters.
Note: The invoice format specified here will be used for all progress billings for this customer. However, if multiple contracts are associated with this customer and one or more of those contracts require a different invoice format than what you have specified here, you can override the invoice format for each applicable contract in JC Contracts (JB Info tab).

### Invoice Format Hierarchy

You can define invoice formats at the company, customer, and contract levels. However, you only need to assign invoice formats at the customer level (in AR Customers) or contract level (in JC Contracts) if the customer or contract (respectively) requires a different invoice format than the one specified at the company level.
 When delivering invoices (via JB Invoice Delivery), the system automatically defaults the invoice format defined for the Job Billing company. If you specified an invoice format at the customer level, the system uses the customer's invoice format instead. However, if you also specified an invoice format for a contract associated with that customer, the contract's invoice format overrides the invoice format specified for the customer.
 If no invoice format is defined at the company, customer, or contract levels, the system will not know what format to use and therefore, will be unable to deliver invoices.

## JB T&M Bills Invoice Format

The JB T&M Bills Invoice Format field on the AR Customers form, Add'l Info tab.

Enter the custom or standard invoice report to use when delivering T&M invoices (via JB Invoice Delivery) for this customer. Press F4 to select from a list of valid reports.
Note: The value entered here must be the exact title name of the report; therefore, it is recommended that you use the F4 lookup to specify the invoice format.

You will only need to enter a value in this field if this customer requires an invoice format that differs from the T&M Bills Invoice Format specified for the company in JB Company Parameters.
Note: The invoice format specified here will be used for all T&M billings for this customer. However, if multiple contracts are associated with this customer and one or more of those contracts require a different invoice format than what you have specified here, you can override the invoice format for each applicable contract in JC Contracts (JB Info tab).

### Invoice Format Hierarchy

You can define invoice formats at the company, customer, and contract levels. However, you only need to assign invoice formats at the customer level (in AR Customers) or contract level (in JC Contracts) if the customer or contract (respectively) requires a different invoice format than the one specified at the company level.
 When delivering invoices (via JB Invoice Delivery), the system automatically defaults the invoice format defined for the Job Billing company. If you specified an invoice format at the customer level, the system uses the customer's invoice format instead. However, if you also specified an invoice format for a contract associated with that customer, the contract's invoice format overrides the invoice format specified for the customer.
 If no invoice format is defined at the company, customer, or contract levels, the system will not know what format to use and therefore, will be unable to deliver invoices.

##  Selective Purge

 This option is used to determine whether or not transaction detail will be purged (deleted) for this customer when running AR Purge Paid Invoices. This allows you to save transaction history on some customers, while others are being purged on a normal cycle.
 Check this box to leave transaction detail intact for this customer when running AR Purge Paid Invoices. (Note: Although this customer will be skipped during the purge process, you can purge the customer’s transaction detail by specifying the customer as the ‘beginning’ and ‘ending’ customer in the purge program.
 Leave this box unchecked if you want all transaction detail for this customer purged when running AR Purge Paid Invoices for all customers.

## Create Miscellaneous Distributions on Invoice

Check this box to automatically create miscellaneous distributions when processing invoice batches in AR Invoice Entry. During batch validation, the system will create one miscellaneous distribution record per invoice, defaulting the miscellaneous distribution code as follows:

- Contract-related invoices - will use the
 miscellaneous distribution code defined for the contract in JC Contracts. If no
 miscellaneous distribution code is assigned to the contract, will use the
 miscellaneous distribution code assigned to the customer (in AR Customers).

- Non-contract invoices - will use the miscellaneous distribution code defined for the customer in AR Customers.

In both cases, if no default distribution code is found, no miscellaneous distribution record will be created.
Leave this box unchecked if miscellaneous distributions are to be created manually when entering invoices.

## Create Miscellaneous Distributions on Payment

Check this box to automatically create miscellaneous distributions when processing a batch of payments in AR Cash Receipts. During batch validation, the system will create one miscellaneous distribution record per cash receipt using the miscellaneous distribution code defined for the customer in AR Customers. If no distribution code is assigned to the customer, no miscellaneous distribution record will be created.
Leave this box unchecked if miscellaneous distributions are to be created manually when entering payments.

## Sync to ProjectSight

The Sync to ProjectSight checkbox on the AR Customers form, Add'l Info tab.
Important: Only if you have a legacy integration with ProjectSight, use this checkbox to sync records. If you have the current integration, this checkbox is *not used at this time*. For information about syncing records with the current integration, see [ProjectSight Integration with Vista](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:vista_60033).

Select this checkbox to sync this customer to ProjectSight. When selected, the system sends the customer record to ProjectSight as a company.

##  Price Template

 For use with Material Sales only.
 Specify the pricing template (from MS Price Template) to use as a default when selling materials to this customer. May be overridden by quote in MS Quotes.

##  Discount Template

 For use with Material Sales only.
 Specify the discount template (from MS Discount Template) to use as a default when selling materials to this Customer. Only used if payment terms for the customer are material based. May be overridden by quote in MS Quotes.

## Haul Tax Option

For use with Material Sales only.
Indicate whether haul charges are taxable when delivering materials to this customer.

- 0=Not Taxable. Haul charges are not taxable.

- 1=Taxable Using Haul Vendor. Haul charges are only taxable when using an outside vendor to haul materials.

- 2=Always Taxable. Haul charges are always taxable, regardless of whether using company vehicle or outside haul vendor.

May be overridden by quote in MS Quotes.

## Invoice Level

For use with Material Sales only.
Indicate the invoice level that will be used when initializing invoices from tickets (in MS) entered for this customer.

- 0 = One Invoice per Customer. All sales to this customer will be grouped together, and one invoice generated for the total. The AR invoice description will be "Material Sales" and the invoice Customer Reference number will default as blank.

- 1 = One Invoice per Customer and Job. All sales to this customer will be grouped by job, and a separate invoice generated for each unique job. The AR invoice description will be based on the MS Quote description (if one exists) or the customer name if no quote exists.

Note: If you will be initializing cash receipts by customer job for this customer (in AR Cash Receipts), you will need to select this option.

- 2 = One Invoice per Customer, Job, and PO#. All sales to this customer will be grouped by job and purchase order, and a separate invoice generated for each unique job/purchase order combination.

Note: Tickets with different shipping addresses will always print on separate invoices, regardless of how you set this option.

## Bill Frequency

For use with Material Sales only.
Specify the bill frequency (from HQ Frequency Codes) to use when generating MS invoices for this customer. During invoice initialization (in MS Invoice Initialize), if you specify to restrict by bill frequency, transactions posted to this customer will only be initialized to an invoice if the bill frequency specified here matches the bill frequency specified in the initialization criteria.
Note: Bill frequency may be overridden by quote in MS Quotes.

## Print Level

Indicate the lowest level of detail you want printed on all MS invoices for this customer. May be overridden by quote (MS Quotes) or by invoice (MS Invoice Edit).

- 1 = Unit Price. Summarize and print detail at the material, unit of measure, and unit price level. All transactions with the same material number, unit of measure, and unit price will be summarized and printed as one line on the invoice.

- 2 = Trans#. Print one line on the invoice for each transaction. (Note: If this option is selected, the MS ticket number for each transaction will print on the invoice.)

## Subtotal Level

Indicate the lowest level of subtotals you want printed on all MS invoices for this customer. May be overridden by quote (MS Quotes) or by invoice (MS Invoice Edit).

- 1 = Customer Job

- 2 = Customer Job/Customer PO

- 3 = Customer Job/Customer PO/Date

- 4 = Customer Job/Customer PO/Date/Location

- 5 = Customer Job/Customer PO/Date/Location/Material.

- 6 = Customer Job/Customer PO/Date/Location/Material/UM. (Quantity subtotals only available at this level.)

The Level you select may be affected by other setup options in AR and in Material Sales. Therefore, you should review those setup options before selecting an option here.
MS Company Parameters — There are two sort options that will affect what subtotal levels can be used: Sort by Sales Date and Sort by Location. If both are checked, all subtotal levels are available. If the Sort by Sales Date option is unchecked, the date will not print on invoices; therefore, Level 3 cannot be used. If Sort by Location is unchecked, the location will not print on invoices, and Level 4 cannot be used.
AR Customers — You have the option to specify that separate invoices will print for each Customer, Customer/Job, or Customer/Job/PO#. If you are printing separate invoices per Customer, then all subtotal levels are available. If printing separate invoices per Customer/Job, Level 1 cannot be used. If printing separate invoices per Customer/Job/PO#, then Levels 1 and 2 cannot be used.
Note: In addition to subtotals being printed at the selected level, subtotals will also be printed for each level above the selected level.

## Invoice Report

Invoice Report field on the Material Sales tab of the AR Customers form.
Enter a default MS invoice report to override the default MS invoice report for invoice delivery (the default of which is set in MS Company Parameters). Press F4 for a list of reports to choose from.

## Non Batch Invoice Report

Non Batch Invoice Report field on the Material Sales tab of the AR Customers form.
Enter a default MS invoice report to override the default MS invoice report for non-batch statement delivery (the default of which is set in MS Company Parameters). Press F4 for a list of reports to choose from.

## Separate Haul Info on Invoice

Check this box if material information and haul information (Haul Rate and Haul Amount) will print in separate columns on the invoice.
Leave this box unchecked if haul information is to be combined with material information when printing invoices for this customer. Haul rate will not print on the invoice, and haul charges will be included with the material amount. The unit price will be calculated as Total / Material Units.

## Seq

Seq field on the Billing Addresses tab of the AR Customers form.
Type "N" for "New" to add a new sequential value for your alternate billing address.

Related information

- [About the AR Customers Form](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form)

## Name

Name field on the Billing Addresses tab of the AR Customers form.
Enter a customer's name (up to 60 characters) for your alternate billing address.

Related information

- [About the AR Customers Form](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form)

## Description

Description field on the Billing Addresses tab of the AR Customers form.
Enter an address description for your alternate billing address (example: office address, service site, etc.)

Related information

- [About the AR Customers Form](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form)

## Email

Email field on the Billing Addresses tab of the AR Customers form.
Enter a billing email for your alternate billing address.

Related information

- [About the AR Customers Form](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form)

## Address

Address field on the Billing Addresses tab of the AR Customers form.
Enter a street address for your alternate billing address.

Related information

- [About the AR Customers Form](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form)

## City

City field on the Billing Addresses tab of the AR Customers form.
Enter a billing city for your alternate billing address.

Related information

- [About the AR Customers Form](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form)

## State

State field on the Billing Addresses tab of the AR Customers form.
Enter a billing states for your alternate billing address.

Related information

- [About the AR Customers Form](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form)

## Zip

Zip field on the Billing Addresses tab of the AR Customers form.
Enter a billing ZIP Code for your alternate billing address.

Related information

- [About the AR Customers Form](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form)

## Country

Country field on the Billing Addresses tab of the AR Customers form.
Enter a billing country for your alternate billing address.

Related information

- [About the AR Customers Form](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form)

## Add'l Address

Add'l Address on the Billing Addresses tab of the AR Customers form.
Enter additional address information for your alternate billing address.

Related information

- [About the AR Customers Form](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form)

## Notes

Notes field on the Billing Addresses tab of the AR Customers form.
Enter any address notes for your alternate billing address.

Related information

- [About the AR Customers Form](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form)
