---
title: "Field Definitions: MS Company Parameters Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-company-parameters-form/field-definitions-ms-company-parameters-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-company-parameters-form/field-definitions-ms-company-parameters-form"
---

# Field Definitions: MS Company Parameters Form

The following is a list of field descriptions for the MS
 Company Parameters form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  MS Company

 Enter a valid company (from HQ Company Setup). This company must be the same as the Inventory company from which materials are sold (e.g., materials stocked in IN Co#1 must be sold from MS Co #1).

## GL Co#

Enter the GL company for use by this MS company. This must be a valid HQ company and be the same GL company assigned to this MS company’s corresponding IN company.

##  Journal

 Enter the GL journal to update when posting Material Sales transactions (i.e. tickets, time sheets, or invoices). Must be a valid journal for the GL company specified above.

##  AP Co#

 Enter the AP company to use for validating material and haul vendors. The system will post haul vendor payables to this AP company. The system allows overrides to this field when posting hauler payments in MS Haul Payment Worksheet.

## Auto-Generate Quote #'s

Check this box to have the system
 automatically generate quote numbers when adding new quotes in MS Quote Entry. When you
 enter N, New, or + for a quote,
 the system will automatically assign the next available sequence number based on the
 Last Used Quote
 # field. In addition, the generated number will be updated to the Last Used Quote
 # field. Select this option only if quote numbers are always numeric.
Uncheck this box if you will be assigning quote numbers manually and/or you use both numeric and alphanumeric quote numbers.

## Last Used Quote #

This field is used in conjunction with the
 Auto-Generate
 Quote #'s field.
Note: The system automatically assigns quote numbers based on this number, and also updates this field when a new quote number is generated.
To start auto-numbering at 1, leave the
 field blank or enter 0. Otherwise, specify the last quote
 number used; the system allows up to 10 characters.
Note: Updates from PM may also use this feature to assign quote numbers.

## Attach batch reports to HQ Batch Control

Check this box if the batch reports should be attached to the batch record that displays in the [HQ Batch Control](/en/vista/vista/administration/headquarters/batch-management/about-the-hq-batch-control-form) form.
 The reports are stored using the Attachment Storage Location and Subdirectory Structure parameters defined in DM Attachment Options.

- The system will attempt to export batch reports before posting the batch. If the export is successful, it will then post the batch. However, if errors occur for any batch report, the system will display an error message and abort the posting process. You will need to correct the error before you can revalidate and post the batch.

- Because you can secure audit reports (in VA Report Security), access to attachments generated through this process is restricted to HQ Batch Control. If you have secured the HQ Batch Control form, users will only be able to access batch reports if they have access to HQ Batch Control. Unlike regular attachments, indexes are not created for batch report attachments and you cannot access them using DM Attachment Search.

## Default Surcharge Group

Enter a valid surcharge group to use as a default for assessing surcharges during ticket entry. This default group will only be used to assess surcharges when either of the following is true:

- a quote exists for the purchaser (customer, job, or
 IN location), but no surcharge group is assigned to the quote and the Apply Surcharges box is checked for the quote.

Note: If a quote exists but the Apply Surcharges box is not checked, no surcharges will be assessed for the ticket, regardless of whether a surcharge group is specified here or on the quote.



- no quote exists for the purchaser.

Note: You will typically enter a surcharge group here if you want surcharges assessed for every ticket. If you do not, leave this field blank and assign surcharges at the quote level for all applicable purchasers.

## Tax Option

Specify from where to default tax codes when entering transactions in MS
 Ticket Entry and MS Haul Ticket Add-Ons. This option only determines the default behavior;
 it can be changed when the tickets are entered.

- 0-No Tax – Tax code defaults as null; enter code manually for taxable items.

- 1-Sales Location – Defaults the tax code assigned to
 the sales location in IN Locations.

- 2-Sale Type/Purchaser – Defaults tax code assigned to the “purchaser” based on the sale type. For example, if the sale type is “Customer”, tax code defaults from AR Customers.

- 3-Sale Type/Purchaser/Sales Location – Defaults tax code assigned to the “purchaser” based on the sale type. However, if a tax code is not assigned, use the tax code assigned to the sales location.

- 4-Delivery – For delivered materials (own equipment or haul vendor), the tax code defaults depending on the sales type and purchaser (e.g. if sales type is ‘customer’, defaults the tax code from AR Customers). For non-delivered materials, the tax code defaults from sales location.

Note: Specifying a tax option here does not guarantee calculation of taxes. The system calculates taxes for materials and/or pay charges that are flagged as taxable.

## Audit Options

The audit options determine when new records of changes are added to the HQ Master Audit (HQMA) database table. For example, if you change a setting on the company parameters form, the system creates a new record of the change in the HQMA table.
You can view records in the HQMA table using the HQ Audit Detail report in the HQ module. See [About Viewing the Master Audit Log](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log) for more information about viewing audit records in the HQMA table.
The following lists and describes the audit options.

- Company Parameters – This option is disabled and will always be checked. Any changes made in the MS Company Parameters program will be tracked in the Master Audit file.

- Pay Codes – Check this box to record additions,
 changes, and deletions to pay codes and their standard pay rates in MS Pay Codes.

- Haul Codes – Check this box to record additions, changes, and deletions to haul codes and their standard pay rates in MS Haul Codes.

- Price/Discount Templates – Check this box to record additions, changes, and deletions to pricing and discount templates in MS Price Templates and MS Payment Discount Templates.

- Quotes – Check this box to record additions,
 changes, and deletions to quotes, quote detail, and any defaults or overrides in MS
 Quotes. System updates to “Sold Units” in quote detail will not be tracked in HQMA.

- Material Tickets – Check this box to record additions, changes, and deletions to ticket detail in MS Ticket Entry. System updates to specific detail in the Ticket Detail table (MSTD) such as Invoice#, Pay Verify, etc., are not tracked in HQMA.

- Hauler Time Sheets – Check this box to record additions, changes, and deletions to pay time sheet header and line detail in MS Pay Time Sheets. System updates to the Pay Header and Pay Lines tables (MSHH, MSHL) such as Invoice#, Pay Verify, etc., are not tracked in HQMA.

- Invoice Detail – Check this box to record the
 addition or removal of tickets from invoices after invoices are printed (in MS
 Invoice Print). When an invoice is printed, an internal flag is set for the invoice
 indicating that it has been printed. If this option is checked, adding or removing
 tickets from printed invoices will automatically generate entries in the HQ Master
 Audit table (HQMA). These entries will be recorded for the MSID table and identify
 the MS Co#, Month, Transaction #, Invoice #, User, Date and time of change.

- Surcharges – Check this box to record additions, changes, or deletions to surcharge values.

Note: When setting up a company, the entry of invalid data in certain fields causes a warning; however, the system allows entry and you can save the record. This primarily applies to (but is not limited to) required data such as the 'interface to' companies and journals, since it is sometimes necessary to set up the company information before setting up requested data.

## Remove From Ticket Entry

For each of the options listed, indicate
 whether the system should remove the associated field(s) from the MS Ticket Entry form.
 Removed fields are still available for reports. If you do not want information removed from
 the form, but want to skip its input, select Options > Ticket Entry
 Options from MS Ticket Entry, and check the Skip Input box for all fields you want
 skipped for input. Otherwise, you will need to use the F3 Properties window to do each
 field manually.

- Material Vendor

- Weights (Gross, Tare, & Net)

- PR Co#/Employee

- Driver

- Start/Stop Times

- Loads

- Miles / Kilometres*

- Hours

- Haul Zone

- EM Revenue Info (Revenue Code, Revenue Basis, & Revenue
 Total)

- Vendor Pay Info (Pay Code, Pay Basis, & Pay Total)

- Tax Info (Tax Code, Tax Type, Tax Basis, Tax Amount, Haul Pay Tax
 Type*, Haul Pay Tax Code*, & Haul Pay Tax Amt*)

- Discount Info (Discount Type, Discount Basis, Discount Rate,
 Discount Offered, & Tax Discount)

- Reason Code

* Displays only when the Default Country
 in HQ Company Setup is AU (Australia) or CA (Canada).

## Ticket Warning

Indicate an option to check for duplicate ticket numbers when entering tickets in MS Ticket Entry.

- 0-No Warning – Do not check for duplicate ticket numbers.

- 1-Material Sales – Check for duplicate ticket numbers, and warn if ticket number already exists within the same MS company.

- 2-Material Sales/Location – Check for duplicate ticket numbers, and warn if ticket number already exists with the same MS company and sales location.

## Check Customer Credit Limit During Ticket Entry

This field is for Customer and Customer/Job tickets only.
Check this box to have the system display a warning when the customer’s credit limit (specified in AR Customers) is exceeded during ticket entry.
Uncheck this box if you do not want a warning displayed when a customer's credit limit is exceeded during ticket entry.

##  Save Deleted Tickets

 Check this box to have the system automatically save a copy of all tickets deleted from the system (except purges). The system saves all new (non-posted) tickets deleted from a ticket batch, as well as existing transactions deleted during a ticket batch update, in the MS Deleted Ticket table (MSTX).
Note: If using a “duplicate ticket warning” (Ticket Warning field), the system does not include deleted tickets when checking for duplicate ticket numbers.

## IN Sales and Purchases

Indicate the level at which to update Inventory when posting sales and purchases of stocked materials.

- 0-No Update – No update to IN will occur.

- 1-Summary – Transactions will be summarized by location, material, transaction type (i.e. AR Sale, JC Sale, IN Sale, etc), GL account (Sales or Inventory Account), and sales U/M. Specific purchaser information will not be interfaced to IN. Posted units will be updated in sales unit of measure, but unit price will be averaged.

- 2-Detail – This option allows full transaction detail, including specific purchaser information and the MS Trans#.

## IN Auto Production

Indicate the level at which to update Inventory for entries related to the production of finished materials. This option only applies to materials flagged for auto production in IN Location Materials. This may include transfers or sales of components from their source location to the production/sales location along with usage and production entries.

- 0-No Update – No update to IN will occur.

- 1-Summary – Transactions will be summarized by location, material, and transaction type (i.e. IN Sale, Purchase, Transfer In, Transfer Out, Usage, and Production).

- 2-Detail – This option allows full transaction detail, including the MS Trans#.

## Job Cost

Indicate the level at which to update Job Cost
 when posting a batch of tickets or time sheets. Updates to JC include actual units and
 costs of materials, paying, and taxes posted as job sales.

- 0-No Update – No update to IN will occur.

- 1-Summary – Transactions will be summarized by job, phase, cost type, location, material, sales U/M, tax code, and tax type (Sales or Use). The JC Actual Date is the Posting Date.

- 2-Detail – One JC entry will be made for each ticket posted.

Note: If you select the Create Intercompany Invoices checkbox, the IN purchase and JC expense updates from inter-company sales are made when intercompany AP invoices are posted, not from the ticket or hauler time sheet batch updates.

## Equipment Revenue

Indicate the level at which to update Equipment Management when posting a batch of tickets or time sheets.  Updates to EM represent equipment revenue earned when your own vehicles are used to deliver materials.  Inter-company invoicing does not apply to inter-company equipment use (i.e. the system will automatically make inter-company journal entries as needed).

- 0-No Update. No Update to EM will occur.

- 1-Summary – The system summarizes transactions by EM Co#, Equipment, Revenue Code, and Sale Type.

- 2-Detail – The system creates one EM entry for each posted ticket.

## General Ledger

General Ledger drop-down on the Ticket Updates tab of the MS Company Parameters form.
Indicate the level at which to update General Ledger when a batch of tickets or payer time sheets is posted.

- 0-No Update. No Update to GL will occur.

- 1-Summary – The system summarizes transactions by GL account, unless the GL Account is set for interface detail (Interface Detail checkbox in GL Chart of Accounts).

- 2-Detail – The system creates one GL entry for each posted ticket.

Note: Production GL Interface level selected in IN Company Parameters controls the update to GL with auto production related entries.
If you selected ‘Detail’ as the GL interface level, use the Select Available Items for Detail-Level GL Descriptions box to select one or more of the following fields to include as part of the GL transaction description:

- Trans#

- Ticket

- Location

- Material

- Purchaser (Sale Type and Cust#/Cust Job, or JC Co /Job, or IN Co/To Loc)

Note: This selection box is also available when the interface level is “Summary” because some accounts may be flagged for detail in GL Charts of Accounts.

## Summary GL Description

This field enabled only when General Ledger interface level is ‘1-Summary’.
Enter the transaction description, up to 60 characters, that the system uses when interfacing ticket data to GL at the summary level.

## Remove From Haul Sheet Entry

Select the checkbox for each option to indicate whether to remove the associated field(s) from the MS Hauler Time Sheet Entry form. All removed fields are still available for reports. If you do not want information removed from the form, but want to skip its input, use the standard F3 Properties option.

- Material Vendor

- Start/Stop Times

- Loads

- Miles / Kilometres*

- Hours

- Haul Zone

- EM Revenue Info (Revenue Code, Revenue Basis, & Revenue Total)

- Vendor Pay Info (Pay Code, Pay Basis, & Pay Total)

- Tax Info (Tax Code, Tax Type, Tax Basis, Tax Amount,
 Haul Pay Tax Type*, Haul Pay Tax Code*, & Haul Pay Tax Amt*)

- Discount Info (Discount Type, Discount Basis, Discount Rate, Discount Offered, & Tax Discount)

* Displays only when the Default Country
 in HQ Company Setup is AU (Australia) or CA (Canada).

## Use Invoice #'s From

- MS - Select this option if MS has its own set of invoice numbers. The system assigns invoice numbers based on the Last Used MS Invoice # field.

- AR - Select this option to share invoices numbers with AR. The system assigns invoice numbers based on the “Last Invoice Number” specified in AR Company Parameters.

##  Last Used MS Invoice #

 This field is for use with MS invoice numbers only.
 If you are using MS invoice numbers, the system will automatically update this field each time you manually enter invoices in MS Invoice Edit or initialize them using MS Invoice Initialize.
 To start auto-numbering at ‘1’, leave blank or set to 0. Otherwise, specify the last invoice number used. The system allows up to 10 characters.

## Initialize Invoices in Customer\Transaction # Order

Check this box to initialize invoices in order by customer number/transaction number. When initializing invoices in MS Invoice Initialize, the system will generate invoices in order by customer number, then by ticket number.
Uncheck this box if you do not want to initialize invoices in order by customer/transaction number. Instead, system will initialize invoices in order by transaction number only.

##  Create Intercompany Invoices

 Check this box if treating intercompany sales as ‘customer’ sales. The system will generate invoices and update AR. The system will generate job and inventory transactions in AP for the ‘purchasing’ company.
 Do not check this box if not invoicing intercompany sales. The system will update JC and IN when posting ticket batches and create journal entries for the intercompany AR and AP accounts; however, no AR or AP transactions will be generated.

##  Invoice Format

 Specify the Crystal Report to use for printing Material Sales invoices. You may specify one of the standard reports provided by Viewpoint V6 Software, or one created by your company to meet your specific needs. This field may be overridden when printing invoices.

## Sort by Sales Date

Check this box to sort transactions by date. The sales date will print on invoices and will be available for subtotals.
Uncheck this box if you do not want transactions sorted by date. The sales date will not print on invoices and will not be available for subtotals.

## Sort by Location

Check this box if transactions will be sorted by location. The “from location” will print on invoices and will be available for subtotals.
Uncheck this box if transactions will not be sorted by location, the “from location” will not print on invoices and will not be available for subtotals.
Note: If you create separate invoices per location, this option should be left unchecked.

##  AR Co#

 Enter the AR company to use for validating customers, and to which invoice transactions will be updated. Must be a valid HQ company.

## AR Interface Level

Indicate the level at which invoices and adjustments will be updated to Accounts Receivable.

- 0-No Update – No update to AR will occur.

- 1-Summary – The system generates one line per invoice and location, sales account, tax code, customer job, and customer PO#. The invoice will not include material codes, units, or unit prices.

- 2-Material – The system generates one line per invoice and location, sales account, tax code, customer job, customer PO#, and material code. The invoice includes units, but not unit price.

- 3-Unit Price – The system generates one line per invoice and location, sales account, tax code, customer job, customer PO#, material code, and unit price. The invoice includes ECM.

## Auto Apply Payments on Cash Sales

Check this box to have the system automatically apply payments to cash sale invoices during the interface to AR. The system applies payments using the CM Account information set up in AR Company Parameters (with overrides by Location). A deposit transaction will be created in CM, with the deposit number being a unique number based on the posting date and an auto generated sequence #. For example, if you posted the invoice on May 5th, 2002, the deposit number would be 020505-1.
Uncheck this box to apply payments manually in AR after the system interfaces invoices from MS.

## GL Interface Level

Indicate the level at which invoices will be updated to General Ledger.

- 0-No Update – No update to GL will occur.

- 1-Summary – The system summarizes a batch of invoices by GL Account.

- 2-Detail – The system creates transactions for each Invoice and GL Account combination.

If you select ‘Detail’ as the GL interface level, use the Select Available Items for Detail-Level GL Descriptions box to select one or more of the following fields to include as part of the GL transaction description:

- Invoice
 #

-
 Customer
 #

-  Customer
 Job


- Customer PO

- Location

-
 Material

##  Summary GL Description

 This field enabled only when GL Interface Level is ‘1-Summary’.
 Enter the transaction description, up to 60 characters, that the system uses when interfacing invoice data to GL at the summary level.

## From Address

From Address field on the Email Settings tab of the MS Company Parameters form.
Enter the email address to use as the reply email address.

Related concepts

- [About the MS Company Parameters Form](/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-company-parameters-form)

## Subject

Subject field on the Email Settings tab of the MS Company Parameters form.
Enter the text that should appear in the Subject line of the email. Up to 60 characters allowed.

Related concepts

- [About the MS Company Parameters Form](/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-company-parameters-form)

## Body

Body field on the Email Settings tab of the MS Company Parameters form.
Enter the text that will appear in the body of the email. You can format your email text using the text-formatting toolbar above this field.

Related concepts

- [About the MS Company Parameters Form](/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-company-parameters-form)
