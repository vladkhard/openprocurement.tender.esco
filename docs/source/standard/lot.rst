.. . Kicking page rebuild 2014-10-30 17:00:08
.. include:: defs.hrst

.. index:: Lot

.. _Lot:

Lot
===

Schema
------

:id:
    string, auto-generated

:title:
   string, multilingual

   The name of the tender lot.

:description:
   string, multilingual

   Detailed description of tender lot.

:minValue:
   :ref:`minValue`, required

   Total available tender lot budget. Bids smaller then ``minValue`` will be rejected.

:guarantee:
    :ref:`Guarantee`

    Bid guarantee

:minimalStep:
   float, required

   The minimal step of auction (raising). Validation:

   * minimal value for minimal step is 0 (0%)
   * maximum value for miminal step is 1 (100%)


:auctionPeriod:
   :ref:`period`, read-only

   Period when Auction is conducted.

:auctionUrl:
    url

    A web address for view auction.

:status:
   string

   :`active`:
       Active tender lot
   :`unsuccessful`:
       Unsuccessful tender lot
   :`complete`:
       Completed tender lot
   :`cancelled`:
       Cancelled tender lot

   Status of the Lot.

Workflow
--------

.. graphviz::

    digraph G {
        A [ label="active*" ]
        B [ label="complete"]
        C [ label="cancelled"]
        D [ label="unsuccessful"]
         A -> B;
         A -> C;
         A -> D;
    }

\* marks initial state
