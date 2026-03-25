---
title: "Field Definitions: AR Payment on Account Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-payment-on-account-form/field-definitions-ar-payment-on-account-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-payment-on-account-form/field-definitions-ar-payment-on-account-form"
---

# Field Definitions: AR Payment on Account Form

The following is a list of field descriptions for the AR Payment on Account form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Line #

 Enter the line number of an existing entry or enter N, New, or + to add a new line. The system will automatically assign the next sequential line number.

##  Description

 Enter a description of this payment transaction, up to 30 characters.

##  Rec Type

 This field is accessible only if the Allow Override of Receivable Type checkbox is selected in AR Company Parameters.
 Specify a valid receivable type (defined in AR Receivable Types) for this payment transaction. Defaults the receivable type assigned to the specified customer (in AR Customers). If the customer does not have an assigned receivable type, this field defaults the receivable type specified in AR Company Parameters.

##  Tax Code

 This field is accessible only if the Post Taxes on Payments checkbox is selected in AR Company Parameters.
 Specify the tax code (defined in HQ Tax Codes) to use for calculating tax on this payment transaction.

##  Amount

 Enter the amount of the total payment that is to apply to this “on account” transaction. This field defaults the amount in the Check Amount field on AR Cash Receipts.
 If applying a discount to this item, enter the pre-discount amount. For example, if the Total Amount to apply is 1000.00, and the Disc Taken is 50.00, enter 1050.00 here.
 If applying taxes to this item, enter the pre-tax amount. For example, if the Total Amount to apply is 1060.00, and the Tax Amount is 60.00, enter 1000.00 here.

##  Tax Basis

 This field is accessible only if the Post Taxes on Payments checkbox is selected in AR Company Parameters.
 If the taxable amount differs from the line’s Amount (previous field), specify the tax basis amount here.

##  Tax Amount

 This field is accessible only if the Post Taxes on Payments checkbox is selected in AR Company Parameters.
 The field defaults a tax amount based on the tax code and the tax basis (which may differ from the line’s amount).
The line’s Amount must reflex the pre-tax amount. For example, if the Total Amount to apply is 1060.00, and the Tax Amount is 60.00, enter 1000.00 as the line’s Amount. If you override the tax amount calculation, adjust the line’s Amount to ensure the Total Amount to be applied is accurate.

## Disc Taken

This field is accessible only if allowing discounts on receipts (flag in AR Company Parameters).
Specify the discount amount taken for this line item.
Note: The line’s Amount must reflect the pre-discount
 amount. For example, if the Total Amount to apply is 1000.00, and the Disc Taken is 50.00,
 the line’s Amount would be entered as 1050.00.
