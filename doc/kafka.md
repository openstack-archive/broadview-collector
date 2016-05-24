Using the kafka plugin
======================

This document runs through the steps needed to configure and test out the 
kafka plugin for BroadView Collector.

Enabling the kafka plugin
-------------------------

The kafka plugin is located in broadview_collector/plugins/kafkapublisher.py. 
In the plugin constructor (__init__), the following defaults related to the
kafka message bus are assigned:

* ip address of kafka - 127.0.0.1
* port - 9092
* topic - broadview-bst

You can override any or all of these settings in /etc/broadviewcollector.conf 
in the [kafka] section of the file. The checked in version of this file in
github has these settings commented out. To enable them, uncomment the
[kafka] section and the settings that you would like to override, and give
appropriate values. The following example configures the IP address, port
and topic and will override the default settings of the plugin:

    [kafka]

    # ip address, port, and topic for kafka

    ip_address: 192.168.0.120
    port: 8088
    topic: broadview-bst

You'll also need to enable the kafka plugin in /etc/broadviewcollector.conf.
To do this, add the string "kafkapublisher" (no quotes) to the publishers 
setting in the [plugins] section. The following example enables both the 
log publisher and the kafka publisher plugins:

    [plugins]
    publishers: logpublisher, kafkapublisher

Testing the Kafka Publisher Plugin
----------------------------------

To test out, or experiment with, the kafka publisher plugin, consider doing
the following:

* Install broadview-collector. See the instructions in the main README.md
* Configure the collector for kafka as described above.
* Install kafka. There are tutorials on the web for this. One that is known
to work for Ubuntu 14.04 can be found at DigitalOcean's website:

 https://www.digitalocean.com/community/tutorials/how-to-install-apache-kafka-on-ubuntu-14-04

* Start up the collector, and then launch kafka from a terminal window. If you
are using the DigitalOcean kafka tutorial: 

    $ nohup ~/kafka/bin/kafka-server-start.sh ~/kafka/config/server.properties > ~/kafka/kafka.log 2>&1 &

* In a separate terminal window, run the following to view the data that is
being written to the kafka queue by BroadView Collector:

    $ ~/kafka/bin/kafka-console-consumer --zookeeper 127.0.0.1:2181 --topic broadview.bst 

Note in the above, the path to kafka-console-consumber may be different based
on how you installed kafka. The IP address and port should work if you 
installed everything on a single host, and zookeeper is configured to use the 
default listen port of 2181. On Ubuntu 14.04, the settings can be found in
/etc/zookeeper/zooinspector/defaultConnectionSettings.cfg in the "hosts"
setting.

* Run the BST burst simulator. Instructions for this are provided in the next
section. 

Starting the Simulator
----------------------

To start the bst simulator, go to where broadview-collector was cloned from
github. Then, cd into broadview-collector/broadview_collector/tools. Edit the 
script bst_burst.py to set the host and port variables to the IP address and 
port that the collector is running on, then run the following in a bash window:

    $ while true; do sleep 90; python bst_burst.py; done

This will get data flowing into the collector and then into the configured 
plugin.

If everything is working, you should see output like the following displayed 
from kafka-console-consumer:

    {"timestamp": 1464032262000.0, "name": "broadview.bst.ingress-port-priority-group", "value": 15, "dimensions": {"asic-id": "20", "stat": "um-share-buffer-count", "priority-group": 5, "port": "2", "bv-agent": "192.168.0.120"}}
    {"timestamp": 1464032262000.0, "name": "broadview.bst.ingress-port-priority-group", "value": 15, "dimensions": {"asic-id": "20", "stat": "um-headroom-buffer-count", "priority-group": 5, "port": "2", "bv-agent": "192.168.0.120"}}
    {"timestamp": 1464032262000.0, "name": "broadview.bst.ingress-port-priority-group", "value": 15, "dimensions": {"asic-id": "20", "stat": "um-share-buffer-count", "priority-group": 6, "port": "3", "bv-agent": "192.168.0.120"}}
    {"timestamp": 1464032262000.0, "name": "broadview.bst.ingress-port-priority-group", "value": 15, "dimensions": {"asic-id": "20", "stat": "um-headroom-buffer-count", "priority-group": 6, "port": "3", "bv-agent": "192.168.0.120"}}
    {"timestamp": 1464032262000.0, "name": "broadview.bst.ingress-port-service-pool", "value": 15, "dimensions": {"asic-id": "20", "stat": "um-share-buffer-count", "service-pool": 5, "port": "2", "bv-agent": "192.168.0.120"}}
    {"timestamp": 1464032262000.0, "name": "broadview.bst.ingress-port-service-pool", "value": 15, "dimensions": {"asic-id": "20", "stat": "um-share-buffer-count", "service-pool": 6, "port": "3", "bv-agent": "192.168.0.120"}}
    {"timestamp": 1464032262000.0, "name": "broadview.bst.ingress-service-pool", "value": 15, "dimensions": {"asic-id": "20", "stat": "um-share-buffer-count", "service-pool": 1, "bv-agent": "192.168.0.120"}}

Congratulations - you've properly installed and configured the BroadView
Collector to accept BST data from an agent, and publish it to kafka.

