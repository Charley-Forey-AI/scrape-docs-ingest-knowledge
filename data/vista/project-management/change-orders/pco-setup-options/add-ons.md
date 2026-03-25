---
title: "Add-Ons | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/change-orders/pco-setup-options/add-ons"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/change-orders/pco-setup-options/add-ons"
---

# Add-Ons

The Add-Ons tab in the PM Pending Change Orders form is used to create and modify add-on costs for items on a pending change order. Each change order item will initially default all add-ons set up for the project in PM Project Add-ons (accessed from PM Projects). Any add-ons entered for a project after a change order has been set up must be added for applicable change order items manually.
The add-on basis (Percent or Amount) determines whether the add-on will be a calculation or a fixed amount. If the add-on is a Percent type, the add-on amount is percentage of the Net Amount plus markups, plus any previous add-on amounts.
Add-on Phases/Cost Types
If add-on phases and cost types are not already set
 up for the project, they will be added to JCJP (Job Phases) and JCCH (Job Cost Header)
 as soon as the first pending change item for a given project is saved, regardless of how
 the ‘Phases on this Job are Locked’ option is set in PM Projects.
Note: Deleting a pending change order item does not automatically
 delete the add-on phase/cost type from JCJP and JCCH—you must delete them
 manually.)
You also have the option to override the Total Amount by entering a fixed amount. This is useful if the final amount of the change order item is negotiated and agreed upon as a fixed amount, or if the unit price requires an override to make “even amount” unit prices. To enter a fixed amount, check the Fixed Amount Flag (Info tab, PM Pending Change Order items), and enter the Fixed Amt for the selected change order item.
Example
Net Amount = $6,000.00
Markup Total = $600.00
Add-On
Description
Basis
Add-On %
Add-On Amount
Calculation

1
Taxes
P
6.00%
396.00
(6,000 + 600 = 6,600) X 6%

2
Bonds
P
10.00%
699.60
(6,000 + 600 + 396 = 6,996) x 10%

Amount-type add-ons are flat amounts, so the percentage is calculated instead of the add-on amount. The percentage is a calculation of the Add-On Amount divided by the Net Amount plus the Markup Total, plus any previous Add-On amounts.
The 'Add-on Type' assigned to each add-on determines how it will be calculated, and in what order. There are three types of add-ons:

- Net Total – The system calculates these add-ons
 first and bases them on Cost, Cost plus Markup, or Total, depending on the ‘Net
 Add-On Calculation Level’ you specified for the add-on in PM Project Add-Ons.

- Sub Total – These add-ons are calculated second and
 are based on the net amount plus markups, plus 'net total' add-ons. Sub total
 add-ons are calculated using a '5-cycle' method to provide the most accurate
 add-on total; that is, five calculations will occur for each sub total add-on,
 with the final calculation being the 'add-on' amount. This allows sub total
 calculations to include themselves, with the result being a more accurate add-on
 amount. The 5-cycle process works like this: The first calculation produces an
 'add-on' amount, which is added to the 'total'. The four remaining calculations
 are handled in the same manner, except that the 'add-on amount' will be the
 'variance' amount (i.e. the add-on's previous amount minus the current amount).
 During this process, the variance amount eventually nets to the lowest value
 possible, with the final 'add-on' amount being the add-on amount calculated during
 the last cycle.

For example:
Net Amount: $600,000.00
Markups: $4020.00
'Net Total' Add-ons: $0.00 
 The following 'Sub-Total' add-ons would be calculated as follows:
Subtotal Add-ons
Add-on Total
Variance
Total

Pass 1:

Add-on 1 (1.00%)
6,040.20
0.00
610,060.20

Add-on 2 (1.00%)
6,100.60
0.00
616,160.80

Add-on 3 (5.00%)
30,808.04
0.00
646,968.84

Pass 2:

Add-on 1
6,469.69
429.49
647,398.33

Add-on 2
6,473.98
373.38
647,771.71

Add-on 3
32,388.59
1,580.55
649,352.26

Pass 3:

Add-on 1
6,493.52
23.83
649,376.09

Add-on 2
6,493.76
19.78
649,395.87

Add-on 3
32,469.79
81.20
649,477.07

Pass 4:

Add-on 1
6,494.77
1.25
649,478.32

Add-on 2
6,494.78
1.02
649,479.34

Add-on 3
32,473.97
4.18
649,483.52

Pass 5:

Add-on 1
6,494.84
0.07
649,483.59

Add-on 2
6,494.84
0.06
649,483.65

Add-on 3
32,474.19
0.22
649,483.87

Sub Total Add-ons:
45,463.87

Grand Total:
649,483.87

Grand Total Add-ons:
3,247.42

CO Item Total:
652,731.29

- Grand Total – This type of add-on
 will calculate an add-on amount based on the net amount plus markups plus 'net total'
 add-ons plus 'sub total' add-ons. The exception to this rule is when the ‘Include in
 Subtotal Add-on Calculation’ option is checked (in PM Project Add-Ons). In this case,
 grand total add-ons are calculated after net add-ons, with the resulting amount
 accumulated into the pending total. Subtotal add-ons are calculated next and will
 include the grand total add-ons. The sum of the grand total add-ons will then be
 subtracted from the pending total, and the grand total add-ons recalculated. You will
 typically use this feature when sub-total add-ons need to be based on the grand total
 rather than the net total.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Orders - Overview
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form)Project Add-Ons
