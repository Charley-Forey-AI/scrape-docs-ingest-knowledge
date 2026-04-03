---
title: "Reclassify Pay Among Tax Jurisdictions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/in-depth-overview/reclassify-pay-among-tax-jurisdictions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/in-depth-overview/reclassify-pay-among-tax-jurisdictions"
---

# Reclassify Pay Among Tax Jurisdictions

If an operator enters a negative time card line to a job
 with state, county and local tax in the Job File Maintenance fields, and reviews the check
 adjustment entry for the negative state, county and local taxes, he or she will see that it
 does not reflect any dollar amounts.
The Wage and Tax Listing reflects the negative "subject to" amounts for the taxes but the
 actual negative tax is not calculated and reflected for any of the tax jurisdictions. The
 same results are found on the Sales Tax History Report. This is because the software has
 been designed to reflect the negative income tax "subject to" amount, but not calculate the
 negative income tax automatically to allow the user the option to decide whether or not it
 is appropriate to refund the taxes or not. If it is decided that the taxes need to be
 refunded, the correct taxes can be edited in the "SIT" window as found in the Check
 Adjustment Entry screen (PR.EDENT). The operator will need to be aware that if there are
 both negative and positive time card lines to these tax codes, the net amount must be
 entered.
Sometimes, entry of negative hours in Time Card Entry is made in order to reclassify time to a different job and/or phase. If this case and the job and/or phase have the same tax code setup as the original entries, then it is not necessary to correct any related income tax withheld, since these taxes do not affect the expenses distributed to the job because they are paid by the employee.
The best way to reclassify the hours as described above, is to include positive (correct job and/or phase) and negative (initial job and/or phase) time card line entries on a regular payroll check. This ensures that the FICA, FUTA and SUTA taxes are calculated correctly since these taxes are calculated on total "gross" pay. The Worker's Compensation and/or SDI may need to be edited within the Check Adjustment Entry screen depending upon changes in rates and/or limits at the time the entry is made. The Wage and Tax Listing and/or Job Distribution Reports from the initial payroll can be used to determine the appropriate tax amounts. A Wage and Tax History Report can be printed for that pay period to provide tax information as well.
If a "zero" dollar check is processed as a result of entering the positive and negative time card entries, the FICA, FUTA, and SUTA taxes will not calculate to be redistributed, since calculation of these taxes is based on the total "gross" pay and not by time card line entry. If this is the preferred method to reclassify the hours, then additional entries for the applicable tax amounts in the Job Cost Transaction Entry screen are necessary to redistribute the taxes to the correct job(s) and /or phase(s). The Worker's Compensation and/or SDI may need to be edited within the Check Adjustment Entry screen depending upon changes in rates and/or limits at the time the entry is made. The Wage and Tax Listing and/or Job Distribution Reports from the initial payroll can be used to determine the correct tax amounts. Also, a Wage and Tax History Report can be run for that pay period to provide tax information as well.
If the reclassification would involve changes to the tax jurisdiction(s) "subject to" and tax amount(s), typically the best way to make this correction is to void the original payroll check and enter a new check to correct both the distribution to the job and/or phase(s) as well as any tax related issues. If the employee has cashed the original check, it still needs to be voided in the software and a manual check using a similar check number (such as the same number with a zero in front of it or an "A" next to it) can be entered. This entry will require corrections to the income tax amounts in the Check Adjustment Entry screen. By windowing on the SIT field, the user can adjust the applicable tax amounts per jurisdiction. Be sure to enter over to the FIT field to correct this tax amount as well.
Important: If you are unable to determine which method is
 best for you, please contact Viewpoint Support by visiting the [Viewpoint
 Customer Portal](https://support.viewpoint.com/s/).
