import pytest


@pytest.fixture
def system_output():
    return b"""
        Model Name                  : LANCOM GS-3510XP
        System Description          : Managed L2+ PoE+ Switch, 4x 10/100/1000Base-T ports + 4x 100M/1G/2,5G ports + 2x 1G/10G SFP+ slots
        Location                    : 
        Contact                     : 
        System Name                 : GS-3510XP
        System Date                 : 2022-01-01T01:42:36+01:00
        System Uptime               : 0d 00:43:51
        Bootloader Version          : V1.05
        Firmware Version            : 4.30.0147RU4
        Hardware Version            : B1
        Mechanical Version          : v1.01
        Production Date             : 2024-05-06
        Serial Number               : 4006396720100720
        MAC Address                 : 00-a0-57-96-48-87
        Total Memory                : 500MB
        Free Memory                 : 335MB
        Fan Speed                   : 0
        Temperature 1               : 58
        Temperature 2               : 43
        Power                       : 1V0:1.04V; 2V5:2.53V; 12V:11.90V; 0V95:0.98V; 3V3:3.23V
        """


@pytest.fixture
def version_output():
    return b"""
        
        MAC Address      : 00-a0-57-96-48-87
        Previous Restart : Cold
        
        System Contact   : 
        System Name      : GS-3510XP
        System Location  : 
        System Time      : 2022-01-01T01:43:14+01:00
        System Uptime    : 00:44:29
        
        
        Bootloader
        ----------
        Image            : RedBoot 
        Version          : version V1.05
        Date             : 18:27:14, Jul 16 2020
        
        Primary Image
        -------------
        Image            : linux (Active)
        Version          : 4.30.0147RU4
        Date             : 2025-01-20T09:46:05+01:00
        Upload filename  : LC-GS-3510XP-4.30.0147-RU4.upx  
        
        Backup Image
        ------------
        Image            : linux.bk 
        Version          : 4.30.0072RU1
        Date             : 2024-07-18T15:29:44+02:00
        Upload filename  : LC-GS-3510XP-4.30.0072-RU1.mfi
        
        ------------------
        SID : 1 
        ------------------
        Chipset ID       : VSC7440 Rev. B
        Board Type       : SparX-IV_34
        Flash Type       : NOR-only
        Port Count       : 10
        Product          : Microchip GS-3510XP Switch
        Software Version : 4.30.0147RU4
        Build Date       : 2025-01-20T09:46:05+01:00
        Code Revision    : 98e6cfb3e
        PoE Version      : HW Ver.:0, Prod:28, sw ver:224, param:19, build:2, internal sw ver:756, Asic Patch Num:20046
        
        """


