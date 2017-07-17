# -*- coding: utf-8 -*-
from openprocurement.api.utils import raise_operation_error


def validate_esco_contract_signing(request):
    data = request.validated['data']
    if 'status' in data and data['status'] == 'active':
        raise_operation_error(request, "Can't sign esco contract (not implemented)")

