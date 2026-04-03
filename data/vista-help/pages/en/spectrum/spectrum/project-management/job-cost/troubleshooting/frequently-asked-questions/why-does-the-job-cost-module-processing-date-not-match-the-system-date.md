---
title: "Why does the Job Cost module processing date not match the system date? | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/troubleshooting/frequently-asked-questions/why-does-the-job-cost-module-processing-date-not-match-the-system-date"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/troubleshooting/frequently-asked-questions/why-does-the-job-cost-module-processing-date-not-match-the-system-date"
---

# Why does the Job Cost module processing date not match the system
 date?

To understand the resolution, you must first understand the
 Spectrum Processing Date Change screen.
The Processing Date Change screen (Admin > Processing Date Change) allows you to define a minimum, maximum, and current date for each module.
Each computer's operating system has a built-in clock, which keeps track of the actual calendar date. Spectrum reads this date when the first user logs on each day. The current processing date is set using the following rules:
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
