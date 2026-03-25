---
title: "Field Definitions: SM Invoice Review Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/sm-invoices/service-management-invoice-forms/sm-invoice-review-form/field-definitions-sm-invoice-review-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/sm-invoices/service-management-invoice-forms/sm-invoice-review-form/field-definitions-sm-invoice-review-form"
---

# Field Definitions: SM Invoice Review Form

The following is a list of field descriptions for the SM
 Invoice Review form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Seq

This field defaults the system-assigned sequence number for this invoice or invoice line. This number cannot be changed.

## Invoice No

This field automatically defaults a system-generated invoice number. Accept the default or enter a new invoice number. Up to 10 characters allowed.

- The system generated invoice number is based on the
 Last
 Invoice Number field in AR Company Parameters; overriding the default
 will not update this field.

- If you override the default with an invoice number that already exists in the SM company (for any customer), you will receive a warning that the number already exists and entry will not be saved.

## Bill To

This field defaults the Bill To customer specified on the work order. Accept the default or enter the customer to which this invoice will be sent. Press F4 for a list of valid AR customers.

## Alternate Billing Address

Alt. Addr. field on the SM Invoice Review form Info tab.
Enter
 the Alternate Billing Address Sequence number created in [ AR Customers](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form). Press F4 for the Accounts Receivable Alt
 Billing Address Lookup form. Press F5 to access the AR Customers form where
 alternate billing addresses are maintained.

## Billing Address

The billing address fields default from the Mailing Address fields in AR Customers when you enter the customer name in the Bill To field. You can override this address in these fields as necessary. When you update a field on this form, the system will not update the fields in AR Customers.

## Pay Terms

Enter the payment terms to use for this invoice. Initially defaults the pay terms assigned to the "bill to" customer in AR Customers or as blank if no pay terms are defined for the customer.
Note: It is not required that you specify pay terms in this field; however, if no pay terms are specified, you will need to manually enter an invoice due date before you process the invoice.

## Custom Invoice Report

Enter the identification number of the invoice
 report to use for previewing/printing this invoice or accept the default. Press F4 for a list
 of valid custom reports.
 This field defaults the custom invoice report
 assigned to the service site in SM Service Sites. If a custom report is not specified for
 the service site, the system defaults the custom report assigned to the customer (in SM
 Customers). If no custom report is specified for the customer, it will use the Default WO Invoice
 Report specified in SM Company Parameters. If a default work order invoice
 is not defined for the company, this field defaults as blank.
Leave this field blank to use the standard SM Invoice report.
Note: The report specified here must be a custom report; entry of a standard report ID is not allowed.

## Invoice Summary Level

Specify how to summarize invoice detail for this invoice. Initially defaults the summary level defined for the customer in SM Customers.

- L-Line — This option will summarize invoice detail at the line level as follows:

- For invoice lines associated with work complete lines, the system will summarize, for each scope on a work order, all work completed lines of the same type (Labor, Equip, Part, and Misc) and print the totals in their respective columns on the invoice (Labor, Equipment, Parts, and Other).

- For invoice lines associated with Flat Price work order scopes, the system will print a summary of each scope based on the specified billable amount and the revenue breakdown by cost type category. For example, if the revenue breakdown specifies 30% of the flat price for Labor, the Labor colum will show 30% of the billable amount.

- C-Cost Type — This option will summarize invoice detail at the cost type level as follows:

- For invoices associated with work completed lines, the system will summarize all work completed lines referencing the same cost type and print a single line for that cost type on the invoice. Totals for work completed lines with no cost type assigned will print first, under the heading of "***NO COST TYPE***".

- For invoice lines associated with Flat Price work order scopes, the system will summarize each scope based on the specified billable amount and the revenue breakdown by cost type category and cost type. For example, if the revenue breakdown specifies 30% of the flat price for Labor/Cost Type 1, and 25% for Labor/Cost Type 2, the invoice will print one line for Cost Type 1 for 30% of the billable amount, and a second line for Cost Type 2 for 25% of the billable amount. Revenue breakdown entries with no cost type specified will be summarized under the heading of "***NO COST TYPE***"

- T-Transaction — This option will summarize invoice detail at the transaction level as follows:

- For invoices associated with work completed lines, the system will print a separate line for each work completed line associated with the scope.

- For invoices associated with Flat Price work order scopes, the system will print a separate line for each revenue breakdown category/cost type combination associated with the scope. All revenue breakdown entries without a cost type specified will be summarized under the heading of "***NO COST TYPE***".

## Description of Work

Use this field to enter a description of the work included on this invoice (e.g. reason for billing). The space allowance is virtually unlimited; however, the information entered here will print on the invoice, so it is suggested that you limit entry to only that information that is important to include on the invoice.

