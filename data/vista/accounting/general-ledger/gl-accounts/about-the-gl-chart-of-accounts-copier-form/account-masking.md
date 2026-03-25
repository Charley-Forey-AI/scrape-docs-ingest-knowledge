---
title: "Account Masking | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-accounts/about-the-gl-chart-of-accounts-copier-form/account-masking"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-accounts/about-the-gl-chart-of-accounts-copier-form/account-masking"
---

# Account Masking

When copying accounts from one source to another, you must specify both a source and destination 'account mask' using the format defined for your company.If you are not sure what format to use, contact your system administrator.
The ‘account mask’ identifies exactly what is to be copied, and is used to create the new accounts. For example, if you have GL accounts set up for one department (01) and you want to copy all of these accounts into a different department (02), you would enter ‘?????.01??’ as the source mask and ‘?????.02??’ as the destination mask. The same would apply if you wanted to copy accounts set up with one location to a different location (e.g. ‘?????.??01’ to ‘?????.??02’). In each case, numbers represented by a '?' in the source mask will be copied 'as is' to the destination account; the numbers specified for the department or location will be changed as indicated (as shown below).

## Preview

Once you have designated both the source
 and destination account masks, click the Preview button. The grid at the bottom of the
 form will display all of the existing account codes that will be copied (based on the
 specified source account mask) and the new account codes that will be created (based on
 the destination account mask). Once you have reviewed the codes, click the Copy button
 to implement the copy process. Once completed, a message is displayed informing you how
 many accounts were found, and how many were actually copied.
Note: If the GL accounts you are copying have specified
 Summary and/or Cross-Reference Memo accounts that do not exist in the destination
 company, those accounts will also be copied, even if they exist outside the range of
 accounts you specified to copy (e.g. you are copying accounts in the 21000. – 25000.
 range, but your summary and cross-reference memo accounts are in the 50000. and 80000.
 range). This allows for keeping Summary and Cross-Reference Memo account assignments
 intact, since those accounts must exist in the destination company in order to be
 assigned.
