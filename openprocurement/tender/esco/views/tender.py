# -*- coding: utf-8 -*-
from openprocurement.tender.openeu.views.tender import TenderEUResource
from openprocurement.tender.core.utils import optendersresource


#  TODO: remove these import section after adding auction
from openprocurement.api.utils import json_view, error_handler
from openprocurement.tender.core.validation import (
    validate_tender_status_update_in_terminated_status,
    validate_tender_status_update_not_in_pre_qualificaton
)
from openprocurement.tender.openua.validation import validate_patch_tender_ua_data


@optendersresource(name='esco:Tender',
                   path='/tenders/{tender_id}',
                   procurementMethodType='esco',
                   description="Open Contracting compatible data exchange format. See http://ocds.open-contracting.org/standard/r/master/#tender for more info")
class TenderESCOResource(TenderEUResource):
    """ Resource handler for Tender ESCO """
