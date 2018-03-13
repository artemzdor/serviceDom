#!/usr/bin/python3
# -*- coding: utf-8 -*-
import lib.master
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker

import app.config
import app.config
engine = create_engine(config.DATABASE, config.DATABASE_ENGINE_CONFIG)

metadata = MetaData()
users_table = Table('users', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String),
                    Column('fullname', String),
                    Column('password', String))


Session = sessionmaker(engine)
Session.configure()
session = Session()
vasiaUser = lib.master.User("vasia", "Vasiliy Pypkin", "vasia2000")
session.add(vasiaUser)
session.commit()

