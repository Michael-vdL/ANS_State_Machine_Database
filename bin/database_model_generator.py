#Takes Dictionary Items, Stores them into juniper.models.py

#Import from the juniper app models file, imports each model as a module
from juniper.models import Device, User, Interface, Logical_Interface, Address_Family, Address


#Simple get_dict function I use in almost all my files for json resources

def get_dict(file_name):
    import json
    with open('resources/{}.json'.format(file_name)) as resource_file:
        dict = json.load(resource_file)
    return dict

#Driver for generating models, just iterates through to generate models

def generate_models():
    dev_list = gen_device_models()
    for dev in dev_list:
        gen_user_models(dev)
        interface_list = gen_interface_models(dev)
        for interface in interface_list:
            gen_log_interface_models(dev, interface)

#Each gen_<foo>_models takes in a dict
# Then Goes through a try except to see if an entity of that type is already present
# The Try checks if it is present, and if it is present it updates data that isnt name
# The Except Creates a new entity with all present data

def gen_device_models():
    dev_model_list = []
    dev_dict = get_dict('entities/junos/devices')
    for dev_name in dev_dict:
        ip = dev_dict[dev_name]['ip']  # Gets IP
        username = dev_dict[dev_name]['username']  # Gets Username
        password = dev_dict[dev_name]['password']  # Gets Password

        try:
            device_model = Device.objects.get(host_name=dev_name)
            device_model.ipv4_address = ip
            device_model.root_name = username
            device_model.password = password
        except Device.DoesNotExist:
            device_model = Device(host_name=dev_name, ipv4_address=ip, root_name=username, password=password)

        device_model.save()
        dev_model_list.append(device_model)
    return dev_model_list


def gen_user_models(device):
    user_dict = get_dict('entities/junos/{}/users'.format(device.host_name))
    for user in user_dict:
        user_full_name = user_dict[user]['full_name']
        user_id = user_dict[user]['id']
        user_class = user_dict[user]['class']

        try:
            user_model = device.user_set.get(user_name=user)
            user_model.full_name = user_full_name
            user_model.user_id = user_id
            user_model.permission_class = user_class
            user_model.save()
        except User.DoesNotExist:
            user_model = device.user_set.create(user_name=user, full_name=user_full_name, user_id=user_id, permission_class=user_class)

def gen_interface_models(device):
    interface_model_list = []
    interface_dict = get_dict('entities/junos/{}/interfaces'.format(device.host_name))
    for interface in interface_dict:
        ad_stat = interface_dict[interface]['admin-status']
        op_stat = interface_dict[interface]['oper-status']
        desc = interface_dict[interface]['description']

        try:
            interface_model = device.interface_set.get(iface_name=interface)
            interface_model.admin_status = ad_stat
            interface_model.oper_status = op_stat
            interface_model.description = desc
            interface_model.save()
        except Interface.DoesNotExist:
            interface_model = device.interface_set.create(iface_name=interface, admin_status=ad_stat, oper_status=op_stat, description=desc)

        interface_model_list.append(interface_model)
    return interface_model_list

def gen_log_interface_models(device, interface):
    interface_dict = get_dict('entities/junos/{}/interfaces'.format(device.host_name))
    logical_dict = interface_dict[interface.iface_name]['logical_interfaces']
    for logface in logical_dict:
        ad_stat = logical_dict[logface]['admin_status']
        oper_stat = logical_dict[logface]['oper_status']

        try:
            logface_model = interface.logical_interface_set.get(logface_name=logface)
            logface_model.log_admin_status = ad_stat
            logface_model.log_oper_status = oper_stat
            logface_model.save()
        except Logical_Interface.DoesNotExist:
            logface_model = interface.logical_interface_set.create(logface_name=logface, log_admin_status=ad_stat, log_oper_status=oper_stat)

        #Makes Address Families for Logical Interface
        ad_fams = logical_dict[logface]['address_families']
        gen_address_families(logface_model, ad_fams)

def gen_address_families(logface, adfam_dict):
    for adfam in adfam_dict:
        try:
            adfam_model = logface.address_family_set.get(name=adfam)
        except Address_Family.DoesNotExist:
            adfam_model = logface.address_family_set.create(name=adfam)

        address_dict_list = adfam_dict[adfam]
        for address_pair in address_dict_list:
            local = address_pair['local']
            dest = address_pair['destination']
            try:
                address_model = adfam_model.address_set.get(address_local=local)
                address_model.remote = dest
            except Address.DoesNotExist:
                adfam_model.address_set.create(address_local=local, address_remote=dest)


