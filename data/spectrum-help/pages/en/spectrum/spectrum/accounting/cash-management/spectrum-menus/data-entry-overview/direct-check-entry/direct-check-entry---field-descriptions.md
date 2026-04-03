---
title: "Direct Check Entry - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/data-entry-overview/direct-check-entry/direct-check-entry---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/data-entry-overview/direct-check-entry/direct-check-entry---field-descriptions"
---

# Direct Check Entry - Field Descriptions

Use this table for reference when completing the fields on this screen.
Field/Button
Description

Form
Click this button to open the [Print Direct Check](/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/data-entry-overview/direct-check-entry/print-direct-check) window. This button will only be available before entering into transaction mode.

Update
Click this button to open the [Direct Checks Register](/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/data-entry-overview/direct-check-entry/direct-checks-register) window. This button will only be available before entering into transaction mode.

Direct check

Bank account
Enter the bank account code.
Note: During entry in this screen, Spectrum automatically
 disallows any accounts that are not bank accounts. In other words, credit
 card accounts are not permitted in this screen.

Check #
Enter the check number, or press Enter to automatically select the next check number. The
 check number defaults to the next available number from the Cash
 Management Bank Account Maintenance screen.

Cost center
If the cost center feature is enabled in the Enterprise
 Installation screen, enter a direct check cost center in this
 field. This cost center will serve as a default during entry.

G/L transaction date
Enter the General Ledger date, or press Enter to accept the default of the current cash management processing date. The fiscal year and period will display to the right of this field.

Payment information

Pay to the order of
Enter the payee, or press F4 to select from a list of valid vendor codes, customer codes, or employee names. It is not necessary for the payee to be previously set up in any of these files in order to create a direct check.

Address
The payee's mailing address displays. Press Enter to accept the default address; otherwise, enter the correct information.

Check date
Enter the check date, or press Enter to accept the default of the current cash management processing date.

Amount
Enter the check amount (up to $99,999,999.99). The check amount is validated
 against the amount entered at the "Direct check dollar limit:" prompt of the
 Cash Management Installation screen.
If the direct check amount exceeds the amount entered at the prompt, an error
 message appears stating that the amount entered exceeds the amount allowed
 for a direct check. If the check amount exceeds the direct check dollar
 limit, it would be possible for an employee with the appropriate security to
 change the amount in the Direct check dollar limit:
 prompt of the Cash Management Installation page in
 order to accommodate the amount of the check.

Memo
Check defaults to memo field in header. Press Enter to accept the default or enter other notes.

Detail lines

G/L account
Enter the General Ledger account code. The account description displays to the right of this field.
Note: Entry is prevented when the account code status is set to
 Not used. A warning displays when the status is
 set to Inactive. Entry is also disallowed if the
 direct cost option is set to Equipment cost in the
 G/L Master File Maintenance screen.

Job
If the General Ledger account associated with this line is a Direct Job Cost account, enter the job number for this distribution. The job description will display to the right of this field.

Phase
Enter the phase to which this direct check is to be distributed. The phase description will display to the right of this field.
Note: Data entry is prevented if the phase status is 'Complete'. A
 warning displays if the status is 'Inactive'.

Ct
Enter the cost type to which this direct check is to be distributed.

Amount
Enter the amount associated with the current distribution line number. The sum of all totals in this column will display in the Amount field.

Memo
Enter a memo related to this line item.

Cost center
A Cost center field is provided on each detail line for
 expense distribution. As the cost center is recorded, Spectrum compares the
 bank account's list of shared cost centers with cost centers in the
 operator's assigned scheme; if there are no common cost centers, then that
 cost center is not allowed.
