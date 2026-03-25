---
title: "Moving Progress Billings | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/moving-progress-billings"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/moving-progress-billings"
---

# Moving Progress Billings

You can use the Move tab on the JB
 Interface form to move progress billings forward a month if you do not want to interface
 them to AR for the current month when closing the GL for month end.
You can also move progress billings back
 to the previous month, if necessary.
The grid on the Move tab
 is identical to the grid on the Interface tab, except for the following
 differences:

- Only billings with a status of active will
 display;

- The grid always displays bills without an
 invoice number; and

- The billings will be ordered by contract,
 customer, and bill number.

When moving a progress billing forward a
 month, the system will also move all future progress billings with the same customer
 and contract that are in the same month. Additionally, all related future progress
 billings (with the same customer and contract) in the next month will be ordered to
 occur after the moved billings to maintain consistency.
When moving a progress billing back a
 month, the system will also move all earlier bills with the same customer and
 contract that are in the same month, provided that the previous month remains open.
 Additionally, all related progress billings with an earlier bill number (with the
 same customer and contract) will also be moved to maintain consistency. All moved
 bills will be in the same order as in the originating month.
The following steps detail how to move
 progress billings to the next month.

1. From the JB Interface
 form, in the Bill Month field, enter the
 current bill month for the billings you wish to move.

1. Select
 Move
 Forward
 or
 Move
 Back
 from the
 Move
 Option
 field.

1. Check the
 Move
 box for each billing in the grid that you wish to move. You can
 also check the
 Move
 all bills
 box to automatically check the
 Move
 box for all billings in the grid.

1. Click Move. The system displays a confirmation message.

1. Click Yes
 to move the billings. The system sets the bill month to the next month for all
 selected billings and removes them from the grid. The records will redisplay if
 you enter the corresponding month in the Bill Month field.

For more information about the JB Interface form, see [JB Interface Form](/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/jb-interface-form#ID-00014dd7--en__ID-00014dd7).
