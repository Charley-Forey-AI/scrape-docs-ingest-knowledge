---
title: "Determining the Current Processing Date | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/data-entry-overview/gl-processing-date-change/determining-the-current-processing-date"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/data-entry-overview/gl-processing-date-change/determining-the-current-processing-date"
---

# Determining the Current Processing Date

The Processing Date Change screen (available on the System Administration menu) allows you to define a minimum, maximum, and current date for each module. Minimum and maximum dates can help prevent posting errors. For example, the minimum and maximum processing dates can be set to the first and last days of the current fiscal year, thus allowing posting only to the current year and not to a previous fiscal year by mistake. A more restrictive minimum and maximum date range can be set (for example, the beginning and end of the current month) in order to prevent posting to prior or future months. The date range is specified for each individual module to provide flexibility when working in Spectrum.
Each computer's operating system has a built-in clock, which keeps track of the actual calendar date. Spectrum reads this date when the first user logs on each day. The current processing date is set using the following rules:

- Computer Date. Use the computer's date when it is within the minimum/maximum date range, and it is greater than the current processing date previously entered.

- Current Processing Date (no change). If the computer's date is less than the existing current processing date, do not change the date.

- Maximum Date. If the computer's date is past the maximum date, use the maximum date as the current processing date.

- Why? The current processing date is set based on the first user to log on to Spectrum each day. If the computer date is earlier than the current processing date, then it is assumed that the date on the computer is incorrect and is not used. The theory is that you would not want to use an earlier date just because the first person that logged in that day manually changed his/her computer system date. Spectrum has always used this logic. If this is not desired, then manually change the current processing date accordingly.
