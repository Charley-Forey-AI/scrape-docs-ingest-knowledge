---
title: "Dashboard App Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/getting-started/about-dashboards/dashboard-app-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/getting-started/about-dashboards/dashboard-app-descriptions"
---

# Dashboard App Descriptions

Descriptions of the standard apps in the Spectrum Dashboard.

## Accounting

AppDescription
Customer Aging Totals

- Pie chart showing the total dollars of open invoices.

- Links open the Customer Open Items screen.

- Clicking on a section shows the top 10 customers, by amount owed, for that section (as a bar chart). Clicking on a customer within that bar chart opens the Customer Open Items screen for that customer.

- Information shown is restricted based on Cost Center restriction to the Customer.

- The amount shown is Current thru Over 90 day past due. Retention and un-posted invoices are not included.

- Data is based on the System date.

Customer Balance (Top 10)

- Bar chart showing the balance per customer. Sorted by balance amount and shows the top 10 customers. The chart shows only if the user has sufficient security in the current company.

My Current Workflow Assignments


- Tasks that have been assigned to you appear on the My Current Workflow Assignments app. Items on this list are ordered by most overdue first.

- The status of the step appears as a prefix to the workflow item. Items without a 'Due in' prefix indicate that no due date has been set.

- Hovering over an item displays who the assignment is assigned to (you, a group, a role), as well as the date and time it is due.

- Click on a record to open in the appropriate screen for that step.

G/L Account Balance

- See up-to-date account balance information, such as cash on-hand, loan balance, or the current line of credit.

- This app links to the [ G/L Detail Analysis Inquiry](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/general-ledger-inquiries-overview/gl-detail-analysis-inquiry) screen, in context to the particular account code.

Unapproved Invoice Aging Totals

- Displays a pie chart broken down by number of days waiting for approval (1-15, 16-30, or 30+), based on the total dollar value of all unapproved invoices.

Unapproved Invoice $ (Top 10)

- Displays as a bar chart with operator name and total dollar amount of invoices waiting for approval.

- Clicking on a bar opens the Unapproved Invoices screen.

Vendor Aging Totals

- Displays a pie chart broken down by number of days overdue (Not Yet Due, 1-30, 31-60, 61-90, 90).

- Clicking on a section lists the top 10 amounts by vendor making up that section.

Vendor Pay-When-Paid Invoices

- Displays pay-when-paid transactions for all jobs.

- Clicking on a job takes you to the Job Payables screen for the job in context.

## Employee Kiosk

Requires the Employee Kiosk module. Users must have EK (Employee Kiosk) security in the current company to use this app.
AppDescription
My Time Entry

- Displays all pre-time card currently in progress for the current operator for Regular checks (ignores manual checks, void checks, replacement checks and layoff checks).

- Clicking on a row in the My Time app opens the [New/Edit Employee Time Entry](/en/spectrum/spectrum/human-resources/employee-kiosk-module/my-time-entry/newedit-employee-time-entry) window in the current company with the employee in context.

- The list box shows time cards across all work dates.

- 'No items found' indicates that the current operator is not set up properly.

My Payroll Checks

- Displays up to 100 payroll checks, with the most recent listed first.

- If multiple checks are present for the same date, each check displays separately, and they both display the same YTD values on the Earnings Statement.

- Regular and Manual checks display, including ones that may have originated in Layoff Check or Replacement Check.

- Clicking on a row in this app generates a Payroll [My Earnings Statement](/en/spectrum/spectrum/human-resources/employee-kiosk-module/my-earnings-statement) (Crystal Report).

My Training and Certifications

- Displays a list of the operator's HR Training and Certifications.

- Items appear in date order (latest date at the top and undated items at the bottom).

- If there is no expiration date for an item, the app uses the required date or the end date if they are available.

My Year-end Tax StatementAllows employees to access their current year tax form. When the employee selects a form, his/her standard plain paper W-2 (for US), 1095-C Form (for US), or T4 Slip (for Canada) displays. If the employee has worked for multiple entities during the year, each form displays separately in the Dashboard app.In addition:

- a relevant PDF of instructions is included

- the app prevents employees from retrieving their forms while the Payroll Department is still reviewing year end information

Employee List

- Displays a list of employees filtered by employee status code - for example, new hires.

## Equipment

AppDescription
Equipment and Maintenance Due

- Displays a list based on information found in the Preventive Maintenance Schedule screen and shows anything 90% due or greater.

