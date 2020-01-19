# algokit
a python module published by Pypl

## modules
| Module Name | Function |
| ----- | ----- |
| algokit | the core module will installed by pip |
| arcgis_tools | some auxiliary arcpy tools used in Arcgis |  

## how to install

+ check  
`python setup.py check`

+ package  
`python setup.py sdist bdist_wheel`

+ install  
`pip install ./dist/algokit.x.x.x-pyX-none-any.whl`  
x.x.x is the version of algokit  

+ upload to pip  
`python setup.py register sdist upload  (deprecated)`    
or  
`twine upload dist/*`