@pytest.fixture
def running_config():
    return b"""
        Building configuration...
        hostname GS-3510XP
        prompt %h
        no logging on
        no logging host
        logging port 514
        logging protocol udp
        logging level informational
        no logging hostname
        enforce-password-rules
        no ip gratuitous-arp-learning
        username admin privilege 15 password encrypted $argon2id$v=19$m=9216,t=1,p=1$8F/KXwdnxqaiTnv9KdUi4A$tj+5IDWZwmRSuqNsRA0DRg
        system description Managed L2+ PoE+ Switch, 4x 10/100/1000Base-T ports + 4x 100M/1G/2,5G ports + 2x 1G/10G SFP+ slots
        system reboot mode disable
        no system reboot
        no access management
        no loop-protect
        loop-protect transmit-time 5
        loop-protect shutdown-time 180
        no ip dhcp server
        !                                                  
        vlan 1
        !
        !
        !
        no ipmc profile
        !
        no ip routing
        no ip name-server 0
        ip name-server 1 dhcp ipv4 interface vlan 1
        no ip name-server 2
        no ip name-server 3
        no ip domain name
        no ip dns proxy
        no mvr
        no ip igmp host-proxy leave-proxy
        no ip igmp host-proxy
        ip igmp unknown-flooding
        no ip igmp snooping
        ip igmp ssm-range 232.0.0.0 8
        no ipv6 mld host-proxy leave-proxy
        no ipv6 mld host-proxy
        ipv6 mld unknown-flooding
        no ipv6 mld snooping                               
        ipv6 mld ssm-range ff3e:: 96
        vlan ethertype s-custom-port 0x88a8
        no svl fid all
        no ip dhcp snooping
        no ipv6 dhcp snooping
        no ip dhcp relay
        no ip helper-address
        no ip dhcp relay information option
        ip dhcp relay information policy keep
        no ip arp inspection
        no ip verify source
        no ipv6 verify source
        no ntp
        no ntp server 1
        no ntp server 2
        no ntp server 3
        no ntp server 4
        no ntp server 5
        clock summer-time '' recurring last 7 3 02:00 last 7 10 03:00 60
        clock timezone '' 1
        ip http secure-server
        no ip http secure-redirect
        ip ssh                                             
        no monitor session 1 source interface GigabitEthernet 1/1-4 2.5GigabitEthernet 1/1-4 10GigabitEthernet 1/1-2
        no monitor session 1 source cpu
        no monitor session 1 destination interface GigabitEthernet 1/1-4 2.5GigabitEthernet 1/1-4 10GigabitEthernet 1/1-2
        no monitor session 1
        no monitor session 2 source interface GigabitEthernet 1/1-4 2.5GigabitEthernet 1/1-4 10GigabitEthernet 1/1-2
        no monitor session 2 source cpu
        no monitor session 2 destination interface GigabitEthernet 1/1-4 2.5GigabitEthernet 1/1-4 10GigabitEthernet 1/1-2
        no monitor session 2
        no monitor session 3 source interface GigabitEthernet 1/1-4 2.5GigabitEthernet 1/1-4 10GigabitEthernet 1/1-2
        no monitor session 3 source cpu
        no monitor session 3 destination interface GigabitEthernet 1/1-4 2.5GigabitEthernet 1/1-4 10GigabitEthernet 1/1-2
        no monitor session 3
        no monitor session 4 source interface GigabitEthernet 1/1-4 2.5GigabitEthernet 1/1-4 10GigabitEthernet 1/1-2
        no monitor session 4 source cpu
        no monitor session 4 destination interface GigabitEthernet 1/1-4 2.5GigabitEthernet 1/1-4 10GigabitEthernet 1/1-2
        no monitor session 4
        no monitor session 5 source interface GigabitEthernet 1/1-4 2.5GigabitEthernet 1/1-4 10GigabitEthernet 1/1-2
        no monitor session 5 source cpu
        no monitor session 5 destination interface GigabitEthernet 1/1-4 2.5GigabitEthernet 1/1-4 10GigabitEthernet 1/1-2
        no monitor session 5
        mac address-table aging-time 300
        mac address-table learning vlan 1-4094
        aggregation mode smac ip port
        lacp system-priority 32768
        spanning-tree mode mstp
        spanning-tree mst hello-time 2
        spanning-tree mst max-age 20 forward-time 15
        spanning-tree transmit hold-count 6
        spanning-tree mst max-hops 20
        no spanning-tree edge bpdu-filter
        no spanning-tree edge bpdu-guard
        no spanning-tree recovery interval
        spanning-tree mst 0 priority 32768
        spanning-tree mst 1 priority 32768
        spanning-tree mst 2 priority 32768                 
        spanning-tree mst 3 priority 32768
        spanning-tree mst 4 priority 32768
        spanning-tree mst 5 priority 32768
        spanning-tree mst 6 priority 32768
        spanning-tree mst 7 priority 32768
        spanning-tree mst name 00-a0-57-96-48-87 revision 0
        no spanning-tree mst 1 vlan
        no spanning-tree mst 2 vlan
        no spanning-tree mst 3 vlan
        no spanning-tree mst 4 vlan
        no spanning-tree mst 5 vlan
        no spanning-tree mst 6 vlan
        no spanning-tree mst 7 vlan
        no spanning-tree mst te vlan
        green-ethernet fan temp-on 75 temp-max 100
        green-ethernet fan power-on 0 power-max 30000
        lldp holdtime 4
        lldp transmission-delay 2
        lldp timer 30
        lldp reinit 2
        lldp med location-tlv altitude meters 0.0
        lldp med location-tlv latitude north 0.0000
        lldp med location-tlv longitude east 0.0000        
        no lldp med datum wgs84
        lldp med fast 4
        no lldp med location-tlv civic-addr country 
        no lldp med location-tlv civic-addr state 
        no lldp med location-tlv civic-addr county 
        no lldp med location-tlv civic-addr city 
        no lldp med location-tlv civic-addr district 
        no lldp med location-tlv civic-addr block 
        no lldp med location-tlv civic-addr street 
        no lldp med location-tlv civic-addr leading-street-direction 
        no lldp med location-tlv civic-addr trailing-street-suffix 
        no lldp med location-tlv civic-addr street-suffix 
        no lldp med location-tlv civic-addr house-no 
        no lldp med location-tlv civic-addr house-no-suffix 
        no lldp med location-tlv civic-addr landmark 
        no lldp med location-tlv civic-addr additional-info 
        no lldp med location-tlv civic-addr name 
        no lldp med location-tlv civic-addr zip-code 
        no lldp med location-tlv civic-addr building 
        no lldp med location-tlv civic-addr apartment 
        no lldp med location-tlv civic-addr floor 
        no lldp med location-tlv civic-addr room-number 
        no lldp med location-tlv civic-addr place-type     
        no lldp med location-tlv civic-addr postal-community-name 
        no lldp med location-tlv civic-addr p-o-box 
        no lldp med location-tlv civic-addr additional-code 
        no lldp med location-tlv elin-addr 
        no poe management mode
        poe legacy-pd-detection
        poe profile id 1 name Profile 1
        poe profile id 1 Mon 0 0 0 0 Tue 0 0 0 0 Wed 0 0 0 0 Thu 0 0 0 0 Fri 0 0 0 0 Sat 0 0 0 0 Sun 0 0 0 0 
        poe profile id 2 name Profile 2
        poe profile id 2 Mon 0 0 0 0 Tue 0 0 0 0 Wed 0 0 0 0 Thu 0 0 0 0 Fri 0 0 0 0 Sat 0 0 0 0 Sun 0 0 0 0 
        poe profile id 3 name Profile 3
        poe profile id 3 Mon 0 0 0 0 Tue 0 0 0 0 Wed 0 0 0 0 Thu 0 0 0 0 Fri 0 0 0 0 Sat 0 0 0 0 Sun 0 0 0 0 
        poe profile id 4 name Profile 4
        poe profile id 4 Mon 0 0 0 0 Tue 0 0 0 0 Wed 0 0 0 0 Thu 0 0 0 0 Fri 0 0 0 0 Sat 0 0 0 0 Sun 0 0 0 0 
        poe profile id 5 name Profile 5
        poe profile id 5 Mon 0 0 0 0 Tue 0 0 0 0 Wed 0 0 0 0 Thu 0 0 0 0 Fri 0 0 0 0 Sat 0 0 0 0 Sun 0 0 0 0 
        poe profile id 6 name Profile 6
        poe profile id 6 Mon 0 0 0 0 Tue 0 0 0 0 Wed 0 0 0 0 Thu 0 0 0 0 Fri 0 0 0 0 Sat 0 0 0 0 Sun 0 0 0 0 
        poe profile id 7 name Profile 7
        poe profile id 7 Mon 0 0 0 0 Tue 0 0 0 0 Wed 0 0 0 0 Thu 0 0 0 0 Fri 0 0 0 0 Sat 0 0 0 0 Sun 0 0 0 0 
        poe profile id 8 name Profile 8
        poe profile id 8 Mon 0 0 0 0 Tue 0 0 0 0 Wed 0 0 0 0 Thu 0 0 0 0 Fri 0 0 0 0 Sat 0 0 0 0 Sun 0 0 0 0 
        poe profile id 9 name Profile 9
        poe profile id 9 Mon 0 0 0 0 Tue 0 0 0 0 Wed 0 0 0 0 Thu 0 0 0 0 Fri 0 0 0 0 Sat 0 0 0 0 Sun 0 0 0 0 
        poe profile id 10 name Profile 10
        poe profile id 10 Mon 0 0 0 0 Tue 0 0 0 0 Wed 0 0 0 0 Thu 0 0 0 0 Fri 0 0 0 0 Sat 0 0 0 0 Sun 0 0 0 0 
        poe profile id 11 name Profile 11
        poe profile id 11 Mon 0 0 0 0 Tue 0 0 0 0 Wed 0 0 0 0 Thu 0 0 0 0 Fri 0 0 0 0 Sat 0 0 0 0 Sun 0 0 0 0 
        poe profile id 12 name Profile 12
        poe profile id 12 Mon 0 0 0 0 Tue 0 0 0 0 Wed 0 0 0 0 Thu 0 0 0 0 Fri 0 0 0 0 Sat 0 0 0 0 Sun 0 0 0 0 
        poe profile id 13 name Profile 13
        poe profile id 13 Mon 0 0 0 0 Tue 0 0 0 0 Wed 0 0 0 0 Thu 0 0 0 0 Fri 0 0 0 0 Sat 0 0 0 0 Sun 0 0 0 0 
        poe profile id 14 name Profile 14                  
        poe profile id 14 Mon 0 0 0 0 Tue 0 0 0 0 Wed 0 0 0 0 Thu 0 0 0 0 Fri 0 0 0 0 Sat 0 0 0 0 Sun 0 0 0 0 
        poe profile id 15 name Profile 15
        poe profile id 15 Mon 0 0 0 0 Tue 0 0 0 0 Wed 0 0 0 0 Thu 0 0 0 0 Fri 0 0 0 0 Sat 0 0 0 0 Sun 0 0 0 0 
        poe profile id 16 name Profile 16
        poe profile id 16 Mon 0 0 0 0 Tue 0 0 0 0 Wed 0 0 0 0 Thu 0 0 0 0 Fri 0 0 0 0 Sat 0 0 0 0 Sun 0 0 0 0 
        no poe ping-check
        thermal-protect grp 0 temperature 255
        thermal-protect grp 1 temperature 255
        thermal-protect grp 2 temperature 255
        thermal-protect grp 3 temperature 255
        no snmp-server
        snmp-server engine-id local 80000934800500a057964887
        no snmp-server contact
        no snmp-server location
        snmp-server security-to-group model v1 name public group default_ro_group
        snmp-server security-to-group model v1 name private group default_rw_group
        snmp-server security-to-group model v2c name public group default_ro_group
        snmp-server security-to-group model v2c name private group default_rw_group
        snmp-server view default_view .1 include
        snmp-server access default_ro_group model any level noauth read default_view 
        snmp-server access default_rw_group model any level noauth read default_view write default_view
        !
        trap mac-change format lancom
        trap mac-change interval 1
        trap mac-change aging
        trap mac-change aging time 300
        aaa authentication login console local
        ip telnet port 23
        no aaa authentication login telnet
        ip ssh port 22
        aaa authentication login ssh local
        ip http port 80
        aaa authentication login http local
        ip http secure-server port 443
        aaa authentication login https local
        no aaa authorization console
        no aaa authorization telnet
        no aaa authorization ssh
        no aaa accounting console
        no aaa accounting telnet
        no aaa accounting ssh
        no radius-server timeout                           
        no radius-server retransmit
        no radius-server deadtime
        no radius-server key
        no radius-server attribute 4
        no radius-server attribute 95
        no radius-server attribute 32
        no radius-server message-authenticator enforce
        no radius-server dynamic-authorization mode
        radius-server dynamic-authorization port 3799
        radius-server dynamic-authorization duplicate-window 300
        no radius-server dynamic-authorization message-authenticator enforce
        no radius-server dynamic-authorization event-timestamp enforce
        radius-server mac-format called-station groupsize 2 separator hyphen lowercase
        radius-server mac-format calling-station groupsize 2 separator hyphen lowercase
        radius-server mac-format macbased-identity groupsize 2 separator hyphen lowercase
        no tacacs-server timeout
        no tacacs-server deadtime
        no tacacs-server key
        no upnp
        upnp advertising-duration 100
        upnp ip-addressing-mode dynamic
        upnp static interface vlan 1                       
        no qos storm unicast
        no qos storm multicast
        no qos storm broadcast
        no qos wred group 1 queue 0 dpl 1 
        no qos wred group 1 queue 0 dpl 2 
        no qos wred group 1 queue 0 dpl 3 
        no qos wred group 1 queue 1 dpl 1 
        no qos wred group 1 queue 1 dpl 2 
        no qos wred group 1 queue 1 dpl 3 
        no qos wred group 1 queue 2 dpl 1 
        no qos wred group 1 queue 2 dpl 2 
        no qos wred group 1 queue 2 dpl 3 
        no qos wred group 1 queue 3 dpl 1 
        no qos wred group 1 queue 3 dpl 2 
        no qos wred group 1 queue 3 dpl 3 
        no qos wred group 1 queue 4 dpl 1 
        no qos wred group 1 queue 4 dpl 2 
        no qos wred group 1 queue 4 dpl 3 
        no qos wred group 1 queue 5 dpl 1 
        no qos wred group 1 queue 5 dpl 2 
        no qos wred group 1 queue 5 dpl 3 
        no qos wred group 1 queue 6 dpl 1 
        no qos wred group 1 queue 6 dpl 2                  
        no qos wred group 1 queue 6 dpl 3 
        no qos wred group 1 queue 7 dpl 1 
        no qos wred group 1 queue 7 dpl 2 
        no qos wred group 1 queue 7 dpl 3 
        no qos wred group 2 queue 0 dpl 1 
        no qos wred group 2 queue 0 dpl 2 
        no qos wred group 2 queue 0 dpl 3 
        no qos wred group 2 queue 1 dpl 1 
        no qos wred group 2 queue 1 dpl 2 
        no qos wred group 2 queue 1 dpl 3 
        no qos wred group 2 queue 2 dpl 1 
        no qos wred group 2 queue 2 dpl 2 
        no qos wred group 2 queue 2 dpl 3 
        no qos wred group 2 queue 3 dpl 1 
        no qos wred group 2 queue 3 dpl 2 
        no qos wred group 2 queue 3 dpl 3 
        no qos wred group 2 queue 4 dpl 1 
        no qos wred group 2 queue 4 dpl 2 
        no qos wred group 2 queue 4 dpl 3 
        no qos wred group 2 queue 5 dpl 1 
        no qos wred group 2 queue 5 dpl 2 
        no qos wred group 2 queue 5 dpl 3 
        no qos wred group 2 queue 6 dpl 1                  
        no qos wred group 2 queue 6 dpl 2 
        no qos wred group 2 queue 6 dpl 3 
        no qos wred group 2 queue 7 dpl 1 
        no qos wred group 2 queue 7 dpl 2 
        no qos wred group 2 queue 7 dpl 3 
        no qos wred group 3 queue 0 dpl 1 
        no qos wred group 3 queue 0 dpl 2 
        no qos wred group 3 queue 0 dpl 3 
        no qos wred group 3 queue 1 dpl 1 
        no qos wred group 3 queue 1 dpl 2 
        no qos wred group 3 queue 1 dpl 3 
        no qos wred group 3 queue 2 dpl 1 
        no qos wred group 3 queue 2 dpl 2 
        no qos wred group 3 queue 2 dpl 3 
        no qos wred group 3 queue 3 dpl 1 
        no qos wred group 3 queue 3 dpl 2 
        no qos wred group 3 queue 3 dpl 3 
        no qos wred group 3 queue 4 dpl 1 
        no qos wred group 3 queue 4 dpl 2 
        no qos wred group 3 queue 4 dpl 3 
        no qos wred group 3 queue 5 dpl 1 
        no qos wred group 3 queue 5 dpl 2 
        no qos wred group 3 queue 5 dpl 3                  
        no qos wred group 3 queue 6 dpl 1 
        no qos wred group 3 queue 6 dpl 2 
        no qos wred group 3 queue 6 dpl 3 
        no qos wred group 3 queue 7 dpl 1 
        no qos wred group 3 queue 7 dpl 2 
        no qos wred group 3 queue 7 dpl 3 
        no qos map dscp-cos 0
        no qos map dscp-cos 1
        no qos map dscp-cos 2
        no qos map dscp-cos 3
        no qos map dscp-cos 4
        no qos map dscp-cos 5
        no qos map dscp-cos 6
        no qos map dscp-cos 7
        no qos map dscp-cos 8
        no qos map dscp-cos 9
        no qos map dscp-cos 10
        no qos map dscp-cos 11
        no qos map dscp-cos 12
        no qos map dscp-cos 13
        no qos map dscp-cos 14
        no qos map dscp-cos 15
        no qos map dscp-cos 16                             
        no qos map dscp-cos 17
        no qos map dscp-cos 18
        no qos map dscp-cos 19
        no qos map dscp-cos 20
        no qos map dscp-cos 21
        no qos map dscp-cos 22
        no qos map dscp-cos 23
        no qos map dscp-cos 24
        no qos map dscp-cos 25
        no qos map dscp-cos 26
        no qos map dscp-cos 27
        no qos map dscp-cos 28
        no qos map dscp-cos 29
        no qos map dscp-cos 30
        no qos map dscp-cos 31
        no qos map dscp-cos 32
        no qos map dscp-cos 33
        no qos map dscp-cos 34
        no qos map dscp-cos 35
        no qos map dscp-cos 36
        no qos map dscp-cos 37
        no qos map dscp-cos 38
        no qos map dscp-cos 39                             
        no qos map dscp-cos 40
        no qos map dscp-cos 41
        no qos map dscp-cos 42
        no qos map dscp-cos 43
        no qos map dscp-cos 44
        no qos map dscp-cos 45
        no qos map dscp-cos 46
        no qos map dscp-cos 47
        no qos map dscp-cos 48
        no qos map dscp-cos 49
        no qos map dscp-cos 50
        no qos map dscp-cos 51
        no qos map dscp-cos 52
        no qos map dscp-cos 53
        no qos map dscp-cos 54
        no qos map dscp-cos 55
        no qos map dscp-cos 56
        no qos map dscp-cos 57
        no qos map dscp-cos 58
        no qos map dscp-cos 59
        no qos map dscp-cos 60
        no qos map dscp-cos 61
        no qos map dscp-cos 62                             
        no qos map dscp-cos 63
        qos map dscp-ingress-translation 0 to 0
        qos map dscp-ingress-translation 1 to 1
        qos map dscp-ingress-translation 2 to 2
        qos map dscp-ingress-translation 3 to 3
        qos map dscp-ingress-translation 4 to 4
        qos map dscp-ingress-translation 5 to 5
        qos map dscp-ingress-translation 6 to 6
        qos map dscp-ingress-translation 7 to 7
        qos map dscp-ingress-translation 8 to 8
        qos map dscp-ingress-translation 9 to 9
        qos map dscp-ingress-translation 10 to 10
        qos map dscp-ingress-translation 11 to 11
        qos map dscp-ingress-translation 12 to 12
        qos map dscp-ingress-translation 13 to 13
        qos map dscp-ingress-translation 14 to 14
        qos map dscp-ingress-translation 15 to 15
        qos map dscp-ingress-translation 16 to 16
        qos map dscp-ingress-translation 17 to 17
        qos map dscp-ingress-translation 18 to 18
        qos map dscp-ingress-translation 19 to 19
        qos map dscp-ingress-translation 20 to 20
        qos map dscp-ingress-translation 21 to 21          
        qos map dscp-ingress-translation 22 to 22
        qos map dscp-ingress-translation 23 to 23
        qos map dscp-ingress-translation 24 to 24
        qos map dscp-ingress-translation 25 to 25
        qos map dscp-ingress-translation 26 to 26
        qos map dscp-ingress-translation 27 to 27
        qos map dscp-ingress-translation 28 to 28
        qos map dscp-ingress-translation 29 to 29
        qos map dscp-ingress-translation 30 to 30
        qos map dscp-ingress-translation 31 to 31
        qos map dscp-ingress-translation 32 to 32
        qos map dscp-ingress-translation 33 to 33
        qos map dscp-ingress-translation 34 to 34
        qos map dscp-ingress-translation 35 to 35
        qos map dscp-ingress-translation 36 to 36
        qos map dscp-ingress-translation 37 to 37
        qos map dscp-ingress-translation 38 to 38
        qos map dscp-ingress-translation 39 to 39
        qos map dscp-ingress-translation 40 to 40
        qos map dscp-ingress-translation 41 to 41
        qos map dscp-ingress-translation 42 to 42
        qos map dscp-ingress-translation 43 to 43
        qos map dscp-ingress-translation 44 to 44          
        qos map dscp-ingress-translation 45 to 45
        qos map dscp-ingress-translation 46 to 46
        qos map dscp-ingress-translation 47 to 47
        qos map dscp-ingress-translation 48 to 48
        qos map dscp-ingress-translation 49 to 49
        qos map dscp-ingress-translation 50 to 50
        qos map dscp-ingress-translation 51 to 51
        qos map dscp-ingress-translation 52 to 52
        qos map dscp-ingress-translation 53 to 53
        qos map dscp-ingress-translation 54 to 54
        qos map dscp-ingress-translation 55 to 55
        qos map dscp-ingress-translation 56 to 56
        qos map dscp-ingress-translation 57 to 57
        qos map dscp-ingress-translation 58 to 58
        qos map dscp-ingress-translation 59 to 59
        qos map dscp-ingress-translation 60 to 60
        qos map dscp-ingress-translation 61 to 61
        qos map dscp-ingress-translation 62 to 62
        qos map dscp-ingress-translation 63 to 63
        no qos map dscp-classify 0
        no qos map dscp-classify 1
        no qos map dscp-classify 2
        no qos map dscp-classify 3                         
        no qos map dscp-classify 4
        no qos map dscp-classify 5
        no qos map dscp-classify 6
        no qos map dscp-classify 7
        no qos map dscp-classify 8
        no qos map dscp-classify 9
        no qos map dscp-classify 10
        no qos map dscp-classify 11
        no qos map dscp-classify 12
        no qos map dscp-classify 13
        no qos map dscp-classify 14
        no qos map dscp-classify 15
        no qos map dscp-classify 16
        no qos map dscp-classify 17
        no qos map dscp-classify 18
        no qos map dscp-classify 19
        no qos map dscp-classify 20
        no qos map dscp-classify 21
        no qos map dscp-classify 22
        no qos map dscp-classify 23
        no qos map dscp-classify 24
        no qos map dscp-classify 25
        no qos map dscp-classify 26                        
        no qos map dscp-classify 27
        no qos map dscp-classify 28
        no qos map dscp-classify 29
        no qos map dscp-classify 30
        no qos map dscp-classify 31
        no qos map dscp-classify 32
        no qos map dscp-classify 33
        no qos map dscp-classify 34
        no qos map dscp-classify 35
        no qos map dscp-classify 36
        no qos map dscp-classify 37
        no qos map dscp-classify 38
        no qos map dscp-classify 39
        no qos map dscp-classify 40
        no qos map dscp-classify 41
        no qos map dscp-classify 42
        no qos map dscp-classify 43
        no qos map dscp-classify 44
        no qos map dscp-classify 45
        no qos map dscp-classify 46
        no qos map dscp-classify 47
        no qos map dscp-classify 48
        no qos map dscp-classify 49                        
        no qos map dscp-classify 50
        no qos map dscp-classify 51
        no qos map dscp-classify 52
        no qos map dscp-classify 53
        no qos map dscp-classify 54
        no qos map dscp-classify 55
        no qos map dscp-classify 56
        no qos map dscp-classify 57
        no qos map dscp-classify 58
        no qos map dscp-classify 59
        no qos map dscp-classify 60
        no qos map dscp-classify 61
        no qos map dscp-classify 62
        no qos map dscp-classify 63
        no qos map cos-dscp 0 dpl 0
        no qos map cos-dscp 0 dpl 1
        no qos map cos-dscp 0 dpl 2
        no qos map cos-dscp 0 dpl 3
        no qos map cos-dscp 1 dpl 0
        no qos map cos-dscp 1 dpl 1
        no qos map cos-dscp 1 dpl 2
        no qos map cos-dscp 1 dpl 3
        no qos map cos-dscp 2 dpl 0                        
        no qos map cos-dscp 2 dpl 1
        no qos map cos-dscp 2 dpl 2
        no qos map cos-dscp 2 dpl 3
        no qos map cos-dscp 3 dpl 0
        no qos map cos-dscp 3 dpl 1
        no qos map cos-dscp 3 dpl 2
        no qos map cos-dscp 3 dpl 3
        no qos map cos-dscp 4 dpl 0
        no qos map cos-dscp 4 dpl 1
        no qos map cos-dscp 4 dpl 2
        no qos map cos-dscp 4 dpl 3
        no qos map cos-dscp 5 dpl 0
        no qos map cos-dscp 5 dpl 1
        no qos map cos-dscp 5 dpl 2
        no qos map cos-dscp 5 dpl 3
        no qos map cos-dscp 6 dpl 0
        no qos map cos-dscp 6 dpl 1
        no qos map cos-dscp 6 dpl 2
        no qos map cos-dscp 6 dpl 3
        no qos map cos-dscp 7 dpl 0
        no qos map cos-dscp 7 dpl 1
        no qos map cos-dscp 7 dpl 2
        no qos map cos-dscp 7 dpl 3                        
        qos map dscp-egress-translation 0 to 0
        qos map dscp-egress-translation 1 to 1
        qos map dscp-egress-translation 2 to 2
        qos map dscp-egress-translation 3 to 3
        qos map dscp-egress-translation 4 to 4
        qos map dscp-egress-translation 5 to 5
        qos map dscp-egress-translation 6 to 6
        qos map dscp-egress-translation 7 to 7
        qos map dscp-egress-translation 8 to 8
        qos map dscp-egress-translation 9 to 9
        qos map dscp-egress-translation 10 to 10
        qos map dscp-egress-translation 11 to 11
        qos map dscp-egress-translation 12 to 12
        qos map dscp-egress-translation 13 to 13
        qos map dscp-egress-translation 14 to 14
        qos map dscp-egress-translation 15 to 15
        qos map dscp-egress-translation 16 to 16
        qos map dscp-egress-translation 17 to 17
        qos map dscp-egress-translation 18 to 18
        qos map dscp-egress-translation 19 to 19
        qos map dscp-egress-translation 20 to 20
        qos map dscp-egress-translation 21 to 21
        qos map dscp-egress-translation 22 to 22           
        qos map dscp-egress-translation 23 to 23
        qos map dscp-egress-translation 24 to 24
        qos map dscp-egress-translation 25 to 25
        qos map dscp-egress-translation 26 to 26
        qos map dscp-egress-translation 27 to 27
        qos map dscp-egress-translation 28 to 28
        qos map dscp-egress-translation 29 to 29
        qos map dscp-egress-translation 30 to 30
        qos map dscp-egress-translation 31 to 31
        qos map dscp-egress-translation 32 to 32
        qos map dscp-egress-translation 33 to 33
        qos map dscp-egress-translation 34 to 34
        qos map dscp-egress-translation 35 to 35
        qos map dscp-egress-translation 36 to 36
        qos map dscp-egress-translation 37 to 37
        qos map dscp-egress-translation 38 to 38
        qos map dscp-egress-translation 39 to 39
        qos map dscp-egress-translation 40 to 40
        qos map dscp-egress-translation 41 to 41
        qos map dscp-egress-translation 42 to 42
        qos map dscp-egress-translation 43 to 43
        qos map dscp-egress-translation 44 to 44
        qos map dscp-egress-translation 45 to 45           
        qos map dscp-egress-translation 46 to 46
        qos map dscp-egress-translation 47 to 47
        qos map dscp-egress-translation 48 to 48
        qos map dscp-egress-translation 49 to 49
        qos map dscp-egress-translation 50 to 50
        qos map dscp-egress-translation 51 to 51
        qos map dscp-egress-translation 52 to 52
        qos map dscp-egress-translation 53 to 53
        qos map dscp-egress-translation 54 to 54
        qos map dscp-egress-translation 55 to 55
        qos map dscp-egress-translation 56 to 56
        qos map dscp-egress-translation 57 to 57
        qos map dscp-egress-translation 58 to 58
        qos map dscp-egress-translation 59 to 59
        qos map dscp-egress-translation 60 to 60
        qos map dscp-egress-translation 61 to 61
        qos map dscp-egress-translation 62 to 62
        qos map dscp-egress-translation 63 to 63
        !
        access-list rate-limiter 10pps 1
        no voice vlan
        voice vlan vid 1000
        voice vlan aging-time 86400                        
        voice vlan class 7
        voice vlan oui 00-01-E3 description Siemens AG phones
        voice vlan oui 00-03-6B description Cisco phones
        voice vlan oui 00-0F-E2 description H3C phones
        voice vlan oui 00-60-B9 description Philips and NEC AG phones
        voice vlan oui 00-90-33 description Innovaphone
        voice vlan oui 00-D0-1E description Pingtel phones
        voice vlan oui 00-E0-75 description Polycom phones
        voice vlan oui 00-E0-BB description 3Com phones
        dot1x authentication timer re-authenticate 3600
        dot1x timeout tx-period 30
        dot1x authentication timer inactivity 300
        no dot1x re-authentication
        dot1x macbased-eap
        no dot1x macbased-credentials identity password
        no dot1x system-auth-control
        dot1x timeout quiet-period 10
        dot1x guest-vlan 1
        dot1x max-reauth-req 2
        no dot1x guest-vlan supplicant
        no dot1x feature guest-vlan
        no dot1x feature radius-vlan
        no dot1x feature radius-qos                        
        port-security aging time 3600
        no port-security aging
        port-security hold time 300
        web privilege group Aggregation level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group Alarm level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group DDMI level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group Debug level configRoPriv 15 configRwPriv 15 statusRoPriv 15 statusRwPriv 15
        web privilege group DHCP level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group DHCPv6_Client level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group Diagnostics level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group Firmware level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group Green_Ethernet level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group IP level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group IPMC_Snooping level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group LACP level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group LLDP level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group Loop_Protect level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group MAC_Table level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group Miscellaneous level configRoPriv 15 configRwPriv 15 statusRoPriv 15 statusRwPriv 15
        web privilege group MRP level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group MVR level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group NTP level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group POE level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group Ports level configRoPriv 5 configRwPriv 10 statusRoPriv 1 statusRwPriv 10
        web privilege group Private_VLANs level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group QoS level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group RMirror level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group Security(access) level configRoPriv 10 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group Security(network) level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group sFlow level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group Spanning_Tree level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group System level configRoPriv 5 configRwPriv 10 statusRoPriv 1 statusRwPriv 10
        web privilege group UDLD level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group uFDMA_AIL level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group uFDMA_CIL level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group UPnP level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group VCL level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group VLAN_Translation level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group VLANs level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group Voice_VLAN level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        web privilege group XXRP level configRoPriv 5 configRwPriv 10 statusRoPriv 5 statusRwPriv 10
        gvrp max-vlans 20
        no gvrp
        gvrp time join-time 20 leave-time 60 leave-all-time 1000
        mvrp managed vlan 1-4094
        no mvrp
        no ddmi
        no green-ethernet eee optimize-for-power
        !
        interface GigabitEthernet 1/1
         switchport voice vlan mode disable                
         no switchport voice vlan security
         switchport voice vlan discovery-protocol oui
         loop-protect
         no loop-protect action
         loop-protect tx-mode
         no loop-protect act-port
         switchport access vlan 1
         switchport trunk native vlan 1
         switchport hybrid native vlan 1
         switchport trunk allowed vlan 1-4094
         switchport hybrid allowed vlan 1-4094
         no switchport trunk vlan tag native
         switchport hybrid acceptable-frame-type all
         no switchport hybrid ingress-filtering
         switchport hybrid egress-tag all except-native
         switchport hybrid port-type c-port
         switchport mode access
         switchport forbidden vlan remove 1-4094
         vcl smacsip
         no pvlan isolation
         pvlan 1
         no mvr immediate-leave
         no ip igmp snooping filter                        
         no ip igmp snooping max-groups
         no ip igmp snooping mrouter
         no ip igmp snooping immediate-leave
         no ipv6 mld snooping filter
         no ipv6 mld snooping max-groups
         no ipv6 mld snooping mrouter
         no ipv6 mld snooping immediate-leave
         ip dhcp snooping trust
         no ipv6 dhcp snooping trust
         ip arp inspection trust
         no ip arp inspection check-vlan
         no ip arp inspection logging
         no ip verify source
         no ip verify source limit
         no ipv6 verify source
         no ipv6 verify source limit
         lldp receive
         lldp transmit
         lldp tlv-select management-address
         lldp tlv-select port-description
         lldp tlv-select system-capabilities
         lldp tlv-select system-name
         lldp tlv-select system-description                
         no lldp cdp-aware
         no lldp trap
         lldp med transmit-tlv capabilities network-policy location poe
         no lldp med media-vlan policy-list
         lldp med type connectivity
         poe mode enable
         poe priority low
         poe lldp
         no poe ping-ip-addr
         no poe startup-time
         no poe interval-time
         no poe ping-retry-time
         no poe failure-action
         no poe reboot-time
         no poe max-reboot-time
         no poe delay-mode
         no poe delay-time
         no poe port-profile
         qos cos 0
         qos pcp 0
         qos dpl 0
         qos dei 0
         qos class 0                                       
         no qos trust tag
         qos map tag-cos pcp 0 dei 0 cos 1 dpl 0
         qos map tag-cos pcp 0 dei 1 cos 1 dpl 1
         qos map tag-cos pcp 1 dei 0 cos 0 dpl 0
         qos map tag-cos pcp 1 dei 1 cos 0 dpl 1
         qos map tag-cos pcp 2 dei 0 cos 2 dpl 0
         qos map tag-cos pcp 2 dei 1 cos 2 dpl 1
         qos map tag-cos pcp 3 dei 0 cos 3 dpl 0
         qos map tag-cos pcp 3 dei 1 cos 3 dpl 1
         qos map tag-cos pcp 4 dei 0 cos 4 dpl 0
         qos map tag-cos pcp 4 dei 1 cos 4 dpl 1
         qos map tag-cos pcp 5 dei 0 cos 5 dpl 0
         qos map tag-cos pcp 5 dei 1 cos 5 dpl 1
         qos map tag-cos pcp 6 dei 0 cos 6 dpl 0
         qos map tag-cos pcp 6 dei 1 cos 6 dpl 1
         qos map tag-cos pcp 7 dei 0 cos 7 dpl 0
         qos map tag-cos pcp 7 dei 1 cos 7 dpl 1
         no qos trust dscp
         no qos policer
         no qos queue-policer queue 0
         no qos queue-policer queue 1
         no qos queue-policer queue 2
         no qos queue-policer queue 3                      
         no qos queue-policer queue 4
         no qos queue-policer queue 5
         no qos queue-policer queue 6
         no qos queue-policer queue 7
         no qos shaper
         no qos queue-shaper queue 0
         no qos queue-shaper queue 1
         no qos queue-shaper queue 2
         no qos queue-shaper queue 3
         no qos queue-shaper queue 4
         no qos queue-shaper queue 5
         no qos queue-shaper queue 6
         no qos queue-shaper queue 7
         no qos wrr
         no qos tag-remark
         qos map cos-tag cos 0 dpl 0 pcp 1 dei 0
         qos map cos-tag cos 0 dpl 1 pcp 1 dei 1
         qos map cos-tag cos 1 dpl 0 pcp 0 dei 0
         qos map cos-tag cos 1 dpl 1 pcp 0 dei 1
         qos map cos-tag cos 2 dpl 0 pcp 2 dei 0
         qos map cos-tag cos 2 dpl 1 pcp 2 dei 1
         qos map cos-tag cos 3 dpl 0 pcp 3 dei 0
         qos map cos-tag cos 3 dpl 1 pcp 3 dei 1           
         qos map cos-tag cos 4 dpl 0 pcp 4 dei 0
         qos map cos-tag cos 4 dpl 1 pcp 4 dei 1
         qos map cos-tag cos 5 dpl 0 pcp 5 dei 0
         qos map cos-tag cos 5 dpl 1 pcp 5 dei 1
         qos map cos-tag cos 6 dpl 0 pcp 6 dei 0
         qos map cos-tag cos 6 dpl 1 pcp 6 dei 1
         qos map cos-tag cos 7 dpl 0 pcp 7 dei 0
         qos map cos-tag cos 7 dpl 1 pcp 7 dei 1
         no qos dscp-translate
         no qos dscp-classify
         no qos dscp-remark
         qos wred-group 1
         no qos ingress-map
         no qos egress-map
         access-list action permit
         no access-list rate-limiter 
         access-list policy 0
         no access-list redirect
         no access-list mirror
         no access-list logging
         no access-list shutdown
         no thermal-protect grp
         mac address-table learning                        
         spanning-tree
         no spanning-tree edge
         spanning-tree auto-edge
         spanning-tree link-type auto
         no spanning-tree restricted-role
         no spanning-tree restricted-tcn
         no spanning-tree bpdu-guard
         spanning-tree mst 0 cost auto
         spanning-tree mst 0 port-priority 128
         spanning-tree mst 1 cost auto
         spanning-tree mst 1 port-priority 128
         spanning-tree mst 2 cost auto
         spanning-tree mst 2 port-priority 128
         spanning-tree mst 3 cost auto
         spanning-tree mst 3 port-priority 128
         spanning-tree mst 4 cost auto
         spanning-tree mst 4 port-priority 128
         spanning-tree mst 5 cost auto
         spanning-tree mst 5 port-priority 128
         spanning-tree mst 6 cost auto
         spanning-tree mst 6 port-priority 128
         spanning-tree mst 7 cost auto
         spanning-tree mst 7 port-priority 128             
         lacp port-priority 32768
         lacp timeout fast
         media-type rj45
         speed auto 10 100 1000
         duplex full
         flowcontrol off
         no priority-flowcontrol prio 0-7
         mtu 10240
         no excessive-restart
         no frame-length-check
         no shutdown
         no description
         no green-ethernet eee
         no green-ethernet eee urgent-queue 
         no green-ethernet energy-detect
         no green-ethernet short-reach
         dot1x port-control force-authorized
         no dot1x guest-vlan
         no dot1x radius-vlan
         no dot1x radius-qos
         no dot1x mac-based-fallback
         port-security maximum 4
         port-security maximum-violation 4                 
         port-security violation protect
         no port-security
         no port-security mac-address sticky
         switchport vlan mapping 1
         no aggregation group
         no gvrp
         mrp timers join-time 20 leave-time 60 leave-all-time 1000
         no mrp periodic
         no mvrp
         no udld port
         no trap mac-change
        !
        interface GigabitEthernet 1/2
         switchport voice vlan mode disable
         no switchport voice vlan security
         switchport voice vlan discovery-protocol oui
         loop-protect
         no loop-protect action
         loop-protect tx-mode
         no loop-protect act-port
         switchport access vlan 1
         switchport trunk native vlan 1
         switchport hybrid native vlan 1                   
         switchport trunk allowed vlan 1-4094
         switchport hybrid allowed vlan 1-4094
         no switchport trunk vlan tag native
         switchport hybrid acceptable-frame-type all
         no switchport hybrid ingress-filtering
         switchport hybrid egress-tag all except-native
         switchport hybrid port-type c-port
         switchport mode access
         switchport forbidden vlan remove 1-4094
         vcl smacsip
         no pvlan isolation
         pvlan 1
         no mvr immediate-leave
         no ip igmp snooping filter
         no ip igmp snooping max-groups
         no ip igmp snooping mrouter
         no ip igmp snooping immediate-leave
         no ipv6 mld snooping filter
         no ipv6 mld snooping max-groups
         no ipv6 mld snooping mrouter
         no ipv6 mld snooping immediate-leave
         ip dhcp snooping trust
         no ipv6 dhcp snooping trust                       
         ip arp inspection trust
         no ip arp inspection check-vlan
         no ip arp inspection logging
         no ip verify source
         no ip verify source limit
         no ipv6 verify source
         no ipv6 verify source limit
         lldp receive
         lldp transmit
         lldp tlv-select management-address
         lldp tlv-select port-description
         lldp tlv-select system-capabilities
         lldp tlv-select system-name
         lldp tlv-select system-description
         no lldp cdp-aware
         no lldp trap
         lldp med transmit-tlv capabilities network-policy location poe
         no lldp med media-vlan policy-list
         lldp med type connectivity
         poe mode enable
         poe priority low
         poe lldp
         no poe ping-ip-addr                               
         no poe startup-time
         no poe interval-time
         no poe ping-retry-time
         no poe failure-action
         no poe reboot-time
         no poe max-reboot-time
         no poe delay-mode
         no poe delay-time
         no poe port-profile
         qos cos 0
         qos pcp 0
         qos dpl 0
         qos dei 0
         qos class 0
         no qos trust tag
         qos map tag-cos pcp 0 dei 0 cos 1 dpl 0
         qos map tag-cos pcp 0 dei 1 cos 1 dpl 1
         qos map tag-cos pcp 1 dei 0 cos 0 dpl 0
         qos map tag-cos pcp 1 dei 1 cos 0 dpl 1
         qos map tag-cos pcp 2 dei 0 cos 2 dpl 0
         qos map tag-cos pcp 2 dei 1 cos 2 dpl 1
         qos map tag-cos pcp 3 dei 0 cos 3 dpl 0
         qos map tag-cos pcp 3 dei 1 cos 3 dpl 1           
         qos map tag-cos pcp 4 dei 0 cos 4 dpl 0
         qos map tag-cos pcp 4 dei 1 cos 4 dpl 1
         qos map tag-cos pcp 5 dei 0 cos 5 dpl 0
         qos map tag-cos pcp 5 dei 1 cos 5 dpl 1
         qos map tag-cos pcp 6 dei 0 cos 6 dpl 0
         qos map tag-cos pcp 6 dei 1 cos 6 dpl 1
         qos map tag-cos pcp 7 dei 0 cos 7 dpl 0
         qos map tag-cos pcp 7 dei 1 cos 7 dpl 1
         no qos trust dscp
         no qos policer
         no qos queue-policer queue 0
         no qos queue-policer queue 1
         no qos queue-policer queue 2
         no qos queue-policer queue 3
         no qos queue-policer queue 4
         no qos queue-policer queue 5
         no qos queue-policer queue 6
         no qos queue-policer queue 7
         no qos shaper
         no qos queue-shaper queue 0
         no qos queue-shaper queue 1
         no qos queue-shaper queue 2
         no qos queue-shaper queue 3                       
         no qos queue-shaper queue 4
         no qos queue-shaper queue 5
         no qos queue-shaper queue 6
         no qos queue-shaper queue 7
         no qos wrr
         no qos tag-remark
         qos map cos-tag cos 0 dpl 0 pcp 1 dei 0
         qos map cos-tag cos 0 dpl 1 pcp 1 dei 1
         qos map cos-tag cos 1 dpl 0 pcp 0 dei 0
         qos map cos-tag cos 1 dpl 1 pcp 0 dei 1
         qos map cos-tag cos 2 dpl 0 pcp 2 dei 0
         qos map cos-tag cos 2 dpl 1 pcp 2 dei 1
         qos map cos-tag cos 3 dpl 0 pcp 3 dei 0
         qos map cos-tag cos 3 dpl 1 pcp 3 dei 1
         qos map cos-tag cos 4 dpl 0 pcp 4 dei 0
         qos map cos-tag cos 4 dpl 1 pcp 4 dei 1
         qos map cos-tag cos 5 dpl 0 pcp 5 dei 0
         qos map cos-tag cos 5 dpl 1 pcp 5 dei 1
         qos map cos-tag cos 6 dpl 0 pcp 6 dei 0
         qos map cos-tag cos 6 dpl 1 pcp 6 dei 1
         qos map cos-tag cos 7 dpl 0 pcp 7 dei 0
         qos map cos-tag cos 7 dpl 1 pcp 7 dei 1
         no qos dscp-translate                             
         no qos dscp-classify
         no qos dscp-remark
         qos wred-group 1
         no qos ingress-map
         no qos egress-map
         access-list action permit
         no access-list rate-limiter 
         access-list policy 0
         no access-list redirect
         no access-list mirror
         no access-list logging
         no access-list shutdown
         no thermal-protect grp
         mac address-table learning
         spanning-tree
         no spanning-tree edge
         spanning-tree auto-edge
         spanning-tree link-type auto
         no spanning-tree restricted-role
         no spanning-tree restricted-tcn
         no spanning-tree bpdu-guard
         spanning-tree mst 0 cost auto
         spanning-tree mst 0 port-priority 128             
         spanning-tree mst 1 cost auto
         spanning-tree mst 1 port-priority 128
         spanning-tree mst 2 cost auto
         spanning-tree mst 2 port-priority 128
         spanning-tree mst 3 cost auto
         spanning-tree mst 3 port-priority 128
         spanning-tree mst 4 cost auto
         spanning-tree mst 4 port-priority 128
         spanning-tree mst 5 cost auto
         spanning-tree mst 5 port-priority 128
         spanning-tree mst 6 cost auto
         spanning-tree mst 6 port-priority 128
         spanning-tree mst 7 cost auto
         spanning-tree mst 7 port-priority 128
         lacp port-priority 32768
         lacp timeout fast
         media-type rj45
         speed auto 10 100 1000
         duplex full
         flowcontrol off
         no priority-flowcontrol prio 0-7
         mtu 10240
         no excessive-restart                              
         no frame-length-check
         no shutdown
         no description
         no green-ethernet eee
         no green-ethernet eee urgent-queue 
         no green-ethernet energy-detect
         no green-ethernet short-reach
         dot1x port-control force-authorized
         no dot1x guest-vlan
         no dot1x radius-vlan
         no dot1x radius-qos
         no dot1x mac-based-fallback
         port-security maximum 4
         port-security maximum-violation 4
         port-security violation protect
         no port-security
         no port-security mac-address sticky
         switchport vlan mapping 2
         no aggregation group
         no gvrp
         mrp timers join-time 20 leave-time 60 leave-all-time 1000
         no mrp periodic
         no mvrp                                           
         no udld port
         no trap mac-change
        !
        interface GigabitEthernet 1/3
         switchport voice vlan mode disable
         no switchport voice vlan security
         switchport voice vlan discovery-protocol oui
         loop-protect
         no loop-protect action
         loop-protect tx-mode
         no loop-protect act-port
         switchport access vlan 1
         switchport trunk native vlan 1
         switchport hybrid native vlan 1
         switchport trunk allowed vlan 1-4094
         switchport hybrid allowed vlan 1-4094
         no switchport trunk vlan tag native
         switchport hybrid acceptable-frame-type all
         no switchport hybrid ingress-filtering
         switchport hybrid egress-tag all except-native
         switchport hybrid port-type c-port
         switchport mode access
         switchport forbidden vlan remove 1-4094           
         vcl smacsip
         no pvlan isolation
         pvlan 1
         no mvr immediate-leave
         no ip igmp snooping filter
         no ip igmp snooping max-groups
         no ip igmp snooping mrouter
         no ip igmp snooping immediate-leave
         no ipv6 mld snooping filter
         no ipv6 mld snooping max-groups
         no ipv6 mld snooping mrouter
         no ipv6 mld snooping immediate-leave
         ip dhcp snooping trust
         no ipv6 dhcp snooping trust
         ip arp inspection trust
         no ip arp inspection check-vlan
         no ip arp inspection logging
         no ip verify source
         no ip verify source limit
         no ipv6 verify source
         no ipv6 verify source limit
         lldp receive
         lldp transmit                                     
         lldp tlv-select management-address
         lldp tlv-select port-description
         lldp tlv-select system-capabilities
         lldp tlv-select system-name
         lldp tlv-select system-description
         no lldp cdp-aware
         no lldp trap
         lldp med transmit-tlv capabilities network-policy location poe
         no lldp med media-vlan policy-list
         lldp med type connectivity
         poe mode enable
         poe priority low
         poe lldp
         no poe ping-ip-addr
         no poe startup-time
         no poe interval-time
         no poe ping-retry-time
         no poe failure-action
         no poe reboot-time
         no poe max-reboot-time
         no poe delay-mode
         no poe delay-time
         no poe port-profile                               
         qos cos 0
         qos pcp 0
         qos dpl 0
         qos dei 0
         qos class 0
         no qos trust tag
         qos map tag-cos pcp 0 dei 0 cos 1 dpl 0
         qos map tag-cos pcp 0 dei 1 cos 1 dpl 1
         qos map tag-cos pcp 1 dei 0 cos 0 dpl 0
         qos map tag-cos pcp 1 dei 1 cos 0 dpl 1
         qos map tag-cos pcp 2 dei 0 cos 2 dpl 0
         qos map tag-cos pcp 2 dei 1 cos 2 dpl 1
         qos map tag-cos pcp 3 dei 0 cos 3 dpl 0
         qos map tag-cos pcp 3 dei 1 cos 3 dpl 1
         qos map tag-cos pcp 4 dei 0 cos 4 dpl 0
         qos map tag-cos pcp 4 dei 1 cos 4 dpl 1
         qos map tag-cos pcp 5 dei 0 cos 5 dpl 0
         qos map tag-cos pcp 5 dei 1 cos 5 dpl 1
         qos map tag-cos pcp 6 dei 0 cos 6 dpl 0
         qos map tag-cos pcp 6 dei 1 cos 6 dpl 1
         qos map tag-cos pcp 7 dei 0 cos 7 dpl 0
         qos map tag-cos pcp 7 dei 1 cos 7 dpl 1
         no qos trust dscp                                 
         no qos policer
         no qos queue-policer queue 0
         no qos queue-policer queue 1
         no qos queue-policer queue 2
         no qos queue-policer queue 3
         no qos queue-policer queue 4
         no qos queue-policer queue 5
         no qos queue-policer queue 6
         no qos queue-policer queue 7
         no qos shaper
         no qos queue-shaper queue 0
         no qos queue-shaper queue 1
         no qos queue-shaper queue 2
         no qos queue-shaper queue 3
         no qos queue-shaper queue 4
         no qos queue-shaper queue 5
         no qos queue-shaper queue 6
         no qos queue-shaper queue 7
         no qos wrr
         no qos tag-remark
         qos map cos-tag cos 0 dpl 0 pcp 1 dei 0
         qos map cos-tag cos 0 dpl 1 pcp 1 dei 1
         qos map cos-tag cos 1 dpl 0 pcp 0 dei 0           
         qos map cos-tag cos 1 dpl 1 pcp 0 dei 1
         qos map cos-tag cos 2 dpl 0 pcp 2 dei 0
         qos map cos-tag cos 2 dpl 1 pcp 2 dei 1
         qos map cos-tag cos 3 dpl 0 pcp 3 dei 0
         qos map cos-tag cos 3 dpl 1 pcp 3 dei 1
         qos map cos-tag cos 4 dpl 0 pcp 4 dei 0
         qos map cos-tag cos 4 dpl 1 pcp 4 dei 1
         qos map cos-tag cos 5 dpl 0 pcp 5 dei 0
         qos map cos-tag cos 5 dpl 1 pcp 5 dei 1
         qos map cos-tag cos 6 dpl 0 pcp 6 dei 0
         qos map cos-tag cos 6 dpl 1 pcp 6 dei 1
         qos map cos-tag cos 7 dpl 0 pcp 7 dei 0
         qos map cos-tag cos 7 dpl 1 pcp 7 dei 1
         no qos dscp-translate
         no qos dscp-classify
         no qos dscp-remark
         qos wred-group 1
         no qos ingress-map
         no qos egress-map
         access-list action permit
         no access-list rate-limiter 
         access-list policy 0
         no access-list redirect                           
         no access-list mirror
         no access-list logging
         no access-list shutdown
         no thermal-protect grp
         mac address-table learning
         spanning-tree
         no spanning-tree edge
         spanning-tree auto-edge
         spanning-tree link-type auto
         no spanning-tree restricted-role
         no spanning-tree restricted-tcn
         no spanning-tree bpdu-guard
         spanning-tree mst 0 cost auto
         spanning-tree mst 0 port-priority 128
         spanning-tree mst 1 cost auto
         spanning-tree mst 1 port-priority 128
         spanning-tree mst 2 cost auto
         spanning-tree mst 2 port-priority 128
         spanning-tree mst 3 cost auto
         spanning-tree mst 3 port-priority 128
         spanning-tree mst 4 cost auto
         spanning-tree mst 4 port-priority 128
         spanning-tree mst 5 cost auto                     
         spanning-tree mst 5 port-priority 128
         spanning-tree mst 6 cost auto
         spanning-tree mst 6 port-priority 128
         spanning-tree mst 7 cost auto
         spanning-tree mst 7 port-priority 128
         lacp port-priority 32768
         lacp timeout fast
         media-type rj45
         speed auto 10 100 1000
         duplex full
         flowcontrol off
         no priority-flowcontrol prio 0-7
         mtu 10240
         no excessive-restart
         no frame-length-check
         no shutdown
         no description
         no green-ethernet energy-detect
         no green-ethernet short-reach
         dot1x port-control force-authorized
         no dot1x guest-vlan
         no dot1x radius-vlan
         no dot1x radius-qos                               
         no dot1x mac-based-fallback
         port-security maximum 4
         port-security maximum-violation 4
         port-security violation protect
         no port-security
         no port-security mac-address sticky
         switchport vlan mapping 3
         no aggregation group
         no gvrp
         mrp timers join-time 20 leave-time 60 leave-all-time 1000
         no mrp periodic
         no mvrp
         no udld port
         no trap mac-change
        !
        interface GigabitEthernet 1/4
         switchport voice vlan mode disable
         no switchport voice vlan security
         switchport voice vlan discovery-protocol oui
         loop-protect
         no loop-protect action
         loop-protect tx-mode
         no loop-protect act-port                          
         switchport access vlan 1
         switchport trunk native vlan 1
         switchport hybrid native vlan 1
         switchport trunk allowed vlan 1-4094
         switchport hybrid allowed vlan 1-4094
         no switchport trunk vlan tag native
         switchport hybrid acceptable-frame-type all
         no switchport hybrid ingress-filtering
         switchport hybrid egress-tag all except-native
         switchport hybrid port-type c-port
         switchport mode access
         switchport forbidden vlan remove 1-4094
         vcl smacsip
         no pvlan isolation
         pvlan 1
         no mvr immediate-leave
         no ip igmp snooping filter
         no ip igmp snooping max-groups
         no ip igmp snooping mrouter
         no ip igmp snooping immediate-leave
         no ipv6 mld snooping filter
         no ipv6 mld snooping max-groups
         no ipv6 mld snooping mrouter                      
         no ipv6 mld snooping immediate-leave
         ip dhcp snooping trust
         no ipv6 dhcp snooping trust
         ip arp inspection trust
         no ip arp inspection check-vlan
         no ip arp inspection logging
         no ip verify source
         no ip verify source limit
         no ipv6 verify source
         no ipv6 verify source limit
         lldp receive
         lldp transmit
         lldp tlv-select management-address
         lldp tlv-select port-description
         lldp tlv-select system-capabilities
         lldp tlv-select system-name
         lldp tlv-select system-description
         no lldp cdp-aware
         no lldp trap
         lldp med transmit-tlv capabilities network-policy location poe
         no lldp med media-vlan policy-list
         lldp med type connectivity
         poe mode enable                                   
         poe priority low
         poe lldp
         no poe ping-ip-addr
         no poe startup-time
         no poe interval-time
         no poe ping-retry-time
         no poe failure-action
         no poe reboot-time
         no poe max-reboot-time
         no poe delay-mode
         no poe delay-time
         no poe port-profile
         qos cos 0
         qos pcp 0
         qos dpl 0
         qos dei 0
         qos class 0
         no qos trust tag
         qos map tag-cos pcp 0 dei 0 cos 1 dpl 0
         qos map tag-cos pcp 0 dei 1 cos 1 dpl 1
         qos map tag-cos pcp 1 dei 0 cos 0 dpl 0
         qos map tag-cos pcp 1 dei 1 cos 0 dpl 1
         qos map tag-cos pcp 2 dei 0 cos 2 dpl 0           
         qos map tag-cos pcp 2 dei 1 cos 2 dpl 1
         qos map tag-cos pcp 3 dei 0 cos 3 dpl 0
         qos map tag-cos pcp 3 dei 1 cos 3 dpl 1
         qos map tag-cos pcp 4 dei 0 cos 4 dpl 0
         qos map tag-cos pcp 4 dei 1 cos 4 dpl 1
         qos map tag-cos pcp 5 dei 0 cos 5 dpl 0
         qos map tag-cos pcp 5 dei 1 cos 5 dpl 1
         qos map tag-cos pcp 6 dei 0 cos 6 dpl 0
         qos map tag-cos pcp 6 dei 1 cos 6 dpl 1
         qos map tag-cos pcp 7 dei 0 cos 7 dpl 0
         qos map tag-cos pcp 7 dei 1 cos 7 dpl 1
         no qos trust dscp
         no qos policer
         no qos queue-policer queue 0
         no qos queue-policer queue 1
         no qos queue-policer queue 2
         no qos queue-policer queue 3
         no qos queue-policer queue 4
         no qos queue-policer queue 5
         no qos queue-policer queue 6
         no qos queue-policer queue 7
         no qos shaper
         no qos queue-shaper queue 0                       
         no qos queue-shaper queue 1
         no qos queue-shaper queue 2
         no qos queue-shaper queue 3
         no qos queue-shaper queue 4
         no qos queue-shaper queue 5
         no qos queue-shaper queue 6
         no qos queue-shaper queue 7
         no qos wrr
         no qos tag-remark
         qos map cos-tag cos 0 dpl 0 pcp 1 dei 0
         qos map cos-tag cos 0 dpl 1 pcp 1 dei 1
         qos map cos-tag cos 1 dpl 0 pcp 0 dei 0
         qos map cos-tag cos 1 dpl 1 pcp 0 dei 1
         qos map cos-tag cos 2 dpl 0 pcp 2 dei 0
         qos map cos-tag cos 2 dpl 1 pcp 2 dei 1
         qos map cos-tag cos 3 dpl 0 pcp 3 dei 0
         qos map cos-tag cos 3 dpl 1 pcp 3 dei 1
         qos map cos-tag cos 4 dpl 0 pcp 4 dei 0
         qos map cos-tag cos 4 dpl 1 pcp 4 dei 1
         qos map cos-tag cos 5 dpl 0 pcp 5 dei 0
         qos map cos-tag cos 5 dpl 1 pcp 5 dei 1
         qos map cos-tag cos 6 dpl 0 pcp 6 dei 0
         qos map cos-tag cos 6 dpl 1 pcp 6 dei 1           
         qos map cos-tag cos 7 dpl 0 pcp 7 dei 0
         qos map cos-tag cos 7 dpl 1 pcp 7 dei 1
         no qos dscp-translate
         no qos dscp-classify
         no qos dscp-remark
         qos wred-group 1
         no qos ingress-map
         no qos egress-map
         access-list action permit
         no access-list rate-limiter 
         access-list policy 0
         no access-list redirect
         no access-list mirror
         no access-list logging
         no access-list shutdown
         no thermal-protect grp
         mac address-table learning
         spanning-tree
         no spanning-tree edge
         spanning-tree auto-edge
         spanning-tree link-type auto
         no spanning-tree restricted-role
         no spanning-tree restricted-tcn                   
         no spanning-tree bpdu-guard
         spanning-tree mst 0 cost auto
         spanning-tree mst 0 port-priority 128
         spanning-tree mst 1 cost auto
         spanning-tree mst 1 port-priority 128
         spanning-tree mst 2 cost auto
         spanning-tree mst 2 port-priority 128
         spanning-tree mst 3 cost auto
         spanning-tree mst 3 port-priority 128
         spanning-tree mst 4 cost auto
         spanning-tree mst 4 port-priority 128
         spanning-tree mst 5 cost auto
         spanning-tree mst 5 port-priority 128
         spanning-tree mst 6 cost auto
         spanning-tree mst 6 port-priority 128
         spanning-tree mst 7 cost auto
         spanning-tree mst 7 port-priority 128
         lacp port-priority 32768
         lacp timeout fast
         media-type rj45
         speed auto 10 100 1000
         duplex full
         flowcontrol off                                   
         no priority-flowcontrol prio 0-7
         mtu 10240
         no excessive-restart
         no frame-length-check
         no shutdown
         no description
         no green-ethernet energy-detect
         no green-ethernet short-reach
         dot1x port-control force-authorized
         no dot1x guest-vlan
         no dot1x radius-vlan
         no dot1x radius-qos
         no dot1x mac-based-fallback
         port-security maximum 4
         port-security maximum-violation 4
         port-security violation protect
         no port-security
         no port-security mac-address sticky
         switchport vlan mapping 4
         no aggregation group
         no gvrp
         mrp timers join-time 20 leave-time 60 leave-all-time 1000
         no mrp periodic                                   
         no mvrp
         no udld port
         no trap mac-change
        !
        interface 2.5GigabitEthernet 1/1
         switchport voice vlan mode disable
         no switchport voice vlan security
         switchport voice vlan discovery-protocol oui
         loop-protect
         no loop-protect action
         loop-protect tx-mode
         no loop-protect act-port
         switchport access vlan 1
         switchport trunk native vlan 1
         switchport hybrid native vlan 1
         switchport trunk allowed vlan 1-4094
         switchport hybrid allowed vlan 1-4094
         no switchport trunk vlan tag native
         switchport hybrid acceptable-frame-type all
         no switchport hybrid ingress-filtering
         switchport hybrid egress-tag all except-native
         switchport hybrid port-type c-port
         switchport mode access                            
         switchport forbidden vlan remove 1-4094
         vcl smacsip
         no pvlan isolation
         pvlan 1
         no mvr immediate-leave
         no ip igmp snooping filter
         no ip igmp snooping max-groups
         no ip igmp snooping mrouter
         no ip igmp snooping immediate-leave
         no ipv6 mld snooping filter
         no ipv6 mld snooping max-groups
         no ipv6 mld snooping mrouter
         no ipv6 mld snooping immediate-leave
         ip dhcp snooping trust
         no ipv6 dhcp snooping trust
         ip arp inspection trust
         no ip arp inspection check-vlan
         no ip arp inspection logging
         no ip verify source
         no ip verify source limit
         no ipv6 verify source
         no ipv6 verify source limit
         lldp receive                                      
         lldp transmit
         lldp tlv-select management-address
         lldp tlv-select port-description
         lldp tlv-select system-capabilities
         lldp tlv-select system-name
         lldp tlv-select system-description
         no lldp cdp-aware
         no lldp trap
         lldp med transmit-tlv capabilities network-policy location poe
         no lldp med media-vlan policy-list
         lldp med type connectivity
         poe mode enable
         poe priority low
         poe lldp
         no poe ping-ip-addr
         no poe startup-time
         no poe interval-time
         no poe ping-retry-time
         no poe failure-action
         no poe reboot-time
         no poe max-reboot-time
         no poe delay-mode
         no poe delay-time                                 
         no poe port-profile
         qos cos 0
         qos pcp 0
         qos dpl 0
         qos dei 0
         qos class 0
         no qos trust tag
         qos map tag-cos pcp 0 dei 0 cos 1 dpl 0
         qos map tag-cos pcp 0 dei 1 cos 1 dpl 1
         qos map tag-cos pcp 1 dei 0 cos 0 dpl 0
         qos map tag-cos pcp 1 dei 1 cos 0 dpl 1
         qos map tag-cos pcp 2 dei 0 cos 2 dpl 0
         qos map tag-cos pcp 2 dei 1 cos 2 dpl 1
         qos map tag-cos pcp 3 dei 0 cos 3 dpl 0
         qos map tag-cos pcp 3 dei 1 cos 3 dpl 1
         qos map tag-cos pcp 4 dei 0 cos 4 dpl 0
         qos map tag-cos pcp 4 dei 1 cos 4 dpl 1
         qos map tag-cos pcp 5 dei 0 cos 5 dpl 0
         qos map tag-cos pcp 5 dei 1 cos 5 dpl 1
         qos map tag-cos pcp 6 dei 0 cos 6 dpl 0
         qos map tag-cos pcp 6 dei 1 cos 6 dpl 1
         qos map tag-cos pcp 7 dei 0 cos 7 dpl 0
         qos map tag-cos pcp 7 dei 1 cos 7 dpl 1           
         no qos trust dscp
         no qos policer
         no qos queue-policer queue 0
         no qos queue-policer queue 1
         no qos queue-policer queue 2
         no qos queue-policer queue 3
         no qos queue-policer queue 4
         no qos queue-policer queue 5
         no qos queue-policer queue 6
         no qos queue-policer queue 7
         no qos shaper
         no qos queue-shaper queue 0
         no qos queue-shaper queue 1
         no qos queue-shaper queue 2
         no qos queue-shaper queue 3
         no qos queue-shaper queue 4
         no qos queue-shaper queue 5
         no qos queue-shaper queue 6
         no qos queue-shaper queue 7
         no qos wrr
         no qos tag-remark
         qos map cos-tag cos 0 dpl 0 pcp 1 dei 0
         qos map cos-tag cos 0 dpl 1 pcp 1 dei 1           
         qos map cos-tag cos 1 dpl 0 pcp 0 dei 0
         qos map cos-tag cos 1 dpl 1 pcp 0 dei 1
         qos map cos-tag cos 2 dpl 0 pcp 2 dei 0
         qos map cos-tag cos 2 dpl 1 pcp 2 dei 1
         qos map cos-tag cos 3 dpl 0 pcp 3 dei 0
         qos map cos-tag cos 3 dpl 1 pcp 3 dei 1
         qos map cos-tag cos 4 dpl 0 pcp 4 dei 0
         qos map cos-tag cos 4 dpl 1 pcp 4 dei 1
         qos map cos-tag cos 5 dpl 0 pcp 5 dei 0
         qos map cos-tag cos 5 dpl 1 pcp 5 dei 1
         qos map cos-tag cos 6 dpl 0 pcp 6 dei 0
         qos map cos-tag cos 6 dpl 1 pcp 6 dei 1
         qos map cos-tag cos 7 dpl 0 pcp 7 dei 0
         qos map cos-tag cos 7 dpl 1 pcp 7 dei 1
         no qos dscp-translate
         no qos dscp-classify
         no qos dscp-remark
         qos wred-group 1
         no qos ingress-map
         no qos egress-map
         access-list action permit
         no access-list rate-limiter 
         access-list policy 0                              
         no access-list redirect
         no access-list mirror
         no access-list logging
         no access-list shutdown
         no thermal-protect grp
         mac address-table learning
         spanning-tree
         no spanning-tree edge
         spanning-tree auto-edge
         spanning-tree link-type auto
         no spanning-tree restricted-role
         no spanning-tree restricted-tcn
         no spanning-tree bpdu-guard
         spanning-tree mst 0 cost auto
         spanning-tree mst 0 port-priority 128
         spanning-tree mst 1 cost auto
         spanning-tree mst 1 port-priority 128
         spanning-tree mst 2 cost auto
         spanning-tree mst 2 port-priority 128
         spanning-tree mst 3 cost auto
         spanning-tree mst 3 port-priority 128
         spanning-tree mst 4 cost auto
         spanning-tree mst 4 port-priority 128             
         spanning-tree mst 5 cost auto
         spanning-tree mst 5 port-priority 128
         spanning-tree mst 6 cost auto
         spanning-tree mst 6 port-priority 128
         spanning-tree mst 7 cost auto
         spanning-tree mst 7 port-priority 128
         lacp port-priority 32768
         lacp timeout fast
         media-type rj45
         speed auto 100 1000 2500
         duplex full
         flowcontrol off
         no priority-flowcontrol prio 0-7
         mtu 10240
         no excessive-restart
         no frame-length-check
         no shutdown
         no description
         no green-ethernet energy-detect
         no green-ethernet short-reach
         dot1x port-control force-authorized
         no dot1x guest-vlan
         no dot1x radius-vlan                              
         no dot1x radius-qos
         no dot1x mac-based-fallback
         port-security maximum 4
         port-security maximum-violation 4
         port-security violation protect
         no port-security
         no port-security mac-address sticky
         switchport vlan mapping 5
         no aggregation group
         no gvrp
         mrp timers join-time 20 leave-time 60 leave-all-time 1000
         no mrp periodic
         no mvrp
         no udld port
         no trap mac-change
        !
        interface 2.5GigabitEthernet 1/2
         switchport voice vlan mode disable
         no switchport voice vlan security
         switchport voice vlan discovery-protocol oui
         loop-protect
         no loop-protect action
         loop-protect tx-mode                              
         no loop-protect act-port
         switchport access vlan 1
         switchport trunk native vlan 1
         switchport hybrid native vlan 1
         switchport trunk allowed vlan 1-4094
         switchport hybrid allowed vlan 1-4094
         no switchport trunk vlan tag native
         switchport hybrid acceptable-frame-type all
         no switchport hybrid ingress-filtering
         switchport hybrid egress-tag all except-native
         switchport hybrid port-type c-port
         switchport mode access
         switchport forbidden vlan remove 1-4094
         vcl smacsip
         no pvlan isolation
         pvlan 1
         no mvr immediate-leave
         no ip igmp snooping filter
         no ip igmp snooping max-groups
         no ip igmp snooping mrouter
         no ip igmp snooping immediate-leave
         no ipv6 mld snooping filter
         no ipv6 mld snooping max-groups                   
         no ipv6 mld snooping mrouter
         no ipv6 mld snooping immediate-leave
         ip dhcp snooping trust
         no ipv6 dhcp snooping trust
         ip arp inspection trust
         no ip arp inspection check-vlan
         no ip arp inspection logging
         no ip verify source
         no ip verify source limit
         no ipv6 verify source
         no ipv6 verify source limit
         lldp receive
         lldp transmit
         lldp tlv-select management-address
         lldp tlv-select port-description
         lldp tlv-select system-capabilities
         lldp tlv-select system-name
         lldp tlv-select system-description
         no lldp cdp-aware
         no lldp trap
         lldp med transmit-tlv capabilities network-policy location poe
         no lldp med media-vlan policy-list
         lldp med type connectivity                        
         poe mode enable
         poe priority low
         poe lldp
         no poe ping-ip-addr
         no poe startup-time
         no poe interval-time
         no poe ping-retry-time
         no poe failure-action
         no poe reboot-time
         no poe max-reboot-time
         no poe delay-mode
         no poe delay-time
         no poe port-profile
         qos cos 0
         qos pcp 0
         qos dpl 0
         qos dei 0
         qos class 0
         no qos trust tag
         qos map tag-cos pcp 0 dei 0 cos 1 dpl 0
         qos map tag-cos pcp 0 dei 1 cos 1 dpl 1
         qos map tag-cos pcp 1 dei 0 cos 0 dpl 0
         qos map tag-cos pcp 1 dei 1 cos 0 dpl 1           
         qos map tag-cos pcp 2 dei 0 cos 2 dpl 0
         qos map tag-cos pcp 2 dei 1 cos 2 dpl 1
         qos map tag-cos pcp 3 dei 0 cos 3 dpl 0
         qos map tag-cos pcp 3 dei 1 cos 3 dpl 1
         qos map tag-cos pcp 4 dei 0 cos 4 dpl 0
         qos map tag-cos pcp 4 dei 1 cos 4 dpl 1
         qos map tag-cos pcp 5 dei 0 cos 5 dpl 0
         qos map tag-cos pcp 5 dei 1 cos 5 dpl 1
         qos map tag-cos pcp 6 dei 0 cos 6 dpl 0
         qos map tag-cos pcp 6 dei 1 cos 6 dpl 1
         qos map tag-cos pcp 7 dei 0 cos 7 dpl 0
         qos map tag-cos pcp 7 dei 1 cos 7 dpl 1
         no qos trust dscp
         no qos policer
         no qos queue-policer queue 0
         no qos queue-policer queue 1
         no qos queue-policer queue 2
         no qos queue-policer queue 3
         no qos queue-policer queue 4
         no qos queue-policer queue 5
         no qos queue-policer queue 6
         no qos queue-policer queue 7
         no qos shaper                                     
         no qos queue-shaper queue 0
         no qos queue-shaper queue 1
         no qos queue-shaper queue 2
         no qos queue-shaper queue 3
         no qos queue-shaper queue 4
         no qos queue-shaper queue 5
         no qos queue-shaper queue 6
         no qos queue-shaper queue 7
         no qos wrr
         no qos tag-remark
         qos map cos-tag cos 0 dpl 0 pcp 1 dei 0
         qos map cos-tag cos 0 dpl 1 pcp 1 dei 1
         qos map cos-tag cos 1 dpl 0 pcp 0 dei 0
         qos map cos-tag cos 1 dpl 1 pcp 0 dei 1
         qos map cos-tag cos 2 dpl 0 pcp 2 dei 0
         qos map cos-tag cos 2 dpl 1 pcp 2 dei 1
         qos map cos-tag cos 3 dpl 0 pcp 3 dei 0
         qos map cos-tag cos 3 dpl 1 pcp 3 dei 1
         qos map cos-tag cos 4 dpl 0 pcp 4 dei 0
         qos map cos-tag cos 4 dpl 1 pcp 4 dei 1
         qos map cos-tag cos 5 dpl 0 pcp 5 dei 0
         qos map cos-tag cos 5 dpl 1 pcp 5 dei 1
         qos map cos-tag cos 6 dpl 0 pcp 6 dei 0           
         qos map cos-tag cos 6 dpl 1 pcp 6 dei 1
         qos map cos-tag cos 7 dpl 0 pcp 7 dei 0
         qos map cos-tag cos 7 dpl 1 pcp 7 dei 1
         no qos dscp-translate
         no qos dscp-classify
         no qos dscp-remark
         qos wred-group 1
         no qos ingress-map
         no qos egress-map
         access-list action permit
         no access-list rate-limiter 
         access-list policy 0
         no access-list redirect
         no access-list mirror
         no access-list logging
         no access-list shutdown
         no thermal-protect grp
         mac address-table learning
         spanning-tree
         no spanning-tree edge
         spanning-tree auto-edge
         spanning-tree link-type auto
         no spanning-tree restricted-role                  
         no spanning-tree restricted-tcn
         no spanning-tree bpdu-guard
         spanning-tree mst 0 cost auto
         spanning-tree mst 0 port-priority 128
         spanning-tree mst 1 cost auto
         spanning-tree mst 1 port-priority 128
         spanning-tree mst 2 cost auto
         spanning-tree mst 2 port-priority 128
         spanning-tree mst 3 cost auto
         spanning-tree mst 3 port-priority 128
         spanning-tree mst 4 cost auto
         spanning-tree mst 4 port-priority 128
         spanning-tree mst 5 cost auto
         spanning-tree mst 5 port-priority 128
         spanning-tree mst 6 cost auto
         spanning-tree mst 6 port-priority 128
         spanning-tree mst 7 cost auto
         spanning-tree mst 7 port-priority 128
         lacp port-priority 32768
         lacp timeout fast
         media-type rj45
         speed auto 100 1000 2500
         duplex full                                       
         flowcontrol off
         no priority-flowcontrol prio 0-7
         mtu 10240
         no excessive-restart
         no frame-length-check
         no shutdown
         no description
         no green-ethernet energy-detect
         no green-ethernet short-reach
         dot1x port-control force-authorized
         no dot1x guest-vlan
         no dot1x radius-vlan
         no dot1x radius-qos
         no dot1x mac-based-fallback
         port-security maximum 4
         port-security maximum-violation 4
         port-security violation protect
         no port-security
         no port-security mac-address sticky
         switchport vlan mapping 6
         no aggregation group
         no gvrp
         mrp timers join-time 20 leave-time 60 leave-all-time 1000
         no mrp periodic
         no mvrp
         no udld port
         no trap mac-change
        !
        interface 2.5GigabitEthernet 1/3
         switchport voice vlan mode disable
         no switchport voice vlan security
         switchport voice vlan discovery-protocol oui
         loop-protect
         no loop-protect action
         loop-protect tx-mode
         no loop-protect act-port
         switchport access vlan 1
         switchport trunk native vlan 1
         switchport hybrid native vlan 1
         switchport trunk allowed vlan 1-4094
         switchport hybrid allowed vlan 1-4094
         no switchport trunk vlan tag native
         switchport hybrid acceptable-frame-type all
         no switchport hybrid ingress-filtering
         switchport hybrid egress-tag all except-native
         switchport hybrid port-type c-port                
         switchport mode access
         switchport forbidden vlan remove 1-4094
         vcl smacsip
         no pvlan isolation
         pvlan 1
         no mvr immediate-leave
         no ip igmp snooping filter
         no ip igmp snooping max-groups
         no ip igmp snooping mrouter
         no ip igmp snooping immediate-leave
         no ipv6 mld snooping filter
         no ipv6 mld snooping max-groups
         no ipv6 mld snooping mrouter
         no ipv6 mld snooping immediate-leave
         ip dhcp snooping trust
         no ipv6 dhcp snooping trust
         ip arp inspection trust
         no ip arp inspection check-vlan
         no ip arp inspection logging
         no ip verify source
         no ip verify source limit
         no ipv6 verify source
         no ipv6 verify source limit                       
         lldp receive
         lldp transmit
         lldp tlv-select management-address
         lldp tlv-select port-description
         lldp tlv-select system-capabilities
         lldp tlv-select system-name
         lldp tlv-select system-description
         no lldp cdp-aware
         no lldp trap
         lldp med transmit-tlv capabilities network-policy location poe
         no lldp med media-vlan policy-list
         lldp med type connectivity
         poe mode enable
         poe priority low
         poe lldp
         no poe ping-ip-addr
         no poe startup-time
         no poe interval-time
         no poe ping-retry-time
         no poe failure-action
         no poe reboot-time
         no poe max-reboot-time
         no poe delay-mode                                 
         no poe delay-time
         no poe port-profile
         qos cos 0
         qos pcp 0
         qos dpl 0
         qos dei 0
         qos class 0
         no qos trust tag
         qos map tag-cos pcp 0 dei 0 cos 1 dpl 0
         qos map tag-cos pcp 0 dei 1 cos 1 dpl 1
         qos map tag-cos pcp 1 dei 0 cos 0 dpl 0
         qos map tag-cos pcp 1 dei 1 cos 0 dpl 1
         qos map tag-cos pcp 2 dei 0 cos 2 dpl 0
         qos map tag-cos pcp 2 dei 1 cos 2 dpl 1
         qos map tag-cos pcp 3 dei 0 cos 3 dpl 0
         qos map tag-cos pcp 3 dei 1 cos 3 dpl 1
         qos map tag-cos pcp 4 dei 0 cos 4 dpl 0
         qos map tag-cos pcp 4 dei 1 cos 4 dpl 1
         qos map tag-cos pcp 5 dei 0 cos 5 dpl 0
         qos map tag-cos pcp 5 dei 1 cos 5 dpl 1
         qos map tag-cos pcp 6 dei 0 cos 6 dpl 0
         qos map tag-cos pcp 6 dei 1 cos 6 dpl 1
         qos map tag-cos pcp 7 dei 0 cos 7 dpl 0           
         qos map tag-cos pcp 7 dei 1 cos 7 dpl 1
         no qos trust dscp
         no qos policer
         no qos queue-policer queue 0
         no qos queue-policer queue 1
         no qos queue-policer queue 2
         no qos queue-policer queue 3
         no qos queue-policer queue 4
         no qos queue-policer queue 5
         no qos queue-policer queue 6
         no qos queue-policer queue 7
         no qos shaper
         no qos queue-shaper queue 0
         no qos queue-shaper queue 1
         no qos queue-shaper queue 2
         no qos queue-shaper queue 3
         no qos queue-shaper queue 4
         no qos queue-shaper queue 5
         no qos queue-shaper queue 6
         no qos queue-shaper queue 7
         no qos wrr
         no qos tag-remark
         qos map cos-tag cos 0 dpl 0 pcp 1 dei 0           
         qos map cos-tag cos 0 dpl 1 pcp 1 dei 1
         qos map cos-tag cos 1 dpl 0 pcp 0 dei 0
         qos map cos-tag cos 1 dpl 1 pcp 0 dei 1
         qos map cos-tag cos 2 dpl 0 pcp 2 dei 0
         qos map cos-tag cos 2 dpl 1 pcp 2 dei 1
         qos map cos-tag cos 3 dpl 0 pcp 3 dei 0
         qos map cos-tag cos 3 dpl 1 pcp 3 dei 1
         qos map cos-tag cos 4 dpl 0 pcp 4 dei 0
         qos map cos-tag cos 4 dpl 1 pcp 4 dei 1
         qos map cos-tag cos 5 dpl 0 pcp 5 dei 0
         qos map cos-tag cos 5 dpl 1 pcp 5 dei 1
         qos map cos-tag cos 6 dpl 0 pcp 6 dei 0
         qos map cos-tag cos 6 dpl 1 pcp 6 dei 1
         qos map cos-tag cos 7 dpl 0 pcp 7 dei 0
         qos map cos-tag cos 7 dpl 1 pcp 7 dei 1
         no qos dscp-translate
         no qos dscp-classify
         no qos dscp-remark
         qos wred-group 1
         no qos ingress-map
         no qos egress-map
         access-list action permit
         no access-list rate-limiter                       
         access-list policy 0
         no access-list redirect
         no access-list mirror
         no access-list logging
         no access-list shutdown
         no thermal-protect grp
         mac address-table learning
         spanning-tree
         no spanning-tree edge
         spanning-tree auto-edge
         spanning-tree link-type auto
         no spanning-tree restricted-role
         no spanning-tree restricted-tcn
         no spanning-tree bpdu-guard
         spanning-tree mst 0 cost auto
         spanning-tree mst 0 port-priority 128
         spanning-tree mst 1 cost auto
         spanning-tree mst 1 port-priority 128
         spanning-tree mst 2 cost auto
         spanning-tree mst 2 port-priority 128
         spanning-tree mst 3 cost auto
         spanning-tree mst 3 port-priority 128
         spanning-tree mst 4 cost auto                     
         spanning-tree mst 4 port-priority 128
         spanning-tree mst 5 cost auto
         spanning-tree mst 5 port-priority 128
         spanning-tree mst 6 cost auto
         spanning-tree mst 6 port-priority 128
         spanning-tree mst 7 cost auto
         spanning-tree mst 7 port-priority 128
         lacp port-priority 32768
         lacp timeout fast
         media-type rj45
         speed auto 100 1000 2500
         duplex full
         flowcontrol off
         no priority-flowcontrol prio 0-7
         mtu 10240
         no excessive-restart
         no frame-length-check
         no shutdown
         no description
         no green-ethernet energy-detect
         no green-ethernet short-reach
         dot1x port-control force-authorized
         no dot1x guest-vlan                               
         no dot1x radius-vlan
         no dot1x radius-qos
         no dot1x mac-based-fallback
         port-security maximum 4
         port-security maximum-violation 4
         port-security violation protect
         no port-security
         no port-security mac-address sticky
         switchport vlan mapping 7
         no aggregation group
         no gvrp
         mrp timers join-time 20 leave-time 60 leave-all-time 1000
         no mrp periodic
         no mvrp
         no udld port
         no trap mac-change
        !
        interface 2.5GigabitEthernet 1/4
         switchport voice vlan mode disable
         no switchport voice vlan security
         switchport voice vlan discovery-protocol oui
         loop-protect
         no loop-protect action                            
         loop-protect tx-mode
         no loop-protect act-port
         switchport access vlan 1
         switchport trunk native vlan 1
         switchport hybrid native vlan 1
         switchport trunk allowed vlan 1-4094
         switchport hybrid allowed vlan 1-4094
         no switchport trunk vlan tag native
         switchport hybrid acceptable-frame-type all
         no switchport hybrid ingress-filtering
         switchport hybrid egress-tag all except-native
         switchport hybrid port-type c-port
         switchport mode access
         switchport forbidden vlan remove 1-4094
         vcl smacsip
         no pvlan isolation
         pvlan 1
         no mvr immediate-leave
         no ip igmp snooping filter
         no ip igmp snooping max-groups
         no ip igmp snooping mrouter
         no ip igmp snooping immediate-leave
         no ipv6 mld snooping filter                       
         no ipv6 mld snooping max-groups
         no ipv6 mld snooping mrouter
         no ipv6 mld snooping immediate-leave
         ip dhcp snooping trust
         no ipv6 dhcp snooping trust
         ip arp inspection trust
         no ip arp inspection check-vlan
         no ip arp inspection logging
         no ip verify source
         no ip verify source limit
         no ipv6 verify source
         no ipv6 verify source limit
         lldp receive
         lldp transmit
         lldp tlv-select management-address
         lldp tlv-select port-description
         lldp tlv-select system-capabilities
         lldp tlv-select system-name
         lldp tlv-select system-description
         no lldp cdp-aware
         no lldp trap
         lldp med transmit-tlv capabilities network-policy location poe
         no lldp med media-vlan policy-list                
         lldp med type connectivity
         poe mode enable
         poe priority low
         poe lldp
         no poe ping-ip-addr
         no poe startup-time
         no poe interval-time
         no poe ping-retry-time
         no poe failure-action
         no poe reboot-time
         no poe max-reboot-time
         no poe delay-mode
         no poe delay-time
         no poe port-profile
         qos cos 0
         qos pcp 0
         qos dpl 0
         qos dei 0
         qos class 0
         no qos trust tag
         qos map tag-cos pcp 0 dei 0 cos 1 dpl 0
         qos map tag-cos pcp 0 dei 1 cos 1 dpl 1
         qos map tag-cos pcp 1 dei 0 cos 0 dpl 0           
         qos map tag-cos pcp 1 dei 1 cos 0 dpl 1
         qos map tag-cos pcp 2 dei 0 cos 2 dpl 0
         qos map tag-cos pcp 2 dei 1 cos 2 dpl 1
         qos map tag-cos pcp 3 dei 0 cos 3 dpl 0
         qos map tag-cos pcp 3 dei 1 cos 3 dpl 1
         qos map tag-cos pcp 4 dei 0 cos 4 dpl 0
         qos map tag-cos pcp 4 dei 1 cos 4 dpl 1
         qos map tag-cos pcp 5 dei 0 cos 5 dpl 0
         qos map tag-cos pcp 5 dei 1 cos 5 dpl 1
         qos map tag-cos pcp 6 dei 0 cos 6 dpl 0
         qos map tag-cos pcp 6 dei 1 cos 6 dpl 1
         qos map tag-cos pcp 7 dei 0 cos 7 dpl 0
         qos map tag-cos pcp 7 dei 1 cos 7 dpl 1
         no qos trust dscp
         no qos policer
         no qos queue-policer queue 0
         no qos queue-policer queue 1
         no qos queue-policer queue 2
         no qos queue-policer queue 3
         no qos queue-policer queue 4
         no qos queue-policer queue 5
         no qos queue-policer queue 6
         no qos queue-policer queue 7                      
         no qos shaper
         no qos queue-shaper queue 0
         no qos queue-shaper queue 1
         no qos queue-shaper queue 2
         no qos queue-shaper queue 3
         no qos queue-shaper queue 4
         no qos queue-shaper queue 5
         no qos queue-shaper queue 6
         no qos queue-shaper queue 7
         no qos wrr
         no qos tag-remark
         qos map cos-tag cos 0 dpl 0 pcp 1 dei 0
         qos map cos-tag cos 0 dpl 1 pcp 1 dei 1
         qos map cos-tag cos 1 dpl 0 pcp 0 dei 0
         qos map cos-tag cos 1 dpl 1 pcp 0 dei 1
         qos map cos-tag cos 2 dpl 0 pcp 2 dei 0
         qos map cos-tag cos 2 dpl 1 pcp 2 dei 1
         qos map cos-tag cos 3 dpl 0 pcp 3 dei 0
         qos map cos-tag cos 3 dpl 1 pcp 3 dei 1
         qos map cos-tag cos 4 dpl 0 pcp 4 dei 0
         qos map cos-tag cos 4 dpl 1 pcp 4 dei 1
         qos map cos-tag cos 5 dpl 0 pcp 5 dei 0
         qos map cos-tag cos 5 dpl 1 pcp 5 dei 1           
         qos map cos-tag cos 6 dpl 0 pcp 6 dei 0
         qos map cos-tag cos 6 dpl 1 pcp 6 dei 1
         qos map cos-tag cos 7 dpl 0 pcp 7 dei 0
         qos map cos-tag cos 7 dpl 1 pcp 7 dei 1
         no qos dscp-translate
         no qos dscp-classify
         no qos dscp-remark
         qos wred-group 1
         no qos ingress-map
         no qos egress-map
         access-list action permit
         no access-list rate-limiter 
         access-list policy 0
         no access-list redirect
         no access-list mirror
         no access-list logging
         no access-list shutdown
         no thermal-protect grp
         mac address-table learning
         spanning-tree
         no spanning-tree edge
         spanning-tree auto-edge
         spanning-tree link-type auto                      
         no spanning-tree restricted-role
         no spanning-tree restricted-tcn
         no spanning-tree bpdu-guard
         spanning-tree mst 0 cost auto
         spanning-tree mst 0 port-priority 128
         spanning-tree mst 1 cost auto
         spanning-tree mst 1 port-priority 128
         spanning-tree mst 2 cost auto
         spanning-tree mst 2 port-priority 128
         spanning-tree mst 3 cost auto
         spanning-tree mst 3 port-priority 128
         spanning-tree mst 4 cost auto
         spanning-tree mst 4 port-priority 128
         spanning-tree mst 5 cost auto
         spanning-tree mst 5 port-priority 128
         spanning-tree mst 6 cost auto
         spanning-tree mst 6 port-priority 128
         spanning-tree mst 7 cost auto
         spanning-tree mst 7 port-priority 128
         lacp port-priority 32768
         lacp timeout fast
         media-type rj45
         speed auto 100 1000 2500                          
         duplex full
         flowcontrol off
         no priority-flowcontrol prio 0-7
         mtu 10240
         no excessive-restart
         no frame-length-check
         no shutdown
         no description
         no green-ethernet energy-detect
         no green-ethernet short-reach
         dot1x port-control force-authorized
         no dot1x guest-vlan
         no dot1x radius-vlan
         no dot1x radius-qos
         no dot1x mac-based-fallback
         port-security maximum 4
         port-security maximum-violation 4
         port-security violation protect
         no port-security
         no port-security mac-address sticky
         switchport vlan mapping 8
         no aggregation group
         no gvrp                                           
         mrp timers join-time 20 leave-time 60 leave-all-time 1000
         no mrp periodic
         no mvrp
         no udld port
         no trap mac-change
        !
        interface 10GigabitEthernet 1/1
         switchport voice vlan mode disable
         no switchport voice vlan security
         switchport voice vlan discovery-protocol oui
         loop-protect
         no loop-protect action
         loop-protect tx-mode
         no loop-protect act-port
         switchport access vlan 1
         switchport trunk native vlan 1
         switchport hybrid native vlan 1
         switchport trunk allowed vlan 1-4094
         switchport hybrid allowed vlan 1-4094
         no switchport trunk vlan tag native
         switchport hybrid acceptable-frame-type all
         no switchport hybrid ingress-filtering
         switchport hybrid egress-tag all except-native    
         switchport hybrid port-type c-port
         switchport mode access
         switchport forbidden vlan remove 1-4094
         vcl smacsip
         no pvlan isolation
         pvlan 1
         no mvr immediate-leave
         no ip igmp snooping filter
         no ip igmp snooping max-groups
         no ip igmp snooping mrouter
         no ip igmp snooping immediate-leave
         no ipv6 mld snooping filter
         no ipv6 mld snooping max-groups
         no ipv6 mld snooping mrouter
         no ipv6 mld snooping immediate-leave
         ip dhcp snooping trust
         no ipv6 dhcp snooping trust
         ip arp inspection trust
         no ip arp inspection check-vlan
         no ip arp inspection logging
         no ip verify source
         no ip verify source limit
         no ipv6 verify source                             
         no ipv6 verify source limit
         lldp receive
         lldp transmit
         lldp tlv-select management-address
         lldp tlv-select port-description
         lldp tlv-select system-capabilities
         lldp tlv-select system-name
         lldp tlv-select system-description
         no lldp cdp-aware
         no lldp trap
         lldp med transmit-tlv capabilities network-policy location poe
         no lldp med media-vlan policy-list
         lldp med type connectivity
         qos cos 0
         qos pcp 0
         qos dpl 0
         qos dei 0
         qos class 0
         no qos trust tag
         qos map tag-cos pcp 0 dei 0 cos 1 dpl 0
         qos map tag-cos pcp 0 dei 1 cos 1 dpl 1
         qos map tag-cos pcp 1 dei 0 cos 0 dpl 0
         qos map tag-cos pcp 1 dei 1 cos 0 dpl 1           
         qos map tag-cos pcp 2 dei 0 cos 2 dpl 0
         qos map tag-cos pcp 2 dei 1 cos 2 dpl 1
         qos map tag-cos pcp 3 dei 0 cos 3 dpl 0
         qos map tag-cos pcp 3 dei 1 cos 3 dpl 1
         qos map tag-cos pcp 4 dei 0 cos 4 dpl 0
         qos map tag-cos pcp 4 dei 1 cos 4 dpl 1
         qos map tag-cos pcp 5 dei 0 cos 5 dpl 0
         qos map tag-cos pcp 5 dei 1 cos 5 dpl 1
         qos map tag-cos pcp 6 dei 0 cos 6 dpl 0
         qos map tag-cos pcp 6 dei 1 cos 6 dpl 1
         qos map tag-cos pcp 7 dei 0 cos 7 dpl 0
         qos map tag-cos pcp 7 dei 1 cos 7 dpl 1
         no qos trust dscp
         no qos policer
         no qos queue-policer queue 0
         no qos queue-policer queue 1
         no qos queue-policer queue 2
         no qos queue-policer queue 3
         no qos queue-policer queue 4
         no qos queue-policer queue 5
         no qos queue-policer queue 6
         no qos queue-policer queue 7
         no qos shaper                                     
         no qos queue-shaper queue 0
         no qos queue-shaper queue 1
         no qos queue-shaper queue 2
         no qos queue-shaper queue 3
         no qos queue-shaper queue 4
         no qos queue-shaper queue 5
         no qos queue-shaper queue 6
         no qos queue-shaper queue 7
         no qos wrr
         no qos tag-remark
         qos map cos-tag cos 0 dpl 0 pcp 1 dei 0
         qos map cos-tag cos 0 dpl 1 pcp 1 dei 1
         qos map cos-tag cos 1 dpl 0 pcp 0 dei 0
         qos map cos-tag cos 1 dpl 1 pcp 0 dei 1
         qos map cos-tag cos 2 dpl 0 pcp 2 dei 0
         qos map cos-tag cos 2 dpl 1 pcp 2 dei 1
         qos map cos-tag cos 3 dpl 0 pcp 3 dei 0
         qos map cos-tag cos 3 dpl 1 pcp 3 dei 1
         qos map cos-tag cos 4 dpl 0 pcp 4 dei 0
         qos map cos-tag cos 4 dpl 1 pcp 4 dei 1
         qos map cos-tag cos 5 dpl 0 pcp 5 dei 0
         qos map cos-tag cos 5 dpl 1 pcp 5 dei 1
         qos map cos-tag cos 6 dpl 0 pcp 6 dei 0           
         qos map cos-tag cos 6 dpl 1 pcp 6 dei 1
         qos map cos-tag cos 7 dpl 0 pcp 7 dei 0
         qos map cos-tag cos 7 dpl 1 pcp 7 dei 1
         no qos dscp-translate
         no qos dscp-classify
         no qos dscp-remark
         qos wred-group 1
         no qos ingress-map
         no qos egress-map
         access-list action permit
         no access-list rate-limiter 
         access-list policy 0
         no access-list redirect
         no access-list mirror
         no access-list logging
         no access-list shutdown
         no thermal-protect grp
         mac address-table learning
         spanning-tree
         no spanning-tree edge
         spanning-tree auto-edge
         spanning-tree link-type auto
         no spanning-tree restricted-role                  
         no spanning-tree restricted-tcn
         no spanning-tree bpdu-guard
         spanning-tree mst 0 cost auto
         spanning-tree mst 0 port-priority 128
         spanning-tree mst 1 cost auto
         spanning-tree mst 1 port-priority 128
         spanning-tree mst 2 cost auto
         spanning-tree mst 2 port-priority 128
         spanning-tree mst 3 cost auto
         spanning-tree mst 3 port-priority 128
         spanning-tree mst 4 cost auto
         spanning-tree mst 4 port-priority 128
         spanning-tree mst 5 cost auto
         spanning-tree mst 5 port-priority 128
         spanning-tree mst 6 cost auto
         spanning-tree mst 6 port-priority 128
         spanning-tree mst 7 cost auto
         spanning-tree mst 7 port-priority 128
         lacp port-priority 32768
         lacp timeout fast
         media-type sfp
         fec auto
         clause-73 parallel-detect                         
         speed auto
         duplex full
         flowcontrol off
         no priority-flowcontrol prio 0-7
         mtu 10240
         no excessive-restart
         no frame-length-check
         no shutdown
         no description
         dot1x port-control force-authorized
         no dot1x guest-vlan
         no dot1x radius-vlan
         no dot1x radius-qos
         no dot1x mac-based-fallback
         port-security maximum 4
         port-security maximum-violation 4
         port-security violation protect
         no port-security
         no port-security mac-address sticky
         switchport vlan mapping 9
         no aggregation group
         no gvrp
         mrp timers join-time 20 leave-time 60 leave-all-time 1000
         no mrp periodic
         no mvrp
         no udld port
         no trap mac-change
        !
        interface 10GigabitEthernet 1/2
         switchport voice vlan mode disable
         no switchport voice vlan security
         switchport voice vlan discovery-protocol oui
         loop-protect
         no loop-protect action
         loop-protect tx-mode
         no loop-protect act-port
         switchport access vlan 1
         switchport trunk native vlan 1
         switchport hybrid native vlan 1
         switchport trunk allowed vlan 1-4094
         switchport hybrid allowed vlan 1-4094
         no switchport trunk vlan tag native
         switchport hybrid acceptable-frame-type all
         no switchport hybrid ingress-filtering
         switchport hybrid egress-tag all except-native
         switchport hybrid port-type c-port                
         switchport mode access
         switchport forbidden vlan remove 1-4094
         vcl smacsip
         no pvlan isolation
         pvlan 1
         no mvr immediate-leave
         no ip igmp snooping filter
         no ip igmp snooping max-groups
         no ip igmp snooping mrouter
         no ip igmp snooping immediate-leave
         no ipv6 mld snooping filter
         no ipv6 mld snooping max-groups
         no ipv6 mld snooping mrouter
         no ipv6 mld snooping immediate-leave
         ip dhcp snooping trust
         no ipv6 dhcp snooping trust
         ip arp inspection trust
         no ip arp inspection check-vlan
         no ip arp inspection logging
         no ip verify source
         no ip verify source limit
         no ipv6 verify source
         no ipv6 verify source limit                       
         lldp receive
         lldp transmit
         lldp tlv-select management-address
         lldp tlv-select port-description
         lldp tlv-select system-capabilities
         lldp tlv-select system-name
         lldp tlv-select system-description
         no lldp cdp-aware
         no lldp trap
         lldp med transmit-tlv capabilities network-policy location poe
         no lldp med media-vlan policy-list
         lldp med type connectivity
         qos cos 0
         qos pcp 0
         qos dpl 0
         qos dei 0
         qos class 0
         no qos trust tag
         qos map tag-cos pcp 0 dei 0 cos 1 dpl 0
         qos map tag-cos pcp 0 dei 1 cos 1 dpl 1
         qos map tag-cos pcp 1 dei 0 cos 0 dpl 0
         qos map tag-cos pcp 1 dei 1 cos 0 dpl 1
         qos map tag-cos pcp 2 dei 0 cos 2 dpl 0           
         qos map tag-cos pcp 2 dei 1 cos 2 dpl 1
         qos map tag-cos pcp 3 dei 0 cos 3 dpl 0
         qos map tag-cos pcp 3 dei 1 cos 3 dpl 1
         qos map tag-cos pcp 4 dei 0 cos 4 dpl 0
         qos map tag-cos pcp 4 dei 1 cos 4 dpl 1
         qos map tag-cos pcp 5 dei 0 cos 5 dpl 0
         qos map tag-cos pcp 5 dei 1 cos 5 dpl 1
         qos map tag-cos pcp 6 dei 0 cos 6 dpl 0
         qos map tag-cos pcp 6 dei 1 cos 6 dpl 1
         qos map tag-cos pcp 7 dei 0 cos 7 dpl 0
         qos map tag-cos pcp 7 dei 1 cos 7 dpl 1
         no qos trust dscp
         no qos policer
         no qos queue-policer queue 0
         no qos queue-policer queue 1
         no qos queue-policer queue 2
         no qos queue-policer queue 3
         no qos queue-policer queue 4
         no qos queue-policer queue 5
         no qos queue-policer queue 6
         no qos queue-policer queue 7
         no qos shaper
         no qos queue-shaper queue 0                       
         no qos queue-shaper queue 1
         no qos queue-shaper queue 2
         no qos queue-shaper queue 3
         no qos queue-shaper queue 4
         no qos queue-shaper queue 5
         no qos queue-shaper queue 6
         no qos queue-shaper queue 7
         no qos wrr
         no qos tag-remark
         qos map cos-tag cos 0 dpl 0 pcp 1 dei 0
         qos map cos-tag cos 0 dpl 1 pcp 1 dei 1
         qos map cos-tag cos 1 dpl 0 pcp 0 dei 0
         qos map cos-tag cos 1 dpl 1 pcp 0 dei 1
         qos map cos-tag cos 2 dpl 0 pcp 2 dei 0
         qos map cos-tag cos 2 dpl 1 pcp 2 dei 1
         qos map cos-tag cos 3 dpl 0 pcp 3 dei 0
         qos map cos-tag cos 3 dpl 1 pcp 3 dei 1
         qos map cos-tag cos 4 dpl 0 pcp 4 dei 0
         qos map cos-tag cos 4 dpl 1 pcp 4 dei 1
         qos map cos-tag cos 5 dpl 0 pcp 5 dei 0
         qos map cos-tag cos 5 dpl 1 pcp 5 dei 1
         qos map cos-tag cos 6 dpl 0 pcp 6 dei 0
         qos map cos-tag cos 6 dpl 1 pcp 6 dei 1           
         qos map cos-tag cos 7 dpl 0 pcp 7 dei 0
         qos map cos-tag cos 7 dpl 1 pcp 7 dei 1
         no qos dscp-translate
         no qos dscp-classify
         no qos dscp-remark
         qos wred-group 1
         no qos ingress-map
         no qos egress-map
         access-list action permit
         no access-list rate-limiter 
         access-list policy 0
         no access-list redirect
         no access-list mirror
         no access-list logging
         no access-list shutdown
         no thermal-protect grp
         mac address-table learning
         spanning-tree
         no spanning-tree edge
         spanning-tree auto-edge
         spanning-tree link-type auto
         no spanning-tree restricted-role
         no spanning-tree restricted-tcn                   
         no spanning-tree bpdu-guard
         spanning-tree mst 0 cost auto
         spanning-tree mst 0 port-priority 128
         spanning-tree mst 1 cost auto
         spanning-tree mst 1 port-priority 128
         spanning-tree mst 2 cost auto
         spanning-tree mst 2 port-priority 128
         spanning-tree mst 3 cost auto
         spanning-tree mst 3 port-priority 128
         spanning-tree mst 4 cost auto
         spanning-tree mst 4 port-priority 128
         spanning-tree mst 5 cost auto
         spanning-tree mst 5 port-priority 128
         spanning-tree mst 6 cost auto
         spanning-tree mst 6 port-priority 128
         spanning-tree mst 7 cost auto
         spanning-tree mst 7 port-priority 128
         lacp port-priority 32768
         lacp timeout fast
         media-type sfp
         fec auto
         clause-73 parallel-detect
         speed auto                                        
         duplex full
         flowcontrol off
         no priority-flowcontrol prio 0-7
         mtu 10240
         no excessive-restart
         no frame-length-check
         no shutdown
         no description
         dot1x port-control force-authorized
         no dot1x guest-vlan
         no dot1x radius-vlan
         no dot1x radius-qos
         no dot1x mac-based-fallback
         port-security maximum 4
         port-security maximum-violation 4
         port-security violation protect
         no port-security
         no port-security mac-address sticky
         switchport vlan mapping 10
         no aggregation group
         no gvrp
         mrp timers join-time 20 leave-time 60 leave-all-time 1000
         no mrp periodic                                   
         no mvrp
         no udld port
         no trap mac-change
        !
        interface vlan 1
         ip mtu 1500
         ip address dhcp fallback 172.23.56.250 255.255.255.0 timeout 60
         no ipv6 address
         no ipv6 address dhcp
         no ip igmp snooping
         ip igmp snooping querier election
         no ip igmp snooping querier address
         ip igmp snooping compatibility auto
         ip igmp snooping priority 0
         ip igmp snooping robustness-variable 2
         ip igmp snooping query-max-response-time 100
         ip igmp snooping query-interval 125
         ip igmp snooping last-member-query-interval 10
         ip igmp snooping unsolicited-report-interval 1
         no ipv6 mld snooping
         ipv6 mld snooping querier election
         ipv6 mld snooping compatibility auto
         ipv6 mld snooping priority 0                      
         ipv6 mld snooping robustness-variable 2
         ipv6 mld snooping query-max-response-time 100
         ipv6 mld snooping query-interval 125
         ipv6 mld snooping last-member-query-interval 10
         ipv6 mld snooping unsolicited-report-interval 1
         no ip dhcp server
        !
        spanning-tree aggregation
         spanning-tree
         no spanning-tree edge
         spanning-tree auto-edge
         spanning-tree link-type point-to-point
         no spanning-tree restricted-role
         no spanning-tree restricted-tcn
         no spanning-tree bpdu-guard
         spanning-tree mst 0 cost auto
         spanning-tree mst 0 port-priority 128
         spanning-tree mst 1 cost auto
         spanning-tree mst 1 port-priority 128
         spanning-tree mst 2 cost auto
         spanning-tree mst 2 port-priority 128
         spanning-tree mst 3 cost auto
         spanning-tree mst 3 port-priority 128             
         spanning-tree mst 4 cost auto
         spanning-tree mst 4 port-priority 128
         spanning-tree mst 5 cost auto
         spanning-tree mst 5 port-priority 128
         spanning-tree mst 6 cost auto
         spanning-tree mst 6 port-priority 128
         spanning-tree mst 7 cost auto
         spanning-tree mst 7 port-priority 128
        !
        !
        event group Cold-Start level 4
        event group Cold-Start syslog enable
        event group Cold-Start trap disable
        event group Cold-Start smtp disable
        event group Link-Status level 4
        event group Link-Status syslog enable
        event group Link-Status trap disable
        event group Link-Status smtp disable
        event group Login level 6
        event group Login syslog enable
        event group Login trap disable
        event group Login smtp disable
        event group Logout level 6                         
        event group Logout syslog enable
        event group Logout trap disable
        event group Logout smtp disable
        event group Auth-Failed level 4
        event group Auth-Failed syslog enable
        event group Auth-Failed trap disable
        event group Auth-Failed smtp disable
        event group Password-Change level 6
        event group Password-Change syslog enable
        event group Password-Change trap disable
        event group Password-Change smtp disable
        event group Mgmt-IP-Change level 6
        event group Mgmt-IP-Change syslog enable
        event group Mgmt-IP-Change trap disable
        event group Mgmt-IP-Change smtp disable
        event group Module-Change level 4
        event group Module-Change syslog enable
        event group Module-Change trap disable
        event group Module-Change smtp disable
        event group LACP level 6
        event group LACP syslog enable
        event group LACP trap disable
        event group LACP smtp disable                      
        event group NAS level 6
        event group NAS syslog enable
        event group NAS trap disable
        event group NAS smtp disable
        event group Config-Info level 6
        event group Config-Info syslog enable
        event group Config-Info trap disable
        event group Config-Info smtp disable
        event group Firmware-Upgrade level 6
        event group Firmware-Upgrade syslog enable
        event group Firmware-Upgrade trap disable
        event group Firmware-Upgrade smtp disable
        event group Import-Export level 6
        event group Import-Export syslog enable
        event group Import-Export trap disable
        event group Import-Export smtp disable
        event group Port-Security level 6
        event group Port-Security syslog enable
        event group Port-Security trap disable
        event group Port-Security smtp disable
        event group Access-Mgmt level 6
        event group Access-Mgmt syslog enable
        event group Access-Mgmt trap disable               
        event group Access-Mgmt smtp disable
        event group ACL level 6
        event group ACL syslog enable
        event group ACL trap disable
        event group ACL smtp disable
        event group ACL-Log level 6
        event group ACL-Log syslog enable
        event group ACL-Log trap disable
        event group ACL-Log smtp disable
        event group Loop-Protect level 6
        event group Loop-Protect syslog enable
        event group Loop-Protect trap disable
        event group Loop-Protect smtp disable
        event group PoE-Auto-Check level 4
        event group PoE-Auto-Check syslog enable
        event group PoE-Auto-Check trap disable
        event group PoE-Auto-Check smtp disable
        event group PoE-PD-On level 4
        event group PoE-PD-On syslog enable
        event group PoE-PD-On trap disable
        event group PoE-PD-On smtp disable
        event group PoE-PD-Off level 4
        event group PoE-PD-Off syslog enable               
        event group PoE-PD-Off trap disable
        event group PoE-PD-Off smtp disable
        event group Over-Max-PoE-Power-Limitation level 4
        event group Over-Max-PoE-Power-Limitation syslog enable
        event group Over-Max-PoE-Power-Limitation trap disable
        event group Over-Max-PoE-Power-Limitation smtp disable
        event group PoE-PD-Over-Current level 4
        event group PoE-PD-Over-Current syslog enable
        event group PoE-PD-Over-Current trap disable
        event group PoE-PD-Over-Current smtp disable
        event group  level 6
        event group  syslog enable
        event group  trap disable
        event group  smtp disable
        event group  level 6
        event group  syslog enable
        event group  trap disable
        event group  smtp disable
        event group Spanning-Tree level 6
        event group Spanning-Tree syslog enable
        event group Spanning-Tree trap disable
        event group Spanning-Tree smtp disable
        !                                                  
        line console 0
         editing
         exec-banner
         exec-timeout 10 0
         history size 32
         length 24
         motd-banner
         privilege level 2
         width 80
        !
        line vty 0
         editing
         exec-banner
         exec-timeout 10 0
         history size 32
         length 24
         motd-banner
         privilege level 2
         width 80
        !
        line vty 1
         editing
         exec-banner                                       
         exec-timeout 10 0
         history size 32
         length 24
         motd-banner
         privilege level 2
         width 80
        !
        line vty 2
         editing
         exec-banner
         exec-timeout 10 0
         history size 32
         length 24
         motd-banner
         privilege level 2
         width 80
        !
        line vty 3
         editing
         exec-banner
         exec-timeout 10 0
         history size 32
         length 24                                         
         motd-banner
         privilege level 2
         width 80
        !
        line vty 4
         editing
         exec-banner
         exec-timeout 10 0
         history size 32
         length 24
         motd-banner
         privilege level 2
         width 80
        !
        line vty 5
         editing
         exec-banner
         exec-timeout 10 0
         history size 32
         length 24
         motd-banner
         privilege level 2
         width 80                                          
        !
        line vty 6
         editing
         exec-banner
         exec-timeout 10 0
         history size 32
         length 24
         motd-banner
         privilege level 2
         width 80
        !
        line vty 7
         editing
         exec-banner
         exec-timeout 10 0
         history size 32
         length 24
         motd-banner
         privilege level 2
         width 80
        !
        line vty 8
         editing                                           
         exec-banner
         exec-timeout 10 0
         history size 32
         length 24
         motd-banner
         privilege level 2
         width 80
        !
        line vty 9
         editing
         exec-banner
         exec-timeout 10 0
         history size 32
         length 24
         motd-banner
         privilege level 2
         width 80
        !
        line vty 10
         editing
         exec-banner
         exec-timeout 10 0
         history size 32                                   
         length 24
         motd-banner
         privilege level 2
         width 80
        !
        line vty 11
         editing
         exec-banner
         exec-timeout 10 0
         history size 32
         length 24
         motd-banner
         privilege level 2
         width 80
        !
        line vty 12
         editing
         exec-banner
         exec-timeout 10 0
         history size 32
         length 24
         motd-banner
         privilege level 2                                 
         width 80
        !
        line vty 13
         editing
         exec-banner
         exec-timeout 10 0
         history size 32
         length 24
         motd-banner
         privilege level 2
         width 80
        !
        line vty 14
         editing
         exec-banner
         exec-timeout 10 0
         history size 32
         length 24
         motd-banner
         privilege level 2
         width 80
        !
        line vty 15                                        
         editing
         exec-banner
         exec-timeout 10 0
         history size 32
         length 24
         motd-banner
         privilege level 2
         width 80
        !
        supplicant 1 port 
        supplicant 1 username 
        supplicant 1 password 
        nosupplicant 1 mode
        supplicant 2 port 
        supplicant 2 username 
        supplicant 2 password 
        nosupplicant 2 mode
        supplicant 3 port 
        supplicant 3 username 
        supplicant 3 password 
        nosupplicant 3 mode
        supplicant 4 port 
        supplicant 4 username                              
        supplicant 4 password 
        nosupplicant 4 mode
        supplicant 5 port 
        supplicant 5 username 
        supplicant 5 password 
        nosupplicant 5 mode
        supplicant mac-mode port
        supplicant methods all
        nosupplicant mode
        lmc DHCP-Client-Auto-Renew yes
        lmc Configuration-via-DHCP yes
        lmc Config-Notifier yes
        lmc Domain cloud.lancom.de
        no lmc Rollout-Project
        no lmc Rollout-Location
        no lmc Rollout-Role
        no lmc proxy-username
        no lmc proxy-password
        lmc proxy-tunnel no
        no lmc proxy-url
        lmc Operating try
        rollout-agent operating Only-Unconfigured
        automatic-firmware-update Mode check-and-update    
        automatic-firmware-update Version-Policy security-updates-only
        automatic-firmware-update Check-Interval daily
        automatic-firmware-update Base-Url update.lancom-systems.de
        automatic-firmware-update Check-Time-Begin 0
        automatic-firmware-update Check-Time-End 0
        automatic-firmware-update Install-Time-Begin 2
        automatic-firmware-update Install-Time-End 4
        !
        end
        """
