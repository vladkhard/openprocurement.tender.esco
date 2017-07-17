# -*- coding: utf-8 -*-
from openprocurement.tender.openeu.views.contract import TenderAwardContractResource as TenderEUContractResource
from openprocurement.tender.core.utils import optendersresource, save_tender, apply_patch
from openprocurement.api.utils import (
    context_unpack,
    json_view,
    get_now,
    raise_operation_error
)
from openprocurement.tender.openua.utils import check_tender_status
from openprocurement.tender.core.validation import (
    validate_contract_signing,
    validate_patch_contract_data,
    validate_update_contract_value,
    validate_update_contract_only_for_active_lots,
    validate_contract_operation_not_in_allowed_status
)
from openprocurement.tender.openua.validation import validate_contract_update_with_accepted_complaint
from openprocurement.tender.esco.validation import validate_esco_contract_signing


@optendersresource(name='esco.EU:Tender Contracts',
                   collection_path='/tenders/{tender_id}/contracts',
                   path='/tenders/{tender_id}/contracts/{contract_id}',
                   procurementMethodType='esco.EU',
                   description="Tender ESCO EU contracts")
class TenderESCOEUContractResource(TenderEUContractResource):
    """ Tender ESCO EU Contract Resource """
    @json_view(content_type="application/json", permission='edit_tender', validators=(validate_patch_contract_data, validate_contract_operation_not_in_allowed_status,
               validate_update_contract_only_for_active_lots, validate_contract_update_with_accepted_complaint, validate_update_contract_value, validate_contract_signing,
               validate_esco_contract_signing))
    def patch(self):
        """Update of contract
        """
        contract_status = self.request.context.status
        apply_patch(self.request, save=False, src=self.request.context.serialize())
        if contract_status != self.request.context.status and (contract_status != 'pending' or self.request.context.status != 'active'):
            raise_operation_error(self.request, 'Can\'t update contract status')
        if self.request.context.status == 'active' and not self.request.context.dateSigned:
            self.request.context.dateSigned = get_now()
        check_tender_status(self.request)
        if save_tender(self.request):
            self.LOGGER.info('Updated tender contract {}'.format(self.request.context.id),
                        extra=context_unpack(self.request, {'MESSAGE_ID': 'tender_contract_patch'}))
            return {'data': self.request.context.serialize()}
