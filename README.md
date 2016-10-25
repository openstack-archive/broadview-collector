Note
====

This repo supports versions of BroadView up to, but not including, version
3 of the agent protocol. For all later versions of BroadView, please visit
https://github.com/Broadcom-Switch/broadview-collector.

# Overview

`broadview-collector` is a service capable of receiving and publishing 
BroadView data received from a network device that is running Broadcom's 
BroadView agent. It is built on top of
[broadview-lib](https://github.com/openstack/broadview-lib/tree/master/broadview_lib).
broadview-collector is designed to support multiple metrics-gathering 
infrastructures via a plugin architecture.

## Publisher Plugins

broadview-collector is designed to accept plugins that are capable of
publishing BroadView data received by the collector to metric-collecting 
services such as OpenStack Monasca. These plugins are in the 
form of Python classes. These classes inherit from a base class that
defines the interface the collector will invoke when data is received
from the BroadView agent.

A serializer takes BroadView data and converts it into a playload that
is suitable for a given publisher plugin.

Data coming into the collector from a BroadView agent is passed to a
list of handlers. Each handler is designed to convert the payload 
that was received by the agent into an object form (currently, only BST 
data is supported, but handlers for additional BroadView components will 
be developed). This object form is canonical in the sense that it is
independent of any publisher plugin.

Once the payload is in an object form, a list of publisher plugins is
iterated. Each publisher is given a chance to serialize the data (it 
does this by instantiating a serializer object, described below). If
the serialization is successful, then the publisher plugin will write
the data to the service that it directly supports.  

## Creating Publisher Plugins

Publisher plugins are simply python source files that exist in the directory
broadview_collector/plugins. A single class inheriting BroadViewPublisherBase
is implemented in this file. This base class defines a single method, 
publish(), which accepts a data object from the collector. The plugin
must provide an override to this method.

Addition directories can be configured to hold plugins. These directories,
if configured, will be searched for plugins at startup in addition to
broadview_collector/plugins. See the documentation on the searchpath config
variable in /etc/broadviewcollector.conf, below, for details and an 
example. 

The name of the class implemented by the plugin must be BroadViewPlublisher.

The set of plugins used at runtime is defined in configuration, and only 
configured plugins will be invoked by the collector. Simply placing a 
python source file in the plugins directory will not cause it to be 
recognized by broadview-collector. Further details on configuration is 
provided below.

The job of the publish() method is to (optionally) call a serializer to 
convert the data into payload (e.g., JSON) understandable to the service
that the publisher plugin targets, and to publish the data using whatever
API that the target service provides for doing so.

Two example publishers are provided:

* monascapublisher: targets the OpenStack Monasca Python metric publishing API
* logpublisher: appends data to a configured text file

For a complete list of publishers, look in the broadview_collector/plugins 
directory.

To use a publisher, it must be added to the comma-separated list of publishers
listed in /etc/broadviewcollector.conf, and the collector must be restarted. 

## Serializers

Serializers are python source files that are located in the directory
broadview_collector/serializers. The broadview-collector is not directly 
aware of these serializers, nor are they required to be configured in order 
to be used. They are aggregated in the serializers directory simply to make
them available for whatever plugins wish to use (or not use) them.

A serializer should inherit from BroadViewSerializerBase. The intent is to 
promote a uniform API among the serializers. If the target of a
publisher plugin requires a new serializer be written, consider creating a 
serializer that inherits BroadViewSerializerBase and locating it in the 
serializers directory so that it might be of use to developers of other 
publisher plugins.

The monasca and log publishers both use the BSTToMonasca serializer located 
in serializers/bst_to_monasca.py to illustrate this concept of reuse. If you 
don't like the format of the messages that are written by an existing 
publisher, you can write your own serializer (if one of the existing ones 
does not fit your needs) and hack the publisher to import and use it instead.

## Handlers

A handler is designed to take traffic incoming to the collector, parse it,
and return an object (of some type) that represents the parsed data. The
returned  object (or list of objects perhaps) is then sent to each registered
publisher. 

Handlers map to BroadView components. Handlers, like publisher plugins and
serializers, inherit a base class, in this case BroadViewHandlerBase. This
class, and the handlers themselves, are located in 
broadview_collector/handlers. 

Handlers directly correspond to BroadView components that are supported in
broadview-lib. See https://github.com/openstack/broadview-lib for more 
information on the BroadView components supported by broadview-lib.

To use a handler, it must be listed in the comma-separated list of handlers
in /etc/broadviewcollector.conf, and it must be located in the handlers 
directory. 

The name of the handler class must be BroadViewHandler. 

See broadview_collector/handlers/bsthandler.py for an example. Handlers have 
a tight coupling to parsers provided in broadview-lib, and normally they will 
be added (or updated) as parsers are added (or updated) in the broadview-lib 
project.

# Installing BroadView Collector

## Basic Installation and Configuration<a name="basicinstall">

Installation requires the following steps:

1. Install OpenStack, including the services to which you intend to publish
data to. We discuss below Monasca-based publishing in more detail. Steps for
other services are currently not supported, but will be similar in scope.
Your OpenStack vendor/supplier may have installation instructions specific to 
products that they support, contact your supplier for more details.

2. Install broadview-lib:

    $ git clone https://github.com/openstack/broadview-lib.git
    $ cd broadview-lib
    $ python setup.py install

3. Install broadview-collector

    $ git clone https://github.com/openstack/broadview-collector.git
    $ cd broadview-collector
    $ python setup.py install

4. Copy the file broadview_collector/config/broadviewcollector.conf to /etc

    $ sudo cp broadview_collector/config/broadviewcollector.conf /etc

5. Edit /etc/broadviewcollector.conf as needed

    $ sudo vi /etc/broadviewcollector.conf

6. Copy broadview collector application to /usr/local/bin:

    $ sudo cp broadview_collector/bin/bvcollect.py /usr/local/bin
    $ sudo chmod 755 /usr/local/bin/bvcollect.py

7. Start the collector (assuming /usr/local/bin is in your PATH):

    $ bvcollect.py &

In addition, you must configure the broadview agent. This involves two
steps: editing the device configuration so that the agent knows the IP
address and port where the collector is listening, and configuring the
agent to publish desired statistics.

To configure the agent, refer to instructions provided by your vendor.
The IP address and port of the collector is in the [network] section of
/etc/broadviewcollector.conf, for example:

    [network]

    ip_address: 10.14.244.143
    port: 8082

Once the agent is up and running on the networking device, you can use 
bv-bstctl.py (included in broadview-lib) to configure BST.

## Detailed Installation: Monasca API

This section details how to set up and configure a devstack-based install
of broadview-collector that publishes to Monasca API.

The following assumes you are on a host running Ubuntu 14.04. Later versions
of Ubuntu may work, but as of this writing, are not tested or supported.

1. Follow the directions for bringing up Monasca with devstack which are
located here:
https://github.com/openstack/monasca-api/blob/master/devstack/README.txt

If you already have OpenStack and Monasca working, then you probably can
skip the above step.

2. Follow the instructions above in [Basic Installation and
Configuration](#basicinstall)

3. Add monascapublisher to the list of publishers in
/etc/broadviewcollector.conf

4. Add a section, [monasca], to /etc/broadviewcollector.conf, as in the
following:

    [monasca]

    username: mini-mon
    password: password
    project_name: mini-mon
    auth_url: http://10.14.245.57:35357/v3
    endpoint: http://10.14.245.57:8070/v2.0
    api_version: 2_0

A /etc/broadviewcollector.conf known to work with monasca-api devstack looks 
like the following (you'll need to change the IP addresses to match the one 
of your host system):

    [plugins]

    # comma separated list of plugin modules

    publishers: monascapublisher, logpublisher

    # handlers map to broadview components, e.g., bst, packet trace

    handlers: bsthandler

    [logging]

    # this section sets prefs for the logging handler.

    file: /tmp/broadview-bstlogging.log

    [network]

    ip_address: 10.14.245.57
    port: 8082

    [monasca]

    username: mini-mon
    password: password
    project_name: mini-mon
    auth_url: http://10.14.245.57:35357/v3
    endpoint: http://10.14.245.57:8070/v2.0
    api_version: 2_0

# Configuration File Syntax

This section describes the syntax of the configuration file 
/etc/broadviewcollector.conf. 

## [DEFAULT]

The [DEFAULT] section defines logging parameters. Refer to the example
in config/broadviewcollector.conf for details. Logs in the default
configuration are written to the file
/var/log/broadview-collector/broadview-collector.log

## [plugins]

The [plugins] section supports the following settings related to publisher
plugins:

### publishers

publishers is a list of comma-separated python modules that are located in
the plugins directory, or the plugins searchpath (see searchpath, below). 

Example:

publishers: monascapublisher, logpublisher, syslogpublisher

### searchpath

searchpath is a comma-separated list of prefixes that are preprended to the
publisher names when the collector attempts to load plugins.

A search order is defined by the order of items in this comma-separated list.
The "plugins" directory associated with broadview-collector is searched 
last. Each plugin is searched for in each directory, in order. If the plugin
is successfully loaded using an entry in the search path, the search ceases.
Otherwise, the search will continue in the next directory defined in the 
search path.

Note: the python searchpath (e.g., PYTHONPATH) is not modified by the value
of this variable. 

Items in the searchpath must be for the form a.b.c 

Example:

searchpath: tmp, home.broadview.plugins

## [misc]

### handlers

The handlers setting is a list of handlers of broadview payload sent by an
agent. This setting generally is defined to reflect the capabilities of 
broadview-lib. If you are only interested in a subset of the functions that
BroadView supports, reducing the list of handlers to contain only those 
BroadView components you are interested in can increase the performance of
the collector, and reduce the burden on your metric collection/analytics
pipeline. Items in this setting are comma-separated.

Example:

handlers: bsthandler 

## [logging]

This section supports the logpublisher publisher plugin.

### file

This setting is the absolute path of the logfile written by the publisher
plugin

Example:

file: /tmp/broadview-bstlogging.log

## [network]

This section contains the networking configuration of the collector

### ip_address

The IP address (IPV4) that the collector will listen for connections on

Example:

ip_address: 10.14.245.57

### port

The port that the collector will listen for connections on

Example:

port: 8082

## [monasca]

This section supports the monascapublisher publisher plugin. These settings
are passed by the monasca publisher as arguments to the monasca python client
constructor. An example of how a python app creates a client object:

    from monascaclient import client
    import monascaclient.exc as exc

    api_version = '2_0'
    endpoint = 'http://192.168.10.4:8080/v2.0'

    auth_kwargs = {'username': 'mini-mon',
                   'password': 'password',
                   'project_name': 'mini-mon',
                   'auth_url': 'http://192.168.10.5:35357/v3/'}
    monasca_client = client.Client(api_version, endpoint, **auth_kwargs)

The settings in this section directory correspond (in name and purpose) with
the arguments pass to the Client constructor above.

### username

The username to authenticate

Example:

username: mini-mon

### password

The password associated with the user being authenticated

Example:

password: password

### project_name

The project name for which the above user is authenticated 

Example:

project_name: mini-mon

### auth_url

The URL of the authentication service (keystone)

example:

auth_url: http://10.14.245.57:35357/v3

### endpoint

The URL that defines where monasca API is running

Example:

endpoint: http://10.14.245.57:8070/v2.0

### api_version

The version of the Monasca API

Example:

api_version: 2_0

## DevStack Support

Devstack support is provided by the files located in the directory
broadview_controller/devstack. Devstack is probably the easiest way
to experiment with BroadView Collector. 

Refer to the README.txt file in broadview_controller/devstack for 
details on how to setup a devstack-based environment for executing
BroadView Collector.

# License

(C) Copyright Broadcom Corporation 2016

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.

You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


