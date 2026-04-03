---
title: "Setting up Formulas | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/electronic-file-table-maintenance/using-the-electronic-file-build-steps/setting-up-formulas"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/electronic-file-table-maintenance/using-the-electronic-file-build-steps/setting-up-formulas"
---

# Setting up Formulas

Using the Electronic File Formula Maintenance screen, you
 can set up formulas for use later on with the Electronic File Table Maintenance
 screen.
For example, you might want to set up a formula for an
 employee bonuses, based on their annual salary.

1. From the Payroll  >  Maintenance  >  Electronic > File Table Maintenance screen, click the Formula button. The Electronic File Formula Maintenance screen displays.

1. Enter a formula Code name (for example, BONUS).

1. Enter the formula code Descriptions (for example, EMPLOYEE BONUS 2002).

1. Enter the formula Type. Formulas can be calculated using either Records (in other words, individual pieces of information as they relate to an employee, such as an annual salary amount), or Totals (for example, an employee's year-to-date salary), or Dates.

1. In the line transactions portion of the screen, the line sequence number defaults. In the Result column, enter A for Answer (because this is a simple two-part formula).

1. In the 1st factor column, enter the variable, result code or number. In this example, press F4 or double-click in this field to open the Search File Variables window and select the PR.EHIST (Check History) file.

1. Enter the Period (in this case, select Current to base the employee bonus on their annual salary amount).

1. In the Operator field, enter * to signify that the bonus will be based on a percentage (multiplied by a percent).

1. In the 2nd factor column, enter the number that will determine the bonus percentage (for example, .02 = 2% of annual salary amount).

1. In the 2nd factor Period field, enter Current to base the bonus percentage on the current salary amount.

1. Click OK to save your formula entry.
