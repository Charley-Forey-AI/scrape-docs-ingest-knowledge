---
title: "About Revenue Recognition for Agreements | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/revenue-recognition/about-revenue-recognition-for-agreements"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/revenue-recognition/about-revenue-recognition-for-agreements"
---

# About Revenue Recognition for
 Agreements

The revenue recognition process allows you to recognize
 deferred revenue based on a defined deferral schedule and billed-to-date amounts.
When you recognize revenue for agreements and/or
 periodic services (in the SM Revenue Recognition form), the system moves the recognized
 amounts from the appropriate Deferred Revenue accounts to the appropriate Revenue
 accounts.
If you are distributing revenue to multiple
 departments (that is, you selected the Post Revenue to Service Center
 Department checkbox for applicable periodic services on the agreement),
 the system posts revenue as follows:

- Agreement revenue is posted to the department specified for the Agreement
 Type associated with the agreement.

- Service revenue is posted to the department specified for the service center
 associated with each applicable service (in SM Service).

For agreement services billed separately,
 the system determines the amount to recognize based on the deferral schedule for the
 agreement service, less amounts already recognized. It then moves that amount from the
 Deferred Rev account to the specified department's Revenue account.
For agreement services included in the agreement
 billing, the system determines the amount to recognize based on the agreement's deferral
 schedule, less previously recognized amounts. It then distributes the amount
 proportionately to each specified Revenue account.
ExampleThe total billable amount for an agreement is $25,000, which includes the
 agreement price of $21,500, one periodic service for $2000, and one periodic service
 for $1500. The percentages for revenue distribution are calculated as follows:
Agreement: 21,500 / 25,000 = .86
 (86%)
Service 1: 2000 / 25,000 =
 .08 (8%)
Service 2: 1500 / 25,000
 = .06 (6%)
When recognizing revenue, these percentages are applied to
 determine the amount moved from the Deferred Rev accounts to the Revenue accounts.
 For our example, we will assume a recognized revenue amount of $5000. In this case,
 the amount would be distributed to the applicable Revenue accounts as follows:
Table 1. DepartmentRevenue AccountAmount DistributedCalculation
AgreementA10000.$4,3005,000 x .86 = 4,300.00
Service 1B11000.$4005,000 x .08 = 400.00
Service 2C12000.$3005,000 x .06 = 300.00

The system allows you to recognize revenue even if you have not created a billing
 for the agreement or agreement service, as long as the deferral dates fall on or
 before the recognition date. However, recognizing revenue before any billing occurs
 may cause the deferral revenue account (defined by department in SM Departments) to
 have a negative balance until you create and process the applicable
 billings.

Related information

- [About Full vs. Partial Revenue Recognition](/en/vista/vista/service-management/agreements/revenue-recognition/about-revenue-recognition-for-agreements/about-full-vs.-partial-revenue-recognition)

- [About Revenue Amortization for Amendments](/en/vista/vista/service-management/agreements/revenue-recognition/about-revenue-recognition-for-agreements/about-revenue-amortization-for-amendments)
