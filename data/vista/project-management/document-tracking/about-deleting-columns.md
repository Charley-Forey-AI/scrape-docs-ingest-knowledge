---
title: "About Deleting Columns | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/document-tracking/about-deleting-columns"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/document-tracking/about-deleting-columns"
---

# About Deleting Columns

You can delete columns you do not want displayed. Deleting
 column does not delete them from the table, so you can add them back in later if necessary.
Note: For the Submittals, Other Documents, RFI’s, and
 RFQ’s grids, deleting a column may interfere with row highlighting functionality. Row
 highlighting occurs when certain 'conditions' exist. For example, if a submittal, row
 highlighting occurs when the submittal is overdue; that is, the current date is equal to
 or greater than the due date and no 'received date' has been entered.
The following is a list of columns that are
 required for these tabs in order to maintain row highlighting functionality:
Submittals
Other Documents
RFI'sRFQs

PMSC.CodeType
PMSC.CodeType
PMSC.CodeType

PMSM.DateReqd
PMOD.DateDue
PMRI.RFIDate

PMSM.DateRecd
PMOD.DateRecd
PMRI.DateDue

PMSM.ToArchEng
PMOD.DateDueBack

PMSM.DueBackArch
PMOD.DateRecdBack

PMSM.RecdBackArch

PMSM.DateRetd

Deleting any of these columns from their
 corresponding grids causes the required data to be unavailable; therefore, the
 highlighting function cannot determine whether the 'condition' exists and no
 highlighting will occur. If you do not want these columns displayed, just uncheck the
 Visible box. This will make the column invisible but leave the data available for the
 highlighting function.
