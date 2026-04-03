---
title: "Create a Transaction Code for Credit Card Payments | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/service-tech/set-up-service-tech-mobile-credit-card-payment-collection/create-a-transaction-code-for-credit-card-payments"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/service-tech/set-up-service-tech-mobile-credit-card-payment-collection/create-a-transaction-code-for-credit-card-payments"
---

# Create a Transaction Code for Credit Card Payments

Create a transaction code that records credit card fee expenses as discounts.
When Stripe remits payments to you, they withhold a given percentage, resulting in a lesser amount than the full invoice. You can record this as a discount using the code you set up here.To set up the code:

1. Go to Accounts Receivable > Maintenance > Transaction Code File Maintenance.

1. Select New.

1. Enter a Transaction code and Description.

1. Set the Type to Payment.

1. Enter the G/L codes:

- G/L account code - where the cash funds from Stripe will reside.

- G/L discount taken code - where the Stripe service fee will be recorded.

- A/R G/L account code - your main A/R Trade code.

1. Select the Post to Cash Management checkbox and enter the Bank account code.

1. Select OK.

Use this code to record credit card processing fees when entering receivables.
