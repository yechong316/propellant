# -*- coding: utf-8 -*-
#!/usr/bin/python3
# propellant 
# Authorn:Jaime Lannister
# Time:2019/3/7-0:37 
1.23e-06,235000,0.33,0.00043,826,0.00143,5,
1.23e-06,0.384, 0.3, 1,      1219,0.000326,5,
0.00785, 200000,0.3, 1.6578, 512,1.22e-05,3,
1.65e-06,4000,  0.3 ,0.001,  1500,0.0001263,5,
part_var(
    filepath_c=r'D:\Temp\abaqus_plugins\propellant\propellent_06_CAD\composite.sat',
    filepath_b=r'D:\Temp\abaqus_plugins\propellant\propellent_06_CAD\bfc.sat',
    filepath_f=r'D:\Temp\abaqus_plugins\propellant\propellent_06_CAD\fengtou.sat',
    filepath_h=r'D:\Temp\abaqus_plugins\propellant\propellent_06_CAD\propeller.sat',
desity_c =1.23e-06, Elastic_c = 235000, Poisson_c = 0.33,Conductivity_c = 0.00043, SpecificHeat_c =826, Expansion_c = 0.00143, size_c = 5,
desity_b =1.23e-06, Elastic_b = 0.384,  Poisson_b = 0.3, Conductivity_b = 1,      SpecificHeat_b =1219, Expansion_b = 0.000326, size_b = 5,
desity_f =0.00785, Elastic_f =  200000, Poisson_f = 0.3, Conductivity_f = 1.6578, SpecificHeat_f =512, Expansion_f = 1.22e-05, size_f = 3,
desity_h =1.65e-06, Elastic_h = 4000,   Poisson_h = 0.3, Conductivity_h = 0.001, SpecificHeat_h = 1500, Expansion_h = 0.0001263, size_h = 5
    , var_export=True, var_input=False, var_WCM=True, inputfile=None
)