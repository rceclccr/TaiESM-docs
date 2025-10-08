.. _newbie:

Newbies guide to running TaiESM
================================                               

The purpose of this page is to be able to set up and run the model
within 10 minutes.

This guide assumes that you have properly checked out the model to some
directory which will call $TAIESM_PATH. This directory will contain
subdirectories "models" and "scripts".

Go to scripts directory
~~~~~~~~~~~~~~~~~~~~~~

::

  cd $TAIESM_PATH/scripts

Create the case
~~~~~~~~~~~~~~

:: 

  ./create_newcase -case /${case_path}/${casename}/ -mach ${machinename} -res f09_g16 -compset compsetname

(where casename, machinename and compsetname are user input.
Res is imodel resolution. The user can *not* give any resolution since
input data are not prepared for any resolution in NorESM.)

To see a list of available composets type

::

  ./create_newcase -list

The simplest case which runs production for fully coupled and amip-type only 

::

  ./create_newcase -case /path/to/where/I/store/the/case -compset B_1850_TAI -mach f1 -res f09_g16

or

::

  ./create_newcase -case /path/to/where/I/store/the/case -compset F_2000_TAI -mach f1 -res f09_f09

Configure the case
~~~~~~~~~~~~~~~~~

:: 

  cd $WORKDIR//casename

edit any configuration files (understand env_conf.xml and env_run.xml)

:: 

  ./configure -case (in NorESM1 / CAM4)


After these two commands, the case is configured

Build the case
~~~~~~~~~~~~~

::

  ./${casename}.build 


Run the case
~~~~~~~~~~~

::

  ./${casename}.submit

Example
~~~~~~


There are already several pre-defined compsets. They all have long and
short names. As and example we can use the compset B_2000_TAI
(with short name N2000AERCN). Thus a valid command on the machine
*hexagon* is:

::

  ./create_newcase -case /path/to/my/case/directory/ -mach f1 -res f09_g16 -compset B_2000_TAI

(will run a "year 2000" TaiESM1 case with the AMIP-type)

:: 

  ./create_newcase -case /path/to/my/case/directory/ -mach f1 -res f19_g16 -compset F_2000_TAI 

(will configure the "default" atmoshere-only simulation of CAM5)

Important files
~~~~~~~~~~~~~~

The most important files to understand in your case-directory are:


- env_run.xml (model run type, how long time to run etc)

