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

# BroadView Collector DevStack plugin
#
# Install and start BroadView Collector service in devstack
#
# To enable broadview-collector in devstack add an entry to local.conf that
# looks like
#
# [[local|localrc]]
# enable_plugin broadview-collector git://github.com/openstack/broadview-collector
#

# Save trace setting
XTRACE=$(set +o | grep xtrace)
set -o xtrace

ERREXIT=$(set +o | grep errexit)
set -o errexit

# Determine if we are running in devstack-gate or devstack.
if [[ $DEST ]]; then

    # We are running in devstack-gate.
    export BROADVIEW_COLLECTOR_BASE=${BROADVIEW_COLLECTOR_BASE:-"${DEST}"}

else

    # We are running in devstack.
    export BROADVIEW_COLLECTOR_BASE=${BROADVIEW_COLLECTOR_BASE:-"/opt/stack"}

fi

function pre_install_broadview_collector {
:
}

function install_broadview_collector {

    install_broadview_collector_env

    install_git

    install_broadview_lib

    install_broadview_collector_python
}

function post_config_broadview_collector {
:
}

function unstack_broadview_collector {
    sudo service broadview_collector stop || true
}

function clean_broadview_collector {

    set +o errexit

    unstack_broadview_collector

# XXX this comnes later...
#    if is_service_enabled horizon; then
#
#        clean_broadview_horizon_ui
#
#    fi

    clean_broadview_collector_python

    clean_broadview_lib

    clean_broadview_collector_env

    #Restore errexit
    set -o errexit
}

function install_broadview_collector_env {

    echo_summary "Install BroadView Collector Virtual Environment"

    sudo groupadd --system broadview_collector || true

    sudo mkdir -p /opt/broadview-collector || true

    sudo chown $STACK_USER:broadview_collector /opt/broadview-collector
}

function clean_broadview_collector_env {

    echo_summary "Clean BroadView Collector Virtual Environment"

    sudo rm -rf /opt/broadview-collector

    sudo groupdel broadview_collector

}

function install_git {

    echo_summary "Install git"

    sudo apt-get -y install git

}

function install_broadview_lib {

    echo_summary "Install broadview_lib"

    if [[ ! -d /opt/broadview-lib ]]; then

        sudo git clone https://git.openstack.org/openstack/broadview-lib.git /opt/broadview-lib

    fi

    (cd /opt/broadview-lib; sudo python setup.py sdist)

    BROADVIEW_LIB_SRC_DIST=$(ls -td /opt/broadview-lib/dist/broadview-lib-*.tar.gz)

    pip_install $BROADVIEW_LIB_SRC_DIST
}

function clean_broadview_lib {
    echo_summary "Clean broadview_lib"
}

function install_broadview_collector_python {

    echo_summary "Install broadview_collector_python"

    sudo mkdir -p /opt/broadview-collector/bin

    sudo chown $STACK_USER:broadview_collector /opt/broadview-collector
    sudo chown $STACK_USER:broadview_collector /opt/broadview-collector/bin

    (cd "${BROADVIEW_COLLECTOR_BASE}"/broadview-collector; sudo python setup.py install)

    sudo cp -f "${BROADVIEW_COLLECTOR_BASE}"/broadview-collector/broadview_collector/bin/bvcollect.py /opt/broadview-collector/bin

    sudo chown root:broadview_collector /opt/broadview-collector/bin/bvcollect.py
    sudo chmod 755 /opt/broadview-collector/bin/bvcollect.py

    sudo cp -f "${BROADVIEW_COLLECTOR_BASE}"/broadview-collector/devstack/files/broadview-collector/broadview_collector.conf /etc/init/broadview_collector.conf

    sudo chown root:broadview_collector /etc/init/broadview_collector.conf

    sudo chmod 0755 /etc/init/broadview_collector.conf

    sudo mkdir -p /var/log/broadview-collector || true

    sudo chown root:broadview_collector /var/log/broadview-collector

    sudo chmod 0755 /var/log/broadview-collector

    sudo cp -f "${BROADVIEW_COLLECTOR_BASE}"/broadview-collector/broadview_collector/config/broadviewcollector.conf /etc/broadviewcollector.conf

    sudo chown root:broadview_collector /etc/broadviewcollector.conf

    sudo chmod 0755 /etc/broadviewcollector.conf

    if [[ ${SERVICE_HOST} ]]; then

        sudo sed -i "s/127\.0\.0\.1/${SERVICE_HOST}/g" /etc/broadviewcollector.conf
    fi

    if [[ ${SERVICE_HOST} ]]; then

        # set broadview_collector server listening ip address
        sudo sed -i "s/host = 127\.0\.0\.1/host = ${SERVICE_HOST}/g" /etc/broadviewcollector.conf

    fi

    sudo start broadview_collector || sudo restart broadview_collector
}

