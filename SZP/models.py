from django.contrib.auth.models import User, Group
from django.db import models

# Create your models here.



class Employee(models.Model):
    position = models.CharField(max_length=64)
    vacations_start = models.DateField(null=True, blank=True)
    vacations_end = models.DateField(null=True, blank=True)
    sick_leave = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.position}, {self.vacations_start}, {self.vacations_end}, {self.sick_leave}. {self.user}"

class Tank(models.Model):
    NOT_DEFINED = -1
    TANK_CHOICES = [
        (0, 'hydroakumulator'),
        (1, 'akumulator tłokowy'),
    ]
    capacity = models.IntegerField()
    type = models.IntegerField(choices=TANK_CHOICES, default=NOT_DEFINED)
    max_pressure = models.IntegerField()
    work_pressure = models.IntegerField()
    valve_setting_pressure = models.IntegerField()
    serial_number = models.CharField(max_length=128)
    UDT_number = models.CharField(max_length=128)
    UDT_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.capacity}, {self.type}, {self.max_pressure}, {self.work_pressure}, {self.valve_setting_pressure}, {self.serial_number}, {self.UDT_number}, {self.UDT_date}"

class Machines(models.Model):
    MT_NOT_DEFINED = -1
    MACHINE_CHOICES = [
        (0, 'odlewnicza'),
        (1, 'wózek widłowy'),
        (2, 'CNC'),
    ]
    OC_NOT_DEFINED = -1
    ORIENTATION_CHOICES = [
        (0, 'horyzontalna'),
        (1, 'wertykalna'),
    ]
    name = models.CharField(max_length=128)
    vendor = models.CharField(max_length=128)
    serial_number = models.CharField(max_length=128)
    power_consumption = models.IntegerField()
    type = models.IntegerField(choices=MACHINE_CHOICES, default=MT_NOT_DEFINED)
    orientation = models.IntegerField(choices=ORIENTATION_CHOICES, default=OC_NOT_DEFINED)
    pressure = models.IntegerField()
    pressure_tank = models.IntegerField()
    technological_schema = models.BooleanField(default=True)
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name}, {self.vendor}, {self.serial_number}, {self.power_consumption}, {self.type}, {self.orientation}, {self.pressure}, {self.pressure_tank}, {self.technological_schema}, {self.tank}"

class Furnace(models.Model):
    NOT_DEFINED = -1
    PS_CHOICES = [
        (0, 'gaz'),
        (1, 'prąd'),
    ]
    capacity = models.IntegerField()
    power_source = models.IntegerField(choices=PS_CHOICES, default=NOT_DEFINED)
    machine = models.OneToOneField(Machines, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.capacity}, {self.power_source}, {self.machine}"

class CastingMold(models.Model):
    index = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    tool_shop = models.CharField(max_length=128)
    machines = models.ManyToManyField(Machines, through="TechSchema")

    def __str__(self):
        return f"{self.index}, {self.owner}, {self.tool_shop}, {self.machines}"

class TechSchema(models.Model):
    NOT_DEFINED = -1
    ALLOY_CHOICES = [
        (0, '226'),
        (1, '231'),
        (2, '230'),
        (3, 'ZL5'),
    ]
    machine = models.ForeignKey(Machines, on_delete=models.CASCADE, null=True)
    casting_mold = models.ForeignKey(CastingMold, on_delete=models.CASCADE, null=True)
    detail_name = models.CharField(max_length=128)
    alloy_type = models.IntegerField(choices=ALLOY_CHOICES, default=NOT_DEFINED)
    pdf_file = models.FileField(upload_to='uploads/%Y/%m/%d/')

    def __str__(self):
        return f"{self.machine}, {self.casting_mold}, {self.detail_name}, {self.alloy_type}, {self.pdf_file}"

