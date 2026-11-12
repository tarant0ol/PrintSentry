from typing import Optional
import datetime
import decimal

from sqlalchemy import Boolean, Date, DateTime, ForeignKeyConstraint, Identity, Integer, Numeric, PrimaryKeyConstraint, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Clients(Base):
    __tablename__ = 'clients'
    __table_args__ = (
        PrimaryKeyConstraint('client_id', name='clients_pk'),
    )

    client_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    name: Mapped[Optional[str]] = mapped_column(String)
    phone: Mapped[Optional[str]] = mapped_column(String)
    email: Mapped[Optional[str]] = mapped_column(String)
    address: Mapped[Optional[str]] = mapped_column(Text)
    create_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    orders: Mapped[list['Orders']] = relationship('Orders', back_populates='client')


class DefectCauses(Base):
    __tablename__ = 'defect_causes'
    __table_args__ = (
        PrimaryKeyConstraint('defect_cause_id', name='defect_causes_pk'),
    )

    defect_cause_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    name: Mapped[Optional[str]] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)

    defect_cause_links: Mapped[list['DefectCauseLinks']] = relationship('DefectCauseLinks', back_populates='defect_cause')


class DefectRecomendations(Base):
    __tablename__ = 'defect_recomendations'
    __table_args__ = (
        PrimaryKeyConstraint('defect_recomendation_id', name='defect_recomendations_pk'),
    )

    defect_recomendation_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    name: Mapped[Optional[str]] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)

    defect_recomendation_links: Mapped[list['DefectRecomendationLinks']] = relationship('DefectRecomendationLinks', back_populates='defect_recomendation')


class DefectType(Base):
    __tablename__ = 'defect_type'
    __table_args__ = (
        PrimaryKeyConstraint('defect_type_id', name='defect_type_pk'),
    )

    defect_type_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    name: Mapped[Optional[str]] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)

    defect_cause_links: Mapped[list['DefectCauseLinks']] = relationship('DefectCauseLinks', back_populates='defect_type')
    defect_recomendation_links: Mapped[list['DefectRecomendationLinks']] = relationship('DefectRecomendationLinks', back_populates='defect_type')
    defect_parameters: Mapped[list['DefectParameters']] = relationship('DefectParameters', back_populates='defect_type')


class EquipmentType(Base):
    __tablename__ = 'equipment_type'
    __table_args__ = (
        PrimaryKeyConstraint('equipment_type_id', name='equipment_type_pk'),
    )

    equipment_type_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    name: Mapped[Optional[str]] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)

    equipment_models: Mapped[list['EquipmentModels']] = relationship('EquipmentModels', back_populates='equipment_type')
    equipment_parameters: Mapped[list['EquipmentParameters']] = relationship('EquipmentParameters', back_populates='equipment_type')


class Materials(Base):
    __tablename__ = 'materials'
    __table_args__ = (
        PrimaryKeyConstraint('material_id', name='materials_pk'),
    )

    material_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    name: Mapped[Optional[str]] = mapped_column(String)
    manufacturer: Mapped[Optional[str]] = mapped_column(String)
    color: Mapped[Optional[str]] = mapped_column(String)
    type: Mapped[Optional[str]] = mapped_column(String)
    density: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric)
    viscosity: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric)

    material_batches: Mapped[list['MaterialBatches']] = relationship('MaterialBatches', back_populates='material')


class Products(Base):
    __tablename__ = 'products'
    __table_args__ = (
        PrimaryKeyConstraint('product_id', name='products_pk'),
    )

    product_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    name: Mapped[Optional[str]] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(Text)
    weight: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric)
    volume: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric)
    height: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric)
    width: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric)
    length: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric)

    product_files: Mapped[list['ProductFiles']] = relationship('ProductFiles', back_populates='product')
    order_products: Mapped[list['OrderProducts']] = relationship('OrderProducts', back_populates='product')


class QualityResults(Base):
    __tablename__ = 'quality_results'
    __table_args__ = (
        PrimaryKeyConstraint('result_id', name='quality_results_pk'),
    )

    result_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    name: Mapped[Optional[str]] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(Text)

    quality_checks: Mapped[list['QualityChecks']] = relationship('QualityChecks', back_populates='result')


class Roles(Base):
    __tablename__ = 'roles'
    __table_args__ = (
        PrimaryKeyConstraint('role_id', name='roles_pk'),
    )

    role_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    name: Mapped[Optional[str]] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)

    employees: Mapped[list['Employees']] = relationship('Employees', back_populates='role')


