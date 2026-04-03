---
title: "Draw Request Entry - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/draw-request-entry/draw-request-entry---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/draw-request-entry/draw-request-entry---field-descriptions"
---

# Draw Request Entry - Field Descriptions

Use this table for reference when completing the fields on this screen.
Field/ButtonDescription
JobEnter the job for this contract. If this screen was accessed from the Customer Info Bar, the selected job code will default.
CustomerThe customer code will default from the Jobs screen; press Enter to accept. If the customer code is not recorded in the Jobs, or a different customer is desired, enter the customer code. If the customer code's status is set to Not used, then no entry is allowed.
Application #Enter the draw request application number. Numbers will typically start with one (1) for the first draw request and proceed sequentially, but any starting application # can be entered. Generally, you will create the first application; the software will create subsequent draw request applications.

- If no applications are found for the job and customer, Spectrum automatically assigns the next application number.

- If any applications are found for the job and customer, a new application number cannot be added, and the largest application number will default in this field. The reason for this is that there can only be one unposted draw request application for a given contract

Application dateEnter the application date for the draw request being entered. This will be used as the invoice date when the draw request is transferred using Update Draws to A/R Invoice.
If new or upcoming tax rates are recorded in the Rate History window, the dated entered in this field dictates which sales tax rate to use. If this field is blank, Spectrum uses the current tax rate.

Period toEnter the date through which the work on the job is to be billed. This will be used as the G/L date on the invoice when the draw request is transferred using Update Draws to A/R Invoice.
If change orders or change requests have already been transferred using the Transfer Change Orders screen, then the date in this field may not be set earlier than the change request/change order approval date.

Architect's project #Enter the architect's project number, if applicable.
If the contract for this job specifies the use of unit pricing (Use unit pricing checkbox is selected) in Contracts, the additions to the screen differ slightly from those described below.
After the architect's project number is entered (and the job does not use unit pricing), additions are made to the screen.
For each billing item to appear on the draw request, the first line will include the system generated line number, the billing item number and description, and the taxable flag. The second line will include dollar values.

Financials - these totals appear for fixed price draw requests:
Previous workThe sum of values in the applicable column in the grid.
This period work
Material stored
Completed and storedThe sum of the above values.
% completeThe sum of the Completed and stored total divided by the Scheduled value total.
Financials - these totals appear for unit price draw requests:
This period $The sum value of the This period $ column.
Calculated online sales taxAppears only when the Use online tax calculation service checkbox is selected on the Installation screen and the sales tax code for the draw request is an online tax code.
Online Tax CalculationSelect to display the calculated sales tax amount.
