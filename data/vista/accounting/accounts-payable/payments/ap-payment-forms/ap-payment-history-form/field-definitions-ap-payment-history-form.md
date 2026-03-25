---
title: "Field Definitions: AP Payment History Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-history-form/field-definitions-ap-payment-history-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-history-form/field-definitions-ap-payment-history-form"
---

# Field Definitions: AP Payment History Form

The following is a list of field descriptions for the AP Payment History form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## CM Account

 Enter the CM bank account that made the payment.

## CM Reference

Enter the CM reference number for this
 payment. If the Payment Method field is set to:

- C-Check, enter the check number.

- E-EFT, enter the EFT number.

- S-Credit Service, the system
 automatically creates a reference number during the process of payment posting.

## CM Ref Seq#

Enter the reference sequence number.

- If a check payment, this can be any number, but is usually zero (0).

- If an EFT or credit service payment, this number must be zero (0).

Once you enter a value in this field, and if you are referencing an existing payment, all information about the payment displays on the form.

## EFT Seq#

 If the Payment Method is ‘E’, enter the EFT sequence number. This number identifies each vendor’s payment within a single EFT.
 Once you enter a value in this field, and if you are referencing an existing payment, all information about the payment displays on the form.

## Payment Method

Payment Method drop down in the AP Payment History form.

Select the payment method. This could be for a payment record you are entering for the first time or for locating a payment that already exists.

- N-ePayments (U.S. only)Vista retains payment method N-ePayments even after you have processed your response file, which places values in the ePayments fields on the Add'l Info tab.

- C-Check

- E-EFT

- S-Credit Service

Related information

- [ePayments](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-history-form/field-definitions-ap-payment-history-form#ID-000062ba--en)

## Payee - Vendor

 Enter the payee’s vendor number or sort name.
 If you are referencing an existing payment, this field is inaccessible and defaults the vendor name associated with the payment.

## Name

 This field defaults the vendor name associated
 with the vendor number entered in the Payee – Vendor field (AP Vendors).
 Enter the payee’s name or accept the default. If you are referencing an existing payment, this field is inaccessible.

## Add'l Info

The Add'l Info field in the
 AP Payment History form
The default value for this field comes from the Add'l Info
 field in the AP Vendors form. You may override this value, up to 60 characters.
If you are viewing an existing payment, this field is inaccessible and displays whatever was in the field at the time the payment was posted.

## Address

 This field defaults the Payment Address for this vendor (defined in AP Vendors).
 Enter the payment address or accept the default. If you are referencing an existing payment, this field is inaccessible.

## City

 This field defaults the Payment Address city for this vendor (defined in AP Vendors).
 Enter the city or accept the default. If you are referencing an existing payment, this field is inaccessible.

## State

This field defaults the Payment Address state for this vendor (defined
 in AP Vendors).
Enter a valid state (as defined in HQ States)
 or accept the default. If you are referencing an existing payment, this field is
 inaccessible.
The system validates the state based on the
 Default Country specified in HQ Company Parameters for the active company. If not valid, an
 error displays, but entry is allowed. You must then enter a valid country for this state in
 the Country field.

## Zip Code

 This field defaults the Payment Address zip
 code for this vendor (defined in AP Vendors).
 Enter the zip code or accept the default. If you are referencing an existing payment, this field is inaccessible.

## Country

This field defaults the Payment Address country for this vendor
 (defined in AP Vendors).
Enter the 2-character country code or accept the default. If you are referencing an existing payment, this field is inaccessible.
Entry in this field is required when the address exists outside the Default Country specified in HQ Company Setup for the active company. Country must be valid for the specified state (e.g. state, province, territory, etc.) as defined in HQ States.

## Paid Date

 Enter the payment date. If you are referencing an existing payment, this field is inaccessible and defaults the payment date.

## Paid Month

 Enter the payment month. If you are referencing an existing payment, this field is inaccessible and defaults the payment month.

## Payment Total

 Enter the net amount of this payment (gross minus discount, if applicable). If you are referencing an existing payment, this field is inaccessible and defaults the payment total.

## 2nd Party - Vendor/Supplier

 If you made this payment with a 2-party check, enter the vendor/supplier number of the second party. If you are referencing an existing payment, this field is inaccessible and automatically defaults.

## Payment has been voided

Select this checkbox if you voided the payment. If you are referencing an existing payment, this checkbox is inaccessible and will be checked if you previously voided the payment.
This field is informational only and does not
 void the payment within the system. To void a payment in the system, use either AP Void
 Payments or AP Prior Month Payment Reversal. For more information on these forms, refer to
 Related Topics below.

Related information

- [AP Void Payments Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-void-payments-form)

- [AP Prior Mth Payment Reversal Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-prior-mth-payment-reversal-form)

## Void Memo

Enter miscellaneous note or information about
 this voided check, up to 255 characters. If you are referencing an existing payment, this
 field is inaccessible.

## Credit Services

Credit Services section in the AP Payment History form, Add'l Info tab
These read-only fields apply to payments made using Comdata. You can filter on the field values on the grid tab.
These three fields display credit card information for successful payments:

- Card Number

- Expire Date

- CVC

These two fields display error code information for failed credit card payments:

- Error Code

- Error Code Description

## ePayments

The Paid Date, Pay Method, and Pay Reference fields on the AP Payment History form, Add'l Info tab.

These display-only fields apply to payments made using ePayments.
The values in these fields come from Corpay's response file. Each time you open this form, Vista checks whether Corpay has a response file ready for your company. When Vista retrieves one or more response files, the AP Payment History form header displays a message in red-colored text.
If the response file contains information for this record, Vista inserts it when you select Tasks > Update Payment History - ePayments.

Related information

- [AP ePayments Export Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-epayments-export-form)
