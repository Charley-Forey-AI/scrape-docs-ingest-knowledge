---
title: "What does Spectrum consider an unposted draw? | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/general-ledger/troubleshooting/frequently-asked-questions/what-does-spectrum-consider-an-unposted-draw"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/general-ledger/troubleshooting/frequently-asked-questions/what-does-spectrum-consider-an-unposted-draw"
---

# What does Spectrum consider an unposted draw?

There appear to be unposted draw requests on the G/L Unposted Transactions Inquiry and Report. After further review, it has been determined that they are not unposted transactions, but rather the next draws waiting for processing next month. What does Spectrum consider to be an unposted draw?
 Answer:
Spectrum considers an unposted draw request as having a G/L Date or Period to date that is less than what was entered in the Through transaction date field of the [Unposted Transactions Inquiry](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/general-ledger-inquiries-overview/unposted-transactions-inquiry) screen. For example, assume that the draw request has a G/L Date / Period to date of 6/30/10. This draw will appear as an unposted transaction when you run the G/L Unposted Transaction Inquiry and Report AND you use a date of 7/1/10. If you run the inquiry with a Through transaction date of 6/15/10, this draw will not appear as an unposted item.
