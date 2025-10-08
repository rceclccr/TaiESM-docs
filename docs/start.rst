.. _start:


Introduction
=============

TaiESM1 User's Guide
^^^^^^^^^^^^^^^^^^^^

This guide instructs both novice and experienced users on building and running TaiESM1 for various experiment set ups. The chapters attempt to provide relatively detailed information on how to make, set up, build, run and modify experiments using TaiESM1.


TaiESM1
^^^^^^^^
The TaiESM Earth System Model version 1 (TaiESM1) is an coupled Earth System Model developed by the AC3/RCEC, Academia Sinica. TaiESM1 is based on the Community Earth System Model 1, CESM1 (https://www.cesm.ucar.edu/models/cesm1.2.2), developed and operated at the National Center for Atmospheric Research (NCAR), Boulder, US. 

The NorESM specific development is led by the Norwegian Meteorological Institute and NORCE Norwegian Research Centre AS. Other partners involved are the University of Oslo (UiO), CICERO, Nansen Environmental and Remote Sensing Center (NERSC) and the University of Bergen (UiB). 

TaiESM1 specific additions to CESM1 includes (but is not limited to):
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

- Atmosphere model : TaiAM1 replaces standard CAM

  - Atmospheric chemistry/aerosol module: SNAP (Chen et al., 2013)
  - Atmospheric cloud module: GTS (Shiu et al., 2020)
  - Atmospheric trigger function for deep convection module: TFZM (Wang et al., 2015b)

- Land model : 
  - Parameterization for 3D radiation-topography interation (Lee et al., 2013) 
  
For a short description of the model components, please see :ref:`model-description`

TaiESM1 exists in three versions:
+++++++++++++++++++++++++++++++++

- **TaiESM1**
   
  - 1 degree resolution for all model components
   
- **TaiESM1-LM**
 
  - 2 degree resolution for the atmosphere and land components
  - 1 degree resolution for the ocean and sea-ice components
  
- **TaiESM1-HR**
 
  - 0.25/0.5 degree resolution for the atmosphere and land components
  - 0.1/1.0 degree resolution for the ocean and sea-ice components

   
| TaiESM1 contributes to the 6th phase of the Coupled Model Intercomparison Project (CMIP6):   
| https://www.wcrp-climate.org/wgcm-cmip/wgcm-cmip6   
| 
| Scientific documentation in the GMD – Special issue "The TaiESM Earth System Model: TaiESM":     
| https://gmd.copernicus.org/articles/special_issue20.html
| 
| TaiESM1 Documentation is found here: https://taiesm-docs.readthedocs.io/en/taiesm1/  



References
^^^^^^^^^^
Wang, Y.-C., Hsu, H.-H., Chen, C.-A., Tseng, W.-L., Hsu, P.-C., Lin, C.-W., et al. (2021). Performance of the Taiwan Earth System Model in simulating climate variability compared with observations and CMIP6 model simulations. Journal of Advances in Modeling Earth Systems, 13, e2020MS002353. https://doi.org/10.1029/2020MS002353

Lee, W.-L., Wang, Y.-C., Shiu, C.-J., Tsai, I., Tu, C.-Y., Lan, Y.-Y., Chen, J.-P., Pan, H.-L., and Hsu, H.-H.: Taiwan Earth System Model Version 1: description and evaluation of mean state, Geosci. Model Dev., 13, 3887–3904, https://doi.org/10.5194/gmd-13-3887-2020, 2020.

.. bibliography:: references_taiesm.bib
   :cited:
   :style: unsrt
