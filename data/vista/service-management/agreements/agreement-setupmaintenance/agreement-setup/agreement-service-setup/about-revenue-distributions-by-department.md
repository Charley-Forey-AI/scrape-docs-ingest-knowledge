---
title: "About Revenue Distributions by Department | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/about-revenue-distributions-by-department"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/about-revenue-distributions-by-department"
---

# About Revenue Distributions by Department

You can have the revenue for periodic agreement services distributed to a different department than the one specified for an agreement.
If you require revenue to be distributed by department for periodic services, you can do so by selecting the Post Revenue to Service Center Department checkbox in SM Service and then specifying the department to use for the agreement service.
When you bill the agreement or agreement service (those billed separately), the system posts the revenue for that service to the Revenue account defined for the specified department. If you require separate accounting by division, you can specify a division for the agreement service; however, the division must have an alternate department specified. Then when posting revenue for the agreement service, the system uses the Revenue account for alternate department.
For periodic services that you bill separately, the total revenue amount accrued for each billing is posted to the specified Revenue account. However, for periodic services that you do not bill separately, distribution is handled somewhat differently. Because the service is billed with the agreement, the system distributes the revenue amount for each service based on the percentage of the total amount to bill that the service represents. The remainder is posted to the revenue account for the agreement's department.
For example, say the total billable amount for the agreement is $25,000, billed quarterly. This amount includes the agreement price of $21,500, one periodic service for $2000, and one periodic service for $1500. Each of the services is flagged to post to a separate department. The percentage applied to each account is calculated as follows:
Agreement: 21,500 / 25,000 = .86 (86%)
Service 1: 2000 / 25,000 = .08 (8%)
Service 2: 1500 / 25,000 = .06 (6%)
Since the agreement is billed quarterly, the amount billed each quarter is $6,250. The distributions for each payment are calculated as follows:
Included in Billing
Department
Revenue Account
Amount Distributed

Agreement
A
10000.
$5375
6250.00 x .86 = 5375.00

Service 1
B
11000.
$500
6250.00 x .08 = 500.00

Service 2
C
12000.
$375
6250.00 x .06 = 375.00

## Deferred Revenue

If the agreement is set up for revenue deferral, the system posts revenue to the Deferred Rev account for each specified department. The deferral amounts depend on the deferral schedule defined for the agreement. For example, if using a monthly deferral schedule with equal deferral amounts, the total deferred amount for our sample agreement would be 2083.33 each month (25,000 / 12). The amount posted to each Deferred Rev account would be as follows:
Included in Billing
Department
Deferred Rev Account
Amount Distributed

Agreement
A
90000.
$1791.66
2083.00 x .86 = 1791.66

Service 1
B
91000.
$166.67
2083.00 x .08 = 166.67

Service 2
C
92000.
$125.00
2083.00 x .86 = 125.00

Once you have recognized revenue (using SM Agreement Amortize Revenue), the system moves the deferred amounts from the Deferred Rev accounts to the specified department Revenue accounts.
Note: If you recognize revenue prior to billing, this may cause the deferral revenue accounts to have a negative balance until you create and process the applicable billings.

Related information

- [SM Agreements Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form)

- [SM Agreement Billings Due Form](/en/vista/vista/service-management/sm-invoices/service-management-invoice-forms/sm-agreement-billings-due-form)
