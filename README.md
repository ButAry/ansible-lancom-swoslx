# LANCOM Systems SWOSLX Collection for Ansible

The Ansible LANCOM Systens SWOSLX collection includes a variety of Ansible content to help automate the management of LANCOM Systems SWOSLX network appliances.

This collection has been tested against LANCOM GS-3510XP v

## Our mission

<!-- Put your collection's mission statement in here. Example follows. -->

At the LANCOM Systems SWOSLX, our mission is to produce and maintain simple, flexible,
and powerful open-source software tailored to help automate the management of LANCOM Systems SWOSLX network appliances.

We welcome members from all skill levels to participate actively in our open, inclusive, and vibrant community.
Whether you are an expert or just beginning your journey with Ansible and LANCOM Systems SWOSLX,
you are encouraged to contribute, share insights, and collaborate with fellow enthusiasts!

## Code of Conduct

We follow the [Ansible Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html) in all our interactions within this project.

If you encounter abusive behavior, please refer to the [policy violations](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html#policy-violations) section of the Code for information on how to raise a complaint.

## Communication

* Join the Ansible forum:
  * [Get Help](https://forum.ansible.com/c/help/6): get help or help others. Please add appropriate tags if you start new discussions, for example the `YOUR TAG` tag.
  * [Posts tagged with 'your tag'](https://forum.ansible.com/tag/YOUR_TAG): subscribe to participate in collection/technology-related conversations.
  * [Refer to your forum group here if exists](https://forum.ansible.com/g/): by joining the team you will automatically get subscribed to the posts tagged with [your group forum tag here](https://forum.ansible.com/tags).
  * [Social Spaces](https://forum.ansible.com/c/chat/4): gather and interact with fellow enthusiasts.
  * [News & Announcements](https://forum.ansible.com/c/news/5): track project-wide announcements including social events. The [Bullhorn newsletter](https://docs.ansible.com/ansible/devel/community/communication.html#the-bullhorn), which is used to announce releases and important changes, can also be found here.

For more information about communication, see the [Ansible communication guide](https://docs.ansible.com/ansible/devel/community/communication.html).

## Contributing to this collection

The content of this collection is made by people like you, a community of individuals collaborating on making the world better through developing automation software.

We are actively accepting new contributors and all types of contributions are very welcome.

Don't know how to start? Refer to the [Ansible community guide](https://docs.ansible.com/ansible/devel/community/index.html)!

Want to submit code changes? Take a look at the [Quick-start development guide](https://docs.ansible.com/ansible/devel/community/create_pr_quick_start.html).

We also use the following guidelines:

* [Collection review checklist](https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_reviewing.html)
* [Ansible development guide](https://docs.ansible.com/ansible/devel/dev_guide/index.html)
* [Ansible collection development guide](https://docs.ansible.com/ansible/devel/dev_guide/developing_collections.html#contributing-to-collections)

## Collection maintenance

The current maintainers are listed in the [MAINTAINERS](MAINTAINERS) file. If you have questions or need help, feel free to mention them in the proposals.

To learn how to maintain/become a maintainer of this collection, refer to the [Maintainer guidelines](https://docs.ansible.com/ansible/devel/community/maintainers.html).

It is necessary for maintainers of this collection to be subscribed to:

* The collection itself (the `Watch` button -> `All Activity` in the upper right corner of the repository's homepage).
* The [news-for-maintainers repository](https://github.com/ansible-collections/news-for-maintainers).

They also should be subscribed to Ansible's [The Bullhorn newsletter](https://docs.ansible.com/ansible/devel/community/communication.html#the-bullhorn).

## Governance

The process of decision making in this collection is based on discussing and finding consensus among participants.

Every voice is important. If you have something on your mind, create an issue or dedicated discussion and let's discuss it!

## Tested with Ansible

This collection has been tested against following Ansible versions **>=2.16.0**.

### Supported connections

The LANCOM Systems SWOSLX collection supports `network_cli` connections.

## Included content

<!-- Galaxy now usually displays full module and plugin docs within the UI. If you don't use Galaxy for your collection, you may need to either describe your plugins etc here, or point to an external docsite to cover that information. -->

## Using this collection

You can call modules by their Fully Qualified Collection Namespace (FQCN), such as `lancom.swoslx.swoslx_l2_interfaces`.
The following example task replaces configuration changes in the existing configuration on a LANCOM Systems SWOSLX network device, using the FQCN:

```yaml
---
  - name: Replace device configuration of specified L2 interfaces with provided configuration.
    lancom.swoslx.swoslx_l2_interfaces:
      config:
        - name: Ethernet1
          trunk:
            native_vlan: 20
            trunk_vlans: 5-10, 15
      state: replaced
```

**NOTE**: For Ansible 2.9, you may not see deprecation warnings when you run your playbooks with this collection. Use this documentation to track when a module is deprecated.

### Installing the Collection from Ansible Galaxy

Before using this collection, you need to install it with the Ansible Galaxy command-line tool:
```bash
ansible-galaxy collection install lancom.swoslx
```

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:
```yaml
---
collections:
  - name: lancom.swoslx
```

Note that if you install the collection from Ansible Galaxy, it will not be upgraded automatically when you upgrade the `ansible` package. To upgrade the collection to the latest available version, run the following command:
```bash
ansible-galaxy collection install lancom.swoslx --upgrade
```

You can also install a specific version of the collection, for example, if you need to downgrade when something is broken in the latest version (please report an issue in this repository). Use the following syntax to install version `0.1.0`:

```bash
ansible-galaxy collection install lancom.swoslx:==0.1.0
```

See [using Ansible collections](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for more details.

## Release notes

See the [changelog](https://github.com/ButAry/ansible-lancom-swoslx/tree/main/CHANGELOG.rst).

## Disclaimer

See the [disclaimer](https://github.com/ButAry/ansible-lancom-swoslx/tree/main/DISCLAIMER.md).

## Roadmap

"It's usually my policy not to speculate on release dates, since that's what it is – pure speculation.
It's not always possible to know how long it will take to make the upgrades needed and tie up all the related loose ends.
As things are built for the upcoming release, they'll be uploaded into the -main tree."

## More information

- [Ansible user guide](https://docs.ansible.com/ansible/devel/user_guide/index.html)
- [Ansible developer guide](https://docs.ansible.com/ansible/devel/dev_guide/index.html)
- [Ansible collections requirements](https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_requirements.html)
- [Ansible community Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html)
- [The Bullhorn (the Ansible contributor newsletter)](https://docs.ansible.com/ansible/devel/community/communication.html#the-bullhorn)
- [Important announcements for maintainers](https://github.com/ansible-collections/news-for-maintainers)

## Licensing

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
