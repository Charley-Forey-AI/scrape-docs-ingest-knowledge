---
title: "About Revenue Amortization for Amendments | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/revenue-recognition/about-revenue-recognition-for-agreements/about-revenue-amortization-for-amendments"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/revenue-recognition/about-revenue-recognition-for-agreements/about-revenue-amortization-for-amendments"
---

# About Revenue Amortization for Amendments

When you recognize revenue for amended agreements, the system determines the amount to recognize based on the amortization schedule defined for the amended agreement or agreement service.
When you amend an agreement, the system copies the
 agreement's amortization schedule, minus any revenue that has already been billed. The
 portion of the amortization schedule containing the billed amount(s) will remain with the
 terminated revision.
When you recognize revenue (via SM Agreement
 Amortize Revenue) for the amendment, the system determines the amount to recognize based on
 the deferral schedule, less amounts already recognized. Scheduled revenue that was
 recognized prior to the amendment but was moved to the amendment because it was not billed,
 will be reversed out from the terminated revision and applied to the amendment
 revision.
 For example, say you recognize $6000 of revenue and have billings that total $5000. You then create an amendment. Because you only billed $5000, the deferral schedule for the terminated revision will include only entries for the $5,000 that was billed. The remaining entries will move to the amendment revision, including an entry for the $1000 of revenue that you recognized but did not bill for (as shown in the example below).
Original AgreementDeferralDateAmountRecognizedTotal Billed
11/1/19$3,000Y$5,000
24/1/19$3,000Y
37/1/19$3,000N
410/1/19$3,000N

After Amending the AgreementTerminated RevisionAmendment
DeferralDateAmountDeferralDateAmount
11/1/19$3,00014/1/19$1,000
24/1/19$2,00027/1/19$3,000
310/1/19$3,000

When you run SM Agreement Amortize Revenue, the $1000 of scheduled revenue that
 moved to the amendment will be reversed from the recognized revenue of the terminated
 revision and included in the revenue recognition for the amendment
 revision.

Related information

- [Run the Revenue Recognition Process](/en/vista/vista/service-management/agreements/revenue-recognition/run-the-revenue-recognition-process)

- [SM Revenue Recognition Form](/en/vista/vista/service-management/agreements/revenue-recognition/service-management-revenue-recognition-forms/sm-revenue-recognition-form)
