# ansible-role-cyhy-commander #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-cyhy-commander/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-cyhy-commander/actions)
[![License](https://img.shields.io/github/license/cisagov/ansible-role-cyhy-commander)](https://spdx.org/licenses/)
[![CodeQL](https://github.com/cisagov/ansible-role-cyhy-commander/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-cyhy-commander/actions/workflows/codeql-analysis.yml)

An Ansible role for installing
[cisagov/cyhy-commander](https://github.com/cisagov/cyhy-commander).

## Requirements ##

None.

## Role Variables ##

| Variable | Description | Default | Required |
| -------- | ----------- | ------- | -------- |
| cyhy\_commander\_cyhy\_core\_version | The version of cisagov/cyhy-core to use; must be a valid git reference. | `v1.3.2` | No |
| cyhy\_commander\_domainsync\_frequency | The frequency of running `cyhy-domainsync`, the hostname housekeeping script.  Must be a calendar event in the [format understood by systemd](https://www.freedesktop.org/software/systemd/man/latest/systemd.time.html#Calendar%20Events). | `daily` | No |
| cyhy\_commander\_wd40\_frequency | The frequency of running `cyhy-wd40`, the script for unsticking stuck scans.  Must be a calendar event in the [format understood by systemd](https://www.freedesktop.org/software/systemd/man/latest/systemd.time.html#Calendar%20Events). | `daily` | No |
| cyhy\_commander\_file\_owner\_group | The name of the group that should own any non-system files or directories created by this role. | [Omitted](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html#making-variables-optional) | No |
| cyhy\_commander\_file\_owner\_username | The name of the user that should own any non-system files or directories created by this role. | [Omitted](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html#making-variables-optional) | No |
| cyhy\_commander\_install\_geoipupdate | Whether to install the MaxMind geoipupdate tool. | `false` | No |
| cyhy\_commander\_maxmind\_account\_id | The MaxMind account ID for access to a GeoIP2 database subscription. | n/a | Yes |
| cyhy\_commander\_maxmind\_license\_key | The MaxMind license key that provides access to a GeoIP2 database subscription. | n/a | Yes |
| cyhy\_commander\_version | The version of cisagov/cyhy-commander to install; must be a valid git reference. | `v1.2.0` | No |

## Dependencies ##

- [cisagov/ansible-role-cyhy-core](https://github.com/cisagov/ansible-role-cyhy-core)
- [cisagov/ansible-role-pip](https://github.com/cisagov/ansible-role-pip)
- [cisagov/ansible-role-python](https://github.com/cisagov/ansible-role-python)

## Installation ##

This role can be installed via the command:

```console
ansible-galaxy install --role-file path/to/requirements.yml
```

where `requirements.yml` looks like:

```yaml
---
- name: cyhy_commander
  src: https://github.com/cisagov/ansible-role-cyhy-commander
```

and may contain other roles as well.

For more information about installing Ansible roles via a YAML file,
please see [the `ansible-galaxy`
documentation](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#installing-multiple-roles-from-a-file).

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: true
  become_method: sudo
  tasks:
    - name: Install the CyHy commander
      ansible.builtin.include_role:
        name: cyhy_commander
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Shane Frasier - <jeremy.frasier@gwe.cisa.dhs.gov>
