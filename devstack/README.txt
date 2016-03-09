# (C) Copyright Broadcom Corporation 2016
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
#
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

The broadview-collector DevStack plugin currently only works on Ubuntu 14.04 
(Trusty). It may work elsewhere, we just haven't tried :-)

Directions for installing an running Devstack can be found here:

    http://docs.openstack.org/developer/devstack/

To run broadview-collector in DevStack, perform the following steps:

1. Clone the DevStack repo.

    git clone https://git.openstack.org/openstack-dev/devstack

2. Add the following to the end of the DevStack local.conf file in the 
   root of the devstack directory. You may need to create the local.conf if 
   it does not already exist. 

    # The following will enable broadview-collector
    
    enable_plugin broadview-collector git://github.com/openstack/broadview-collector

4.   Run './stack.sh' from the root of the devstack directory.

The default configuration enables the logfile publisher plugin. You can 
view/modify the configuration by editing /etc/broadviewcolector.conf and
then restarting the collector.

Minimal Devstack local.conf
---------------------------

The following minimal local.conf should be all that is needed to bring
up the BroadView Collector:

[[local|localrc]]
MYSQL_PASSWORD=secretmysql
DATABASE_PASSWORD=secretdatabase
RABBIT_PASSWORD=secretrabbit
ADMIN_PASSWORD=secretadmin
SERVICE_PASSWORD=secretservice
SERVICE_TOKEN=111222333444

LOGFILE=$DEST/logs/stack.sh.log
LOGDIR=$DEST/logs
LOG_COLOR=False

disable_all_services
enable_service rabbit mysql key tempest

enable_plugin broadview-collector git://git.openstack.org/openstack/broadview-collector 

Restarting the Collector
------------------------

To restart the collector:

$ sudo service broadview_collector restart

Stopping the Collector
---------------------

To stop the collector:

$ sudo service broadview_collector stop

Starting the Collector
----------------------

To start the collector:

$ sudo service broadview_collector start

Exercising The Collector
------------------------

A simple python script in broadview_collector/tests named bst_report.py can
be used to simulate data incoming from a BroadView agent. Combined with 
configuration that enables the log publisher plugin (or any other plugin
for that matter), you can validate that the installation and configuration
is valid. To run it, edit the script by changing the host and port that 
the collector is listening on:

# Change these to the host and port the collector is listening on

host = "172.16.170.175"
port = 8082

And then run the script:

$ python bst_report

You can then look at the configured plugin publishing targets to validate
that the data was published as expected. The script sends the data to the
collector and looks at the return code to verify the response is 200 (OK).
The Python unittest module is used to validate the return code and determine
a pass or fail status.

Enabling Monasca
----------------

Follow these steps:

1. Follow the instructions for devstack in the Monasca API project. The 
README.txt file in https://github.com/openstack/monasca-api has all the
details.

2. Add the following the end of their local.conf:

enable_plugin broadview-collector git://git.openstack.org/openstack/broadview-collector 

3. Run devstack as usual with ./stack.sh

4. Stop the collector

$ sudo service broadview_collector stop

5. Edit /etc/broadviewcollector.conf and add monascapublisher as a publisher
in the plugins section, e.g.,

[plugins]

# comma separated list of plugin modules

# publishers receive JSON encoded reports and write them somewhere

publishers: logpublisher, monascapublisher


6. Restart the broadview collector:

$ sudo service broadview_collector start

7. Send some metrics using the bst simulator bst_report.py

8. View the metric list in monasca

$ monasca --os-username mini-mon --os-password password metric-list 

You should see some bst statistics in the report that is dislayed.
$ 
