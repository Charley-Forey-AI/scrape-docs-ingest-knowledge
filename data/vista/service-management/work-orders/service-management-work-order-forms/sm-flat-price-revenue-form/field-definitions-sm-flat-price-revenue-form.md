---
title: "Field Definitions: SM Flat Price Revenue Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-flat-price-revenue-form/field-definitions-sm-flat-price-revenue-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-flat-price-revenue-form/field-definitions-sm-flat-price-revenue-form"
---

# Field Definitions: SM Flat Price Revenue Form

The following is a list of field descriptions for the SM Flat
 Price Revenue form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Seq

Seq field on the SM Flat Price Revenue form.
Enter N, New, or + to add a new revenue sequence.
Note: This field is disabled for split revenue entries on an approved work order quote or an agreement service that has been activated.

## Cost Type Category

Cost Type Category drop-down on the SM Flat Price Revenue form.
Required.
Select the cost type category for this revenue sequence.

- L-Labor

- E-Equipment

- M-Material

- O-Other

- S-Subcontract

Note: This field is disabled for split revenue entries on an approved work order quote or an agreement service that has been activated.

## Cost Type

Cost Type field on the SM Flat Price Revenue form.
Enter the SM cost type for this revenue sequence. The cost type must be valid for the specified cost type category (i.e. have a cost type category of L-Labor in SM Cost Types). The only exception is if you specified a Cost Type Category of O-Other; this category allows entering any cost type, regardless of it's category.
Leave this field blank if you do not want a further breakdown of revenue for this sequence by cost type.
Note: This field is disabled for split revenue entries on an approved work order quote or an agreement service that has been activated.

## Price Percent

Price Percent field on the SM Flat Price Revenue form.
Enter the percentage of flat price revenue to apply to the specified cost type and/or cost type category (enter 50% as 50.00).
Work Scopes
The sum of all entries in the grid must equal 100.00% (leaving a
 Percent Remaining
 of 0.00). If they do not, upon closing the form, the system will display a message indicating that percent remaining must be 0 or 100. You will be unable to close the form until either of these values are met.
Agreement Services, Quotes, and Work Orders
Once you enter a percent, the system will automatically calculate a revenue amount (next field) based on this percentage and the flat price amount. If you prefer to enter a fixed amount, leave this field blank and enter a value in the
 Amount
 field. The system will automatically calculate the percentage based on the amount specified and the flat price amount.
The sum of all entries in the grid must equal
 100.00% (leaving a Total Remaining amount of 0.00). If they do not, upon closing the form, the
 system will display a message indicating that the split price doesn't match the flat price,
 and asking if you want to update the flat price. If you click Yes, the system will
 automatically update the flat price to equal the total of all entries in the grid. If you do
 not want the flat price adjusted, click No. Then either add additional entries or
 adjust the existing entries as applicable.
Note: This field is disabled for split revenue entries on an approved work order quote or an agreement service that has been activated.

## Amount

Amount field on the SM Flat Price Revenue form.
This field is not available for work scopes (i.e. when form is accessed from SM Work Scopes).
Enter the amount of the flat price (specified
 for the quote sequence, work order sequence, or agreement service) to apply to the
 specified cost type and/or cost type category. If you specified a Price Percent,
 this field automatically defaults an amount based on the specified percent and the flat
 price amount. Overriding the amount will cause the Price Percent to be recalculated.
The total amount of all entries in the grid
 must equal the flat price (leaving the Total Remaining at 0.00). If they do not,
 upon closing the form, the system will display a message indicating that the split price
 doesn't match the flat price, and asking if you want to update the flat price. If you click
 Yes, the system will automatically update the flat price to equal the total of all entries
 in the grid. If you do not want the flat price adjusted, click No. Then either
 add additional entries or adjust the existing entries as applicable.
Note: This field is disabled for split revenue entries on an approved work order quote or an agreement service that has been activated.

## Taxable

Taxable checkbox on the SM Flat Price Revenue form.
Select this checkbox if this split revenue entry is taxable. Quotes and work orders flagged as taxable will calculate the tax amount based on all split revenue amounts that are flagged as taxable.
Do not select this checkbox if the revenue amount is not taxable.
This checkbox initially defaults as selected for all cost type categories except Labor. If you also specified a Cost Type for the revenue sequence, this flag will default based on the Taxable setting for the cost type (e.g. if the cost type is not taxable, this checkbox will default as unchecked.
Note: This field is disabled for split revenue entries on an approved work order quote or an agreement service that has been activated.