class Units(Base):
    __tablename__ = 'units'
    __table_args__ = (
        PrimaryKeyConstraint('unit_id', name='units_pk'),
    )

    unit_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    name: Mapped[Optional[str]] = mapped_column(String)
    designation: Mapped[Optional[str]] = mapped_column(String)

    equipment_parameters: Mapped[list['EquipmentParameters']] = relationship('EquipmentParameters', back_populates='unit')


class DefectCauseLinks(Base):
    __tablename__ = 'defect_cause_links'
    __table_args__ = (
        ForeignKeyConstraint(['defect_cause_id'], ['defect_causes.defect_cause_id'], ondelete='RESTRICT', onupdate='CASCADE', name='defect_cause_links_defect_causes_fk'),
        ForeignKeyConstraint(['defect_type_id'], ['defect_type.defect_type_id'], ondelete='RESTRICT', onupdate='CASCADE', name='defect_cause_links_defect_type_fk'),
        PrimaryKeyConstraint('defect_cause_link_id', name='defect_cause_links_pk')
    )

    defect_cause_link_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    defect_type_id: Mapped[Optional[int]] = mapped_column(Integer)
    defect_cause_id: Mapped[Optional[int]] = mapped_column(Integer)

    defect_cause: Mapped[Optional['DefectCauses']] = relationship('DefectCauses', back_populates='defect_cause_links')
    defect_type: Mapped[Optional['DefectType']] = relationship('DefectType', back_populates='defect_cause_links')


class DefectRecomendationLinks(Base):
    __tablename__ = 'defect_recomendation_links'
    __table_args__ = (
        ForeignKeyConstraint(['defect_recomendation_id'], ['defect_recomendations.defect_recomendation_id'], ondelete='RESTRICT', onupdate='CASCADE', name='defect_recomendation_links_defect_recomendations_fk'),
        ForeignKeyConstraint(['defect_type_id'], ['defect_type.defect_type_id'], ondelete='RESTRICT', onupdate='CASCADE', name='defect_recomendation_links_defect_type_fk'),
        PrimaryKeyConstraint('defect_recomendation_link_id', name='defect_recomendation_links_pk')
    )

    defect_recomendation_link_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    defect_type_id: Mapped[Optional[int]] = mapped_column(Integer)
    defect_recomendation_id: Mapped[Optional[int]] = mapped_column(Integer)

    defect_recomendation: Mapped[Optional['DefectRecomendations']] = relationship('DefectRecomendations', back_populates='defect_recomendation_links')
    defect_type: Mapped[Optional['DefectType']] = relationship('DefectType', back_populates='defect_recomendation_links')


class Employees(Base):
    __tablename__ = 'employees'
    __table_args__ = (
        ForeignKeyConstraint(['role_id'], ['roles.role_id'], ondelete='RESTRICT', onupdate='CASCADE', name='employees_roles_fk'),
        PrimaryKeyConstraint('employee_id', name='employees_pk')
    )

    employee_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    full_name: Mapped[Optional[str]] = mapped_column(String)
    login: Mapped[Optional[str]] = mapped_column(String)
    password_hash: Mapped[Optional[str]] = mapped_column(String)
    role_id: Mapped[Optional[int]] = mapped_column(Integer)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean)

    role: Mapped[Optional['Roles']] = relationship('Roles', back_populates='employees')
    quality_checks: Mapped[list['QualityChecks']] = relationship('QualityChecks', back_populates='employee')


class EquipmentModels(Base):
    __tablename__ = 'equipment_models'
    __table_args__ = (
        ForeignKeyConstraint(['equipment_type_id'], ['equipment_type.equipment_type_id'], ondelete='RESTRICT', onupdate='CASCADE', name='equipment_models_equipment_type_fk'),
        PrimaryKeyConstraint('equipment_model_id', name='equipment_models_pk')
    )

    equipment_model_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    equipment_type_id: Mapped[Optional[int]] = mapped_column(Integer)
    name: Mapped[Optional[str]] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)

    equipment_type: Mapped[Optional['EquipmentType']] = relationship('EquipmentType', back_populates='equipment_models')
    equipment: Mapped[list['Equipment']] = relationship('Equipment', back_populates='equipment_model')


