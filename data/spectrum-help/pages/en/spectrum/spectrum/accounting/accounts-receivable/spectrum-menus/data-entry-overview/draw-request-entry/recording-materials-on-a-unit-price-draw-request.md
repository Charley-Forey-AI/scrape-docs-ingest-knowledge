---
title: "Recording Materials on a Unit Price Draw Request | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/draw-request-entry/recording-materials-on-a-unit-price-draw-request"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/draw-request-entry/recording-materials-on-a-unit-price-draw-request"
---

# Recording Materials on a Unit Price Draw Request

To track stored materials on a draw request, make sure you
 have selected the Transfer materials stored to previous app checkbox on the Accounts Receivable Installation  >  Draw Request screen.
Recording materials stored to date on unit price draw
 requests is slightly more complicated than fixed price draw requests because there is no
 way to differentiate labor from pre-deposited materials at the work site. To work around
 this issue, it is necessary to create a dummy billing item for recording materials stored
 on unit price draw requests.Note: To determine whether
 the contract is fixed price or unit price, on the Site Map, click Accounts Receivable  >  Maintenance  >  Contract. Type in the Job
 number, press Enter,
 type in the Customer
 code, press Enter,
 and then click the Properties
 button. If the Use unit
 pricing checkbox is selected then the job has a unit priced contract.
 Otherwise, if the checkbox is clear, the job has a fixed price
 contract.

1. On the Site Map, click
 Accounts Receivable  >  Data Entry  >  Draw Request.

1. At the Job field, enter the job
 number for the draw request you are modifying, and then press
 Enter.

1. At the Customer field, press
 Enter to accept the customer code that defaults based on
 your job selection, or press F4 or double-click on this field
 to select from a list of available customers.

1. At the Application # field,
 enter the application number for the draw request you are working on and press
 Enter. If you don't know the application number, press
 F4 or double-click on this field to select from a list of
 available.

1. Enter an Application date and date through which the job is to be billed, and Architect's project #, if applicable.

1. Enter a unique code for this group of billing items and a Bill item for this line.

1. At the Item description field,
 type a description such as Materials Stored.

1. Select the Taxable checkbox if
 the item is taxable, otherwise, leave this checkbox clear.

1. At the Unit Measure field,
 enter a lump sum unit of measure.

1. Press Enter to move through the
 This period quantity to the Contract
 $ field. Do not enter a dollar amount in this field; enter
 .00 to add the line.

1. At the G/L account field, enter
 the G/L code for this item number or leave it blank and it will use the default G/L
 code from the contract.To store billing items, access your draw request and proceed to
 the above line item. Move to the This period $ field and enter the dollar amount for the stored
 materials. When billing items, on the next draw enter a negative dollar amount in
 the This period $ field
 for the materials you will be billing, then enter that dollar amount on the
 appropriate billing item.
