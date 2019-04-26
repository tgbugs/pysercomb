from pathlib import Path
from protcur.config import __script_folder__ as pasf
from pysercomb.parsers import units

(parameter_expression, quantity, unit, *_,
 debug_dict) = units.make_unit_parser(Path(pasf, '../../protc-lib/protc/units'))

*_, test_all, parsed = units.parse_for_tests(parameter_expression)

# evil
_gs = globals()
_gs.update(debug_dict)
