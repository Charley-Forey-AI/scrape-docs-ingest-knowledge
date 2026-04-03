---
title: "Vendor Payment Setup - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-main-properties/about-vendor-payment-setup/vendor-payment-setup---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-main-properties/about-vendor-payment-setup/vendor-payment-setup---field-descriptions"
---

# Vendor Payment Setup - Field Descriptions

Use this table for reference when completing the fields on this screen.
Fields/ButtonsDescriptions
Vendor codeEnter the desired vendor code.
SwitchSelect to quickly switch to a different vendor.
Payment methodIf you want to change the payment method from ePayments to Check on multiple vendors at once, go to Accounts Payable > Utilities > Reset ePayments Vendor to Check.
Select the payment method you would like to use:

- Select ePayments to
 include this vendor in the ePayments export file. The vendor address
 and account reference must be entered on the [Vendor Main Properties](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-main-properties) screen before selecting this
 option.

- If the Cash Management module is not present, only the Print check option is available.

- Only vendors set up for the payment method identified when the processing group was initiated will be included.

- If
 the vendor has a relationship with Comdata, select Comdata; otherwise leave this checkbox clear. This is for informational use only and does not affect
 Spectrum's payment processing.
 See also [Comdata Processing Guide](https://trimble.deploy.heretto.com/v4/deployments/mVyHSMAo9PbkfqcxUBWF/object/f496dede-a1cf-45dd-8801-2ec78df6bb57?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2pvcnNlay5jb20vZXpkX29yZ2FuaXphdGlvbiI6InZpZXdwb2ludCIsImh0dHBzOi8vam9yc2VrLmNvbS9lemQvb2JqZWN0X3V1aWQiOiJmNDk2ZGVkZS1hMWNmLTQ1ZGQtODgwMS0yZWM3OGRmNmJiNTciLCJleHAiOjE3NzUzMzIyNTcsImp0aSI6Ijg4NWI0NThjMjlmYzRjMWJiMGI2NWJkNzk3MjVlNmVmIiwiaHR0cHM6Ly9qb3JzZWsuY29tL2V6ZF9maWxlc2V0IjoiOE1GRmpJZEw3ZEZLQmJiVGwxTXMifQ.Qz3Vfq732HHQyi2ba9OQMCM6-DCdS2KTxF-46yAwMbQ&response-content-disposition=filename%3D%22Comdata_Virtual_Card_Processing_rev0619.pdf%22).

Electronic payment details
When either the Electronic payment or Print check / Send electronic pre-note
 payment method is selected above, the following fields display.Note: Canada does not support pre-notes.

Account codeEnter the vendors account code for ACH payment.
Account typeEnter the vendor's account type for the ACH payment, or use the drop-down list to select from a list of available account types.
Routing #Enter the vendor's ABA number for the ACH payment.
Credit cardNote: These checkboxes display only if the
 Cash Management module is installed.

Credit card issuer?Select this checkbox if the selected vendor is issued to pay the credit card
 bill for purchase of goods and services. Selecting this checkbox also
 prevents the user from accidentally trying to pay the credit card with
 itself.
Account codeEnter the credit card account number associated with this vendor. Entry in this field is required if the Credit card issuer checkbox on this screen is selected. It is important to use a scheme that will not compromise the actual card numbers in the event that a thief comes into contact with discarded reports.Viewpoint recommends that you enter the last four, five, or six digits of the
 account number or use the employee's initials with the last 4 credit card
 numbers. For example, Credit Card Account BOA1234 with Card Number AEO1234
 would protect against fraudulent credit card use.