## Executive

AppDescription
Cash Flow

- Displays as a pie chart with sections for number of jobs with minus cash flow, number of jobs with plus cash flow, and number of jobs with net zero. Only active jobs are shown.

- Clicking on the minus or plus sections will open one of the following bar charts for top 10 or bottom 10 cash flow jobs. (The 'net zero' jobs section does not open any chart, because the cash flow amount would just be a zero bar for each job.)

- When there are a small number of jobs in a company, there may be duplication on the Top and Bottom 10 Jobs. The Bottom 10 Jobs app will display those at the top of the chart.

Cash Flow by Job (Bottom 10)

- Bar chart showing amount of cash flow per job. Sorted by cash flow amount and shows the lowest 10 jobs.

- Clicking on a job opens the Job Analysis screen for that job.

Cash Flow by Job (Top 10)

- Bar chart showing amount of cash flow per job. Sorted by cash flow amount and shows the top 10 jobs.

- Clicking on a job opens the Job Analysis screen for that job.

Job Backlog (Top 10)

- Displays as a bar chart with top 10 Jobs by backlog dollar amount.

- Clicking on a bar will open the Contracts screen for the specified job.

Job Backlog by Division

- For each job, the backlog is calculated as the revised Contract less billed to date.

- Displays as a bar chart with total 'backlog' by division.

- Clicking on a bar opens up the top 10 jobs making up that segment.

Payroll Weekly Dollars

- Displays a stacked column chart for the past 4 weeks with total dollars of Gross Pay and Burden for each week.

- Links to the Job Cost > Payroll Hours Analysis start screen.

Profit FadeShows profit fade information by Job totals, Top 10, and My Jobs. Calculated as:

1. Current Profit = Revised Contract – Current Projected Cost (or Current Estimate if no Projected cost)

1. Original Profit = Original Contract – Original Estimate

1. Profit Fade = Original Profit – Current Profit (negative number is good, positive number is bad)

Total Backlog

- Displays as a pie chart with segments to show the total actual backlog plus 'proposed job' amounts (divided into Proposed, Signed, Awarded).

- 'Current' is the total across all active jobs of Revised contract less billed to date.

- Proposed, Awarded, and Signed are the total of all Proposed jobs for that status, calculated as Estimated contract amount multiplied by win probability for each job.

## Job

AppDescription
Equipment Hours

- Displays JTD equipment hours compared against the Projected Hours. When projected hours are not used, the Current Estimated Hours default in its place. Equipment hours are calculated using the cost type(s) defined on the Job Cost Installation > Cost Types page.

- Clicking on the app launches Job Analysis in a new Spectrum tab.

Gain/Fade

- Analyzing contract revenue and projected cost over time, this graph displays profit fade and profit gain.

- Clicking on the app launches Job Contract Status in a new Spectrum tab.

Labor Hours

- Displays JTD labor hours compared to the Projected Hours. When projected hours are not used, the Current Estimated Hours default in its place. Labor hours are calculated using the cost type(s) defined on the Job Cost Installation > Cost Types page.

- Clicking on the app launches Job Analysis in a new Spectrum tab.

Open Project Documents

- This bar chart shows open documents for each Project Management category, broken out to show 'Overdue', 'Due in next 7 days' and 'Due beyond 7 days'.

- Hover over the bar chart to show a tooltip with totals for that category. Click on an item in the bar chart to link to the Project Log in context.

- Clicking on the app launches the Project Log in a new Spectrum tab for the selected category.

Project Log Shortcuts


- Displays your default Saved Selections for the Project Log.

Progress

- Displays the percent completed vs percentage remaining of Billed-to-date and Cost-to-date.

- Clicking on the app launches Job Analysis in a new Spectrum tab.

Shift

- The first set of bars display the original contract amount compared to the current contract amount. The next set displays the profit with the original.

- Clicking on the app launches Job Analysis in a new Spectrum tab.

## News

AppDescription
Associated General Contractors of America (AGC) News Feed RSS feed
California Transportation Project Addendas
Construction Equipment NewsRSS feed
Google News FeedRSS feed
Road and Bridges NewsRSS feed

## Project Management

AppDescription
My Ball in Court Assignments

- Requires the Project Management module.

- Allows the operators to view all project log items that have been assigned to them.

- Items are formatted to display the job, category and number. The tool tip indicates if no due date is stored.

My Compliance Log Status

