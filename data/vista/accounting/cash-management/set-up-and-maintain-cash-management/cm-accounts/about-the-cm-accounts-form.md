---
title: "About the CM Accounts Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/cash-management/set-up-and-maintain-cash-management/cm-accounts/about-the-cm-accounts-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/cash-management/set-up-and-maintain-cash-management/cm-accounts/about-the-cm-accounts-form"
---

# About the CM Accounts Form

Use the CM Accounts form to define each bank account you wish to track with the CM module.
You will need to set up a separate account for each checking, savings, and investment
 account — any account that has money transferring in and out that requires
 reconciliation.
The GL account code for each cash account is designated so that the debit/credit is
 automatically made to the correct account. There should be only one GL account for each
 CM account, and vice versa, to ensure that the two accounts mirror each other.
The GL account code assigned in this form will be used by AP, AR, PR, and CM (Outstanding
 Entries and Transfers) when posting to this bank account.
As needed, see the F1 Help for each field in the form.

## Beginning Check #

The Beginning Check # field allows you to override the standard default behavior used to determine beginning check numbers when printing checks in the AP Check Print and PR Check Print forms.
 The standard default procedure bases the beginning check number on the highest check number in the system, plus one. If you enter manual checks using numbers in a higher range than printed checks, the system defaults beginning check numbers based on those higher numbers. To avoid having to manually override the beginning check number each time you print checks, you can assign a beginning check number in this form for each applicable CM account. Then when printing checks (in either AP Check Print or PR Check Print), the system uses the value in this field to determine the beginning check number default. Once you complete a check run, the system updates this field based on the last check number used in the check run, plus one.
If you clear checks using the Clear Existing Check #s (Number can be reused.) option in the applicable check print form, the system sets the Beginning Check # value for the specified CM Account back to its original (pre-check run) value.

Related information

- [About Electronic Funds Transfer](/en/vista/vista/accounting/cash-management/set-up-and-maintain-cash-management/cm-accounts/about-electronic-funds-transfer)

- [Delete a CM Account](/en/vista/vista/accounting/cash-management/set-up-and-maintain-cash-management/cm-accounts/delete-a-cm-account)

- [About Account Security](/en/vista/vista/accounting/cash-management/set-up-and-maintain-cash-management/cm-accounts/about-account-security)
