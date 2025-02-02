from policyengine_us.model_api import *


class nc_income_tax_before_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "North Carolina income tax before credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.NC

    def formula(tax_unit, period, parameters):
        income = tax_unit("nc_taxable_income", period)
        rate = parameters(period).gov.states.nc.tax.income.rate
        return income * rate
