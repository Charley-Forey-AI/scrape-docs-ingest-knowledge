---
title: "Field Definitions: SM Agreement Invoice Review Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/sm-invoices/service-management-invoice-forms/sm-agreement-invoice-review-form/field-definitions-sm-agreement-invoice-review-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/sm-invoices/service-management-invoice-forms/sm-agreement-invoice-review-form/field-definitions-sm-agreement-invoice-review-form"
---

# Field Definitions: SM Agreement Invoice Review Form

The following is a list of field descriptions for the SM
 Agreement Invoice Review form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Seq

This field defaults the system-assigned sequence number for this invoice. This number cannot be changed.

## Invoice No

This field automatically defaults a system-generated invoice number. Accept the default or enter a new invoice number. Up to 10 characters allowed.

- The system generated invoice number is based on the
 Last
 Invoice Number field in AR Company Parameters; overriding the default
 will not update this field.

- If you override the default with an invoice number that already exists in the SM company (for any customer), you will receive a warning that the number already exists and entry will not be saved.

## Bill To

This field defaults the customer associated
 with the agreement or the alternate "bill to" customer defined for the agreement's
 customer. Accept the default or enter the customer to which this invoice will be sent.
 Press F4 for a list of valid AR customers.

## Alternate Billing Address

Alt. Addr. field on the SM Agreement Invoice Review form Info tab.
Enter the Alternate Billing Address Sequence
 number created in [ AR Customers](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form). Press F4 for the Accounts Receivable Alt
 Billing Address Lookup form. Press F5 to access the AR Customers form where
 alternate billing addresses are maintained.

## Bill Address

The billing address fields default from the
 Billing
 Address field in AR Customers for the "bill to" customer. Accept the default
 or enter the new billing address.

- Address- Enter the street address.

- City - Enter the city.

- State - Enter a valid state (as defined in HQ
 States). The system validates the state based on the Default Country specified in HQ
 Company Setup for the active company. If not valid, an error displays, but entry is
 allowed. You must then enter a valid country for this state in the Country
 field.

- Zip Code - Enter the zip code or postal code, up to 12 digits.

- Country - Enter the 2-character country code. Entry in this field is required when the address exists outside the Default Country specified in HQ Company Parameters for the active company. Country must be valid for the specified state (e.g. state, province, territory, etc.) as defined in HQ States.

- Add'l Address - Enter additional address information
 for this recipient (e.g. suite number, apartment, etc.). If the recipient receives
 their mail at a PO Box, then you might enter the PO Box in the Address
 field above, and use this field to enter the street address.

## Pay Terms

Required.
Enter the payment terms to use for this agreement invoice. Pay terms are used to calculate the invoice due and discount dates. Initially defaults the pay terms assigned to the "bill to" customer in AR Customers or as blank if no pay terms are defined for the customer.
Note: The system does not require pay terms be assigned to the invoice; however, if you leave the pay terms blank, you will be required to enter an invoice due date before you process the invoice.

## Custom Invoice Report

Enter the identification number of the custom
 invoice report to use for previewing and/or delivering this invoice or accept the default.
 Press F4 to select from a list of valid custom reports.
This field initially defaults from the
 Invoice
 Format field in SM Agreements. If you did not specify a custom report for
 the agreement, the system defaults the Def. Agreement Inv. Report specified in
 SM Company Parameters or blank if a default agreement invoice is not defined for the
 company.
If this field is blank, the system will automatically use the standard SM Agreement Invoice report.

## Description

Use this field to enter a description of the work included on this agreement invoice (e.g. reason for billing). The space allowance is virtually unlimited; however, the information entered here will print on the invoice, so it is suggested that you limit entry to only that information that is important to include on the invoice.

## Invoice Date

Enter the date for this invoice or accept the default date.
This field will default the "due date" shown in the invoice grid for the selected billing. The due date is based on the billing schedule defined for the agreement in SM Agreements.
 For example, say you set up quarterly billings of 3/10/12, 6/10/12, 9/10/12, and 12/10/12. In March, you generate invoices for all billings for that year. The invoice dates will default as 3/10/12, 6/10/12, 9/10/12, and 12/10/12, regardless of the date on which you generate the invoices.

## Due Date

Enter the due date for this invoice. Initially defaults a due date based on the payment terms assigned to this invoice.
Note: If no pay terms are specified for this invoice, you must enter a due date. Otherwise, you will be unable to process the invoice.

## Disc Date

Enter the discount date for this invoice. Initially defaults a discount date based on the payment terms specified for this invoice.

## GL Month

Required.
Enter the month and year (MM/YY) to which the GL entries will be posted when this invoice is processed. Defaults the current month/year.

-  The selected month and year cannot be closed. Months are closed using the [GL Month End Close ](/en/vista/vista/accounting/general-ledger/gl-setup-and-maintenance/about-the-gl-month-end-close-form) form.

-  If multiple invoices exist in the batch and more than one unique GL Month exists, a separate invoice batch will be created for each unique GL month.

## Print Invoice

This checkbox is enabled only for invoices
 that have not been processed and sent to AR (i.e. Status is Pending).
Check this box to print this invoice once processed (default). When you post the invoice batch, the system automatically displays the Print screen, allowing you to print the invoice.
Leave this box unchecked if you do not want to print the invoice immediately upon processing; the system will not automatically display the Print screen once the invoice batch is posted. However, you can still print the invoice via SM Invoices.

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

- S-Service Site, and this is a work order invoice, this field defaults the site description from SM Service Sites. For agreement invoices, this field will default the name from AR Customers (if multiple service sites exist for the agreement) or the site description from SM Service Sites (if a single service site exists for the agreement or the agreement service is flagged as "periodic, billed separately). See the F1 help for the [Deliver To](/en/vista/vista/service-management/sm-invoices/service-management-invoice-forms/sm-agreement-invoice-review-form/field-definitions-sm-agreement-invoice-review-form#ID-00040f18--en) field for more information.

## Email

Required if Delivery Method is E-Email.
Enter the email address to use for this recipient.
 This field defaults based on the Deliver To
 option selected for the recipient sequence. If the Deliver To option is:

- A- AR Customer, this field defaults the email address from AR Customers. This applies to both work order and agreement invoices.

- O-Other, this field defaults the Other email address defined in SM Customers. This applies to both work order and agreement invoices. If you are adding a new recipient, this field defaults as blank.

- S-Service Site, and this is a work order invoice, this field defaults the email address from SM Service Sites. For agreement invoices, this field will default from AR Customers (if multiple service sites exist for the agreement) or SM Service Sites (if a single service site exists for the agreement or the agreement service is flagged as "periodic, billed separately). See the F1 help for the [Deliver To](/en/vista/vista/service-management/sm-invoices/service-management-invoice-forms/sm-agreement-invoice-review-form/field-definitions-sm-agreement-invoice-review-form#ID-00040f18--en) field for more information.

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

- S-Service Site, and this is a work order invoice, this field defaults the billing address from SM Service Sites. For agreement invoices, this field will default from AR Customers (if multiple service sites exist for the agreement) or SM Service Sites (if a single service site exists for the agreement or the agreement service is flagged as "periodic, billed separately). See the F1 help for the [Deliver To](/en/vista/vista/service-management/sm-invoices/service-management-invoice-forms/sm-agreement-invoice-review-form/field-definitions-sm-agreement-invoice-review-form#ID-00040f18--en) field for more information.

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
