---
title: "About the JC Initialize Reversals Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-initialize-reversals-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-initialize-reversals-form"
---

# About the JC Initialize Reversals Form

This form can be accessed by selecting the 'Initialize Reversals' option from the File menu of either JC Cost Adjustments or JC Revenue Adjustments, and is used to reverse accruals; that is, transactions for which the Auto Reversal option is checked.
Note: This feature is not available for intercompany cost adjustments or revenue adjustments. Intercompany adjustments are identified by a transaction type (JC Type or Rev Type) of "IC".
To reverse accruals, create a new batch and specify the 'original month' and 'reversal transaction date'. The new batch must be in a month that is later than the accrual month. Once you click OK, all transactions posted to a month that is less than or equal to the 'Original Month' you specified, and having a reversal status of '1' (i.e. Auto Reversal option checked), will be initialized to the batch.
After reversals are initialized, you are returned to the appropriate adjustments program, where you can make changes to each item as necessary and post the batch. Changes might include editing or deleting transactions or canceling a reversal (Reversal option ‘4-Cancel Reversal’).

- If you delete a transaction, it will be available for reversal the next time you run the program for the current month or a later month.

- Canceled reversals will not be posted and will not be initialized into a later batch.

Once you have reversed an accrual and processed the batch, neither the original accrual transaction nor the reversal transaction can be pulled back into an adjustments batch. Nor can you pull cancelled reversals back into an adjustment batch once processed.
