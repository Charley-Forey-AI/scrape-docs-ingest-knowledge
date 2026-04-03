---
title: "Vendor Invoice Entry FAQs | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/troubleshooting/frequently-asked-questions/vendor-invoice-entry-faqs"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/troubleshooting/frequently-asked-questions/vendor-invoice-entry-faqs"
---

# Vendor Invoice Entry FAQs

Here are some Frequently Asked Questions about vendor invoice
 entry.

## I want the cursor to skip the 'Route for approval?' checkbox when I am in Vendor Invoice Entry.

This is controlled by Access Unposted Transactions in
 Function Security. The default security setting is AP
 level 6. Use Operator Overrides to remove a specific user's
 access to this function.

## Can an invoice that has been 'Confirmed' in Invoice Approval still be modified in Vendor Invoice Entry?

The answer depends on your security setup. You will be allowed to
 call up and modify a confirmed invoice when you have security access to the
 Access Unposted
 Transactions option in Function Security.
 Without that security access, you will not be allowed to edit the confirmed invoice
 and will see the message "ERROR – You are not authorized to access unposted
 transactions."

## What does the message "ERROR – You are not authorized to access unposted transactions." mean?

You will see this message when you do not have security access to
 invoices that have been confirmed through the routing process or have been entered
 directly into Vendor Invoice Entry when the Route for approval? checkbox was
 cleared.

## What are unposted transactions in Vendor Invoice Entry?

The 'unposted transaction' status indicates that the invoice is ready to be updated into the system. Here the invoice either was directly entered into the screen when the Route for approval? checkbox was not selected or the invoice has been confirmed through the approval routing process. Regardless, the invoice is now ready for posting and can be updated into Spectrum.

## Is there any way to add more than a 30 character remark to the invoice and check remittance?

You can add up to 3 lines of 60 characters in the A/P
 Remittance Advice Remarks window. When you are in the
 More Invoice Information window and your cursor is in the
 Invoice remark field,
 press F4 to open this
 window. This information will print a separate check remittance advice during
 Payment Processing automatically.

## How do I use Alternate Payee Entry to pay bills for separate locations, but track everything to a single vendor?

Spectrum's Accounts Payable Alternate Payee Entry
 feature can be used to pay the single vendor, but allows each bill to go to the
 billing address, printing the address and the customer number on the bill. This is
 done by ensuring the One
 time checkbox is clear.

## A vendor wants to place a lien on our subcontractor. In order to make sure everyone gets paid, we need to figure out the supplier's portion of a payment and pay both the subcontractor and the supplier.

Use the alternate payee feature in A/P Payment Processing. This will allow you to create two checks, both payable to the subcontractor. This feature is also useful for people who are being audited for MBE compliance.

## How do I correct a vendor invoice that was entered incorrectly?

Use the A/P Reverse Vendor Invoice feature
 to reverse invoice entries that have already been updated using A/P
 Transaction Update (which follows the A/P Transaction Register). To
 reverse an invoice, the software creates a credit memo; to reverse a credit memo,
 the software creates an invoice. This will leave the correct accounting paper trail.
 Additionally, the software will automatically update the reversed items to open
 items so you don't have to create a $0.00 check in order to transfer these entries
 to the history file. Your security setting determines the level of automation
 offered during the reversal and update processes.
The table below shows how security levels affect the posting options.
Security:
Do you have security to the Transaction Register Update?
Security:
Do you have security to the Manual Check Register Update?
Security:
Do you have security to the Check Register Update?
Dates:
Are the G/L dates for both the invoice & credit memo within the same fiscal period?
Result

No
Yes
Yes
Yes
The update option allows you to create the reversal in unposted transactions.

Yes
No
Yes
Yes
Here you can post the reversal, but will have to create a manual check to clear it.

Yes
Yes
No
Yes
Here you can post the reversal, but will have to create a manual check to clear it.

Yes
Yes
Yes
No
Here you can post the reversal, but will have to create a manual check to clear it.

Yes
Yes
Yes
Yes
On update, you will be able to post reversal and clear history in one step.
