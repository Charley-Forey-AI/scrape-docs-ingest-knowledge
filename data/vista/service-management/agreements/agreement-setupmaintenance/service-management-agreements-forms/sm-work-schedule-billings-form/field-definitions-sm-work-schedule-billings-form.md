---
title: "Field Definitions: SM Work Schedule Billings Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-work-schedule-billings-form/field-definitions-sm-work-schedule-billings-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-work-schedule-billings-form/field-definitions-sm-work-schedule-billings-form"
---

# Field Definitions: SM Work Schedule Billings Form

The following is a list of field descriptions for the SM Work
 Schedule Billings form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Basis

The Basis field on the SM Work Schedule Billings form
Enter the tax basis for this sequence. The
 Amount field will update with the tax amount after invoicing.

## Billing Amount

The Billing Amount field on the SM Work Schedule Billings form.
Enter the billing amount for this billing sequence (equal to or greater than 0.00). When running the periodic billing process, this is amount that will print on the invoice for the customer.
When you have completed entering billing sequences, the Total Remaining amount must equal 0.00. If it does not, you must adjust the billing sequences until it does.
Note: The amount you specify will depend on the service price, the term of the associated agreement, and your billing frequency. For example, if the service amount is $10,000 and it is a 2-year agreement that you bill annually, you would set up two billing sequences and enter $5,000 here for each sequence.If this is a non-expiring agreement, the amount you specify will depend on the service price, the pricing frequency, and your billing frequency. For example, if the service price is $10,000 with a pricing frequency of A-Annually, and you bill quarterly, you would set up four billing sequences and enter $2,500 here for each sequence. The system will continue this quarterly cycle each year until you terminate the agreement.

## Billing Seq

The Billing Seq field on the SM Work Schedule Billings form.
Enter N, New, or + to have
 the system automatically assign the next sequential number available (based on highest
 existing billing sequence for this service).

## Date

The Date field on the SM Work Schedule Billings form.
Required.
Enter the billing date for this sequence.
Note: When running the periodic billing process, the system uses this date to determine which services are due for billing.

## Tax Code

The Tax Code field on the SM Work Schedule Billings form.
Required if a Tax Type is specified (previous field).
Enter a tax code for this sequence. Must be a valid tax code for the specified tax type. Press
 F4
 for a list of valid tax codes.
Note: If you specified a tax type of 3-VAT, you must enter a
 VAT tax code (i.e. tax code with the Value Added Tax (VAT) box checked in HQ
 Tax Codes).

## Tax Type

The Tax Type field on the SM Work Schedule Billings form.
Select the tax type for this work schedule billing or leave blank (default) if taxes are not applicable.

- 1 - Sales

- 2 - Use

- 3 - VAT
Note: For Australian and Canadian companies (where SM company's AR
 company is set up with a Default Country of AU or CA in HQ
 Company Setup), the Tax Type defaults to 3-VAT.
