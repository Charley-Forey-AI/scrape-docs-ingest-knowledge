---
title: "About the MS Quote Close & Purge Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/quotestemplates/quotes/about-the-ms-quote-close--purge-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/quotestemplates/quotes/about-the-ms-quote-close--purge-form"
---

# About the MS Quote Close & Purge Form

Use the MS Quote Close & Purge form to close and/or purge
 quotes that you no longer need.

## Closing Quotes

Closing a quote changes its status to
 “inactive”, but leaves all of its detail, defaults, and override information on
 file. The system updates quote detail lines with a status of “ordered” to
 “complete”, and detail lines with a status of “bid” or “complete” do not change. If
 this is a stocked material, the system relieves any remaining allocated units. If
 you elected to audit quotes (option in MS Company), the system creates audit entries
 in HQMA (HQ Master Audit) when the quote closes.

## Purging Quotes

Purging a quote completely removes it
 from the system. The same updates are performed as when closing quotes (i.e. any
 remaining allocated units are relieved from inventory), but the system removes the
 quote from all of the MS Quote tables. The audit process, regardless of whether you
 elect to audit quotes, does not track purged quotes.

## Selection Criteria

If you want to limit the number of
 quotes that display in the grid, use the available selection criteria to restrict
 quotes for purging or closing. You can restrict by Quote Type and Purchaser, and
 specify the quote type to restrict. Related fields display so that you can enter
 specific values. For example, if restricting by quote type “Customer”, enter the
 customer, and if applicable, the customer job and/or customer PO#. If you do not
 enter a value, then all customers, customer jobs, and customer PO# display.
You can also restrict by quote
 expiration date. All quotes that expire on or before the specified expiration date
 display in the grid. If the quote does not have an expiration date, it will not be
 included.
If you restrict display to only active
 quotes, only quotes that are active and meet the other restriction criteria will
 display in the grid.

## Setting the Purge/Close Options

Once you have entered all the desired
 restrictions, click Refresh to populate the grid. If you subsequently
 change the criteria, click Refresh again. The system clears the grid of
 all previously displayed quotes and repopulates it with quotes meeting the current
 criteria.
Once the grid displays the desired
 selection of quotes, flag the quotes for Closing or Purging. Click Close/Purge to perform the
 update. Each quote in the grid set for Close or Purge processes accordingly. If
 successfully processed, the system removes the quote from the grid. When the form
 finishes processing all quotes in the grid, a message box displays, indicating that
 the update is complete and whether there were any errors.
Important: If you close a quote accidentally, reopen
 it through the MS Quotes by selecting its Active checkbox. You cannot recover
 accidentally purged quotes, however.

Related information

- [About the MS Purge Form](/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-purge-form)