class EquipmentParameters(Base):
    __tablename__ = 'equipment_parameters'
    __table_args__ = (
        ForeignKeyConstraint(['equipment_type_id'], ['equipment_type.equipment_type_id'], ondelete='RESTRICT', onupdate='CASCADE', name='equipment_parameters_equipment_type_fk'),
        ForeignKeyConstraint(['unit_id'], ['units.unit_id'], ondelete='RESTRICT', onupdate='CASCADE', name='equipment_parameters_units_fk'),
        PrimaryKeyConstraint('equipment_parameter_id', name='equipment_parameters_pk')
    )

    equipment_parameter_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    equipment_type_id: Mapped[Optional[int]] = mapped_column(Integer)
    name: Mapped[Optional[str]] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)
    unit_id: Mapped[Optional[int]] = mapped_column(Integer)

    equipment_type: Mapped[Optional['EquipmentType']] = relationship('EquipmentType', back_populates='equipment_parameters')
    unit: Mapped[Optional['Units']] = relationship('Units', back_populates='equipment_parameters')
    defect_parameters: Mapped[list['DefectParameters']] = relationship('DefectParameters', back_populates='equipment_parameter')
    stage_parameters: Mapped[list['StageParameters']] = relationship('StageParameters', back_populates='equipment_parameter')
    stage_requirements: Mapped[list['StageRequirements']] = relationship('StageRequirements', back_populates='equipment_parameter')


class MaterialBatches(Base):
    __tablename__ = 'material_batches'
    __table_args__ = (
        ForeignKeyConstraint(['material_id'], ['materials.material_id'], ondelete='RESTRICT', onupdate='CASCADE', name='material_batches_materials_fk'),
        PrimaryKeyConstraint('batch_id', name='material_batches_pk')
    )

    batch_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    material_id: Mapped[Optional[int]] = mapped_column(Integer)
    batch_number: Mapped[Optional[str]] = mapped_column(String)
    production_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    expiration_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    quantity: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric)

    material: Mapped[Optional['Materials']] = relationship('Materials', back_populates='material_batches')
    production_tasks: Mapped[list['ProductionTasks']] = relationship('ProductionTasks', back_populates='material_batch')


class Orders(Base):
    __tablename__ = 'orders'
    __table_args__ = (
        ForeignKeyConstraint(['client_id'], ['clients.client_id'], ondelete='RESTRICT', onupdate='CASCADE', name='orders_clients_fk'),
        PrimaryKeyConstraint('order_id', name='orders_pk')
    )

    order_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    client_id: Mapped[Optional[int]] = mapped_column(Integer)
    status_id: Mapped[Optional[int]] = mapped_column(Integer)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    deadline: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    total_cost: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric)
    comment: Mapped[Optional[str]] = mapped_column(Text)

    client: Mapped[Optional['Clients']] = relationship('Clients', back_populates='orders')
    order_products: Mapped[list['OrderProducts']] = relationship('OrderProducts', back_populates='order')


class ProductFiles(Base):
    __tablename__ = 'product_files'
    __table_args__ = (
        ForeignKeyConstraint(['product_id'], ['products.product_id'], ondelete='RESTRICT', onupdate='CASCADE', name='product_files_products_fk'),
        PrimaryKeyConstraint('file_id', name='product_files_pk')
    )

    file_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    product_id: Mapped[Optional[int]] = mapped_column(Integer)
    file_name: Mapped[Optional[str]] = mapped_column(String)
    file_path: Mapped[Optional[str]] = mapped_column(Text)
    file_type: Mapped[Optional[str]] = mapped_column(String)
    uploaded_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    product: Mapped[Optional['Products']] = relationship('Products', back_populates='product_files')


class DefectParameters(Base):
    __tablename__ = 'defect_parameters'
    __table_args__ = (
        ForeignKeyConstraint(['defect_type_id'], ['defect_type.defect_type_id'], ondelete='RESTRICT', onupdate='CASCADE', name='defect_parameters_defect_type_fk'),
        ForeignKeyConstraint(['equipment_parameter_id'], ['equipment_parameters.equipment_parameter_id'], ondelete='RESTRICT', onupdate='CASCADE', name='defect_parameters_equipment_parameters_fk'),
        PrimaryKeyConstraint('defect_parameters_id', name='defect_parameters_pk')
    )

    defect_parameters_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    defect_type_id: Mapped[Optional[int]] = mapped_column(Integer)
    equipment_parameter_id: Mapped[Optional[int]] = mapped_column(Integer)
    severity: Mapped[Optional[str]] = mapped_column(String)

    defect_type: Mapped[Optional['DefectType']] = relationship('DefectType', back_populates='defect_parameters')
    equipment_parameter: Mapped[Optional['EquipmentParameters']] = relationship('EquipmentParameters', back_populates='defect_parameters')


