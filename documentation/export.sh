#!/bin/bash

# find the existing hosts
find_existing_hosts() {
    echo Hosts connus :
    grep ros /etc/hosts
}

# picar identity
picar_identity() {
    echo Quelle voiture êtes-vous \(ros1, ros2...\) ? 
    read ros_name
    if grep -q "$ros_name" /etc/hosts; then
        ros_ip="$(grep "$ros_name" /etc/hosts | cut -f 1)"

        picar_master "$ros_name" 
    else
    	echo Entrez l\'adresse ip de "$ros_name" :
    	read new_ros_ip
        add_host "$ros_name" "$new_ros_ip"
        picar_master "$ros_name"
    fi
}

picar_master() {
    echo Quelle voiture est la master \(ros 1, ros2...\)?
    read master_name
    if grep -q "$master_name" /etc/hosts; then
        make_exports "$1" "$master_name"
    else
    	echo Entrez l\'adresse ip de "$master_name" :
    	read new_master_ip
        add_host "$master_name" "$new_master_ip"
        make_exports "$1" "$master_name"
    fi
}

#add a new host
add_host() {
	sudo sed -e "/^$/d; /^#.*/i "$2"\t"$1"\n" /etc/hosts > /etc/temp && mv /etc/temp /etc/hosts
	echo Host ajouté.
}

#make exports
make_exports() {
        #$1 is this picar ; $2 is the master picar
        echo export ROS_MASTER_HOSTNAME=http://"$1":11311/
	if [ "$1" = "$2" ]; then
            #this picar is the master
            echo export ROS_MASTER_URI=http://"$1":11311/
        else
            #the master is another picar
            echo export ROS_MASTER_URI=http://"$2":11311/
       fi
    echo exports done.
}


### main ###
find_existing_hosts
picar_identity
exit 0
