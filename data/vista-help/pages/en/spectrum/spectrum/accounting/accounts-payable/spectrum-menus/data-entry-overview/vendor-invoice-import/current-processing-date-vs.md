---
title: "Current Processing Date vs. True System Date | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-invoice-import/current-processing-date-vs.-true-system-date"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-invoice-import/current-processing-date-vs.-true-system-date"
---

# Current Processing Date vs. True System Date

Business Issue: The Accounts Payable module states that the current processing date is 8/15/XX when the true system date is 8/14/XX. Why don't the dates match?
Solution: To understand the resolution, you must first understand the
 Spectrum Processing Date Change screen.
The Processing Date Change screen (Admin > Processing Date Change) allows you to define a minimum, maximum, and current date for each module.
Each computer's operating system has a built-in clock that keeps track of the actual calendar date. Spectrum reads this date when the first user logs on each day. The current processing date is set using the following rules:
Computer Date: Use the computer's date when it is within the minimum/maximum date range, and it is greater than the current processing date previously entered.
Current Processing Date (no change): If the computer's date is less than the existing current processing date, do not change the date.
Maximum Date: If the computer's date is past the maximum date, use the maximum date as the current processing date.
Why?
The current processing date is set based on the first user to log on to Spectrum each day. If the computer date is earlier than the current processing date, then it is assumed that the date on the computer is incorrect and is not used. The theory is that you would not want to use an earlier date just because the first person that logged in that day manually changed his/her computer system date.
Spectrum has always used this logic. If this is not desired, then manually change the current processing date accordingly.
Examples:
What will the current processing date be based on the following scenarios? All assume these minimum and maximum dates:
Minimum Date 8/01/XX
Maximum Date 8/31/XX
Scenario
Current Processing Date
Reason

On 8/05/XX, I log on to Spectrum. The current processing date is 8/04/XX.
8/05/XX
The computer date is within the minimum/maximum dates and it is greater than the previous current processing date.

On 8/10/XX, I manually change the current processing date to 8/31/XX.
8/31/XX
You can reset the date with manual entry.

On 8/15/XX, I log into Spectrum. The current processing date is 8/31/XX.
8/31/XX
Current processing date does not reset to the computer date because it is earlier than the previous current processing date.

On 9/05/XX, I log into Spectrum. The current processing date is 8/31/XX.
8/31/XX
The computer date is past the maximum date; therefore, the maximum date is used.