class Equipment(Base):
    __tablename__ = 'equipment'
    __table_args__ = (
        ForeignKeyConstraint(['equipment_model_id'], ['equipment_models.equipment_model_id'], ondelete='RESTRICT', onupdate='CASCADE', name='equipment_equipment_models_fk'),
        PrimaryKeyConstraint('equipment_id', name='equipment_pk')
    )

    equipment_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    equipment_model_id: Mapped[Optional[int]] = mapped_column(Integer)
    serial_number: Mapped[Optional[str]] = mapped_column(String)
    status: Mapped[Optional[str]] = mapped_column(String)
    installation_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    equipment_model: Mapped[Optional['EquipmentModels']] = relationship('EquipmentModels', back_populates='equipment')
    stage_equipment: Mapped[list['StageEquipment']] = relationship('StageEquipment', back_populates='equipment')


class OrderProducts(Base):
    __tablename__ = 'order_products'
    __table_args__ = (
        ForeignKeyConstraint(['order_id'], ['orders.order_id'], ondelete='RESTRICT', onupdate='CASCADE', name='order_items_orders_fk'),
        ForeignKeyConstraint(['product_id'], ['products.product_id'], ondelete='RESTRICT', onupdate='CASCADE', name='order_items_products_fk'),
        PrimaryKeyConstraint('order_product_id', name='order_items_pk')
    )

    order_product_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    order_id: Mapped[Optional[int]] = mapped_column(Integer)
    product_id: Mapped[Optional[int]] = mapped_column(Integer)
    quantity: Mapped[Optional[int]] = mapped_column(Integer)
    unit_price: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric)

    order: Mapped[Optional['Orders']] = relationship('Orders', back_populates='order_products')
    product: Mapped[Optional['Products']] = relationship('Products', back_populates='order_products')
    production_tasks: Mapped[list['ProductionTasks']] = relationship('ProductionTasks', back_populates='order_product')


class ProductionTasks(Base):
    __tablename__ = 'production_tasks'
    __table_args__ = (
        ForeignKeyConstraint(['material_batch_id'], ['material_batches.batch_id'], ondelete='RESTRICT', onupdate='CASCADE', name='production_tasks_material_batches_fk'),
        ForeignKeyConstraint(['order_product_id'], ['order_products.order_product_id'], ondelete='RESTRICT', onupdate='CASCADE', name='production_tasks_order_products_fk'),
        PrimaryKeyConstraint('task_id', name='production_tasks_pk')
    )

    task_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    order_product_id: Mapped[Optional[int]] = mapped_column(Integer)
    material_batch_id: Mapped[Optional[int]] = mapped_column(Integer)
    start_time: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    end_time: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    status: Mapped[Optional[str]] = mapped_column(String)

    material_batch: Mapped[Optional['MaterialBatches']] = relationship('MaterialBatches', back_populates='production_tasks')
    order_product: Mapped[Optional['OrderProducts']] = relationship('OrderProducts', back_populates='production_tasks')
    production_stages: Mapped[list['ProductionStages']] = relationship('ProductionStages', back_populates='task')


class ProductionStages(Base):
    __tablename__ = 'production_stages'
    __table_args__ = (
        ForeignKeyConstraint(['task_id'], ['production_tasks.task_id'], ondelete='RESTRICT', onupdate='CASCADE', name='production_stages_production_tasks_fk'),
        PrimaryKeyConstraint('stage_id', name='production_stages_pk')
    )

    stage_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    task_id: Mapped[Optional[int]] = mapped_column(Integer)
    stage_name: Mapped[Optional[str]] = mapped_column(String)
    start_time: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    end_time: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    status: Mapped[Optional[str]] = mapped_column(String)

    task: Mapped[Optional['ProductionTasks']] = relationship('ProductionTasks', back_populates='production_stages')
    quality_checks: Mapped[list['QualityChecks']] = relationship('QualityChecks', back_populates='stage')
    stage_equipment: Mapped[list['StageEquipment']] = relationship('StageEquipment', back_populates='stage')