function clean_broadview_collector_python {

    echo_summary "Clean broadview_collector_python"

    sudo rm /etc/init/broadview_collector.conf

    sudo rm /etc/broadviewcollector.conf

    sudo rm -rf /var/log/broadview-collector

    sudo rm /var/log/upstart/broadview_collector.log*

    sudo rm -rf /opt/broadview-collector

}


function install_broadview_collector_horizon_ui {

    echo_summary "Install BroadView Collector Horizon UI"

    sudo mkdir -p /opt/broadview_collector-horizon-ui || true

    sudo chown $STACK_USER:broadview_collector /opt/broadview_collector-horizon-ui

    (cd /opt/broadview_collector-horizon-ui ; virtualenv .)

    (cd /opt/broadview_collector-horizon-ui ; sudo -H ./bin/pip install broadview_collector-ui)

    sudo ln -sf /opt/broadview_collector-horizon-ui/lib/python2.7/site-packages/monitoring/enabled/_50_admin_add_monitoring_panel.py "${BROADVIEW_COLLECTOR_BASE}"/horizon/openstack_dashboard/local/enabled/_50_admin_add_monitoring_panel.py

    sudo ln -sf /opt/broadview_collector-horizon-ui/lib/python2.7/site-packages/monitoring/static/monitoring "${BROADVIEW_COLLECTOR_BASE}"/horizon/monitoring

    sudo PYTHONPATH=/opt/broadview_collector-horizon-ui/lib/python2.7/site-packages python "${BROADVIEW_COLLECTOR_BASE}"/horizon/manage.py compress --force

    sudo service apache2 restart

}

function extra_broadview_collector {
:
}

function clean_broadview_collector_horizon_ui {

    echo_summary "Clean BroadView Collector Horizon UI"

    sudo rm -f "${BROADVIEW_COLLECTOR_BASE}"/horizon/openstack_dashboard/local/enabled/_50_admin_add_monitoring_panel.py

    sudo rm -f "${BROADVIEW_COLLECTOR_BASE}"/horizon/monitoring

    sudo rm -rf /opt/broadview_collector-horizon-ui

}

# Allows this script to be called directly outside of
# the devstack infrastructure code. Uncomment to use.
#if [[ $(type -t is_service_enabled) != 'function' ]]; then
#
#    function is_service_enabled {
#
#        return 0
#
#     }
#fi
#if [[ $(type -t echo_summary) != 'function' ]]; then
#
#    function echo_summary {
#
#        echo "$*"
#
#    }
#
#fi

# check for service enabled
if is_service_enabled broadview-collector; then

    if [[ "$1" == "stack" && "$2" == "pre-install" ]]; then
        # Set up system services
        echo_summary "Configuring BroadView Collector system services"
        pre_install_broadview_collector

    elif [[ "$1" == "stack" && "$2" == "install" ]]; then
        # Perform installation of service source
        echo_summary "Installing BroadView Collector"
        install_broadview_collector

    elif [[ "$1" == "stack" && "$2" == "post-config" ]]; then
        # Configure after the other layer 1 and 2 services have been configured
        echo_summary "Configuring BroadView Collector"
        post_config_broadview_collector

    elif [[ "$1" == "stack" && "$2" == "extra" ]]; then
        # Initialize and start the BroadView Collector service
        echo_summary "Initializing BroadView Collector"
        extra_broadview_collector
    fi

    if [[ "$1" == "unstack" ]]; then
        # Shut down BroadView Collector services
        echo_summary "Unstacking BroadView Collector"
        unstack_broadview_collector
    fi

    if [[ "$1" == "clean" ]]; then
        # Remove state and transient data
        # Remember clean.sh first calls unstack.sh
        echo_summary "Cleaning BroadView Collector"
        clean_broadview_collector
    fi
fi

#Restore errexit
$ERREXIT

# Restore xtrace
$XTRACE
