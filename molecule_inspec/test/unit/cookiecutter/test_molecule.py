import pytest
import sh

from molecule import util

from molecule.model import schema_v2


from molecule.test.unit.cookiecutter.test_molecule import _base_class  # noqa F401
from molecule.test.unit.cookiecutter.test_molecule import _instance  # noqa F401


def test_verifier_lint_when_verifier_inspec(
    temp_dir, _molecule_file, _role_directory, _command_args, _instance  # noqa F811
):
    _command_args['verifier_name'] = 'inspec'
    _command_args['verifier_lint_name'] = 'rubocop'
    _instance._process_templates('molecule', _command_args, _role_directory)

    data = util.safe_load_file(_molecule_file)

    assert {} == schema_v2.validate(data)

    cmd = sh.yamllint.bake('-s', _molecule_file)
    pytest.helpers.run_command(cmd)
