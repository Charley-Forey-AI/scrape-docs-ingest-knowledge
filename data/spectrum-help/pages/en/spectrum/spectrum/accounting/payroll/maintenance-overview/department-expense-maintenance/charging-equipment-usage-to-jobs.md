---
title: "Charging Equipment Usage to Jobs | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/department-expense-maintenance/charging-equipment-usage-to-jobs"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/department-expense-maintenance/charging-equipment-usage-to-jobs"
---

# Charging Equipment Usage to Jobs

Complete the following steps to charge equipment usage to a selected job.

1. On the Site Map
 screen, click System Administration > Installation > Equipment > Control – G/L Codes.

1. At the Job revenue credit G/L account code field, designate which G/L account to credit for equipment usage on a job.

1. At the Rental revenue credit G/L account code field, designate the G/L account to credit with third party equipment rental, and then click OK.

1. On the Site Map
 screen, click Equipment Control > Maintenance > Equipment.

1. At the Equipment
 code field, enter the equipment code for the equipment you will be
 charging. If you do not know the equipment code, press F4 or double-click on this field to
 select from a list of available equipment codes.

1. In the Rates section, enter the job and rental rates to
 be charged to jobs and third parties respectively, and then click
 OK.Note: You have the option of
 setting up special job usage rates to override the job rates specified in
 Equipment File Maintenance in the
 Job/Equipment Rate File Maintenance screen. Billing
 rates set up in either place will default during time card entry.

1. On the Site Map
 screen, click Payroll > Maintenance > Department Expense and designate the G/L account to debit for equipment usage in the
 Equipmentusage field. [Designating which G/L Account to Debit for Equipment Usage](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/department-expense-maintenance/designating-which-gl-account-to-debit-for-equipment-usage)

1. On the Site Map screen, click Payroll  >  Data Entry  >  Payment Processing  >  Time Card Entry.

1. For each employee with equipment usage charges, be sure to enter one of the following equipment codes at the Pt field when entering equipment usage charges:

1. ER (Equipment regular)

1. EO (Equipment overtime)

1. ED (Equipment double-time)

1. EU (Equipment usage)
Note: Pay types ER, EO and ED allow you to enter time for an
 employee doing work while simultaneously charging a specific piece of equipment to a
 job. This will pay the employee while charging the job at the billing rate designated
 for that piece of equipment in Equipment File Maintenance. Pay type EU allows you to
 enter time the employee spent running the specific piece of equipment only. It does
 not allow you to simultaneously pay the employee and charge a piece of equipment to a
 job. When a transaction for pay type ER, EO, ED, or EU is added, the software will
 evaluate whether the equipment code assigned to the time card entry has any active
 attachments. If so, additional EU time cards will be generated automatically or the
 [Attached Equipment window](/en/spectrum/spectrum/accounting/payroll/data-entry/pre-time-card-entry-by-job/attached-equipment-window) will display (based on the Automatically add transactions for attached equipment setting in the
 Equipment Control Installation - Properties screen).

1. Complete this screen and click Save. When Payroll updates, the ER, EP, EO, and EU entries will post a debit to Direct Job Equipment Cost Usage and a credit to the Equipment Revenue file.
