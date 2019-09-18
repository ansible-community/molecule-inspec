import os
import pytest
import sh
from molecule.test.conftest import change_dir_to  # noqa F401


@pytest.fixture
def scenario_to_test(request):
    return request.param


@pytest.fixture
def scenario_name(request):
    try:
        return request.param
    except AttributeError:
        return None


@pytest.fixture
def driver_name(request):
    return request.param


def test_command_init_role_inspec(temp_dir):
    role_directory = os.path.join(temp_dir.strpath, 'test-init')
    options = {'role_name': 'test-init', 'verifier_name': 'inspec'}
    cmd = sh.molecule.bake('init', 'role', **options)
    pytest.helpers.run_command(cmd)
    pytest.helpers.metadata_lint_update(role_directory)

    with change_dir_to(role_directory):
        cmd = sh.molecule.bake('test')
        pytest.helpers.run_command(cmd)


def test_command_init_scenario_inspec(temp_dir):
    role_directory = os.path.join(temp_dir.strpath, 'test-init')
    options = {'role_name': 'test-init'}
    cmd = sh.molecule.bake('init', 'role', **options)
    pytest.helpers.run_command(cmd)
    pytest.helpers.metadata_lint_update(role_directory)

    with change_dir_to(role_directory):
        molecule_directory = pytest.helpers.molecule_directory()
        scenario_directory = os.path.join(molecule_directory, 'test-scenario')
        options = {
            'scenario_name': 'test-scenario',
            'role_name': 'test-init',
            'verifier_name': 'inspec',
        }
        cmd = sh.molecule.bake('init', 'scenario', **options)
        pytest.helpers.run_command(cmd)

        assert os.path.isdir(scenario_directory)