## Invoice Date

Enter the date for this invoice or accept the current date default.

## Due Date

Required.
Enter the due date for this invoice. Initially defaults a due date based on the payment terms assigned to this customer/invoice.
Note: If you did not specify pay terms for this invoice, you will need to manually enter a due date before you can process the invoice.

## Disc Date

Enter the discount date for this invoice. Initially defaults a discount date based on the payment terms specified for this customer/invoice.

## Post Month

Required.
Use this field to enter the post month of the
 invoice. When you click the Process button, the system will create an
 invoice batch and use this date as the post month.
This field defaults to the current month and year.
Note: The selected month and year cannot be closed. Months are closed using the [GL Month End Close ](/en/vista/vista/accounting/general-ledger/gl-setup-and-maintenance/about-the-gl-month-end-close-form) form.Posted Invoices
If this is a previously posted invoice and the original posting month has been closed, changes to the invoice will require entering a new (open) post month.
Edit Record/Remove Line
If necessary, edit existing invoice lines by
 selecting line from grid and clicking Edit Record; this will open the related
 work completed form, allowing you to make necessary edits.
To remove an invoice line that you do not want included with this invoice, select the line and click Remove Line. This will remove the work completed line from the invoice, but leave it available for invoicing at a later time.
Preview/Process
Click the Preview button to review and/or print the
 invoice before you process it. If ready to process the invoice, click Process. The system
 will create an AR Invoice Entry batch and display the [AR Batch Process](/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/about-the-ar-batch-process-form) form. Then validate the batch, run/print
 the audit reports, and post the batch.

## Payment Type

Payment Type drop-down list on the Info tab of the SM Invoice
 Review form.
Select the payment type (A-On Account,
 C-Cash, X-Credit Card) to restrict by.

- When A-On Account is selected, Payment
 Amount and Payment Ref. fields are
 disabled.

- When C-Cash or X-Credit Card
 payment type is selected, the Payment Amount defaults to the balance due on
 the invoice.

## Payment Amount

Payment Amount field on the Info tab of the SM Invoice Review
 form.
Enter a payment amount.
This field is editable when either the C-Cash or
 X-Credit Card Payment Type option is selected.
This field defaults to the balance due on the invoice. You can edit the amount; but the
 amount cannot exceed the balance of the invoice.

## Ref Number

Ref. Number field on the Info tab of the SM Invoice Review
 form.
Enter a payment reference number, if applicable.

## Is Adj

Appears in the detail section of the SM Invoice review form.
checkbox indicates that cost adjustment to an Equipment, Labor, Miscellaneous or Inventory Work Completed line has been created for this work order line number.

## Orig Line #

Appears in the detail section of the SM Invoice Review form.
The original work order line number appears in this field if there has been a cost adjustment made to this line.

## Seq

For the default recipient, this field defaults the system-assigned sequence number and cannot be changed.
If adding a new recipient, enter N or ; the
 system will automatically assign the next sequential number.

## Bill

Select this checkbox to indicate this invoice serves as the bill for the specified recipient. Defaults as selected for the default recipient (defined in SM Customers). You will generally only select this checkbox for recipients that are responsible for payment of the invoice.
Do not select this checkbox if this invoice is not a bill for the specified recipient. You will typically leave this checkbox unselected for all recipients that are only receiving a copy of the invoice for informational purposes.
Note: This checkbox is informational only.

## Delivery Method

Indicate the delivery method for the selected recipient. Defaults the delivery method selected in SM Customers.

- P-Print — Select this option to print invoices for delivery via postal mail.

- E-Email — Select this option to deliver invoices via email.

## Deliver To

The Deliver To drop-down on the SM Invoice Review form, Recipients tab.
Select the deliver to recipient for this invoice.

- AR Customer - Select this option to send all invoices to the AR customer using the billing address or email address defined in AR Customers.

- Service Site - Select this option to send invoices to the service site using the address or billing email defined in SM Service Sites.
Note: You can only select this option if you chose the S-One per service site, W-One per work order, or P-One per work order scope invoice grouping option in SM Customers.

- Other - Select this option to send invoices to an address or email other than that of the AR customer or service site. Use the Email, Name, and Address fields to indicate the delivery email address, recipient name, and/or mailing address.

This field defaults as follows:

- If this is a work order invoice, this field defaults the Deliver To option selected in SM Customers.

- If this is an agreement invoice and the Deliver To option in SM Customers is AR Customer or Other, this field defaults the specified Deliver To option.

- If this is an agreement invoice and the Deliver To option in SM Customers is Service Site, this field defaults as follows:

