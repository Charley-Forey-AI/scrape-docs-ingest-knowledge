---
title: "Set Up Service Tech Mobile Credit Card Payment Collection | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/service-tech/set-up-service-tech-mobile-credit-card-payment-collection"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/service/service-tech/set-up-service-tech-mobile-credit-card-payment-collection"
---

# Set Up Service Tech Mobile Credit Card Payment Collection

The steps to set up Spectrum and to enable service technicians to collect credit card payments in the field using a mobile device at the time of service.
Technicians can send credit card payment links to customers from Service Tech Mobile with Stripe®, our preferred credit card payment partner.Note:Trimble is not a payment card services provider or a financial institution. Trimble is not responsible for payments processed through Stripe Connect and will not conduct any activity on your behalf in your Stripe Connect account. At no time will Trimble have access to payment card numbers through your use of Stripe Connect with Spectrum Service Tech Mobile. Trimble does not share any personal information with Stripe and does not have access to any personal information that you provide directly into Stripe.

Enabling credit card payments has these main steps:

- Establish an account with Stripe to access Stripe Connect credit card services via Service Tech Mobile, and obtain required information from them.

- Enter values in Spectrum's Service Tech Installation screen, some of which is information you get from Stripe.

- Grant security access to specific Service Tech Mobile users to send credit card payment collection emails in the field.

- Set up work order invoices to be derived from the work order number.

- Create a dedicated Transaction Code.

- Create a dedicated default Dispatch Code.

1. Establish an account with Stripe.

1. Submit a case to Support with the subject "Stripe Account Setup Request." We will respond by sending an initial Stripe Connect URL (sent directly from Stripe), inviting you to set up your Stripe Connect account under your company name.

1. At the URL, follow the steps provided by Stripe and enter the requested information to set up your Stripe account.

1. Obtain and make note of your Stripe Account ID. It is formatted as acct_, followed by a string of alphanumeric characters.

1. Enter the necessary field values in Spectrum's Service Tech Installation screen.

1. Go to System Administration > Installation > Service Tech.The Service Tech Installation screen opens.

1. In the Paid by credit card field, choose the default dispatch status code designated for credit card payment collection.In the Excluded Status Codes grid, Spectrum automatically selects the checkbox in the Exclude column pertaining to your chosen credit card payment collection dispatch status code.

1. Select the Enable mobile payment collection? checkbox.An additional field appears.

1. In the Account ID field, enter the account number you received from Stripe.

1. Select Save.

1. Grant security access to whichever service technicians should have the ability to collect credit card payments using the Service Tech Mobile application. You can approach this in one of several ways; two options are explained here.Note: By default, all users with access to security category FT level 6 and higher have access to mobile payment collection. If you have users with a lower level of access, you may opt between increasing all mobile users' level to 6, or decreasing the security level of the feature, or you may want to leave levels as they are and instead adjust each operator's access.

- Change individual technicians' FT Category permission:

1. Go to System Admin > Security > Operator Maintenance.

1. Locate and select the operator record, and then select Edit.

1. In the Categories tab, locate the FT row and set the security level to 6 or higher.

- Change multiple technicians' permission at the feature level:

1. Go to System Admin > Security > Function Security.

1. In the left panel, select Service Tech.

1. Locate and expand the Service Tech Capture Signature row.

1. In the Service Tech Credit Card Collection row, select the person icon.

1. Add operator codes to give specific users the ability to collect payment no matter the number currently assigned to them.

Once you've granted proper access, technicians can see and use the payment tile in the Service Tech Mobile app.

1. Make it easier to match work order payments to invoices.

1. Go to System Admin > Installation > Work Order > Properties.

1. In the Accounts receivable invoice # field, select Work order number.From now on, the system will create the invoice number using the work order number.Note: If a work order number happens to be the same as an already-existing invoice for the same customer, the system appends a letter to the number to maintain unique numbers. For example, if invoice 234 has already been posted, work order 234 will result in an invoice of 234A.

1. [Create a Transaction Code](/en/spectrum/spectrum/service/service-tech/set-up-service-tech-mobile-credit-card-payment-collection/create-a-transaction-code-for-credit-card-payments) to record Stripe fees as customer discounts.

1. [Create a Default Dispatch Status Code](/en/spectrum/spectrum/service/service-tech/set-up-service-tech-mobile-credit-card-payment-collection/create-a-dispatch-status---paid-by-credit-card) that Spectrum should assign to the work order once the service tech collects credit card payment in the field.

With these setup steps complete, applicable technicians with an active internet connection can send credit card payment collection emails using the STM app on their mobile device. Once the recipient makes the payment, the work order becomes inaccessible in the mobile app.
As needed, refer technicians to [Collect Credit Card Payments using a Mobile Device](/en/spectrum/spectrum/service/service-tech/mobile-overview/collect-credit-card-payments-using-a-mobile-device).
