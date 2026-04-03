---
title: "Collect Credit Card Payments using a Mobile Device | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/service-tech/mobile-overview/collect-credit-card-payments-using-a-mobile-device"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/service/service-tech/mobile-overview/collect-credit-card-payments-using-a-mobile-device"
---

# Collect Credit Card Payments using a Mobile Device

Service technicians can collect payments on work orders in the field using a mobile device at the time of service.
Note:Trimble is not a payment card services provider or a financial institution. Trimble is not responsible for payments processed through Stripe Connect and will not conduct any activity on your behalf in your Stripe Connect account. At no time will Trimble have access to payment card numbers through your use of Stripe Connect with Spectrum Service Tech Mobile. Trimble does not share any personal information with Stripe and does not have access to any personal information that you provide directly into Stripe.

To collect credit card payments using a mobile device:

- Credit card payment collection functionality must be enabled in Spectrum. See [Set Up Service Tech Mobile Credit Card Payment Collection](/en/spectrum/spectrum/service/service-tech/set-up-service-tech-mobile-credit-card-payment-collection).

- An admin must grant you access in Spectrum.

- You must have an active internet connection to send the payment collection link to the recipient.

- The payer must have access to the email account you send the payment collection link.

To use the Service Tech Mobile (STM) application to send a payment collection link to the payer and collect payment:

1. Clock out, then clock back in.The work order retrieves your labor time and will include the applicable charges in the payment request.

1. Open the work order for which you want to collect payment.

1. Select Payments.A summary of labor, material, equipment, and other charges appears.

1. Using the payer's information, complete the Name and Email fields.

1. Select Request Payment.The STM app updates the payment status to Payment Initiated and sends the customer an email with the payment link.Note: If you navigate away from the page which now contains the Check payment status button, you will not be able to check the payment status later.

1. Inform the customer that they should have an email in their inbox and instruct them to use the link to make the payment by credit card.Stripe processes the payment.

If Stripe successfully collects payment:

- your mobile app provides a payment status update

- the Spectrum application assigns the default dispatch status to the work order

- the work order is no longer accessible in the mobile app.Note: If the payment was unsuccessful for any reason, you retain access to the work order.

If you repeat these steps for a given work order, the payment link remains the same, even if the payment request is sent again, and even if sent to another email recipient.