- If the agreement is associated with a single service site, this field defaults as Service Site. The delivery email or address will be pulled from the service site.

- If the agreement is associated with multiple service sites and this invoice is not for an agreement service flagged as "periodic, billed separately", the customer setting is overridden and this field defaults as AR Customer. The delivery email or address will be pulled from AR Customer.

- If the agreement is associated with multiple service sites, but this invoice is for an agreement service that is flagged as "periodic, billed separately", this field defaults as Service Site. The delivery email or address will be pulled from the service site associated with the agreement service.

## Name

Required.
Enter the name of the individual or company to whom you will be mailing or emailing this invoice.
This field defaults based on the Deliver To
 option selected for the recipient sequence. If the Deliver To option is:

- A- AR Customer, this field defaults the name from AR Customers. This applies to both work order and agreement invoices.

- O-Other, this field defaults the Other name defined in SM Customers. This applies to both work order and agreement invoices. If you are adding a new recipient, this field defaults as blank

- S-Service Site, and this is a work order invoice, this field defaults the site description from SM Service Sites. For agreement invoices, this field will default the name from AR Customers (if multiple service sites exist for the agreement) or the site description from SM Service Sites (if a single service site exists for the agreement or the agreement service is flagged as "periodic, billed separately). See the F1 help for the [Deliver To](/en/vista/vista/service-management/sm-invoices/service-management-invoice-forms/sm-invoice-review-form/field-definitions-sm-invoice-review-form#ID-00040f18--en) field for more information.

## Email

Required if Delivery Method is E-Email.
Enter the email address to use for this recipient.
 This field defaults based on the Deliver To
 option selected for the recipient sequence. If the Deliver To option is:

- A- AR Customer, this field defaults the email address from AR Customers. This applies to both work order and agreement invoices.

- O-Other, this field defaults the Other email address defined in SM Customers. This applies to both work order and agreement invoices. If you are adding a new recipient, this field defaults as blank.

- S-Service Site, and this is a work order invoice, this field defaults the email address from SM Service Sites. For agreement invoices, this field will default from AR Customers (if multiple service sites exist for the agreement) or SM Service Sites (if a single service site exists for the agreement or the agreement service is flagged as "periodic, billed separately). See the F1 help for the [Deliver To](/en/vista/vista/service-management/sm-invoices/service-management-invoice-forms/sm-invoice-review-form/field-definitions-sm-invoice-review-form#ID-00040f18--en) field for more information.

Note: You can enter multiple email addresses if applicable; however, you must separate
 them with a semi-colon (for example, jane.doe@email.com; johnd@email.com;
 joe.smith@email.com). The system will send an email to each address specified
 here.

## Address

Required if the Delivery Method
 field is set to P-Print.
The address fields default based on the
 Deliver
 To option selected for the recipient sequence. If the Deliver To option is:

- A- AR Customer, this field defaults the billing address from AR Customers. This applies to both work order and agreement invoices.

- O-Other, this field defaults the Other address defined in SM Customers. This applies to both work order and agreement invoices. If you are adding a new recipient, this field defaults as blank.

- S-Service Site, and this is a work order invoice, this field defaults the billing address from SM Service Sites. For agreement invoices, this field will default from AR Customers (if multiple service sites exist for the agreement) or SM Service Sites (if a single service site exists for the agreement or the agreement service is flagged as "periodic, billed separately). See the F1 help for the [Deliver To](/en/vista/vista/service-management/sm-invoices/service-management-invoice-forms/sm-invoice-review-form/field-definitions-sm-invoice-review-form#ID-00040f18--en) field for more information.

Enter the delivery address to use for this recipient:

- Address- Enter the street address.

- City - Enter the city.

- State - Enter a valid state (as defined in HQ States). The system validates the state based on the Default Country specified in HQ Company Setup for the active company. If not valid, an error displays, but entry is allowed. You must then enter a valid country for this state in the
 Country
 field.

- Zip Code - Enter the zip code or postal code, up to 12 digits.

- Country - Enter the 2-character country code. Entry in this field is required when the address exists outside the Default Country specified in HQ Company Parameters for the active company. Country must be valid for the specified state (e.g. state, province, territory, etc.) as defined in HQ States.

- Add'l Address - Enter additional address information for this recipient (e.g. suite number, apartment, etc.). If the recipient receives their mail at a PO Box, then you might enter the PO Box in the
 Address
 field above, and use this field to enter the street address.
If you have Internet access, you can click the Map button () to view the address using your default map site (
 Options
 ). If you did not specify a country, the system uses the
 Default Country
 defined in HQ Company Setup.