- Displays job compliance log items. The red portion of the bar chart displays overdue items; the green portion displays all others.

- Hover over an item to show the job name and the number of applicable items.

- Click on an item in this app to open the Job Compliance Tracking screen for the selected job.

My Jobs

- Only Active Jobs display.

- Links open the Job Dashboard screen for that job.

- Links display based on Operator Setup.

To enable the My Jobs app, follow these steps:

1. On the Site Map, click System Administration  >  Contacts.

1. Add a new contact for your operator.

1. On the Jobs tab, add some jobs to the contact.

1. On the Site Map, click System Administration  >  Security  >  Operator Maintenance.

1. Add the newly-created contact to your operator.

1. Add the My Jobs widget to your dashboard.

1. Jobs for which your operator is an associated contact will display. Contacts can also be assigned in Job Maintenance.

My Jobs - Backlog

- Displays as a bar chart by backlog dollar amount; lists only the jobs assigned to the current operator.

My Jobs Pay-When-Paid Review

- Displays all pay-when-paid invoices for the your jobs only.

- Clicking on a job takes you to the Job Payables screen.

My Job Subcontract Change Analysis

- Shows a chart of 'My Jobs' (based on operator's contact ID and the jobs that contact ID is associated with). Only jobs with an Active status display.

- Displays subcontract costs accepted from the subcontractor but not yet billed to the customer.

- The top bar shows the total subcontract costs from all change requests with a CR status of Approved or Executed, with separate bar for the Approved amount and a total Approved + Executed amount.

- The bottom bar shows the total subcontract cost from all change requests, by the subcontract CO status (Proposed or Executed - without regard to the CR status).

My Project Log Status Only Jobs with open project log items display. Each job displays two bars:

- The first bar shows all project log items (including change requests) that are open (not checked as 'Closed' on the log).

- The second bar shows the overdue items (a subset of the open items) – these are any items where the 'Respond By' date is today or earlier.

Clicking on a bar opens the Project Log showing the list of appropriate items (either all open items or all overdue items) – UNLESS you have a saved filter, in which case the saved filter will be used to display the log.

My Proposed Purchase Orders

- Lists all proposed purchase orders across all companies, where the operator is set as a contact on a job referenced on a detail line of the purchase order.

- Shows the Job number and PO number.

- A tooltip shows the number of detail lines that reference the job number, and the ordered date. Clicking on one of the detail lines opens the purchase order in PO Entry.

My Responses to Review

- Requires the Project Management module is required.

- Displays all auto-record response project log items that have an email response.

- Item appears on the app until the its status is set to 'Closed' or the response text is removed.

- Sorted with most recent on top. The tool tip provides current information.

My Subcontracts

- Displays a list of subcontracts where the operator has a linked contact (set up in Operator Maintenance) and the contact is listed as both a job contact and a vendor contact. (Adding a contact to the subcontract sets that contact up in both places.)

- Each item displays as subcontract, job description.

- Clicking on a subcontract opens the My Subcontract Manager screen, defaulting in the vendor code and subcontract number.

My Time Cards to Review

- Requires the Workflow module.

- Displays the number of employees that have time cards to be reviewed.

- Totals are sorted by company code.

- Click on a row to be taken to the Time Card Approval screen on a new Spectrum tab.

My Proposed Change Request Aging

- Displays a pie chart showing proposed change requests (status = action type 4), for my jobs.

- Totals are based on the number of days between the origination date and the current server date - less than 8 days, 8 to 30 days, or over 30 days.

- Clicking on any section opens the Proposed Change Requests app for that range of change requests. This displays a bar chart showing number of days old. A tooltip shows the dollar amount, number of days old, and description. Clicking on one of these opens the change request.

My Responses to Review

- Displays the email responses have been received for log entries on 'My Jobs'.

- The Job # and Category # display on each row. Sorted with most recent on top.

- Log entries are sorted by response date (most recent response date on top). Hover over a row to display the response date. Items will appear on the app until the item's status is set to 'Closed' or the response text is removed.

- Click on the link to open the record in either Log Entry or the associated HTML form.

My Unapproved Invoices

- Displays all unapproved invoices for the current operator, across all companies.

- Shows the vendor name, and dollar amount of the invoice.

- A tooltip shows the company code, and clicking on a code opens the Unapproved invoice screen for the current operator (showing all invoices in that company, not just the one clicked on).

My Current Workflow Assignments


- Tasks that have been assigned to you appear on the My Current Workflow Assignments app, ordered by most overdue first.

- The status of the step appears as a prefix to the workflow item. Items without a 'Due in' prefix indicate that no due date has been set.

- Hovering over an item lists who the assignment is assigned to (you, a group, a role), as well as the date and time it is due.

- Click on a record to open in the appropriate screen for that step.

Profit Fade
 Shows profit fade information by Job totals, Top 10, and My Jobs.
Profit fade is calculated as:

1. Current Profit = Revised Contract – Current Projected Cost (or Current Estimate if no Projected cost)

1. Original Profit = Original Contract – Original Estimate

1. Profit Fade = Original Profit – Current Profit (negative number is good, positive number is bad)

Project Log Shortcuts


- Displays your default Saved Selections for the Project Log.

## Service

AppDescription
My Open Work Orders

- Displays all open work orders assigned to the current technician. Open work orders are defined as ones assigned a dispatch code with type = Open, Assigned, Arrived, or None, plus non-complete work orders with no dispatch code assigned.

- Work orders are sorted in order of scheduled date, scheduled time, work order number, and site name.

- If the work order has no scheduled date, it appears below, sorted by priority description in place of date.

My Other Work OrdersDisplays all work orders assigned to the current technician that are not yet completed and don't appear in the My Open Work Orders list.
Other work orders are defined as ones assigned a dispatch code with type = Proposed, Hold, or Finished.
Work orders are sorted by dispatch status description, work order number, and the site name.
Finished work orders appear at the top of the list with the latest date/time on top, and undated work orders appear at the bottom of the list.

My Work Order Time

- Displays labor hours across all work orders assigned to the current technician during the past eight days. Includes all time from both open and completed work orders, time from work order labor transactions originating from Field Tech entry, time posted in Payroll, and any records entered in Work Order regardless of whether they have been transferred to Payroll.

- Sorted with the latest work order date appearing at the top of the list, and Regular and Overtime hours noted when available.

- Double-click on an item to open the Field Tech Time Entry screen.

Truck Inventory

- This dashboard app displays items set up in the warehouse assigned to the current technician, plus the available quantity on-hand of each item. Sorted by item code order.

- Hover over an item to show the reorder point, as specified in Item Warehouse Details.

- Double-click on an item to open the Truck Stock Manager screen.

Truck Restocking Alerts

- Displays items that are at or below the reorder point. Lists only items for the warehouse assigned to the current technician.

- Hover over an item to show the reorder point, as specified in Item Warehouse Details.

- Double-click on an item to open the Truck Stock Manager screen. Note: If the current operator is not a Work Order technician with an assigned warehouse (truck), or if all items in the warehouse are fully stocked, this appears empty.

## Subcontract Kiosk

AppDescription
My Subcontract Warnings and Alerts

- Displays open compliance items among subcontracts for the Subcontract Kiosk user.

- Click on any of the items to open the Submit Documentation screen in context.

- Hover over an item to show the job number associated with the subcontract and the due date of the compliance item.

## Utilities

AppDescription
Favorites

- A customizable list of links that have been added from the Site Map.

- Displays only links which are valid for the current company.

My Current Workflow Assignments


- Tasks that have been assigned to you appear on the My Current Workflow Assignments app. Items on this list are ordered by most overdue first.

- The status of the step appears as a prefix to the workflow item. Items that are the most overdue appear first. Items without a 'Due in' prefix indicate that no due date has been set.

- Hovering over an item lists who the assignment is to (you, a group, a role), as well as the date and time it is due.

- Click on a record to open in the appropriate screen for that step.

RSS Feeds

- Acronym for Really Simple Syndication, RSS feeds are web feed formats that are used to publish frequently-updated works such as blogs or news headlines.

To Do List

- A free-form list of operator tasks.

## Custom Apps

Steps for creating an RSS feed app from another application:

1. For the Type, select RSS Feed.

1. Enter the URL for the feed.

1. If you want to apply different shades to each row marker, choose an Accent color.Choose an HTML color value (RED, BLUE, and so on).

1. If you want to distinguish RSS feed apps from each other, in the Background field, choose Dark or Light.

Related information

- [Customize Dashboard Setup](/en/spectrum/spectrum/getting-started/about-dashboards/customize-dashboard-setup)

- [Dashboard Themes](/en/spectrum/spectrum/getting-started/about-dashboards/dashboard-themes)
