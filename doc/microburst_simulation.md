Showing BST Microbursts in Grafana via Simulation
=================================================

This document runs through the steps needed to launch OpenStack Monasca
and broadview-collector, simulate microburst activity incoming from
a broadview agent, and configure grafana 2.6 to display this data as a 
graph. 

What we are aiming for is represented in the following image:

[Grafana displaying BST microburst data](images/microbursts/screen.png)

The steps provided in this document do not require anything other than 
what is provided in the broadview and monasca github repositories, and 
does not require a BroadView-capable switch. The exercise can be completed
as a single node OpenStack cluster with minimal configuration via devstack.

Bringing up OpenStack Monasca and BroadView Collector
-----------------------------------------------------

Follow the steps outlined in https://github.com/openstack/broadview-collector/blob/master/devstack/README.txt to bring up a minimal OpenStack cluster that 
includes Monasca. Grafana is a web-based monitoring UI that is integrated
with Monasca.

Be sure to test out the setup by running: 

    python bst_report.py

You can veify the operation of the broadview-collector and Monasca setup by 
using the monasca command line client to verify that metrics have been 
recorded by the monasca service.

Directions for using the monasca command line client are found in the above
README.txt file.

If you do not see data, check the settings in /etc/broadviewcollector.conf.
Ensure that monasca is configured as described in the README.txt file.

Using grafana
------------- 

To work with grafana, one needs to do two things:

* configure a datasource
* create a dashboard 

Launching grafana
-----------------

First, visit the openstack dashboard, and login. If you used the instructions
that are in the README.txt file to create your local.conf file, the username
will be "admin" and the password will be "secretadmin". 

In the dashboard, open the panel named "Monitoring".  Click on "Monitoring", 
and then "Overview". Then click on the button labeled "Grafana Home". A 
browser tab should appear which will contain the grafana UI, and you should be
logged in.

Creating the Monasca Data Source
--------------------------------

On the left side of the screen you should see a "Dashboards" and "Data Sources".
Click on Data Sources. Then, at the top of the screen, click on "Add new".

Fill out the settings for the data sources as shown in the figure
[Grafana data source](images/microbursts/datasource.png)

Instead of supplying an auth token, you might want to simply click on the
"Keystone Auth" checkbox. However, a bug at the time of writing this 
document existed with this setting. To obtain an auth token, run the
following coomand:

    curl -s -X POST http://localhost:5000/v2.0/tokens -d '{"auth": {"passwordCredentials": {"username":"mini-mon", "password":"password"}, "tenantName":"mini-mon"}}' -H "Content-type: application/json"

The above will generate output that contains a token, a portion of which is
shown below:

    {"access": {"token": {"issued_at": "2016-04-11T23:24:32.658304Z", "expires": "2016-04-12T00:24:32Z", "id": "7e5ac6a6c2d94b8aac870a32af125059", "tenant": {"description": null, "enabled": true, "id": "fb12e3d3fc534ebaa1aba7c73b573fce", "name": "mini-mon"}, "audit_ids": ["tq_3-j68SPOGZ06zVfhuww"]}, "serviceCatalog": [{"endpoints": [{"adminURL": "http://10.14.244.207:8774/v2.1/fb12e3d3fc534ebaa1aba7c7

Here, the token is the "id" field (7e5ac6a6c2d94b8aac870a32af125059). Copy and
paste this value into the Token text field.

The Url field corresponds to the IP address and port that the Monasca API is
listening on. Make sure to change the IP address, and if necessary, the port.

Use the "Test Connection" button to verify the data source is properly 
configured, and then click on Save.

Starting the Simulator
----------------------

At this point, it will be good to start the simulator to generate simulated
microburst activity. Go to where broadview-collector has been cloned from
github by devstack (likely /opt/broadview-collector), or clone it yourself.
Then, cd into broadview-collector/broadview_collector/tools. Edit the script
bst_burst.py to set the host and port variables to the IP address and port that
the collector is running on, then run the following in a bash window:

    $ while true; do sleep 90; python bst_burst.py; done

This will get data flowing into the collector and then into the monasca API. 

Creating a Dashboard
--------------------

A dashboard is where you display graphics or tables of metrics that are
available in a selected datasource. The Monasca plugin, in association with
grafana, will automatically determine the set of metrics available in the
datasource for display, and provide UI that allows you to drill down on
metrics based on name, dimensions, and other search criteria. The best way
to experiment is perhaps to create a graph dashboard, then add panels,
using the UI to add queries to the panel for each data you wish to view.

To get started, click on Dashboards, then click on the button labeled 
"Home" in the upper left corner. A dialog will display, with three buttons
at the botton. Click on the one labeled "+New". A green bar will display,
click on it and a pullright menu will display. From this menu, select
"Add Panel->Graph".  A graph will display, and below it will be an editor
which you can use to add queries. Each of the queries will be displayed 
in the graph.

In the righthand side of the editor will be a button labeled "Grafana"
This button is used to select a datasource. Click on the button and
select "broadview bst", which is the datasource we created above. See
the screenshot below.

[Grafana Dashboard Editor](images/microbursts/dashboard.png)

Using the editor, set Function to "none", select "broadview.bst.device" as
the Metric, and set the Group By Time text field to 5000. 

Then, click on the "+Query" button, and add a second stat by doing the 
following:

* set Function to "none", 
* Metric to "broadview.bst.egress-cpu-queue", and
* Group By Time to 5000. 

In the Dimensions section, configure the following query 
"stat=cpu-buffer-count". The screen should look something like the
following (depending on what data has been transmitted to the collector):

[Grafana Showing Data](images/microbursts/data.png)

To make the graphic update frequently, use the controls that are in the
upper right hand corner of the grafana dashboard viewer. They can be used
to set the viewing window (e.g., last 6 hours, last 30 minutes) and the
refresh frequency (10 seconds, 1 minute, etc.)
