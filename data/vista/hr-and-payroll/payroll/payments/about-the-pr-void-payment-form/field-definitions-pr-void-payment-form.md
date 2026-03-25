---
title: "Field Definitions: PR Void Payment Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payments/about-the-pr-void-payment-form/field-definitions-pr-void-payment-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payments/about-the-pr-void-payment-form/field-definitions-pr-void-payment-form"
---

# Field Definitions: PR Void Payment Form

The following is a list of field descriptions for the PR Void
 Payment form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Clear/Void Option

-  Clear Check # (number can be reused) - Select this
 option to clear the check number so that it can be reused. When selected, the
 Void
 Memo field is disabled. Additionally, the system adds an entry to the
 PR Void Payments table with the Reuse flag set to “Y,”, but only if the current check
 has already been updated to CM. This entry is used by the CM update to remove the old
 check number from both CM and PR Payment History.

- Void Check # (number cannot be reused) - Select this option to record the old check as void and enter a Void Memo. When updated, an entry is added to the PR Void Payments table with the Reuse flag set to “N.” This records the old check as void.

##  Void Memo

 If the Record Existing Check as Void box is checked, then enter a Void Memo in this field.
