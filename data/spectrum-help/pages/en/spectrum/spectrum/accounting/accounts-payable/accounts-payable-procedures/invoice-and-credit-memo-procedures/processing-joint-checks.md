---
title: "Processing Joint Checks | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/accounts-payable-procedures/invoice-and-credit-memo-procedures/processing-joint-checks"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/accounts-payable-procedures/invoice-and-credit-memo-procedures/processing-joint-checks"
---

# Processing Joint Checks

The construction industry sometimes handles payment processing through the use of
 joint checks to two or more vendors.
The following steps outline how a Spectrum contractor can handle such checks when a
 customer sends a check made payable to one of his vendors.When you
 receive a joint check from a customer:

1. (One time only) Create a G/L code to pass through
 joint check amounts.

1. (One time only) Create a Cash Management account to
 clear the funds. This is not a real bank account, but having it in Cash Management
 will allow you to track and process joint checks more easily:

1. Go to Cash Management  >  Maintenance  >  Accounts.

1. Click New.

1. In the Cash G/L account field,
 choose the G/L code created in step 1.

1. (One time only) Create a joint check transaction code
 in Accounts Receivable:

1. Go to Accounts Receivable  >  Maintenance  >  Transaction.

1. Click New.

1. In the Transaction code field, enter
 'J'.

1. In the Description field, enter
 'Joint Check Transaction'.

1. In the Type field, select
 'Adjustment'.

1. In the G/L account code field,
 choose the G/L code created in step 1.

1. Select the Post to Cash Management check
 box, and enter the Cash Management bank account code created in step 2.

1. In Accounts Receivable  >  Data Entry  >  Cash Receipts, receive the joint check using the 'J' transaction code (set up above)
 against a customer invoice. This will reduce the contractual obligation and record
 the receipt in the joint check Cash Management account (which acts as verification of
 step 5, ensuring that the vendor payment has been recorded in the system).

1. In Accounts Payable  >  Data Entry  >  Payment Processing, pay the vendor invoice using the Cash Management bank account
 code created in step 2. This will balance out the deposit entered in AR, to zero out
 the G/L account and the Cash Management account.

1. Set up monthly routine to validate cash management
 account has a zero balance between deposits and checks.
