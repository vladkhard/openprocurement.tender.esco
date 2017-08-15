from openprocurement.tender.esco.utils import calculate_npv
from openprocurement.tender.esco.constants import DAYS_PER_YEAR
from openprocurement.tender.esco.npv_calculation import (
    calculate_contract_duration,
    calculate_discount_rate,
)


nbu_rate = 0.22


def contract_duration(self):
    # Minimal contract duration
    years = 0
    days = 1
    self.assertEqual(
        calculate_contract_duration(years, days),
        years * DAYS_PER_YEAR + days,
    )

    years = 0
    days = 364
    self.assertEqual(
        calculate_contract_duration(years, days),
        years * DAYS_PER_YEAR + days,
    )

    years = 5
    days = 275
    self.assertEqual(
        calculate_contract_duration(years, days),
        years * DAYS_PER_YEAR + days,
    )

    # Max contract duration
    years = 15
    days = 0
    self.assertEqual(
        calculate_contract_duration(years, days),
        years * DAYS_PER_YEAR + days,
    )


def discount_rate(self):
    days_per_year = 365

    # Predefined value
    nbu_rate = 12.5
    days = 135
    self.assertEqual(
        calculate_discount_rate(nbu_rate, days),
        4.623287671232877,
    )

    # Divide 100% by n parts and check if nbu_rate is the same as
    # nbu_rate * days_per_year / days_per_year
    n = 97
    for i in range(n + 1):
        nbu_rate = (i / float(n)) * 100
        days = days_per_year
        self.assertEqual(
            calculate_discount_rate(nbu_rate, days, days_per_year),
            nbu_rate,
        )
