# Create your models here.

from django.db import models
from django.core.urlresolvers import reverse

from jnpr.junos import Device as jDev
# Create your models here.


class Device(models.Model):
    host_name = models.CharField(max_length=50, unique=True, primary_key=True)
    ipv4_address = models.CharField(max_length=15)
    root_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    session = jDev(str(ipv4_address), host='old-vSRX-1', user=str(root_name), passwd=str(password))

    def to_python(self):
        return [self.ipv4_address, self.host_name, self.root_name, self.password]

    def get_absolute_url(self):
        return reverse('juniper:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "{},{},{},{}".format(self.ipv4_address, self.host_name, self.root_name, self.password)


class User(models.Model):
    #UNIQUE TOGETHER NAME AND DEVICE?
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=30)
    full_name = models.CharField(max_length=100)
    user_id = models.IntegerField()
    permission_class = models.CharField(max_length=50)

    def to_python(self):
        print(self.__str__())

    def __str__(self):
        return "Device: {}, user_name: {}, full_name: {}, user_id: {}, permission_class: {}".format(str(self.device), str(self.user_name), str(self.full_name), str(self.user_id), str(self.permission_class))

class Interface(models.Model):
    #UNIQUE TOGETHER NAME AND DEVICE?
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    iface_name = models.CharField(max_length=50)
    admin_status = models.CharField(max_length=4)
    oper_status = models.CharField(max_length=4)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return "Interface: {}".format(str(self.iface_name))

class Logical_Interface(models.Model):
    physical_interface = models.ForeignKey(Interface, on_delete=models.CASCADE)
    logface_name = models.CharField(max_length=50)
    log_admin_status = models.CharField(max_length=4)
    log_oper_status = models.CharField(max_length=4)

class Address_Family(models.Model):
    logical_interface = models.ForeignKey(Logical_Interface, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

class Address(models.Model):
    address_family = models.ForeignKey(Address_Family, on_delete=models.CASCADE)
    address_local = models.CharField(max_length=15)
    address_remote = models.CharField(max_length=15)
