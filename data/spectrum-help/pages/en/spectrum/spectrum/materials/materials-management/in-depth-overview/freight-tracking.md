---
title: "Freight Tracking | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/materials-management/in-depth-overview/freight-tracking"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/materials-management/in-depth-overview/freight-tracking"
---

# Freight Tracking

Materials Management tickets are normally imported on a
 daily basis. The Scale Ticket Update is also done on a daily basis to get the information to
 Job Cost. Because the actual freight may not be known at the time of update, it is posted to a
 freight reconciliation holding file. When the invoice comes in from the vendor, the tickets
 are then reconciled and an A/P invoice is automatically created to pay the vendor.
Some haulers calculate cost based on tons hauled. Because the tonnage is
 known from the tickets, the estimated freight is fairly accurate and the variance between
 the actual and estimate is small. However, with hourly freight charges that are dependent
 on the daily time logs from the drivers, the variance between what is estimated from the
 tickets and what is actually charged by the haulers could be large.
To account for this, Spectrum posts the variance to the job (through
 A/P). This results in an estimated freight going to the job on a daily basis and on a more
 periodic basis the actual freight is also reflected in job cost.
The process begins when tickets are imported and posted daily. When the
 daily time sheets come in from the drivers, say weekly, the Freight Hours Reconciliation
 screen is used to adjust the tickets to reflect the correct elapsed time. When the invoice
 comes in from the vendor, the tickets are grouped together and an A/P invoice is created.
 This A/P invoice contains adjustments for the freight variance. These will be posted to job
 cost during the A/P invoice update.
This results is the actual freight cost being posted to job cost after
 the A/P invoices have been created and updated (not necessarily paid).
