import gns3fy
from gns3fy import Gns3Connector, Project
from tabulate import tabulate

server = gns3fy.Gns3Connector(url="http://<ip_servidor_gns>:80",user="<usuario_GNS3>",cred="<Contraseña>")
print(server.get_version())
print(server.get_projects())

project = server.create_project(name="Proyecto final automatizado")

# Obtenemos el id del proyecto y lo almaceno

project = server.get_project(name="Proyecto final automatizado")

id_project=project["project_id"]

print("---------------------")
print(id_project)
print("---------------------")

# Convierto el proyecto en objeto

project = Project(name="Proyecto final automatizado", connector=server, project_id=id_project)
# Creamos dispostivios
project.create_node(name='Router', template='OpenWrt 22.03.0')
project.create_node(name='sw_dmz', template='Ethernet switch')
project.create_node(name='sw_int', template='Ethernet switch')
project.create_node(name='srv1', template='Ubuntu Desktop Guest 22.04')
project.create_node(name='srv2', template='Ubuntu Desktop Guest 22.04')
project.create_node(name='PC1', template='Ubuntu Desktop Guest 22.04')
project.create_node(name='PC2', template='Windows 10 w/ Edge')
project.create_node(name='PC3', template='Ubuntu Desktop Guest 22.04')
project.create_node(name='Nube', template='Cloud')

sw_dmz = project.get_node(name="sw_dmz")
srv1 = project.get_node(name="srv1")
print(srv1)
print(sw_dmz)
# Los conectamos
# sw_dmz
project.create_link('srv1', 'eth0', 'sw_dmz', 'Ethernet1')
project.create_link('srv2', 'eth0', 'sw_dmz', 'Ethernet2')
# Router
project.create_link('Router', 'Ethernet1', 'Nube', 'eth0')
project.create_link('sw_dmz', 'Ethernet0', 'Router', 'Ethernet2')
project.create_link('sw_int', 'Ethernet0', 'Router', 'Ethernet0')
#sw_int
project.create_link('PC1', 'eth0', 'sw_int', 'Ethernet1')
project.create_link('PC2', 'NIC1', 'sw_int', 'Ethernet2')
project.create_link('PC3', 'eth0', 'sw_int', 'Ethernet3')