---
title: "Field Definitions: HQ Payment Terms Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form/field-definitions-hq-payment-terms-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form/field-definitions-hq-payment-terms-form"
---

# Field Definitions: HQ Payment Terms Form

The following is a list of field descriptions for the HQ
 Payment Terms form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Payment Terms

 Enter a code, up to 10 characters, that will identify the payment terms used for calculating due dates, discount dates, and discount amounts when posting invoices.

[](/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form)HQ Payment Terms

##  Description

 Enter a description of the payment terms, up to 30 characters.

[](/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form)HQ Payment Terms

##  Discount Date

 Indicate which method will be used to determine the discount date for each month.

- Days Until Discount - Select this option if you want the discount date to be calculated based on a specific number of days after the invoice date. Use the field to the right to indicate the number of days.

- Discount Day - Select this option if you want to specify a set date of each month that will be used as the discount date. Use the field to the right to indicate the day.

- None - Select this option if not using discounts.

[](/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form)HQ Payment Terms

##  Days Until Discount

 Enter the number of days (0-120) past the invoice date that will be used to calculate the discount date when posting invoices.

[](/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form)HQ Payment Terms

##  Discount Day

 Specify the day of the month (1-31) you wish to use as the default discount date. If you want the discount date to fall on the last day of the month, enter 31.

[](/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form)HQ Payment Terms

##  Due Date

 Indicate which method will be used to determine the payment due date for each month.

- Days Until Due - Select this option if you want the payment due date to be calculated based on a specific number of days after the invoice date. Use the field to the right to indicate the number of days.

- Due Day - Select this option if you want to specify a set date of each month that will be used as the payment due date. Use the field to the right to indicate the day.

- None - Select this option if not using due dates.

[](/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form)HQ Payment Terms

##  Days Until Due

 Enter the number of days (0-120) past the invoice date that will be used to calculate the payment due date when posting invoices.

[](/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form)HQ Payment Terms

##  Due Day

 Specify the day of the month (1-31) you wish to use as the default payment due date. If you want the payment due date to fall on the last day of the month, enter 31.

[](/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form)HQ Payment Terms

##  Cutoff Day

 This field is only used if you specified a Discount Day and/or Due Day.
 Specify the day of the month (1-31) used as a cutoff when calculating payment due dates and discount dates. This day will be used in conjunction with the ‘Roll Ahead Two Months After Cutoff Day’ flag to determine the discount and due dates for invoices.
If the Roll Ahead Two Months After Cutoff Day flag is Y (checked):

- and the invoice date is after the cutoff date, the discount and/or due date will default to the specified date of the month after next

- and the invoice date is on or before the cutoff date, the discount date and/or due date will default to the specified day in the following month. .

If the Roll Ahead Two Months After Cutoff Day flag is N (unchecked):

- and the invoice date is on or before the cutoff date, the discount date and/or due date will default to the specified day in the same month.

- and invoice date is after the cutoff date, the discount and/or due date will default to the specified date of the following month.

Note:If the discount date falls after the due date, it will be set equal to the due date, regardless of whether you elect to roll discount dates and due dates ahead two months after the cutoff day.

[](/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form)HQ Payment Terms

##  Discount Percent

 Enter the default discount rate. If no discount rate applies, enter 0.00. This rate is used to calculate a default discount amount on AR and AP invoices.

[](/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form)HQ Payment Terms

##  # Months to Roll Ahead After Cutoff Day

 Enabled only if you specified a Discount Day and/or Due Day
 Using the drop-down menu, specify whether to roll the due date ahead 1, 2, or 3 months after the cutoff day. Based on the number of months specified here, the discount and due dates will be calculated as follows (blue represents ‘before’ cutoff day, green represents ‘after’ cutoff day):
 Due Day: 30
 Discount Day: 10
 Cutoff Day: 20

Roll Ahead Mths
Inv Date
Disc Date
Due Date

 1
02/05/09
02/10/09
02/28/09

02/21/09
03/10/09
03/30/09

 2
02/05/09
03/10/09
03/30/09

02/21/09
04/10/09
03/30/09

 3
02/05/09
04/10/09
04/30/09

02/21/09
05/10/09
05/30/09

[](/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form)HQ Payment Terms

##  Discount Based on Material

 For use with Material Sales only.
 Check this box if discounts for these payment terms will be material based. Material Sales invoices referencing these payment terms will have discounts calculated using:

- the method and discount rate/amount specified for the material on a quote (if a quote exists for the job, customer, or inventory location) or,

- the rate/amount specified for the customer (in AR Customers) if no quote exists or,

- the payment discount type and rate/amount specified for the material in HQ Materials if no rate/amount specified for customer.

 Leave this box unchecked if discounts for these payment terms will be rate based. Material Sales invoices referencing these payment terms will have discounts calculated using the “Discount Percent” specified for the payment terms.

[](/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form)HQ Payment Terms

##  Invoice Date

 Enter an invoice date with which to test discount date and due date calculations. Click the Calc Dates button to calculate the test discount and due dates (displayed below) based on the setup for the current payment terms.

[](/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form)HQ Payment Terms