class QualityChecks(Base):
    __tablename__ = 'quality_checks'
    __table_args__ = (
        ForeignKeyConstraint(['employee_id'], ['employees.employee_id'], ondelete='RESTRICT', onupdate='CASCADE', name='quality_checks_employees_fk'),
        ForeignKeyConstraint(['result_id'], ['quality_results.result_id'], ondelete='RESTRICT', onupdate='CASCADE', name='quality_checks_quality_results_fk'),
        ForeignKeyConstraint(['stage_id'], ['production_stages.stage_id'], ondelete='RESTRICT', onupdate='CASCADE', name='quality_checks_production_stages_fk'),
        PrimaryKeyConstraint('check_id', name='quality_checks_pk')
    )

    check_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    stage_id: Mapped[Optional[int]] = mapped_column(Integer)
    check_type_id: Mapped[Optional[int]] = mapped_column(Integer)
    employee_id: Mapped[Optional[int]] = mapped_column(Integer)
    check_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    result_id: Mapped[Optional[int]] = mapped_column(Integer)
    comment: Mapped[Optional[str]] = mapped_column(Text)

    employee: Mapped[Optional['Employees']] = relationship('Employees', back_populates='quality_checks')
    result: Mapped[Optional['QualityResults']] = relationship('QualityResults', back_populates='quality_checks')
    stage: Mapped[Optional['ProductionStages']] = relationship('ProductionStages', back_populates='quality_checks')


class StageEquipment(Base):
    __tablename__ = 'stage_equipment'
    __table_args__ = (
        ForeignKeyConstraint(['equipment_id'], ['equipment.equipment_id'], ondelete='RESTRICT', onupdate='CASCADE', name='stage_equipment_equipment_fk'),
        ForeignKeyConstraint(['stage_id'], ['production_stages.stage_id'], ondelete='RESTRICT', onupdate='CASCADE', name='stage_equipment_production_stages_fk'),
        PrimaryKeyConstraint('stage_equipment_id', name='stage_equipment_pk')
    )

    stage_equipment_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    equipment_id: Mapped[Optional[int]] = mapped_column(Integer)
    stage_id: Mapped[Optional[int]] = mapped_column(Integer)
    start_time: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    end_time: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    equipment: Mapped[Optional['Equipment']] = relationship('Equipment', back_populates='stage_equipment')
    stage: Mapped[Optional['ProductionStages']] = relationship('ProductionStages', back_populates='stage_equipment')
    stage_parameters: Mapped[list['StageParameters']] = relationship('StageParameters', back_populates='stage_equipment')
    stage_requirements: Mapped[list['StageRequirements']] = relationship('StageRequirements', back_populates='stage_equipment')


class StageParameters(Base):
    __tablename__ = 'stage_parameters'
    __table_args__ = (
        ForeignKeyConstraint(['equipment_parameter_id'], ['equipment_parameters.equipment_parameter_id'], ondelete='RESTRICT', onupdate='CASCADE', name='stage_parameters_equipment_parameters_fk'),
        ForeignKeyConstraint(['stage_equipment_id'], ['stage_equipment.stage_equipment_id'], ondelete='RESTRICT', onupdate='CASCADE', name='stage_parameters_stage_equipment_fk'),
        PrimaryKeyConstraint('stage_parameter_id', name='stage_parameters_pk')
    )

    stage_parameter_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    stage_equipment_id: Mapped[Optional[int]] = mapped_column(Integer)
    equipment_parameter_id: Mapped[Optional[int]] = mapped_column(Integer)
    value: Mapped[Optional[str]] = mapped_column(String)
    time: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    equipment_parameter: Mapped[Optional['EquipmentParameters']] = relationship('EquipmentParameters', back_populates='stage_parameters')
    stage_equipment: Mapped[Optional['StageEquipment']] = relationship('StageEquipment', back_populates='stage_parameters')


class StageRequirements(Base):
    __tablename__ = 'stage_requirements'
    __table_args__ = (
        ForeignKeyConstraint(['equipment_parameter_id'], ['equipment_parameters.equipment_parameter_id'], ondelete='RESTRICT', onupdate='CASCADE', name='stage_requirements_equipment_parameters_fk'),
        ForeignKeyConstraint(['stage_equipment_id'], ['stage_equipment.stage_equipment_id'], ondelete='RESTRICT', onupdate='CASCADE', name='stage_requirements_stage_equipment_fk'),
        PrimaryKeyConstraint('stage_reqiurements_id', name='stage_requirements_pk')
    )

    stage_reqiurements_id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    stage_equipment_id: Mapped[Optional[int]] = mapped_column(Integer)
    equipment_parameter_id: Mapped[Optional[int]] = mapped_column(Integer)
    min_value: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric)
    max_value: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric)
    time: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    equipment_parameter: Mapped[Optional['EquipmentParameters']] = relationship('EquipmentParameters', back_populates='stage_requirements')
    stage_equipment: Mapped[Optional['StageEquipment']] = relationship('StageEquipment', back_populates='stage_requirements')
