from scuq.quantities import Quantity
from scuq.si import *
from scuq.units import AlternateUnit

a=Quantity(VOLT, 2)
mV=AlternateUnit("mV", VOLT/1000)
op_VtomV=VOLT.get_operator_to(mV)

a_mV=op_VtomV.convert(a)

print a, "=", a_mV
