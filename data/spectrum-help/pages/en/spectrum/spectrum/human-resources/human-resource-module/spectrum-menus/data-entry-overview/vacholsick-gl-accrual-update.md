---
title: "Vac/Hol/Sick G/L Accrual Update | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/human-resources/human-resource-module/spectrum-menus/data-entry-overview/vacholsick-gl-accrual-update"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/human-resources/human-resource-module/spectrum-menus/data-entry-overview/vacholsick-gl-accrual-update"
---

# Vac/Hol/Sick G/L Accrual Update

This option will create reversing entries to the General
 Ledger and Human Resources Vacation/Holiday/Sick history.
Protection has been incorporated so that reverse accruals for an invalid date cannot be
 made. Also, the dates must be within the current Payroll minimum and maximum dates to
 perform this update. This update should be performed on a monthly basis; the listing that
 is produced will explain the accrual journal entries to be made. After reviewing the
 information, you will be prompted to perform the update. This screen will not appear until
 any accrual exceptions that printed have been fixed.
Once this update is run, Spectrum will create summary G/L transactions in the General Ledger balance files. One entry will be created per G/L account per accrual type based on the home department of the employee. The debit entry will be assigned to the designated expense G/L account code while the credit entry will be assigned to the designated liability G/L account code. The designated G/L account codes must be both active and valid for this update to proceed.
In addition to updating the General Ledger, this update will also create detail information that will be stored in the Human Resources Vac/Hol/Sick G/L Accrual history file. One transaction record per accrual type (Vac, Hol, and Sick) will be created in the history file for each employee. Additionally, the update will also store the accrual date, hours balance as of the accrual date, and pay rate/accrual calculations.
The total accrual amount and accrual date will also be stored in the Payroll employee file for each employee, overwriting any amounts and dates previously stored.

Related information

- [Explanation of Journal Entries](/en/spectrum/spectrum/human-resources/human-resource-module/spectrum-menus/data-entry-overview/explanation-of-journal-entries)

- [G/L Error Correction Screen](/en/spectrum/spectrum/human-resources/human-resource-module/spectrum-menus/data-entry-overview/gl-error-correction-screen)

- [Reverse Vac/Hol/Sick G/L Accrual](/en/spectrum/spectrum/human-resources/human-resource-module/spectrum-menus/data-entry-overview/reverse-vacholsick-gl-accrual)

- [Vac/Hol/Sick G/L Accrual Report/Update](/en/spectrum/spectrum/human-resources/human-resource-module/spectrum-menus/data-entry-overview/vacholsick-gl-accrual-reportupdate)
