---
title: "Non-Payroll Year-end Processing (Canada) | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/year-end/year-end-for-canada-payrolls/processing/non-payroll-year-end-processing-canada"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/year-end/year-end-for-canada-payrolls/processing/non-payroll-year-end-processing-canada"
---

# Non-Payroll Year-end Processing (Canada)

The year-end processing steps for the following modules:

- [General Ledger](#ID-0000061f11--en__section_qj5_glv_1tb)

- [Equipment Control](#ID-0000061f11--en__section_np4_xlv_1tb)

- [Fixed Assets](#ID-0000061f11--en__section_ohv_wlv_1tb)

- [Materials Management](#ID-0000061f11--en__section_y33_vlv_1tb)

## General Ledger

## Open Forward Balance Update

The Opening Forward Balance Update carries all asset, liability, and equity General Ledger balances forward from one year to the next. All changes are reflected in current balances. Income and expense accounts will be closed to the Retained Earnings account defined in the G/L Installation screen. This update may be run frequently as the company progresses into a new fiscal year. This step should be repeated if changes have been made to the previous year.
Important: When using this function, all balance records for the next year will be affected.

- If any of these account types have year-end balances of $0.00 and a status of Not used, the account code is not rolled forward to the new year:

- Asset

- Liability

- Capital

- All income account codes are closed to Retained Earnings regardless of the account's status.

## Fiscal Calendar Maintenance

The Fiscal Calendar Maintenance screen displays all fiscal years presently set up in the current company. Use this screen to set and maintain Journal Entry sequence numbers and ending dates for each fiscal period. Entries you make here control certain defaults and virtually every transaction updated to the General Ledger.
While changes are rarely required in this screen, the end of your fiscal year is a good time to check whether there need to be any additional years added to the fiscal calendar. If changes are made, the dates on historical transactions aren't changed.

To update the Fiscal Calendar

1. Go to General Ledger > Period End > Fiscal Calendar Maintenance.

1. Select the New Year button. The Add New Fiscal Year window displays.

1. Press Enter until all periods display, and then select OK.Note: Use the Add New Fiscal Year window to add years to your fiscal calendar. After entering the number of periods, press Enter. The dates and period labels for the next future year default, and you are able to edit the period labels. Next, the Auto-Create Additional Fiscal Years window displays, allowing you to create up to nine additional years based on the established settings.

1. Display the new Fiscal Calendar. Review the new dates to verify the update.

1. Select the checkmark to save and exit the calendar.

## Processing Dates Maintenance

At the end of each fiscal year, your system's maximum dates in all modules must fall in the new year.
When you open the Change Processing Dates screen, date-based changes are disallowed for all other users. Anyone else making entries in that company must wait until you close the screen to process date-based transactions.

1. Go to System Installation > Processing Dates.

1. Make any necessary changes.

1. To save changes, select Save and/or the checkmark in the upper right hand corner until the screen has returned to the Site Map.

## Equipment Control

## Open Forward Balance Update

The Open Forward Balance Update screen resets the opening revenue and cost balances for a new fiscal year from the previous year for each piece of equipment. This is a necessary update when moving from one year to the next, and may be run numerous times.

This function is available at Equipment Control > Period End > Open Forward Balance Update, or System Administration > Year End > Year End Processing.

1. Select Equipment Control.

1. Select Open Forward Balance.

1. Enter the fiscal year most recently completed.

1. Select Continue.

## Fixed Assets

For Fixed Assets year-end processing, often companies are required to report on assets that they acquire or dispose of that year, and report on YTD depreciation.

## YTD Depreciation

YTD depreciation can be reported by going to Fixed Assets  > Period End > Depreciation History Report, running the Depreciation History Report for the 01/01/YY through 12/31/YY dates (and then canceling out of the optional Purge step which appears on another screen).

## Disposal

To dispose of an asset without deleting and report on the disposal at year-end, perform the following steps:

1. Create a Department at Fixed Assets > Maintenance > Department for all assets that are disposed of in the current year.

1. When an asset is retired, sold, disposed of, etc., set the asset to Inactive status at Fixed Assets > Maintenance > Fixed Assets Master, to stop depreciation calculation.

1. Enter the date retired and sales price (if applicable) on the asset, and change the department on the asset to the department created in step 1.

1. These changes are not recorded in the general ledger. If you have sold the asset, create a journal entry to reduce the asset, accumulated depreciation amount, and gain/loss on sale, and more.

1. To report on asset disposal for the year, run a fixed asset listing (go to Fixed Assets > Maintenance  > Fixed Assets Master, select the Listing button), using the department created in step 1.

## Deletion

If you choose to delete an asset entirely from Fixed Assets, you can report on disposed assets with the Deletions Report, at Fixed Assets > Reports > Fixed Assets Deletions. Only deleted assets appear in the Deletions report.
Note: Once viewed, the Fixed Assets Deletions report prompts you to purge the data (it purges the retirement activity). If you've never run these reports before, or opted not to purge, you may see several years of data.

1. Go to Fixed Assets > Maintenance > Fixed Assets Master.

1. Press Enter to see all your assets.

1. Locate and select the asset you have sold.

1. Select the Delete button.

1. Select OK to confirm.

## Addition

When you run this report, please retain it as a permanent record of the company, as it cannot be recreated.
To report an asset addition to Spectrum, go to Fixed Assets > Reports > Fixed Assets Additions and select Preview. All assets that have ever been added and not yet purged from this listing appear in this report.
Note: Once viewed, the Fixed Assets Addition report prompts you to purge the data (it purges the addition activity only, not the asset or depreciation records). If you've never run this report before, you will likely see several years of data.

## History Consolidation

The Fixed Assets History Consolidation is an optional function and used only if you have purged General Ledger depreciation records in General Ledger for prior years.

This function is available at Fixed Assets > Period End > History Consolidation, or at System Administration > Year End > Year End Processing.

1. Select Fixed Assets.

1. Select History Consolidation.

## Materials Management

## Open Forward Balance Update

The Open Forward Balance Update function rolls the totals of the plant production file from one year to the next.

This function is available at Materials Management > Period End > Open Forward Balance Update, or at System Administration > Year End > Year End Processing.

1. Select Materials Management.

1. Select Open Forward Balance.

1. In the From fiscal year field, choose a year from the drop-down. The ending balance of that year will roll to the opening balance of the next year.

1. Select Continue.

1. Select OK to confirm.
