---
title: "About Clearing a Batch | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/ap-general-maintenance/batch-processing/about-clearing-a-batch"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/ap-general-maintenance/batch-processing/about-clearing-a-batch"
---

# About Clearing a Batch

You can clear any batch that you create in any module to remove records that you do not want to process.
When you create a batch, the system adds the data to a batch table and stores it until you are ready to post the batch; therefore, you can delete it completely without affecting any modules, including the module in which you created the batch. To clear a batch table of stored data, select File > Clear Batch. The system clears/deletes all data from the batch. Previously posted transactions that you have added to the batch are only cleared from the batch—they are not deleted form your database.
The system creates an audit record each time you clear a batch. For information about cleared batches (i.e., the user who cleared batch,as well as the date and time the batch was cleared), run the VA 'Other Event' Statistics report or look in the HQ Batch Control form.
The Clear Batch option is disabled if the batch's status is 4 (Posting in Progress). This is to prevent partially updated batches from being deleted should the update process be interrupted (for example, power outage, system failure, etc.). When a batch update is interrupted, only a portion of the intended updates may occur. If a user were to clear the batch, there would be no way to determine the updated data.
