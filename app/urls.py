from ctypes.wintypes import PCHAR
from django.urls import path
from .views import home,contacto,registro,recomendaciones,tiendas,tips,listar_contacto,tip1,tip2,tip3,tip4,tip5,agregar_producto, listar_productos, modificar_producto, eliminar_producto,api
urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('registro/', registro,name="registro"),
    path('recomendaciones/',recomendaciones, name="recomendaciones"),
    path('tiendas/', tiendas,name="tiendas"),
    path('tips/', tips,name="tips"),
    path('listar_contacto/', listar_contacto,name="listar_contacto"),
    path('tip1/', tip1,name="tip1"),
    path('tip2/', tip2,name="tip2"),
    path('tip3/', tip3,name="tip3"),
    path('tip4/', tip4,name="tip4"),
    path('tip5/', tip5,name="tip5"),
    path('agregar-producto/', agregar_producto, name='agregar_producto'),
    path('listar-productos/', listar_productos, name='listar_productos'),
    path('modificar-producto/<id>/', modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<id>/', eliminar_producto, name='eliminar_producto'),
    path('api/', api,name="api"),
]