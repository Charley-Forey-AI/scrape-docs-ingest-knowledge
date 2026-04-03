---
title: "Change Processing Dates | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/system-administration/installation/change-processing-dates"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/system-administration/installation/change-processing-dates"
---

# Change Processing Dates

The Change Processing Dates screen is
 used to specify the range of dates within which transactions may be performed. The choice of
 allowable dates is entirely up to the System Administrator.
Minimum and maximum processing dates can help prevent posting errors. For example, minimum and maximum processing dates can be set to the first and last days of the current fiscal year, thus allowing posting only to the current year, and not to a previous fiscal year by mistake. The date range is specified separately for each individual module, allowing the user maximum flexibility in working with the system.
Once a date range has been defined, a current date can be set for each individual module. The computer's operating system has a built-in clock, which keeps track of the actual calendar date. This date is read when the first user logs on to Spectrum each day, and the current processing date is set equal to this date (when allowed by the minimum/maximum date range).
Users can date-stamp with a processing date by specifying the desired date in the current date column. This column will be reset to the calendar date each morning by the operating system's built-in clock. As time passes, when the current date reaches the maximum date of the specified date range, the date will not advance until the maximum date has been reset.
During installation of each individual module, the system administrator should specify a range of dates within which all transactions for that module must fall. This is done through the Change Processing Dates selection from the Installation menu.
The Change Processing Dates page will display a module's name once the installation page has been completed for that module. If the desired module does not display on the page, verify that the module has been installed on the system.
Press the Tab key to advance the cursor to the date columns, then enter dates in the format MMDDYY. The system inserts slashes to display the date in the format MM/DD/YY.
Because conversion typically takes several days and the system resets the date each morning, you may want to set the current, minimum, and maximum dates all equal to the conversion date. When this is done, it will not be necessary to change the processing date each day, as the minimum/maximum date range will disallow the system's automatic changes to the current date. After all data conversion is complete, the minimum/maximum date range should then be set as desired for daily operations.
Important: When using this screen, you are editing processing dates for the entire company. This may result in areas of Spectrum with date-sensitive rate updates being locked until you exit this screen. It is recommended that you promptly make and save the needed changes and exit the screen.
Note: The automatic date advance feature is disabled if your
 server/host clock is not working properly. On your toolbar go to Help and select About
 Spectrum to make sure your server time and date is correct. If you have Enterprise
 Management security authorization (security code EM), a Copy
 button displays. Clicking this button in Spectrum displays the [Copy Processing Dates Across Companies](/en/spectrum/spectrum/system-administration/installation/change-processing-dates/copy-processing-dates-across-companies)
 screen.
