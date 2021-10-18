import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_command(host):
    assert host.run('echo "export TEST=test" > ~/.profile.d/test.sh')
    assert host.check_output('. /etc/profile && echo $TEST') == 'test'
