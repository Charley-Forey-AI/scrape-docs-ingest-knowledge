---
title: "Note Regarding Vac/Hol/Sick G/L Accrual Update Validation | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/human-resources/human-resource-module/spectrum-menus/data-entry-overview/vacholsick-gl-accrual-update/note-regarding-vacholsick-gl-accrual-update-validation"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/human-resources/human-resource-module/spectrum-menus/data-entry-overview/vacholsick-gl-accrual-update/note-regarding-vacholsick-gl-accrual-update-validation"
---

# Note Regarding Vac/Hol/Sick G/L Accrual Update Validation

Each time you exit the G/L Error Correction screen, the software will perform a test to confirm that the sum of the debit amounts equal the sum of the credit amounts within the same fiscal period. Because it is possible for a single update to include multiple periods, it is not sufficient to sum all debits and credits in the batch without regard for date. Instead, each period is validated individually. If an out-of-balance period is encountered, the software will not proceed to the update confirmation screen; instead, all transactions previously shown will display when the G/L Error Correction screen reopens, allowing you to make any required corrections.
During the Vac/Hol/Sick G/L Accrual Update, the cost center validation routine will not treat a blank cost center as an error.
