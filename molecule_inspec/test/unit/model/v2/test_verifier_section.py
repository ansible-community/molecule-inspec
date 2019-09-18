import pytest
from molecule.test.conftest import change_dir_to  # noqa F401
from molecule.model import schema_v2
from molecule.test.unit.model.v2.conftest import _molecule_file  # noqa F401
from molecule.test.unit.model.v2.conftest import _config  # noqa F401
from molecule_inspec.inspec import Inspec


@pytest.fixture
def _model_verifier_allows_inspec_section_data():
    return {'verifier': {'name': 'inspec', 'lint': {'name': 'rubocop'}}}


@pytest.mark.parametrize(
    '_config', [('_model_verifier_allows_inspec_section_data')], indirect=True
)
def test_verifier_allows_name(_config):  # noqa F811
    assert {} == schema_v2.validate(_config)


@pytest.fixture
def _model_verifier_errors_inspec_readonly_options_section_data():
    return {
        'verifier': {
            'name': 'inspec',
            'options': {'foo': 'bar'},
            'lint': {'name': 'rubocop'},
        }
    }


@pytest.fixture
def _config_verifier_inspec_section_data():
    return {'verifier': {'name': 'inspec', 'lint': {'name': 'rubocop'}}}


@pytest.mark.parametrize(
    'config_instance', ['_config_verifier_inspec_section_data'], indirect=True
)
def test_verifier_property_is_inspec(config_instance):
    assert isinstance(config_instance.verifier, Inspec)


@pytest.mark.parametrize(
    '_config',
    [('_model_verifier_errors_inspec_readonly_options_section_data')],
    indirect=True,
)
def test_verifier_errors_readonly_options_section_data(_config):  # noqa F811
    x = {'verifier': [{'options': [{'foo': ['field is read-only']}]}]}

    assert x == schema_v2.validate(_config)
