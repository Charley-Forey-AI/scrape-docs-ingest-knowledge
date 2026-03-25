---
title: "SM Revenue Recognition Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/revenue-recognition/service-management-revenue-recognition-forms/sm-revenue-recognition-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/revenue-recognition/service-management-revenue-recognition-forms/sm-revenue-recognition-form"
---

# SM Revenue Recognition Form

Use the SM Revenue Recognition form to recognize revenue for applicable agreement billings, agreement service billings, and SM customer work orders.
When you run the revenue recognition process, the system creates a batch for all items that are eligible for revenue recognition up through the specified date. Eligibility is determined as follows:

- Agreement and service billings using the A-Amortize revenue recognition method - With this method, the system determines eligibility as follows:

- An [amortization schedule](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-amortization-schedule-setup/set-up-an-agreement-amortization-schedule-manually) must be defined for the agreement or for agreement services with a periodic pricing method that are flagged for separate billing.

- Billings must exist for the agreement and/or agreement service, and deferred amounts must be available for recognition.

- The deferral date(s) defined for the agreement and/or agreement service must fall on or before the Through Date specified for the amortization session.

- Agreement and/or agreement service revision cannot exist in an open batch.

- Agreement cannot be in the process of being amended.

- Agreements and customer work orders using the C-As Cost Incurred revenue recognition method - With this method, the system uses work completed lines to calculate revenue to recognize. Eligibility is determined as follows:

- The work completed line must be posted to an agreement work order scope where the revenue recognition method is 'As Cost Incurred' and where the work completed line's date falls on or before the specified through date.Note: For generated agreement work order scopes, the revenue recognition method defaults to C-As Cost Incurred and cannot be changed. However, if you manually add a work order scope to an agreement work order, you must manually set the revenue recognition method to C-As Cost Incurred if you want work completed lines posted to the work order scope to be eligible for revenue recognition.

- The work completed line must be posted to a customer work order scope where the revenue recognition method is 'As Cost Incurred' and where the work completed line's date falls on or before the specified through date.

- Work completed lines cannot exist in an open batch.

The system determines the amount to recognize for each agreement or agreement service based on the total deferral amounts from the amortization schedule for dates falling on or before the specified Through Date and the total billed to-date for the agreement or agreement service minus revenue amounts already recognized.
Click the following link for more information about revenue recognition.
[Run the Revenue Recognition Process](/en/vista/vista/service-management/agreements/revenue-recognition/run-the-revenue-recognition-process)

Related information

- [SM Agreement Amortization Schedule Form](/en/vista/vista/service-management/agreements/revenue-recognition/service-management-revenue-recognition-forms/sm-agreement-amortization-schedule-form)

- [SM Agreement Service Deferral Form](/en/vista/vista/service-management/agreements/revenue-recognition/service-management-revenue-recognition-forms/sm-agreement-service-deferral-form)

- [SM Agreements Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form)

- [About Revenue Recognition for Agreements](/en/vista/vista/service-management/agreements/revenue-recognition/about-revenue-recognition-for-agreements)

- [About Full vs. Partial Revenue Recognition](/en/vista/vista/service-management/agreements/revenue-recognition/about-revenue-recognition-for-agreements/about-full-vs.-partial-revenue-recognition)

- [About Revenue Amortization for Amendments](/en/vista/vista/service-management/agreements/revenue-recognition/about-revenue-recognition-for-agreements/about-revenue-amortization-for-amendments)

- [About Voiding Billings After Recognizing Revenue](/en/vista/vista/service-management/agreements/revenue-recognition/about-voiding-billings-after-recognizing-revenue)
