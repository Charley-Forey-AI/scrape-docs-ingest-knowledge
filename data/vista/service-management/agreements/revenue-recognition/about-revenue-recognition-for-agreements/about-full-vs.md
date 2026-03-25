---
title: "About Full vs. Partial Revenue Recognition | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/revenue-recognition/about-revenue-recognition-for-agreements/about-full-vs.-partial-revenue-recognition"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/revenue-recognition/about-revenue-recognition-for-agreements/about-full-vs.-partial-revenue-recognition"
---

# About Full vs. Partial Revenue
 Recognition

When you recognize revenue (in SM Revenue Recognition), you
 can have the system perform either a full recognition or a partial recognition.
Full recognition occurs when the
 remaining deferral amount is sufficient enough to cover the scheduled
 recognition amount. Partial recognition occurs when the remaining deferral
 amount does not cover the scheduled recognition amount.
The following examples illustrate
 how the system performs full and partial recognitions.
Full RecognitionAgreement Amount: $12,000 
Billed 1/1/19:
 $6,000 
Billed 7/1/19: $6,000
Amortization MonthRecognition Schedule AmountBalance Deferred RevenueAlready Recognized RevenueAmount to Recognize
Billed 1/1/19: $6,0006,0000--
Billed-to-Date: $6,00001/20191,0006,00001,000
02/20191,0005,0001,0001,000
03/20191,0004,0002,0001,000
04/20191,0003,0003,0001,000
05/20191,0002,0004,0001,000
06/20191,0001,0005,0001,000

Billed 7/1/19: $6,0006,0006,000--
Billed-to-Date: $12,00007/20191,0006,0006,0001,000
08/20191,0005,0007,0001,000
09/20191,0004,0008,0001,000
10/20191,0003,0009,0001,000
11/20191,0002,00010,0001,000
12/20191,0001,00011,0001,000

This example assumes that the revenue recognition process is run on a
 regular monthly basis. However, if you do not run this process
 monthly, the system calculates the total amount to recognize based
 on what is available (as defined by the amortization schedule and
 the available deferred revenue), and posts that amount to the
 specified month. So, using our example above, if you did not run the
 revenue recognition process until February, the system would
 recognize a total amount of $2,000 for February, even though
 February's scheduled amount is $1,000. This is because the amount
 scheduled for January still needs to be recognized, so it is
 included in the recognized amount for February.

Partial RecognitionThe system will perform partial recognitions if the conditions
 require it; that is, if the remaining deferral amount is not
 sufficient to cover the scheduled recognition amount. Using the same
 Recognition Schedule defined above, let's say the first billing is
 less than the second billing:
Agreement Amount: $12,000 
Billed 1/1/19:
 $5,500 
Billed
 7/1/19: $6,500
The result would be as follows:
Amortization MonthRecognition Schedule AmountBalance Deferred RevenueAlready Recognized RevenueAmount to Recognize
Billed 1/1/19: $5,5005,5000--
Billed-to-Date: $5,50001/20191,0005,50001,000
02/20191,0004,5001,0001,000
03/20191,0003,5002,0001,000
04/20191,0002,5003,0001,000
05/20191,0001,5004,0001,000
06/20191,0005005,000500

Billed 7/1/19: $6,5006,5005,500--
Billed-to-Date: $12,00007/20191,0006,5005,5001,500
08/20191,0005,0007,0001,000
09/20191,0004,0008,0001,000
10/20191,0003,0009,0001,000
11/20191,0002,00010,0001,000
12/20191,0001,00011,0001,000

Note that for the month of June, only $500 of the scheduled $1,000
 was recognized due to the fact that only $500 remained in the
 Deferred Revenue account. This left a balance of $500 to be
 recognized when the next payment was made (7/1/2019). When the
 amortization process was run at the end of July, the system included
 the $500 of unrecognized revenue for June in the Amt to Recognize
 for July.

Related information

- [About Revenue Recognition for Agreements](/en/vista/vista/service-management/agreements/revenue-recognition/about-revenue-recognition-for-agreements)
